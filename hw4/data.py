import utility
import math


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

    def __str__(self, other):
        return "({x}, {y}, {z})"

    def distance(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2)


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
    def __init__(self, center, radius, color, finish):
        self.center = center
        self.radius = radius
        self.color = color
        self.finish = finish  # finish object

    def __eq__(self, other):
        return utility.epsilon_equal(self.center.x, other.center.x) and utility.epsilon_equal(self.center.y,
                                                                                              other.center.y) and utility.epsilon_equal(
            self.center.z, other.center.z) and utility.epsilon_equal(self.radius,
                                                                     other.radius) and self.color == other.color and self.finish == other.finish


class Color:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def __eq__(self, other):
        return self.r == other.r and self.g == other.g and self.b == other.b

    def __str__(self):
        return str(self.r) + " " + str(self.g) + " " + str(self.b)


class Finish:
    # ambient: the percentage of ambient light reflected by the finish
    # specular: percentage of specular light reflected by the finish
    # roughness: roughness of the finish (affects the spread of the light across the object)
    def __init__(self, ambient, diffuse, specular, roughness):
        self.ambient = ambient
        self.diffuse = diffuse
        self.specular = specular
        self.roughness = roughness

    def __eq__(self, other):
        return utility.epsilon_equal(self.ambient, other.ambient) and utility.epsilon_equal(self.diffuse, other.diffuse) and utility.epsilon_equal(self.specular, other.specular) and utility.epsilon_equal(self.roughness, other.roughness)


class Light:
    # point represents the position of the light, color represents the color/intensity of the light
    def __init__(self, pt, color):
        self.pt = pt
        self.color = color

    def __eq__(self, other):
        return utility.epsilon_equal(self.pt, other.pt) and self.color == other.color
