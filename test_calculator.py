"""
Unit Tests for Calculator
"""

import pytest
from calculator_logic import Calculator


def test_add():
    assert Calculator.add(5, 23) == 28


def test_subtract():
    assert Calculator.subtract(103, 3) == 100


def test_multiply():
    assert Calculator.multiply(43, 5) == 215


def test_divide():
    assert Calculator.divide(200, 4) == 50


def test_divide_by_zero():
    with pytest.raises(ValueError):
        Calculator.divide(10, 0)