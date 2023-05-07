import re

import pytest


def pytest_addoption(parser):
    group = parser.getgroup('regex')
    group.addoption(
        '--regex',
        action='store',
        dest='dest_regex',
        default=r'.*',
        help='Provide a Python regex to select the tests to run.'
    )


def pytest_collection_modifyitems(session, config, items):
    reg = config.getoption("--regex")
    prog = re.compile(config.getoption("--regex"))
    num_matches = 0
    new_items = []
    for test_element in items:
        node_id = test_element.nodeid
        res = prog.match(node_id)
        if res:
            new_items.append(test_element)
            num_matches += 1
    items[:] = new_items
    # NOTE: leading space in string here helps prevent
    # stripping the first char in pytest output for some reason
    print(f" pytest-regex selected {num_matches} tests to run for regex: {reg}")
