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
        extent = 102
        plane = NumberPlane((-extent, extent), (-extent, extent)).add_coordinates()
        #lambda x, y: ((x ** 3 + (A * x) + B) % P) - ((y ** 2) % P), color=GREEN
        graph = ImplicitFunction(
            lambda x, y: x ** 3 + (A * x) + B - y ** 2, color=GREEN
        )
        self.add(plane, graph)
        colors = [BLUE, GREEN, RED, ORANGE]
        for x, y in [
                (0, 0),
                (1, 0),
                (1, 1),
                (0, 1),
                (-1, 1),
                (-1, 0),
                (-1, -1),
                (0, -1),
                (1, -1),
        ]:
            for n in range(1, 5):
                mx, my = x * n, y * n
                print(mx, my)
                dot = Tex("%d,%d" % (mx, my), color=colors[n - 1]).move_to(plane.coords_to_point(mx, my)).scale(0.5)
                self.add(dot)
        dot = Tex("<%d,%d>" % (13, 7), color=RED).move_to(plane.coords_to_point(13, 7)).scale(1.5)
        self.add(dot)
        return
        point = G
        while True:
            point = point + G
            x = 0 if point.x is None else point.x.value
            y = 0 if point.y is None else point.y.value
            # wat
            FACTOR = 0.1
            tx = FACTOR * x
            ty = FACTOR * y
            # end wat
            dot = Tex("%d,%d" % (x, y), color=RED).move_to(plane.coords_to_point(tx, ty))
            #dot2 = Tex("%d,%d" % (x, y), color=BLUE).scale(2)
            #dot3 = Tex("%d,%d" % (x, y), color=GREEN).next_to(dot2, DOWN).scale(0.5)
            #self.play(Flash(dot, run_time=0.25))
            self.add(dot)
            if point == I:
                break


if __name__ == "__main__":
    config.frame_height = 8 * 2
    config.frame_width = config.frame_height * config.aspect_ratio
    #config.quality = "low_quality"
    scene = EC()
    scene.render()
