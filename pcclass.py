
def _int_add(a, b):
    return int(a + b)

def _float_add(a, b):
    return float(a + b)

class Pc:
    pass

class PcInt:
    def __init__(self, v):
        self.value = int(v)

    def add(self, v):
        return v._add_int(self)

    def _add_int(self, int_o):
        return PcInt(_int_add(self.value, int_o.value))

    def _add_float(self, float_o):
        return PcFloat(_float_add(self.value, float_o.value))

    def __cmp__(self, other):
        return self.value <> other.value

    def __str__(self):
        return self.value

class PcFloat:
    def __init__(self, v):
        self.value = float(v)

    def __cmp__(self, other):
        return self.value <> other.value

    def __str__(self):
        return self.value

    def add(self, v):
        return v._add_float(self)

    def _add_float(self, v):
        return PcFloat(_float_add(self.value, v.value))

    def _add_int(self, pcint):
        f = PcFloat(pcint.value)
        return PcFloat(_float_add(self.value, f.value))

