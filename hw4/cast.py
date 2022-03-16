import collisions
import data
import vector_math


# finds diffuse value for each intersection point for the sphere in the tuple
def find_diffusion(sphere_list, info_tuple, light):
    diffuse_contribution = [0.0, 0.0, 0.0]
    sphere_normal = (collisions.sphere_normal_at_point(info_tuple[0], info_tuple[1]))
    scale_normal = vector_math.scale_vector(sphere_normal, 0.01)
    p = vector_math.translate_point(info_tuple[1], scale_normal)
    p_to_light = vector_math.normalize_vector(vector_math.vector_from_to(p, light.pt))
    dot_product = vector_math.dot_vector(sphere_normal, p_to_light)

    if dot_product < 0:
        return diffuse_contribution

    checking_ray = data.Ray(p, p_to_light)
    if collisions.find_intersection_points(sphere_list, checking_ray) != []:
        ts2 = collisions.find_intersection_points(sphere_list, checking_ray)
        for info in ts2:
            if info[1].distance(light.pt) < info_tuple[1].distance(light.pt):
                return diffuse_contribution
    else:
        # calculate diffuse contribution
        diffuse_contribution[0] = dot_product * light.color.r * info_tuple[0].color.r * info_tuple[0].finish.diffuse
        diffuse_contribution[1] = dot_product * light.color.g * info_tuple[0].color.g * info_tuple[0].finish.diffuse
        diffuse_contribution[2] = dot_product * light.color.b * info_tuple[0].color.b * info_tuple[0].finish.diffuse
        return diffuse_contribution


def find_specular_contribution(info_tuple, light, eye_point):
    specular_contribution = [0, 0, 0]
    sphere_normal = (collisions.sphere_normal_at_point(info_tuple[0], info_tuple[1]))
    scale_normal = vector_math.scale_vector(sphere_normal, 0.01)
    p = vector_math.translate_point(info_tuple[1], scale_normal)
    p_to_light = vector_math.normalize_vector(vector_math.vector_from_to(p, light.pt))
    dot_product = vector_math.dot_vector(sphere_normal, p_to_light)

    reflection_vector = vector_math.difference_vector(p_to_light,
                                                      vector_math.scale_vector(sphere_normal, (2 * dot_product)))

    eye_to_p = vector_math.normalize_vector(vector_math.vector_from_to(eye_point, p))

    specular_intensity = vector_math.dot_vector(reflection_vector, eye_to_p)

    if specular_intensity < 0:
        return specular_contribution

    else:
        specular_contribution[0] = light.color.r * info_tuple[0].finish.specular * pow(specular_intensity, (1 / info_tuple[0].finish.roughness))
        specular_contribution[1] = light.color.g * info_tuple[0].finish.specular * pow(specular_intensity, (1 / info_tuple[0].finish.roughness))
        specular_contribution[2] = light.color.b * info_tuple[0].finish.specular * pow(specular_intensity, (1 / info_tuple[0].finish.roughness))
        return specular_contribution


def cast_ray(ray, sphere_list, ambient_light_color, light, point):
    ts = collisions.find_intersection_points(sphere_list, ray)

    if ts != []:
        for info in ts:  # for each tuple in intersection points
            diffuse = find_diffusion(sphere_list, info, light)
            specular = find_specular_contribution(info, light, point)
            r = int((((info[0].color.r * ambient_light_color.r + diffuse[0] + specular[0]) // 255) * info[0].finish.ambient))
            g = int((((info[0].color.g * ambient_light_color.g + diffuse[1] + specular[1]) // 255) * info[0].finish.ambient))
            b = int((((info[0].color.b * ambient_light_color.b + diffuse[2] + specular[2]) // 255) * info[0].finish.ambient))
        return data.Color(r, g, b)
    else:
        return data.Color(255, 255, 255)


def cast_all_rays(min_x, max_x, min_y, max_y, width, height, eye_point, sphere_list, color_ambient, light):
    x_spacing = (max_x - min_x) / width
    y_spacing = (max_y - min_y) / height

    image_file = open('image.ppm', 'w')

    image_file.write('P3\n')
    image_file.write(str(width) + " " + str(height) + "\n")
    image_file.write('255\n')
    for h in range(height, 0, -1):
        for w in range(width):
            x = min_x + w * x_spacing
            y = min_y + h * y_spacing
            ray = data.Ray(eye_point, vector_math.vector_from_to(eye_point, data.Point(x, y, 0)))

            color = cast_ray(ray, sphere_list, color_ambient, light, eye_point)
            image_file.write(color.__str__() + "\n")
    image_file.close()


if __name__ == '__main__':
    cast_all_rays(-4, 4, -2, 2, 4, 2, data.Point(0, 0, 0),
                  [data.Sphere(data.Point(0, 0, 0), 4, data.Color(1.0, 1.0, 1.0))])
