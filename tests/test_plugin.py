import pytest


def test_suite_output(pytester):
    # a few checks for the scenario where
    # pytest-regex is installed as a plugin
    # but NO usage of --regex on the pytest
    # incantation
    dummy_result = pytester.runpytest()
    dummy_stdout = dummy_result.stdout.str()
    assert "pytest-regex" in dummy_stdout
    assert "dummy_regex" not in dummy_stdout
    assert "regex-" in dummy_stdout

    # next, check the use of the --regex option
    # on the command line
    result = pytester.runpytest("--regex", "dummy_regex")
    actual_stdout = result.stdout.str()
    expected_str1 = "pytest-regex selected"
    expected_str2 = "tests to run for regex: dummy_regex"
    assert expected_str1 in actual_stdout
    assert expected_str2 in actual_stdout
