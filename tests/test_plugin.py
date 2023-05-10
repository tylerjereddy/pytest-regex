import pytest


def test_suite_output(pytester):
    result = pytester.runpytest("--regex", "dummy_regex")
    actual_stdout = result.stdout.str()
    expected_str1 = "pytest-regex selected"
    expected_str2 = "tests to run for regex: dummy_regex"
    assert expected_str1 in actual_stdout
    assert expected_str2 in actual_stdout
