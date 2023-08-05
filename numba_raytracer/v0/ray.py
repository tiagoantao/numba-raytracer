"""Ray module."""
from dataclasses import dataclass

from . import vec


@dataclass
class Ray:
    """Ray class."""

    origin: vec.Vec
    direction: vec.Vec


def point_at_parameter(ray: Ray, t: float) -> vec.Vec:
    """Return a point at parameter t."""
    return vec.sum(ray.origin, vec.mul_num(ray.direction, t))
