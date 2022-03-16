import unittest
import cast
import data
import vector_math
import collisions


class TestCases(unittest.TestCase):

    # Test for Part1

    # def test_cast_ray(self):
    #     sphere1 = data.Sphere(data.Point(1, 1, 1), 2, data.Color(0, 0, 255), data.Finish(0.2))
    #     sphere2 = data.Sphere(data.Point(0.5, 1.5, -3.0), 0.5, data.Color(255, 0, 0), data.Finish(0.4))
    #     sphere_list = [sphere1, sphere2]
    #     vector_in_ray = vector_math.vector_from_to(data.Point(0, 0, -14), data.Point(1, 1, 0))
    #     ray = data.Ray(data.Point(0, 0, -14), vector_in_ray)
    #     self.assertEqual(cast.cast_ray(ray, sphere_list, data.Color(255, 255, 255)), True)

    def test_cast_ray(self):
        ray = data.Ray(data.Point(0.0, 0.0, 0.0), data.Vector(5.0, 0.0, 0.0))
        ambient = data.Color(255, 255, 255)
        sphere1 = data.Sphere(data.Point(5.0, 0, -5.0), 5.0, data.Color(255, 0, 0), data.Finish(0.2, 0.4, 0.5, 0.05))
        sphere2 = data.Sphere(data.Point(17.0, 0, 5.0), 5.0, data.Color(0, 0, 255), data.Finish(0.4, 0.4, 0.5, 0.05))
        sphere_list = [sphere1, sphere2]
        point_color = cast.cast_ray(ray, sphere_list, ambient)
        self.assertEqual(point_color, data.Color(51, 0, 0))

    def test_sphere_intersection_point(self):
        self.assertEqual(collisions.sphere_intersection_point(data.Ray(data.Point(2, 0, 0), data.Vector(8, 0, 0)),
                                                              data.Sphere(data.Point(7, 0, 0), 4,
                                                                          data.Color(255, 255, 255), data.Finish(0.2))),
                         data.Point(3, 0, 0))

    # function not used in this part

    # def test_nearest_sphere(self):
    #     sphere1 = data.Sphere(data.Point(1.0, 1.0, 0.0), 2.0, data.Color(0, 0, 255), data.Finish(0.2))
    #     sphere2 = data.Sphere(data.Point(0.5, 1.5, -3.0), 0.5, data.Color(255, 0, 0), data.Finish(0.4))
    #     eye_point = data.Point(0, 0, -14)
    #     ray = data.Ray(eye_point, vector_math.vector_from_to(eye_point, data.Point(10.0003, 4.26192, 0)))
    #     ts = collisions.find_intersection_points([sphere1, sphere2], ray)
    #     self.assertEqual(cast.nearest_sphere(ts, ray.pt), sphere2)

    def test_find_visibility(self):
        sphere1 = [data.Sphere(data.Point(1.0, 1.0, 0.0), 2.0, data.Color(0, 0, 255), data.Finish(0.4, 0.4, 0.5, 0.05))]
        intersection_point = data.Point(0.6386425853061297, 2.892675239327764, -0.5359116133107715)
        info_tuple = (sphere1, intersection_point)
        light = data.Light(data.Point(-100.0, 100.0, -100.0), data.Color(500, 500, 500))
        diffuse_contribution = [0.0, 0.0, 159.34431710317705]
        self.assertEqual(cast.find_visibility(sphere1, info_tuple, light), diffuse_contribution)

    def test_find_specular_contribution(self):
        sphere1 = [data.Sphere(data.Point(1.0, 1.0, 0.0), 2.0, data.Color(0, 0, 255), data.Finish(0.4, 0.4, 0.5, 0.05))]
        intersection_point = data.Point(0.6386425853061297, 2.892675239327764, -0.5359116133107715)
        info_tuple = (sphere1, intersection_point)
        eye_point = data.Point(0, 0, -14)
        light = data.Light(data.Point(-100.0, 100.0, -100.0), data.Color(500, 500, 500))
        diffuse_contribution = [0, 0, 0]
        self.assertEqual(cast.find_specular_contribution(info_tuple, light, eye_point), diffuse_contribution)
