import math

class Vector3D:
    __slots__ = ['x', 'y', 'z']

    def __init__(self, x=0, y=0, z=0):
        self.x, self.y, self.z = x, y, z

    def as_tuple(self):
        return (self.x, self.y, self.z)

    def __str__(self):
        return '({}, {}, {})'.format(*self.as_tuple())

    def __repr__(self):
        if self:
            return __class__.__name__ + str(self)
        else:
            return __class__.__name__ + '()'

    def __add__(self, other):
        return __class__(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return __class__(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        try:
            k = float(other)
        except (TypeError, ValueError):
            raise NotImplemented
        return __class__(self.x * k, self.y * k, self.z * k)
    
    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        k = float(other)
        return __class__(self.x / k, self.y / k, self.z / k)

    def __floordiv__(self, other):
        k = float(other)
        return __class__(self.x // k, self.y // k, self.z // k)

    def __abs__(self):
        return math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z)

    def __lt__(self, other):
        return abs(self).__lt__(abs(other))

    def __le__(self, other):
        return abs(self).__le__(abs(other))

    def __eq__(self, other):
        return self.as_tuple() == other.as_tuple()

    def __ne__(self, other):
        return self.as_tuple() != other.as_tuple()

    def __gt__(self, other):
        return abs(self).__gt__(abs(other))

    def __ge__(self, other):
        return abs(self).__ge__(abs(other))

    def __iter__(self):
        return iter(self.as_tuple())

    def __len__(self):
        return 3

    def __hash__(self):
        return hash(self.as_tuple())

    def __bool__(self):
        return self.as_tuple() != (0, 0, 0)

