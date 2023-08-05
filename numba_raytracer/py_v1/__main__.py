from enum import StrEnum

import typer
from PIL import Image

from . import ray, vec

app = typer.Typer()


def hit_sphere(center: vec.Vec, radius: float, ray: ray.Ray) -> bool:
    oc = vec.sub(ray.origin, center)
    a = vec.dot(ray.direction, ray.direction)
    b = 2.0 * vec.dot(oc, ray.direction)
    c = vec.dot(oc, oc) - radius * radius
    discriminant = b * b - 4 * a * c
    return discriminant > 0


def color_hello(ray: ray.Ray) -> vec.Vec:
    unit_direction = vec.unit(ray.direction)
    t = 0.5 * (unit_direction.y + 1.0)
    return vec.sum(
            vec.mul_num(vec.Vec(1.0, 1.0, 1.0), 1 - t),
            vec.mul_num(vec.Vec(0.5, 0.7, 1.0), t))


def color_sphere(ray: ray.Ray) -> vec.Vec:
    if hit_sphere(vec.Vec(0, 0, -1), 0.5, ray):
        return vec.Vec(1, 0, 0)
    unit_direction = vec.unit(ray.direction)
    t = 0.5 * (unit_direction.y + 1.0)
    return vec.sum(
            vec.mul_num(vec.Vec(1.0, 1.0, 1.0), 1 - t),
            vec.mul_num(vec.Vec(0.5, 0.7, 1.0), t))


Mode = StrEnum("Mode", ["Hello", "Sphere"])


def run_raytrace(color_fun) -> Image.Image:
    NX = 2000
    NY = 1000
    img = Image.new("RGB", (NX, NY))
    lower_left_corner = vec.Vec(-2, -1, -1)
    horizontal = vec.Vec(4, 0, 0)
    vertical = vec.Vec(0, 2, 0)
    origin = vec.Vec(0, 0, 0)
    for j in range(NY):
        for i in range(NX):
            u = i / NX
            v = j / NY
            r = ray.Ray(
                    origin,
                    vec.sum(lower_left_corner,
                        vec.sum(vec.mul_num(horizontal, u),
                                vec.mul_num(vertical, v))))
            col = color_fun(r)
            ir = int(255.99 * col.x)
            ig = int(255.99 * col.y)
            ib = int(255.99 * col.z)
            img.putpixel((i, NY - j - 1), (ir, ig, ib))
    return img


@app.command()
def run(mode: Mode = typer.Argument("Hello", help="Image mode") ):
    img = run_raytrace
    match mode:
        case Mode.Sphere:
            img = run_raytrace(color_sphere)
        case _:
            img = run_raytrace(color_hello)
    img.save("out.png")


app()
