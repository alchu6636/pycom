
def _float_add(a, b):
    return float(a + b)

class PcLiteral:
    def __eq__(self, other):
        return self.value == other.value

    def __str__(self):
        return str(self.value)

    def type_check(self, name, first, second):
        if first.__class__.__name__ != name:
            raise TypeError('first parameter is not '+name)
        if second.__class__.__name__ != name:
            raise TypeError('second parameter is not '+name)

class PcInt(PcLiteral):
    def __init__(self, v):
        self.value = int(v)

    def add(self, v):
        return v._add_int(self)

    def _add_int(self, int_o):
        return self._prim_add(int_o)

    def _add_float(self, float_o):
        return self._as_float()._add_float(float_o)

    def _prim_add(self, int_o):
        PcLiteral().type_check('PcInt', self, int_o)
        return PcInt(self.value + int_o.value)

    def _as_float(self):
        return PcFloat(self.value)

class PcFloat(PcLiteral):
    def __init__(self, v):
        self.value = float(v)

    def add(self, v):
        return v._add_float(self)

    def _add_int(self, int_o):
        return self._add_float(int_o._as_float())

    def _add_float(self, v):
        return self._prim_add(v)

    def _prim_add(self, float_o):
        PcLiteral().type_check('PcFloat', self, float_o)
        return PcFloat(self.value + float_o.value)
