import pytest
from py_backwards.utils.snippet import VariablesGenerator


@pytest.fixture(autouse=True)
def reset_variables_generator():
    VariablesGenerator._counter = 0