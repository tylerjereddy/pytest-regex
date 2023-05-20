# pytest-regex

## Use Python Standard Library Regular Expressions to Specify Tests to Run

After installing locally with i.e., `python -m pip install .` you can
compare it with more conventional test selection techniques as follows.

Consider working with SciPy development. Let's start off by selecting
all tests with `test_3d` anywhere in their node id, using the conventional/
built-in `-k` flag:

`python dev.py test -- -v -k "test_3d"`

This runs a bunch of tests with string matches as you might expect:

```
scipy/io/tests/test_idl.py::TestArrayDimensions::test_3d PASSED
scipy/io/tests/test_idl.py::TestPointerArray::test_3d PASSED
scipy/optimize/_trustregion_constr/tests/test_qp_subproblem.py::TestBoxBoundariesIntersections::test_3d_box_constraints PASSED
scipy/optimize/_trustregion_constr/tests/test_qp_subproblem.py::TestBoxBoundariesIntersections::test_3d_box_constraints_entire_line PASSED
scipy/optimize/_trustregion_constr/tests/test_qp_subproblem.py::TestModifiedDogleg::test_3d_example PASSED
scipy/stats/tests/test_stats.py::TestGeometricStandardDeviation::test_3d_array PASSED
scipy/stats/tests/test_stats.py::TestGeometricStandardDeviation::test_3d_array_axis_type_tuple PASSED
scipy/stats/tests/test_stats.py::TestGeometricStandardDeviation::test_3d_array_axis_0 PASSED
scipy/stats/tests/test_stats.py::TestGeometricStandardDeviation::test_3d_array_axis_1 PASSED
scipy/stats/tests/test_stats.py::TestGeometricStandardDeviation::test_3d_array_axis_2 PASSED
scipy/stats/tests/test_stats.py::TestFOneWay::test_3d_inputs PASSED
```

What if you want to run only tests with an exact match to `test_3d` or
`test_3d_example`?

Try `pytest-regex` with:
`python dev.py test -- -v --regex "(.*test_3d$|.*test_3d_example$)"`


```
scipy/io/tests/test_idl.py::TestArrayDimensions::test_3d PASSED
scipy/io/tests/test_idl.py::TestPointerArray::test_3d PASSED
scipy/optimize/_trustregion_constr/tests/test_qp_subproblem.py::TestModifiedDogleg::test_3d_example PASSED
```

This does what we want, and is probably more concise than the `-k` alternative. In fact,
I'm not entirely sure how one would do this with `-k` in its current form.

## How it Works

`pytest-regex` simply passes the Python regular expression through
to the list of node ids, where a node id is structured as follows:

`path/to/test_module.py::TestClass::test_name[parameter_value]`

If the regex matches the node id, the test is retained and executed.
