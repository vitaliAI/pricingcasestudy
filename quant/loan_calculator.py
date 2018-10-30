class LoanCalculator(object):
    """
    Loan Payment = Amount / Discount Factor
    P = A / D

    To calculate the discount factor,
    loan payment, total credit and total interest we need the following arguments

    N number of the periodic payments  = Payments per year times number of years
    Periodic Interest Rate (i) = APR divided by 12
    Discount Factor (D) = {[(1 + i) ^n] - 1} / [i(1 + i)^n]
    """

    def __init__(self, amount, period, apr, start=1, end=1):
        self.months = 12
        self.amount = amount
        self.period = period
        self.apr = apr
        self.i = self.apr / (self.months * 100)
        self.start = start
        self.end = end
        self.special_case = False
        if start != end:
            self.special_case = True

    def discount_factor(self):
        i = self.i
        discount_factor_v = (((1 + i) ** self.period) - 1) / (i * (1 + i) ** self.period)
        return discount_factor_v

    def loan_payment(self):
        if not self.special_case:
            return round(self.amount / self.discount_factor(), 2)
        else:
            fv = self.future_value(self.first_month_interest())
            i = self.apr / (100 * 12)
            return round(self.present_value(fv, i) / self.discount_factor(), 2)

    def total_credit(self):
        return round(self.loan_payment() * self.period, 2)

    def total_interest(self):
        return round(self.total_credit() - self.amount, 2)

    def first_months_days_to_pay(self):
        delta_days = 0
        if self.start < self.end:
            delta_days = self.end - self.start
        elif self.start > self.end:
            delta_days = 31 - self.start + self.end
        return delta_days

    def first_month_interest(self):
        i_daily = self.i / (31 * 100)
        i_first_month = i_daily * self.first_months_days_to_pay()
        return i_first_month

    def future_value(self, i, n=1):
        fv = self.amount * (1 + i) ** n
        return fv

    def present_value(self, fv, i, n=1):
        pv = fv * (1 / (1 + i) ** n)
        return pv

    def display_all_information(self):
        if not self.special_case:
            print("\n")
            print("---- Normal Loan Case ----\n")
            print("Annuity: ", round(self.amount / self.discount_factor(), 2))
            print("Total Credit: ", self.total_credit())
            print("Total Interest: ", self.total_interest())
        else:
            fv = self.future_value(self.first_month_interest())
            print("\n")
            print("---- Special Loan Case ----\n")
            print("Monthly Interest Rate: ", self.i)
            print("Present Value: ", round(self.present_value(fv, self.i), 2))
            print("Annuity: ", round(self.present_value(fv, self.i) / self.discount_factor(), 2))
            print("Total Credit: ", self.total_credit())
            print("Total Interest: ", self.total_interest())
            print("Days in the first month: ", self.first_months_days_to_pay())