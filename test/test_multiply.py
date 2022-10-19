#multiply
#test
#remote
from src.calculator import multiply
import pytest
def test_multiply():
    result = multiply(3, 4)
    print(result)
    print("***&")
    assert result == 12
def test_multiply_string():
    with pytest.raises(TypeError):
        multiply("string", 4)

#dd
#dd
