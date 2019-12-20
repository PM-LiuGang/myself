from CreditCard import CreditCard

class PredatoryCreditCard(CreditCard):

    def __init__(self, customer, bank, acnt, limit, apr):
        super().__init__(customer, bank, acnt, limit)
        self._apr = apr
        self.times = 0
        # self._balance = 0 可以不用说明，继承父类的属性

    def charge(self, price):
        success = super().charge(price)
        # C228
        if self.times < 10:
            self.times += 1
        else:
            self._balance += 1

        if not success:
            self._balance += 5
        return success

    def process_month(self):
        if self._balance > 0:
            monthly_factor = pow(1 + self._apr, 1/12)
            self._balance *= monthly_factor

if __name__ == '__main__':
    pc1 = PredatoryCreditCard('liu', 'unknow', 2121, 5000, 0.01)
    # for i in range(10, 50):
    #     pc1.charge(i * 11)
    # print(pc1.get_balance())  # 为什么不自动补全呢

    for i in range(1,15):
        pc1.charge(i)  # +5 * 3
    print(pc1.get_balance())
    # pc1.process_month()
    # print(pc1.get_balance())