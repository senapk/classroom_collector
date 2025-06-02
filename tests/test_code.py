#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tests.grade_submission import MyTest



def test_leds():
    test = MyTest("leds").run()
    assert test.status == "passed"

def test_media():
    test = MyTest("media").run()
    assert test.status == "passed"

def test_traficantes():
    test = MyTest("traficantes").run()
    assert test.status == "passed"
