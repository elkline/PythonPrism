import unittest
import data
import vector_math


class TestCases(unittest.TestCase):

    def test_point_equality(self):
        pt1 = data.Point(1, 2, 3)
        pt2 = data.Point(1, 2, 3)
        self.assertEqual(pt1, pt2)

    def test_vector_equality(self):
        vector1 = data.Vector(4, 5, 6)
        vector2 = data.Vector(4, 5, 6)
        self.assertEqual(vector1, vector2)

    def test_ray_equality(self):
        ray1 = data.Ray((data.Point(1, 2, 3)), (data.Vector(3, 4, 5)))
        ray2 = data.Ray((data.Point(1, 2, 3)), (data.Vector(3, 4, 5)))
        self.assertEqual(ray1, ray2)

    def test_sphere_equality(self):
        sphere1 = data.Sphere((data.Point(0, 0, 0)), 4)
        sphere2 = data.Sphere((data.Point(0, 0, 0)), 4)
        self.assertEqual(sphere1, sphere2)

    def test_scale_vector_1(self):
        vector1 = data.Vector(2, 4, 6)
        vector2 = data.Vector(6, 12, 18)
        self.assertEqual(vector2, vector_math.scale_vector(vector1, 3))

    def test_scale_vector_2(self):
        vector1 = data.Vector(2, 4, 6)
        vector2 = data.Vector(0, 0, 0)
        self.assertEqual(vector2, vector_math.scale_vector(vector1, 0))

    def test_dot_vector_1(self):
        vector1 = data.Vector(1, 2, 3)
        vector2 = data.Vector(3, 4, 5)
        dot_vector = data.Vector(3, 8, 15)
        self.assertEqual(vector_math.dot_vector(vector1, vector2), dot_vector)

    def test_dot_vector_2(self):
        vector1 = data.Vector(1, 2, 3)
        vector2 = data.Vector(0, 4, 5)
        dot_vector = data.Vector(0, 8, 15)
        self.assertEqual(vector_math.dot_vector(vector1, vector2), dot_vector)

    def test_length_vector(self):
        vector1 = data.Vector(1, 2, 3)
        length = 3.741657387
        self.assertAlmostEqual(vector_math.length_vector(vector1), length, 8)

    def test_normalize_vector_1(self):
        vector1 = data.Vector(1, 2, 3)
        normalized_vector = data.Vector(0.2672612419, 0.5345224838, 0.8017837257)
        self.assertAlmostEqual(vector_math.normalize_vector(vector1), normalized_vector)
        # what happens when the magnitude is 0 ?

    def test_normalize_vector_2(self):
        vector1 = data.Vector(0, 0, 0)
        normalized_vector = data.Vector(0, 0, 0)
        self.assertAlmostEqual(vector_math.normalize_vector(vector1), normalized_vector)

    def test_difference_point(self):
        pt1 = data.Point(1, 2, 3)
        pt2 = data.Point(3, 4, 5)
        difference_point = data.Vector(-2, -2, -2)
        self.assertEqual(vector_math.difference_point(pt1, pt2), difference_point)

    def test_difference_vector(self):
        vector1 = data.Vector(1, 2, 3)
        vector2 = data.Vector(3, 4, 5)
        difference_vector = data.Vector(-2, -2, -2)
        self.assertEqual(vector_math.difference_vector(vector1, vector2), difference_vector)

    def test_translate_point_1(self):
        pt1 = data.Point(1, 2, 3)
        vector1 = data.Vector(3, 4, 5)
        translated_point = data.Point(4, 6, 8)
        self.assertEqual(vector_math.translate_point(pt1, vector1), translated_point)

    def test_translate_point_2(self):
        pt1 = data.Point(1, 2, 3)
        vector1 = data.Vector(-3, -4, -5)
        translated_point = data.Point(-2, -2, -2)
        self.assertEqual(vector_math.translate_point(pt1, vector1), translated_point)

    def test_vector_from_to(self):
        pt1 = data.Point(1, 2, 3)
        pt2 = data.Point(3, 4, 5)
        difference_point = data.Vector(-2, -2, -2)
        self.assertEqual(vector_math.difference_point(pt1, pt2), difference_point)


if __name__ == "__main__":
    unittest.main()
