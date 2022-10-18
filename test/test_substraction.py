from src.calculator import subtract
import pytest
def test_subtract():
    result = subtract(8, 4)
    assert result == 4
def test_subtract_string():
    with pytest.raises(TypeError):
        subtract("string", 4)