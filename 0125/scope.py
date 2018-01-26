# http://coreblog.org/ats/stuff/minpy_support/samplecodes04/samplecodes/Chapter09/09-01.html
# ? アトリビュートって？？
class Klass:
    a = 100

def main():
    i1 = Klass()
    i2 = Klass()
    print(i1.a,i2.a)
    i1.a = 10
    Klass().a = 1000
    print(i1.a,i2.a)

if __name__ == "__main__":
    main()
