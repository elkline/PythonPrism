import unittest
import cast
import data

if __name__ == '__main__':
    min_x = -10
    max_x = 10
    min_y = -7.5
    max_y = 7.5
    width = 512
    height = 384
    eye_point = data.Point(0, 0, -14)
    sphere_list = [data.Sphere(data.Point(1.0, 1.0, 0.0), 2.0, data.Color(0, 0, 255), data.Finish(0.2, 0.4, 0.5, 0.05)),
                   data.Sphere(data.Point(0.5, 1.5, -3.0), 0.5, data.Color(255, 0, 0),
                               data.Finish(0.4, 0.4, 0.5, 0.05))]
    color_ambient = data.Color(255, 255, 255)
    light = data.Light(data.Point(-100.0, 100.0, -100.0), data.Color(500, 500, 500))

    cast.cast_all_rays(min_x, max_x, min_y, max_y, width, height, eye_point, sphere_list, color_ambient, light)
