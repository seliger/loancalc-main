### calculations.py - Python module to store all of my amortization functions
###

DOWN_PAYMENT = 0.10
INTEREST_RATE = 0.12
PAYMENT_PCT = 0.05

def getMonthlyPayment(currentBalance):
    monthlyPayment = currentBalance * PAYMENT_PCT

def getIntitialBalance(purchasePrice):
    return purchasePrice - purchasePrice * DOWN_PAYMENT

def getCurrentMonthlyInterest(currentBalance):
    return currentBalance * (INTEREST_RATE / 12)

