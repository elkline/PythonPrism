import utility


class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __eq__(self, other):
        return utility.epsilon_equal(self.x, other.x) and utility.epsilon_equal(self.y,
                                                                                other.y) and utility.epsilon_equal(
            self.z, other.z)

    def __ne__(self, other):
        return (self.x != other.x) or (self.y != other.y) or (self.z != other.z)


class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __eq__(self, other):
        return utility.epsilon_equal(self.x, other.x) and utility.epsilon_equal(self.y,
                                                                                other.y) and utility.epsilon_equal(
            self.z, other.z)

    def __ne__(self, other):
        return (self.x != other.x) or (self.y != other.y) or (self.z != other.z)


# zip files to submit

class Ray:
    def __init__(self, pt, dir):
        self.pt = pt
        self.dir = dir

    def __eq__(self, other):
        return utility.epsilon_equal(self.pt.x, other.pt.x) and utility.epsilon_equal(self.pt.y,
                                                                                      other.pt.y) and utility.epsilon_equal(
            self.pt.z, other.pt.z) and utility.epsilon_equal(self.dir.x, other.dir.x) and utility.epsilon_equal(
            self.dir.y,
            other.dir.y) and utility.epsilon_equal(
            self.dir.z, other.dir.z)


class Sphere:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def __eq__(self, other):
        return utility.epsilon_equal(self.center.x, other.center.x) and utility.epsilon_equal(self.center.y,
                                                                                              other.center.y) and utility.epsilon_equal(
            self.center.z, other.center.z) and utility.epsilon_equal(self.radius, other.radius)
