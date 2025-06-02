#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from subprocess import run, PIPE
import json

class Test:
    def __init__(self, test_name: str, max_score: int, partial: bool = True):
        self.test_name: str = test_name
        self.output: str = "" # attempts, and time spended
        self.status: str = "failed"
        self.points_awarded: int = 0
        self.max_score: int = max_score
        self.partial: bool = partial

    def set_percentage(self, text: str):
        if text[-1] == "%":
            value = int(text[:-1])
            if self.partial:
                self.points_awarded = int((value * self.max_score) / 100)
            else:
                self.points_awarded = self.max_score if value == 100 else 0
            if self.points_awarded == self.max_score:
                self.set_passed()
            else:
                self.set_failed()

    def set_failed(self):
        self.status = "failed"
        return self

    def set_passed(self):
        self.status = "passed"
        return self
    
    def to_dict(self) -> dict[str, str | int | bool]:
        return {
            "test_name": self.test_name,
            "output": self.output,
            "status": self.status,
            "points_awarded": self.points_awarded,
            "max_score": self.max_score,
            "partial": self.partial
        }

class TestList:
    def __init__(self):
        self.tests: list[Test] = []

    def add_test(self, label: str, max_score: int, partial: bool = True):
        test = Test(label, max_score, partial)
        # run comand "tko run src/label" and collect the output
        result = run(["tko", "-m", "eval", '-tsc', f"src/{label}"], stdout=PIPE, stderr=PIPE, text=True)
        self.tests.append(test)
        if result.returncode != 0:
            test.set_failed()
            test.output = result.stdout + result.stderr
        else:
            line = result.stdout.splitlines()[0]
            if line.endswith("%"):
                test.output = line
                test.set_percentage(line.split(" ")[-1])
            else:
                test.set_failed()
                test.output = result.stdout

    def to_json(self) -> str:
        return json.dumps([test.to_dict() for test in self.tests], indent=4)


def main():
    test_list = TestList()
    test_list.add_test("leds", 10)
    test_list.add_test("media", 10)
    test_list.add_test("traficantes", 30)
    print(test_list.to_json())


if __name__ == "__main__":
    main()
