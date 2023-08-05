import math
from dataclasses import dataclass


@dataclass
class Vec:
    x: float
    y: float
    z: float


def sum(vec1: Vec, vec2: Vec) -> Vec:
    return Vec(vec1.x + vec2.x, vec1.y + vec2.y, vec1.z + vec2.z)


def sub(vec1: Vec, vec2: Vec) -> Vec:
    return Vec(vec1.x - vec2.x, vec1.y - vec2.y, vec1.z - vec2.z)

def squared_length(vec: Vec) -> float:
    return vec.x**2 + vec.y**2 + vec.z**2


def length(vec: Vec) -> float:
    return math.sqrt(vec.x**2 + vec.y**2 + vec.z**2)


def unit(vec: Vec) -> Vec:
    l = length(vec)
    unit_vec = Vec(vec.x / l, vec.y / l, vec.z / l)
    return unit_vec


def dot(vec1: Vec, vec2: Vec) -> float:
    return vec1.x * vec2.x + vec1.y * vec2.y + vec1.z * vec2.z


def cross(vec1: Vec, vec2: Vec) -> Vec:
    return Vec(vec1.y * vec2.z - vec1.z * vec2.y,
               vec1.z * vec2.x - vec1.x * vec2.z,
               vec1.x * vec2.y - vec1.y * vec2.x)


def mul_num(vec: Vec, num: float) -> Vec:
    return Vec(vec.x * num, vec.y * num, vec.z * num)
