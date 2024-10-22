from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

@pytest.mark.parametrize("a, b, operation, expected", [
    (Decimal('13'), Decimal('7'), add, Decimal('20')),  
    (Decimal('13'), Decimal('7'), subtract, Decimal('6')),
    (Decimal('13'), Decimal('7'), multiply, Decimal('91')),
    (Decimal('13'), Decimal('2'), divide, Decimal('6.5')),
    (Decimal('13.5'), Decimal('0.7'), add, Decimal('14.2')),
    (Decimal('13.5'), Decimal('0.7'), subtract, Decimal('12.8')),
    (Decimal('13.5'), Decimal('2'), multiply, Decimal('27.0')),
    (Decimal('13'), Decimal('0.2'), divide, Decimal('65')),
])
def test_calculation_operations(a, b, operation, expected):
    calc = Calculation(a,b,operation)  
    assert calc.perform() == expected, f"Failed {operation.__name__} operation with {a} and {b}"  

def test_calculation_repr():
    calc = Calculation(Decimal('13'), Decimal('7'), add)  
    expected_repr = "Calculation(13, 7, add)"  
    assert calc.__repr__() == expected_repr, "The __repr__ method output does not match the expected string." 

def test_divide_by_zero():
    calc = Calculation(Decimal('13'), Decimal('0'), divide)  
    with pytest.raises(ValueError, match="Cannot divide by zero"):  
        calc.perform()  
