import data
import vector_math
import math


def sphere_intersection_point(ray, sphere):
    # returns Point object with coordinates of nearest intersection point or none if the point is not valid
    a = vector_math.dot_vector(ray.dir, ray.dir)
    b = 2 * (vector_math.dot_vector((vector_math.difference_point(ray.pt, sphere.center)), ray.dir))
    c = (vector_math.dot_vector((vector_math.difference_point(ray.pt, sphere.center)),
                                vector_math.difference_point(ray.pt, sphere.center))) - sphere.radius ** 2

    discriminant = ((b ** 2) - 4 * a * c)

    if discriminant < 0:
        return None

    if a is not 0:
        t1 = ((-b) + math.sqrt((b ** 2) - 4 * a * c)) / (2 * a)
        t2 = ((-b) - math.sqrt((b ** 2) - 4 * a * c)) / (2 * a)

        if t1 >= 0 and t2 >= 0:
            return vector_math.translate_point(ray.pt, vector_math.scale_vector(ray.dir, min(t1, t2)))

        if t1 < 0 and t2 < 0:
            return None

        if t1 < 0 or t2 < 0:
            return vector_math.translate_point(ray.pt, vector_math.scale_vector(ray.dir, max(t1, t2)))

        if discriminant == 0:
            return vector_math.translate_point(ray.pt, vector_math.scale_vector(ray.dir, t1))

    return None


def find_intersection_points(sphere_list, ray):
    list1 = []
    for i in range(0, len(sphere_list)):
        if sphere_intersection_point(ray, sphere_list[i]) is not None:
            list1.append((sphere_list[i], sphere_intersection_point(ray, sphere_list[i])))
    return list1


def translated_intersection_points(sphere_list, ray):
    list1 = []
    for i in range(0, len(sphere_list)):
        if sphere_intersection_point(ray, sphere_list[i]) is not None:
            intersection_point = sphere_intersection_point(ray, sphere_list[i])
            scaled_sphere_normal = vector_math.scale_vector(sphere_normal_at_point(sphere_list[i], intersection_point),
                                                            0.01)
            translated_point = vector_math.translate_point(intersection_point, scaled_sphere_normal)
            list1.append((sphere_list[i], translated_point))
    return list1


def sphere_normal_at_point(sphere, point):
    vector_between_points = vector_math.vector_from_to(sphere.center, point)
    return vector_math.normalize_vector(vector_between_points)
