import unittest

from datetime import datetime, timedelta

nowtime = datetime.now()
sumamount = 0
class CreditCard:

    # nowtime = datetime.now() # 为什么报错
    def __init__(self, customer, bank, acnt, limit, balance=0):
        self._customer = customer
        self._bank = bank
        self._accont = acnt
        self._limit = limit
        # R27
        self._balance = balance

    def get_customer(self):
        return self._customer

    def get_bank(self):
        return self._balance

    def get_account(self):
        return self._accont

    def get_limit(self):
        return self._limit

    # def get_balance(self):
    #     return self._balance

    def charge(self, price):
        # R25
        if not isinstance(price, (int, float)):
            raise TypeError('Price Must Be Numeric.')
        # R26
        elif price < 0:
            raise ValueError('Price Cannot Be Negative.')

        if price + self._balance > self._limit:
            return False
        else:
            self._balance += price
            return True

    def make_payment(self, amount):
        min_makepayment = self._limit * 0.1
        # R25
        if not isinstance(amount, (int, float)):
            raise TypeError('Price Must Be Numeric.')
        # R26
        elif amount < 0:
            raise ValueError('Price Cannot Be Negative.')

        self._balance -= amount
        sumamount += amount

    def _set_balance(self, value):
        self._balance = value
#C229
# while True:
#     if (datetime.now()).day() == 28:
#         if sumamount < min_makepayment:
#             pass


class TestCreitCard(unittest.TestCase):

    # def setUp(self):
    #     pass

    def test_charge(self):
        liugang = CreditCard('liugang', 'Bank', 5399, 2500, 100)
        liugang.charge(100)
        self.assertEqual(liugang.get_balance(), 200)

    def test_make_payment(self):
        liugang = CreditCard('liugang', 'Bank', 5399, 2500, 100)
        liugang.charge(100)
        liugang.make_payment(20)
        self.assertEqual(liugang.get_balance(), 180)

    def test_charge_exception_value(self):
        liugang = CreditCard('liugang', 'Bank', 5399, 2500, 100)
        with self.assertRaises(ValueError):
            liugang.charge(-1)

    def test_charge_exception_type(self):
        liugang = CreditCard('liugang', 'Bank', 5399, 2500, 100)
        with self.assertRaises(TypeError):
            liugang.charge('liugang')

    def test_payment_exception_value(self):
        liugang = CreditCard('liugang', 'Bank', 5399, 2500, 100)
        with self.assertRaises(ValueError):
            liugang.make_payment(-1)

    def test_payment_exception_type(self):
        liugang = CreditCard('liugang', 'Bank', 5399, 2500, 100)
        with self.assertRaises(TypeError):
            liugang.make_payment('liugang')

if __name__ == '__main__':
    unittest.main()
