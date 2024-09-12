from hypothesis import given, settings
from hypothesis.strategies import integers
from gaboon.boa_tools import VyperContract

from src import Counter
from script.deploy import deploy

def test_increment(counter_contract):
    counter_contract.increment()
    assert counter_contract.number() == 1

@settings(deadline=None)
@given(num=integers(1, 10_000))
def test_increment_fuzz(num: int):
    counter_contract: VyperContract = Counter.deploy()
    count = counter_contract.number()
    for _ in range(num):
        counter_contract.increment()
        count += 1
    
    assert counter_contract.number() == count