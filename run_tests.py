#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from subprocess import run, PIPE
import os

class MyTest:
    def __init__(self, label: str, weight: int = 1, partial: bool = True):
        self.label: str = label
        self.awarded: int = 0        # Percentage score (0-100)
        self.weight: int = weight    # Used to calculate the weighted mean
        self.partial: bool = partial # Whether the test can be partially scored

    def set_percentage(self, text: str):
        if text[-1] == "%":
            value = int(text[:-1])
            if self.partial:
                self.awarded = value
            else:
                self.awarded = value if value == 100 else 0
        return self

    
    def run(self):
        grade_file = "result.txt"
        result = run(["tko", "eval", '-ts', '-r', grade_file, f"src/{self.label}"], stderr=PIPE, text=True)
        if result.returncode != 0:
           print(result.stderr)
        if result.returncode == 0:
            if os.path.isfile(grade_file):
                percent = open(grade_file, "r").read().splitlines()[0].strip()
                self.set_percentage(percent)
                os.remove(grade_file)
        return self


class MyTestList:
    def __init__(self):
        self.tests: list[MyTest] = []

    def add_test(self, label: str, weight: int, partial: bool = True):
        test = MyTest(label, weight, partial)
        self.tests.append(test)
        test.run()

    def calc_grade(self) -> int:
        total_weight = sum(test.weight for test in self.tests)
        max_label_len = max(len(test.label) for test in self.tests)
        grade = 0
        print(f"{'Test':<{max_label_len}}| awarded | weight | reached")
        for test in self.tests:
            test.weight = test.weight * 100 // total_weight
            awarded = test.awarded * test.weight // 100
            print(f"{test.label.ljust(max_label_len)}|    {test.awarded:03d}% |   {test.weight:03d}% |    {awarded:03d}%")
            grade += awarded
        print(f"{'-' * max_label_len}|---------|--------|-----------")
        print(f"{'Total':<{max_label_len}}|         |   100% |    {grade:03d}%")
        return grade

def main():
    test_list = MyTestList()
    test_list.add_test("leds", 1)
    test_list.add_test("media", 1)
    test_list.add_test("traficantes", 2)
    awarded = test_list.calc_grade()
    with open("awarded.txt", "w") as f:
        print(f"Total awarded: {awarded} writing to awarded.txt")
        f.write(str(awarded))


if __name__ == "__main__":
    main()
