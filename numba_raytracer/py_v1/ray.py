from dataclasses import dataclass

from . import vec 


@dataclass
class Ray:
    origin: vec.Vec
    direction: vec.Vec


def point_at_parameter(ray: Ray, t: float) -> vec.Vec:
    return vec.sum(ray.origin, vec.mul_num(ray.direction, t))
