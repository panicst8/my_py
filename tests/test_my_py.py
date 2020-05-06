""" Sample tests using pytest and hypothesis """
from hypothesis import given
import hypothesis.strategies as st


from my_py.my_py import SampleClass
from my_py.my_py import sample_func_subtract


def test_sample_method_add():
    """ testing for sample_method_add """
    sample_class = SampleClass()
    assert sample_class.sample_method_add(2, 4) == 6  # nosec


def test_sample_func_subtract():
    """ testing for sample_function_subtract """
    assert sample_func_subtract(4, 3) == 1  # nosec


@given(st.integers(), st.integers())
def test_hypothesis_test_of_calc(first_int, second_int):
    """ hypothesis test """
    sample_class = SampleClass()
    assert (
        sample_class.sample_method_add(first_int, second_int) == first_int + second_int
    )  # nosec
