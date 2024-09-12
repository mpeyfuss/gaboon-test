import pytest
from gaboon.boa_tools import VyperContract
from src import Counter

@pytest.fixture
def counter_contract() -> VyperContract:
    return Counter.deploy()