"""Vector module."""
import math
from dataclasses import dataclass


@dataclass
class Vec:
    """Vector class."""

    x: float
    y: float
    z: float


def sum(vec1: Vec, vec2: Vec) -> Vec:  # noqa: A001
    """Sum two vectors."""
    return Vec(vec1.x + vec2.x, vec1.y + vec2.y, vec1.z + vec2.z)


def sub(vec1: Vec, vec2: Vec) -> Vec:
    """Subtract two vectors."""
    return Vec(vec1.x - vec2.x, vec1.y - vec2.y, vec1.z - vec2.z)


def squared_length(vec: Vec) -> float:
    """Squared length of vector."""
    return vec.x**2 + vec.y**2 + vec.z**2


def length(vec: Vec) -> float:
    """Length of vector."""
    return math.sqrt(vec.x**2 + vec.y**2 + vec.z**2)


def unit(vec: Vec) -> Vec:
    """Get unit vector."""
    l = length(vec)  # noqa: E741
    return Vec(vec.x / l, vec.y / l, vec.z / l)


def dot(vec1: Vec, vec2: Vec) -> float:
    """Dot product."""
    return vec1.x * vec2.x + vec1.y * vec2.y + vec1.z * vec2.z


def cross(vec1: Vec, vec2: Vec) -> Vec:
    """Cross product."""
    return Vec(
        vec1.y * vec2.z - vec1.z * vec2.y,
        vec1.z * vec2.x - vec1.x * vec2.z,
        vec1.x * vec2.y - vec1.y * vec2.x,
    )


def mul_num(vec: Vec, num: float) -> Vec:
    """Multiply vector by number."""
    return Vec(vec.x * num, vec.y * num, vec.z * num)
