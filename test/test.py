import pytest
from app.calc import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_correct(self):
        assert self.calc.multiply(self, 2, 1) == 2

    def test_division_correct(self):
         assert self.calc.division(self, 6, 2) == 3

    def test_subtraction_correct(self):
         assert self.calc.subtraction(self, 5, 2) == 3


    def test_adding_correct(self):
        assert self.calc.adding(self, 4, 2) == 6


    def test_adding_failed(self):
        assert self.calc.adding(self, 2, 2) == 5