import utility.utility


class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __eq__(self, other):
        return utility.utility.epsilon_equal(self.x, other.x) and utility.utility.epsilon_equal(self.y,
                                                                                                other.y) and utility.utility.epsilon_equal(
            self.z, other.z)

    def __ne__(self, other):
        return (self.x != other.x) or (self.y != other.y) or (self.z != other.z)


class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __eq__(self, other):
        return utility.utility.epsilon_equal(self.x, other.x) and utility.utility.epsilon_equal(self.y,
                                                                                                other.y) and utility.utility.epsilon_equal(
            self.z, other.z)

    def __ne__(self, other):
        return (self.x != other.x) or (self.y != other.y) or (self.z != other.z)


# zip files to submit

class Ray:
    def __init__(self, pt, dir):
        self.pt = pt
        self.dir = dir


class Sphere:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius
