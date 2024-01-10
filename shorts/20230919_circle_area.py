import math

import numpy as np
from manim import *

# configs
config.background_color = BLACK
config.pixel_width = 180 * 12
config.pixel_height = 320 * 12


class CircleArea(Scene):
    def construct(self):
        g_circle = Circle(radius=2, arc_center=ORIGIN + DOWN * 2, color=GREEN, fill_color=GREEN, fill_opacity=0.5)
        self.play(DrawBorderThenFill(g_circle))

        title = Text("Area", color=WHITE, font_size=80).move_to(UP * 7 + LEFT * 4)
        lefb = MathTex("(", color=WHITE, font_size=80).next_to(title, RIGHT, buff=0.3)
        title = VGroup(title, lefb)
        self.play(Write(title))
        title_circle = Circle(radius=0.5, color=GREEN, fill_color=GREEN, fill_opacity=0.5).next_to(title, RIGHT)
        self.play(TransformFromCopy(g_circle, title_circle))
        right_pan = MathTex(r")", color=WHITE, font_size=80).next_to(title_circle, RIGHT)
        math_1 = MathTex("=", color=WHITE, font_size=80).next_to(right_pan, RIGHT)
        math_2 = title.copy().next_to(math_1, RIGHT)
        math_3 = right_pan.copy()
        right_part_formula = MathTex(r"=\frac{1}{2} \cdot", color=WHITE, font_size=80).align_to(math_1, LEFT)
        self.add(right_pan)

        # radius
        line = Line(start=ORIGIN + DOWN * 2, end=DOWN * 4, color=WHITE)
        self.play(Create(line))
        radius_label = MathTex("r", font_size=80).next_to(line, LEFT)
        circum_label = MathTex(r"2\pi r", font_size=80)
        self.add(radius_label)

        number = 50

        for i in range(0, number, 1):
            increment_circle = 2.0 / number
            increment_height = increment_circle
            increment_line = 2.0 * math.pi / number
            circle = Circle(radius=2 - increment_circle * i, arc_center=ORIGIN + DOWN * 2, color=GREEN)
            circle_ = Circle(radius=2 - increment_circle * (i + 1), arc_center=ORIGIN + DOWN * 2, color=GREEN,
                             fill_color=GREEN,
                             fill_opacity=0.5)
            line = Line(start=[-math.pi * 2 + increment_line * i, -2 + i * increment_height, 0] + DOWN * 2,
                        end=[math.pi * 2 - increment_line * i, -2 + i * increment_height, 0] + DOWN * 2,
                        color=GREEN)

            self.play(TransformFromCopy(circle, line),
                      Transform(g_circle, circle_), run_time=0.5 - (0.5 - 0.2) / number * i)
            if i == 0:
                brace = BraceBetweenPoints(line.start, line.end)
                circum_label.next_to(brace, DOWN)
                self.play(Create(brace))
                self.play(Write(circum_label))

        self.play(Write(math_1))
        self.play(Write(math_2))
        triangle = Polygon(
            [-math.pi * 2, -4, 0], [math.pi * 2, -4, 0], DOWN * 2, fill_color=GREEN,
            fill_opacity=0.5, color=GREEN
        )
        self.play(DrawBorderThenFill(triangle))
        title_triangle = triangle.copy().scale(0.2).next_to(math_2, RIGHT)
        self.play(TransformFromCopy(triangle, title_triangle))
        self.play(Write(math_3.next_to(title_triangle, RIGHT)))

        self.play(Write(right_part_formula.shift(UP * 4)))

        title_circum_label = MathTex(r" 2\pi r ", color=WHITE, font_size=80).next_to(right_part_formula, RIGHT)
        dot_ = MathTex(r"\cdot").next_to(title_circum_label, RIGHT)
        self.play(TransformFromCopy(circum_label, title_circum_label))
        self.add(dot_)
        title_radius_label = MathTex("r", color=WHITE, font_size=80).next_to(dot_, RIGHT)
        self.play(TransformFromCopy(radius_label, title_radius_label))

        self.play(Write(
            MathTex(
                r"=\pi r^{2} ", font_size=80, color=WHITE).align_to(right_part_formula, LEFT)
        )
        )

        self.wait(3)
