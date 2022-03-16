from hw3 import data
import math


def scale_vector(vector, scalar):
    new_vector = data.Vector((vector.x * scalar), (vector.y * scalar), (vector.z * scalar))
    return new_vector


def dot_vector(vector1, vector2):
    scalar_value = (vector1.x * vector2.x) + (vector1.y * vector2.y) + (vector1.z * vector2.z)
    return scalar_value


def length_vector(vector):
    magnitude = math.sqrt((vector.x ** 2) + (vector.y ** 2) +(vector.z ** 2))
    return magnitude


def normalize_vector(vector):
    # normalized vector = inverse of length * each vector component
    if length_vector(vector) == 0:
        vector_scalar = 0
    else:
        vector_scalar = 1 / (length_vector(vector))
    new_vector = scale_vector(vector, vector_scalar)
    return new_vector


def difference_point(point1, point2):
    new_vector = data.Vector((point1.x - point2.x), (point1.y - point2.y), (point1.z - point2.z))
    return new_vector


def difference_vector(vector1, vector2):
    new_vector = data.Vector((vector1.x - vector2.x), (vector1.y - vector2.y), (vector1.z - vector2.z))
    return new_vector


def translate_point(point, vector):
    new_point = data.Point((point.x + vector.x), (point.y + vector.y), (point.z + vector.z))
    return new_point


def vector_from_to(from_point, to_point):
    new_vector = data.Vector((to_point.x - from_point.x), (to_point.y - from_point.y), (to_point.z - from_point.z))
    return new_vector
