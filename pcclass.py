
def _float_add(a, b):
    return float(a + b)

class Pc:
    def __eq__(self, other):
        return self.value == other.value

class PcInt(Pc):
    def __init__(self, v):
        self.value = int(v)

    def add(self, v):
        return v._add_int(self)

    def _add_int(self, int_o):
        return self._prim_add(int_o)

    def _prim_add(self, int_o):
        if self.__class__.__name__ != 'PcInt':
            raise TypeError('self is not PcInt')
        if int_o.__class__.__name__ != 'PcInt':
            raise TypeError('int_o is not PcInt')
        return PcInt(self.value + int_o.value)

    def _add_float(self, float_o):
        return PcFloat(_float_add(self.value, float_o.value))

    def __str__(self):
        return str(self.value)

class PcFloat(Pc):
    def __init__(self, v):
        self.value = float(v)

    def __str__(self):
        return str(self.value)

    def add(self, v):
        return v._add_float(self)

    def _add_float(self, v):
        return PcFloat(_float_add(self.value, v.value))

    def _add_int(self, pcint):
        f = PcFloat(pcint.value)
        return PcFloat(_float_add(self.value, f.value))

