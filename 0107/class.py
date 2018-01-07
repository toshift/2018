class ClassA:
    def summ(self, x, y):
        return (x + y)

class ClassB:
    def summ(self, x, y):
        return (x - y)

if __name__ == '__main__':
    c = [ClassA(), ClassB()]
    for cls in c:
        print(cls.summ(1,2))
