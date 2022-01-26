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
        self.lhs = lambda y: y ** 2
        self.rhs = lambda x: x ** 3 + self.A * x + self.B
        self.implicit = lambda x, y: self.rhs(x) - self.lhs(y)
        self.parametric = lambda x: math.sqrt(self.rhs(x))

    def get_tex(self):
        return r"y^2 = x^3 + %dx + %d, \quad x,y\in\mathbb{Z}_{%d}" % (self.A, self.B, self.P)

    def get_root(self):
        if self.A == 2 and self.B == 2:
            return -0.77091
        raise ValueError


class FFECPlotter(Scene):
    def __init__(self, A, B, P, *args, **kwargs):
        self.P = Decimal(P)
        self.curve = FFEC(A, B, P)
        Scene.__init__(self, *args, **kwargs)

    def construct(self):
        plane = Axes(
            x_range=[self.curve.get_root(), extent, 1],
            y_range=[-extent, extent, 1],
            # x_length=extent + 1,
            # y_length=extent + 1,
            axis_config={"include_numbers": True},
        )
        self.add(plane)

        points = []
        for i, n in enumerate(astoroid.fdrange(self.curve.get_root(), 50, 0.01)):
            points.append((n, self.curve.parametric(n)))
        modular_points = [
            [astoroid.ModularNumber(Decimal(n), self.P) for n in point]
            for point in points
        ]
        lines = astoroid.get_lines(modular_points, self.P)
        colors = list(astoroid.gen_color_gradient((255, 0, 0), (0, 0, 255), len(lines)))
        for j, line in enumerate(lines):
            color = list(
                astoroid.gen_color_gradient((23, 99, 142), (184, 108, 2), len(lines))
            )
            modular_porabola = VGroup(color=colors[j], stroke_width=3)
            modular_porabola.set_points_as_corners(
                [astoroid.to_manim_point(*l) for l in line]
            )
            self.add(modular_porabola)

        tex = MathTex(self.curve.get_tex()).to_edge(DOWN)
        self.add(tex)


if __name__ == "__main__":
    scene = FFECPlotter(2, 2, 11)
    scene.render()
