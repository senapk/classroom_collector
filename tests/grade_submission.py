#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from subprocess import run, PIPE
import json

class MyTest:
    def __init__(self, test_name: str, max_score: int = 10, partial: bool = True):
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
        return self

    def set_failed(self):
        self.status = "failed"
        return self

    def set_passed(self):
        self.status = "passed"
        return self
    
    def run(self):
        result = run(["tko", "-m", "eval", '-ts', f"src/{self.test_name}"], stdout=PIPE, stderr=PIPE, text=True)
        print(result.stdout, result.stderr)
        if result.returncode != 0:
            self.set_failed()
            self.output = result.stdout + result.stderr
        else:
            line = result.stdout.splitlines()[0]
            if line.endswith("%"):
                self.output = line
                self.set_percentage(line.split(" ")[-1])
            else:
                self.set_failed()
                self.output = result.stdout
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

class MyTestList:
    def __init__(self):
        self.tests: list[MyTest] = []

    def add_test(self, label: str, max_score: int, partial: bool = True):
        test = MyTest(label, max_score, partial)
        self.tests.append(test)
        test.run()

    def to_json(self) -> str:
        return json.dumps([test.to_dict() for test in self.tests], indent=4)


def main():
    test_list = MyTestList()
    test_list.add_test("leds", 10)
    test_list.add_test("media", 10)
    test_list.add_test("traficantes", 30)
    print(test_list.to_json())


if __name__ == "__main__":
    main()
