import numpy as np
from manim import *
import math

# configs
config.background_color = BLACK
config.pixel_width = 180 * 12
config.pixel_height = 320 * 12


class SeriesSumFromOneOver8(Scene):
    def construct(self):
        print(config.frame_width, config.frame_height)
        formula = MathTex(r"{{\frac{1}{2}}}+{{\frac{1}{4}}}+{{\frac{1}{8}}}+{{\frac{1}{16}}}+{{\frac{1}{32}}} "
                          r"+{{\frac{1}{64}}}+{{...}}").scale(1.5).shift(UP * 9)

        self.play(Write(formula), run_time=1)
        question_mark = MathTex("?", font_size=200, color=RED).next_to(formula, DOWN * 10)
        self.play(ShowCreationThenFadeOut(question_mark))

        run_t = 0.5
        triangle = Polygon([-4, -4, 0], [4, -4, 0], [-4, 4, 0], color=WHITE)
        self.play(Create(triangle), run_time=1)

        label1 = MathTex(r"\sqrt{2} ", font_size=80, color=BLUE).next_to(triangle, LEFT, buff=0.3)
        label2 = label1.copy().next_to(triangle, DOWN, buff=0.3)
        label3 = MathTex("2", color=BLUE, font_size=80).next_to(triangle, RIGHT, buff=0.2).shift(LEFT*3)
        self.add(label3, label2, label1)

        line1 = DashedLine(start=[-4, -4, 0], end=ORIGIN, color=WHITE)
        self.play(Create(line1))
        triangle1 = Polygon([-4, -4, 0], [-4, 4, 0], ORIGIN, color=BLUE, fill_color=BLUE, fill_opacity=0.5)
        self.play(GrowFromEdge(triangle1, LEFT))
        self.play(formula.submobjects[0].copy().animate.move_to(triangle1.get_center_of_mass()))

        line2 = DashedLine(start=ORIGIN, end=[0, -4, 0], color=WHITE)
        self.play(Create(line2))
        triangle2 = Polygon(ORIGIN, DOWN*4, [-4, -4, 0],  color=YELLOW, fill_color=YELLOW, fill_opacity=0.5)
        self.play(GrowFromEdge(triangle2, DOWN))
        self.play(formula.submobjects[2].copy().animate.move_to(triangle2.get_center_of_mass()))

        line3 = DashedLine(start=[0, -4, 0], end=[2, -2, 0], color=WHITE)
        self.play(Create(line3))
        triangle3 = Polygon([0, -4, 0], [2, -2, 0], ORIGIN, color=BLUE, fill_color=BLUE, fill_opacity=0.5)
        self.play(GrowFromEdge(triangle3, LEFT))
        self.play(formula.submobjects[4].copy().animate.move_to(triangle3.get_center_of_mass()))

        line4 = DashedLine(start=[2, -2, 0], end=[2, -4, 0], color=WHITE)
        self.play(Create(line4))
        triangle4 = Polygon([2, -2, 0], [2, -4, 0], [0, -4, 0], color=YELLOW, fill_color=YELLOW, fill_opacity=0.5)
        self.play(GrowFromEdge(triangle4, DOWN))
        self.play(formula.submobjects[6].copy().animate.scale(1/2).move_to(triangle4.get_center_of_mass()))

        line5 = DashedLine(start=[2, -4, 0], end=[3, -3, 0], color=WHITE)
        self.play(Create(line5))
        triangle5 = Polygon([3, -3, 0], [2, -4, 0], [2, -2, 0], color=BLUE, fill_color=BLUE, fill_opacity=0.5)
        self.play(GrowFromEdge(triangle5, LEFT))
        self.play(formula.submobjects[8].copy().animate.scale(1/3).move_to(triangle5.get_center_of_mass()))

        line6 = DashedLine(start=[3, -3, 0], end=[3, -4, 0], color=WHITE)
        self.play(Create(line6))
        triangle6 = Polygon([3, -3, 0], [3, -4, 0], [2, -4, 0],color=YELLOW, fill_color=YELLOW, fill_opacity=0.5)
        self.play(GrowFromEdge(triangle6, DOWN))
        self.play(formula.submobjects[10].copy().animate.scale(1/4).move_to(triangle6.get_center_of_mass()))

        triangle7 = Polygon([3, -3, 0], [3, -4, 0], [4, -4, 0], color=BLUE,fill_color=BLUE, fill_opacity=0.5)

        self.play(GrowFromEdge(triangle7, LEFT))
        self.play(formula.submobjects[12].copy().animate.scale(1 / 3).move_to(triangle7.get_center_of_mass()))

        triangle_ = Polygon([-4, -4, 0], [4, -4, 0], [-4, 4, 0], color=RED, fill_color=RED, fill_opacity=0.8)
        self.play(GrowFromEdge(triangle_, LEFT))

        equal = MathTex("=").scale(1.5).align_to(formula, LEFT).shift(UP*7)
        self.play(Write(equal))

        self.play(label1.animate.next_to(equal, RIGHT))
        dot = MathTex(r"\cdot").next_to(label1, RIGHT)
        self.add(dot)

        self.play(label2.animate.next_to(dot, RIGHT))
        div = MathTex(r"{\div} 2",  font_size=80, color=BLUE).next_to(label2, RIGHT)
        self.play(Write(div))

        result = MathTex("=1", color=RED).scale(1.5).align_to(equal, LEFT).shift(UP*5)
        self.play(Write(result))

        self.wait(3)