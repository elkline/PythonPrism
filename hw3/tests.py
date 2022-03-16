import unittest
import collisions
import vector_math
import data


class TestCases(unittest.TestCase):

    def test_sphere_intersection_point_1(self):
        ray = data.Ray(data.Point(2, 0, 0), data.Vector(8, 0, 0))
        sphere = data.Sphere(data.Point(7, 0, 0), 4)
        self.assertEqual(collisions.sphere_intersection_point(ray, sphere), data.Point(3, 0, 0))

    def test_sphere_intersection_point_2(self):
        self.assertEqual(collisions.sphere_intersection_point(data.Ray(data.Point(2, 0, 0), data.Vector(8, 0, 0)), data.Sphere(data.Point(7, 0, 0), 4)), data.Point(3, 0, 0))

    def test_sphere_intersection_point_3(self):
        ray = data.Ray(data.Point(2.4, 1, 0), data.Vector(6, 2.5, 0))
        sphere = data.Sphere(data.Point(12, 5, 0), 3)
        intersection = collisions.sphere_intersection_point(ray, sphere)
        self.assertEqual(intersection, data.Point(9.23076, 3.84615, 0))

    def test_find_intersection_point_1(self):
        sphere1 = data.Sphere(data.Point(7, 0, 0), 4)
        sphere2 = data.Sphere(data.Point(6, 0, 0), 4)
        ray = data.Ray(data.Point(0, 0, 0), data.Vector(10, 0, 0))
        self.assertEqual(collisions.find_intersection_points([sphere1, sphere2], ray), [(sphere1, data.Point(3, 0, 0)), (sphere2, data.Point(2, 0, 0))])

    def test_find_intersection_point_2(self):
        sphere3 = data.Sphere(data.Point(0, 5, 0), 3)
        sphere4 = data.Sphere(data.Point(0, 0, 0), 2)
        ray = data.Ray(data.Point(0, -2, 0), data.Vector(0, 7, 0))
        self.assertEqual(collisions.find_intersection_points([sphere3, sphere4], ray), [(sphere3, data.Point(0, 2, 0)), (sphere4, data.Point(0, -2, 0))])

    def test_normalize_1(self):
        sphere1 = data.Sphere(data.Point(7, 0, 0), 4)
        point = data.Point(3, 0, 0)
        self.assertEqual(collisions.sphere_normal_at_point(sphere1, point), data.Vector(-1.0, 0.0, 0.0))

    def test_sphere_normal_at_point_2(self):
        sphere1 = data.Sphere(data.Point(7, 12, 15), 4)
        point1 = data.Point(13, 20, 33)
        self.assertTrue(collisions.sphere_normal_at_point(sphere1, point1), data.Vector(31, 40, 22))