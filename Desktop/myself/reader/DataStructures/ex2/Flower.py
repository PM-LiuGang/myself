class Flower:

    def __init__(self, name=None, nums=None, prices=None):
        self._name = name
        self._nums = nums
        self._prices = prices

    def get_name(self):
        return self._name

    def get_num(self):
        return self._nums

    def get_price(self):
        return self._prices

    def set_name(self, name):
        self._name = name

    def set_num(self, num):
        self._nums = num

    def set_price(self, price):
        self._prices = price

if __name__ == '__main__':
    f1 = Flower()
    f1.set_name('name_f1')
    f1.set_num('num_fi')
    f1.set_price('price_f1')

    print(f1.get_name())
    print(f1.get_num())
    print(f1.get_price())