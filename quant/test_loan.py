from .loan_calculator import LoanCalculator
from unittest import TestCase


class LoanCalculatorTest(TestCase):
    def setUp(self):
        # Normal Case
        self.loan_1 = LoanCalculator(3000, 12, 12, 11, 11)
        # Special case
        self.loan_2 = LoanCalculator(3000, 12, 12, 2, 17)

    def test_loan_payment(self):
        annuity = self.loan_1.loan_payment()
        # Verify the Amount
        self.assertEqual(266.55, annuity)

    def test_loan_payment_2(self):
        annuity = self.loan_2.loan_payment()
        # Verify the Amount
        self.assertEqual(263.92, annuity)

    def test_days_first_month(self):
        days = self.loan_2.first_months_days_to_pay()
        self.assertEqual(15, days)
