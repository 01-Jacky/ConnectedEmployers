class Data(object):
    """ Data Store Class """

    products = {
        'milk': {'price': 1.50, 'quantity': 10},
        'eggs': {'price': 0.20, 'quantity': 100},
        'cheese': {'price': 2.00, 'quantity': 10}
    }

    def __get__(self, obj, klas):
        print("(Fetching from Data Store)")
        return {'products': self.products}


class TestObj:
    a = 1
    b = 2

    def __init__(self, arg1, arg2):
        self.a = arg1;
        self.b = arg2;


class TestObj2:
    def __init__(self, arg1=0, arg2=0):
        self.a = arg1;
        self.b = arg2;


if __name__ == '__main__':
    myObj = TestObj()
    print(myObj.a)
    print(myObj.b)
