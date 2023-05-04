from datetime import date
from calendar import monthrange


def add_months(source_date, months):
    # From: https://stackoverflow.com/questions/4130922/how-to-increment-datetime-by-custom-months-in-python-without-using-library
    month = source_date.month - 1 + months
    year = source_date.year + month // 12
    month = month % 12 + 1
    day = min(source_date.day, monthrange(year, month)[1])
    return date(year, month, day)


class AmortizationTable:
    term = None
    interest_rate = None
    loan_start_date = None
    loan_amount = None
    down_payment = None

    schedule = None
    __current_balance = None
    __current_month = None

    def __init__(self,
                 term=360,
                 interest_rate=0.0527,
                 loan_start_date=date(2023, 4, 1),
                 loan_amount=330000,
                 down_payment=0):
        self.term = term
        self.interest_rate = interest_rate
        self.loan_start_date = loan_start_date
        self.loan_amount = loan_amount
        self.down_payment = down_payment

        self.schedule = []

    def monthly_payment(self):
        return (self.interest_rate / 12) * \
            (1 / (1 - (1 + self.interest_rate / 12) ** (-self.term))) * \
            (self.loan_amount - self.down_payment)

    def calculate(self):
        current_balance = self.loan_amount - self.down_payment

        print(self.loan_amount, current_balance)
        current_month = 0
        while current_balance > 0:
            current_month += 1
            current_interest = current_balance * (self.interest_rate / 12)
            current_principal = self.monthly_payment() - current_interest
            ending_balance = current_balance - current_principal

            self.schedule.append(
                {
                    'current_month': add_months(self.loan_start_date, current_month),
                    'current_balance': current_balance,
                    'current_interest': current_interest,
                    'current_principal': current_principal,
                    'ending_balance': abs(ending_balance)
                }
            )

            # Now that we reported what the payment looks like,
            # actually deduct it from the current balance.
            current_balance -= current_principal
