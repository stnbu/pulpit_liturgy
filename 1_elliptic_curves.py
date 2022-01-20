#!/usr/bin/env python3

import math
from manim import *
from point import Point as ECPoint
from curve import EllipticCurve
from field import PrimeGaloisField

P: int = 101
field = PrimeGaloisField(prime=P)
A: int = 2
B: int = 3
galois101 = EllipticCurve(a=A, b=B, field=field)
I = ECPoint(x=None, y=None, curve=galois101)
G = ECPoint(x=3, y=6, curve=galois101)
# order of group generated by "G" over the "galois101" finite-field EC.
N = 12
assert N * G == I


class EC(Scene):
    def construct(self):
        extent = 25
        plane = NumberPlane((-extent, extent), (-extent, extent)).add_coordinates()
        graph = ImplicitFunction(
            lambda x, y: x ** 3 + (A * x) + B - y ** 2, color=GREEN
        )
        self.add(plane, graph)
        point = G
        while True:
            point = point + G
            x = 0 if point.x is None else point.x.value
            y = 0 if point.y is None else point.y.value
            # wat
            FACTOR = 1
            x = FACTOR * x
            y = FACTOR * y
            # end wat
            dot = Tex("%d,%d" % (x, y), radius=0.2, color=RED)
            #self.play(Flash(dot, run_time=0.25))
            self.add(dot)
            if point == I:
                break


if __name__ == "__main__":
    config.frame_height = 8 * 7
    config.frame_width = config.frame_height * config.aspect_ratio
    config.quality = "low_quality"
    scene = EC()
    scene.render()
