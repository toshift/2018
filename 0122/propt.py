class PropCheckA(object):
    def __init__(self, a, b):
        self._param_a = a
        self._param_b = b

    @property
    def param_property(self):
        return self._param_a, self._param_b


class PropCheckB(object):
    def __init__(self, c):
        self._param_c = c

    @property
    def param_property(self):
        return self._param_c


if __name__ == "__main__":
    propA = PropCheckA(1, 2)
    print(propA.param_property)

    propB = PropCheckB(3)
    print(propB.param_property)
    try:
        propA.param_a = 3
        print(propA.param_property)
    except Exception as e:
        print(e)
    try:
        propB.param_c = 4
        print(propB.param_property)
    except Exception as e:
        print(e)
