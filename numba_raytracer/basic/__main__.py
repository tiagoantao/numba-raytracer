"""Ray tracer entry point."""
# mypy: ignore-errors
import numba
import numpy as np
import typer
from PIL import Image

app = typer.Typer()


# Note that typing confuses stuff - do not go deep
# Ray = NewType("Ray", npt.NDArray)
# Vec3 = NewType("Vec3", npt.NDArray)


def hit_sphere(center, radius, ray):
    """Hit sphere."""
    oc = ray[0] - center
    a = np.dot(ray[1], ray[1])
    b = 2.0 * np.dot(oc, ray[1])
    c = np.dot(oc, oc) - radius * radius
    discriminant = b * b - 4 * a * c
    return discriminant > 0


def color_sphere(ray):
    """Render a simple blue gradient with a sphere."""
    if hit_sphere(np.array([0, 0, -1]), 0.5, ray):
        return np.array([1, 0, 0], dtype=np.float64)
    unit_direction = ray[1] / np.linalg.norm(ray[1])
    t = 0.5 * (unit_direction[1] + 1.0)
    return np.array([1.0, 1.0, 1.0]) * (1 - t) + np.array([0.5, 0.7, 1.0]) * t


def run_raytrace():
    """Run the raytracer."""
    nx = 2000
    ny = 1000
    array = np.empty((nx, ny, 3), dtype=np.uint8)  # explain dtype requirement
    lower_left_corner = np.array([-2, -1, -1], dtype=np.float64)
    horizontal = np.array([4, 0, 0], dtype=np.float64)
    vertical = np.array([0, 2, 0], dtype=np.float64)
    origin = np.array([0, 0, 0], dtype=np.float64)
    for j in range(ny):
        for i in range(nx):
            u = i / nx
            v = j / ny
            ray = np.vstack((origin, lower_left_corner + horizontal * u + vertical * v))
            col = color_sphere(ray)
            ir = int(255.99 * col[0])
            ig = int(255.99 * col[1])
            ib = int(255.99 * col[2])
            array[i, ny - j - 1] = (ir, ig, ib)
    return array


@app.command()
def run_non_numba():
    """CLI entry point for non-Numba."""
    array = run_raytrace()
    # Explain why Image is not used in the numba function
    img = Image.fromarray(np.transpose(array, (1, 0, 2)))
    img.save("out.png")


@app.command()
def run_numba():
    """CLI entry point for Numba."""
    global hit_sphere, color_sphere
    hit_sphere = numba.njit()(hit_sphere)
    color_sphere = numba.njit()(color_sphere)
    array = numba.njit()(run_raytrace)()
    # Explain why Image is not used in the numba function
    img = Image.fromarray(np.transpose(array, (1, 0, 2)))
    img.save("out.png")


# refer no typing

# make a post on profiling the non-numba version
# make a post on profiling the numba version
# make a post on discuss profiling tools

app()
