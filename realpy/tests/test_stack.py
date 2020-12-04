from ds import stack
import pytest

#for repetitive code:
@pytest.fixture
def stack_def():
    return stack.Stack()

def test_constructor():
    s = stack.Stack()
    assert 1 == 1
    assert isinstance(s, stack.Stack)
    assert len(s) == 0

#I inject a stack object inot my test_push function
# so when the test runs it actually calls def stack()
def test_push(stack_def):
    stack_def.push(3)
    assert len(stack_def) == 1
    stack_def.push(5)
    assert len(stack_def) == 2

def test_pop(stack_def):
    stack_def.push("ciao")
    stack_def.push("pontry")
    assert stack_def.pop() == "pontry"
    assert stack_def.pop() == "ciao"
    assert stack_def.pop() is None