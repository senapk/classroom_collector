#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from subprocess import run, PIPE
import os
import configparser
import argparse

class Const:
    ansi_green = "\033[92m"
    ansi_reset = "\033[0m"
    awarded_file = ".config/awarded.txt"
    temp_result_file = ".config/result.txt" # Temporary file to collect results from tko eval command

class Problem:
    config_file = ".config/config.ini"
    tag_value = "value"
    tag_param = "param"
    tag_partial = "partial"


class MyTest:
    def __init__(self, label: str, value: int = 1, partial: bool = True, param: str = ""):
        self.label: str = label
        self.awarded: float = 0      # Percentage score (0-100)
        self.value: float = value    # Used to calculate the weighted mean
        self.param: str = param         # Additional parameters for the test
        self.partial: bool = partial # Whether the test can be partially scored

    def set_percentage(self, text: str):
        if text[-1] == "%":
            value = float(text[:-1])
            if self.partial:
                self.awarded = value
            else:
                self.awarded = value if value == 100 else 0
        return self

    
    def run(self):
        temp_file = Const.temp_result_file
        extra: list[str] = []
        if self.param:
            extra = self.param.split(" ")
        result = run(["tko", "eval", "--timeout", "30"] + extra + ['-r', temp_file, f"src/{self.label}"], stderr=PIPE, text=True)
        if result.returncode != 0:
           print(result.stderr)
        if result.returncode == 0:
            if os.path.isfile(temp_file):
                percent = open(temp_file, "r").read().splitlines()[0].strip()
                self.set_percentage(percent)
                os.remove(temp_file)
        return self


class Runner:
    def __init__(self):
        self.tests: list[MyTest] = []

    def add_and_run_test(self, test: MyTest):
        self.tests.append(test)
        test.run()

    def calc_grade(self) -> int:
        total_weight = sum(test.value for test in self.tests)
        max_label_len = max(len(test.label) for test in self.tests) + 1
        grade: float = 0
        print("")
        print(f"{'TestCases':<{max_label_len}}| passed | value | earned")
        sep = f"{'-' * max_label_len}|--------|-------|-------"
        print(sep)
        for test in self.tests:
            test.value = test.value * 100 // total_weight
            awarded = test.awarded * test.value // 100
            print(f"{test.label.ljust(max_label_len)}|   {round(test.awarded):3d}% |  {round(test.value):3d}% |   {round(awarded):3d}%")
            grade += awarded
        print(sep)
        print(f"{'Total':<{max_label_len}}|        |  100% |    {Const.ansi_green}{round(grade):3d}%{Const.ansi_reset}")
        return round(grade)

    @staticmethod
    def main(args: argparse.Namespace):
        config = configparser.ConfigParser()
        config.read(Problem.config_file)
        test_list = Runner()
        for section in config.sections():
            label = section
            value = config.getint(section, Problem.tag_value, fallback=1)
            param = config.get(section, Problem.tag_param, fallback="")
            partial = config.getboolean(section, Problem.tag_partial, fallback=True)
            test = MyTest(label=label, value=value, param=param, partial=partial)
            test_list.add_and_run_test(test)

        output_file = args.output if args.output else Const.awarded_file
        awarded = test_list.calc_grade()
        with open(output_file, "w") as f:
            print(f"\nSaving final grade in file {output_file}")
            f.write(str(awarded))
        with open(output_file, "r") as f:
            awarded = int(f.read().strip())
            print(f"Grade awarded: {Const.ansi_green}{awarded}%{Const.ansi_reset}")

class Checker:
    @staticmethod
    def load_awarded():
        awarded = 0
        if os.path.exists(Const.awarded_file):
            try:
                awarded = int(open(Const.awarded_file, "r").read().strip())
            except ValueError:
                pass
        return awarded

    @staticmethod
    def load_request(request: int | None):
        if request is None:
            request = int(input())
        return request

    @staticmethod
    def main(args: argparse.Namespace):
        awarded = Checker.load_awarded()
        request = Checker.load_request(args.request)

        if request <= awarded:
            print("1")
        else:
            print("0")


def main():
    parser = argparse.ArgumentParser(description="Run tests and calculate grade.")
    subparsers = parser.add_subparsers(dest="commands", required=True)
    parser_run = subparsers.add_parser("test", help="Run the tests and calculate the grade.")
    parser_run.add_argument("--output", "-o", type=str, help="Output file for the awarded grade.")
    parser_run.set_defaults(func=Runner.main)
    parser_check = subparsers.add_parser("check", help="Check if the grade is awarded.")
    parser_check.add_argument("request", type=int, nargs='?', default=None, help="Request grade to check.")
    parser_check.set_defaults(func=Checker.main)
    args = parser.parse_args()
    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
