import unittest
import data


class TestData(unittest.TestCase):
    def test_point_1(self):
        pt1 = data.Point(3, 4, 5)
        self.assertAlmostEqual(pt1.x, 3)
        self.assertAlmostEqual(pt1.y, 4)
        self.assertAlmostEqual(pt1.z, 5)

    def test_point_2(self):
        pt2 = data.Point(1.2, 2.3, 3.4)
        self.assertAlmostEqual(pt2.x, 1.2)
        self.assertAlmostEqual(pt2.y, 2.3)
        self.assertAlmostEqual(pt2.z, 3.4)

    def test_vector_1(self):
        vector1 = data.Vector(1, 2, 3)
        self.assertAlmostEqual(vector1.x, 1)
        self.assertAlmostEqual(vector1.y, 2)
        self.assertAlmostEqual(vector1.z, 3)

    def test_vector_2(self):
        vector2 = data.Vector(5.6, 4.9, 3.4)
        self.assertAlmostEqual(vector2.x, 5.6)
        self.assertAlmostEqual(vector2.y, 4.9)
        self.assertAlmostEqual(vector2.z, 3.4)

    def test_ray_1(self):
        ray1 = data.Ray(data.Point(3, 4, 5), data.Vector(1, 2, 3))
        self.assertAlmostEqual(ray1.pt, data.Point(3, 4, 5))
        self.assertAlmostEqual(ray1.dir, data.Vector(1, 2, 3))

    def test_ray_2(self):
        ray2 = data.Ray(data.Point(1.2, 2.3, 3.4), data.Vector(4.2, 5.1, 6.9))
        self.assertAlmostEqual(ray2.pt, data.Point(1.2, 2.3, 3.4))
        self.assertAlmostEqual(ray2.dir, data.Vector(4.2, 5.1, 6.9))

    def test_sphere_1(self):
        sphere1 = data.Sphere(data.Point(6, 7, 8), 5.3)
        self.assertAlmostEqual(sphere1.center, data.Point(6, 7, 8))
        self.assertAlmostEqual(sphere1.radius, 5.3)

    def test_sphere_2(self):
        sphere2 = data.Sphere(data.Point(2, 4, 6), 3)
        self.assertAlmostEqual(sphere2.center, data.Point(2, 4, 6))
        self.assertAlmostEqual(sphere2.radius, 3)


if __name__ == "__main__":
    unittest.main()
