from src.calculator import add
import pytest
def test_add():
    result = add(3, 4)
    print(f'result of addition : {result}')
    assert result == 7
def test_add_string():
    with pytest.raises(TypeError):
        add("string", 4)
