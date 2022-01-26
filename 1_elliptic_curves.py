#!/usr/bin/env python3

import math
from decimal import Decimal
from manim import *
import astoroid

extent = 12

class FFEC:

    def __init__(self, A, B, P):
        self.A = A
        self.B = B
        self.P = P
        self.lhs = lambda y: y**2
        self.rhs = lambda x: x**3 + self.A*x + self.B
        self.implicit = lambda x, y: self.rhs(x) - self.lhs(y)
        self.parametric = lambda x: math.sqrt((x) ** 3 + (self.A * (x)) + self.B)

    def get_tex(self):
        return r"y^2 = x^3 + %dx + %d over \mathbb{Z}_%d" % (self.A, self.B, self.P)

class FFECPlotter(Scene):

    def __init__(self, A, B, P, *args, **kwargs):
        self.P = Decimal(P)
        self.ec = FFEC(A, B, P)
        Scene.__init__(self, *args, **kwargs)

    def construct(self):
        plane = NumberPlane(
            [-extent, extent, 1],
            [-extent, extent, 1],
            x_length=extent + 1,
            y_length=extent + 1,
        )
        self.add(plane)

        points = []
        for i, n in enumerate(astoroid.fdrange(-0.77, 50, 0.01)):
            points.append((n, self.ec.parametric(n)))
        modular_points = [[astoroid.ModularNumber(Decimal(n), self.P) for n in point] for point in points]
        lines = astoroid.get_lines(modular_points, self.P)
        colors = list(astoroid.gen_color_gradient((255, 0, 0), (0, 0, 255), len(lines)))
        for j, line in enumerate(lines):
            color = list(astoroid.gen_color_gradient((23, 99, 142), (184, 108, 2), len(lines)))
            modular_porabola = VGroup(color=colors[j], stroke_width=3)
            modular_porabola.set_points_as_corners([astoroid.to_manim_point(*l) for l in line])
            self.add(modular_porabola)

if __name__ == "__main__":
    scene = FFECPlotter(2, 2, 11)
    scene.render()
