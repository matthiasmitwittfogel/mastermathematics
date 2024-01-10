import numpy as np
from manim import *
import math

# configs
config.background_color = BLACK
config.pixel_width = 180 * 12
config.pixel_height = 320 * 12


class SeriesSumFromOneOver3(Scene):
    def construct(self):
        formula = MathTex(r"{{\frac{1}{3}}}+{{(\frac{1}{3})^{2}}}+ {{(\frac{1}{3})^{3}}}+ {{(\frac{1}{3})^{4}}} + {{("
                          r"\frac{1}{3})^{5}}}"
                          r"+{{...}}"
                          ).scale(1.5).shift(UP * 8)

        self.play(Write(formula), run_time=1)
        question_mark = Text("？", font_size=100, color=RED).next_to(formula, DOWN * 10)
        self.play(ShowCreationThenFadeOut(question_mark))

        run_t = 0.5
        square_1 = Square(side_length=8)
        self.play(Create(square_1), run_time=run_t)

        brace_left = BraceBetweenPoints([-4, 4, 0], [-4, -4, 0])
        txt1 = MathTex("1").next_to(brace_left, LEFT)
        brace_down = BraceBetweenPoints([-4, -4, 0], [4, -4, 0])
        txt2 = txt1.copy().next_to(brace_down, DOWN)
        self.play(Create(brace_left), Create(txt1), Create(brace_down), Create(txt2), run_time=1)

        line1_1 = DashedLine(start=[-4, 4/3, 0], end=[4, 4/3, 0])
        line1_2 = line1_1.copy().shift(DOWN*8/3)
        self.play(Create(line1_1), Create(line1_2))

        rect1 = Rectangle(width=8, height=8/3, fill_color=BLUE, fill_opacity=0.4, color=BLUE).shift(8/3*UP)
        self.play(GrowFromEdge(rect1, UP))
        formula1 = formula.submobjects[0].copy()
        self.play(formula1.animate.move_to(rect1.get_center_of_mass()))

        line2_1 = DashedLine(start=[-4+8/3, -4+8/3, 0], end=[-4+8/3, 4-8/3, 0])
        line2_2 = line2_1.copy().shift(RIGHT*8/3)
        self.play(Create(line2_1), Create(line2_2))

        rect2 = Polygon([-4, -4/3, 0], [-4, 4/3, 0], [-4+8/3, 4/3, 0], [-4+8/3, -4/3, 0], fill_color=BLUE, fill_opacity=0.4)
        self.play(GrowFromEdge(rect2, LEFT))
        formula2 = formula.submobjects[2].copy()
        self.play(formula2.animate.move_to(rect2.get_center_of_mass()))

        line3_1 = DashedLine(start=[-4+8/3, -4+8/3+8/3/3, 0], end=[4-8/3, -4+8/3+8/3/3, 0])
        line3_2 = line3_1.copy().shift(UP*8/3/3)
        self.play(Create(line3_2), Create(line3_1))

        rect3 = Polygon([-4+8/3, -4+8/3+8/3/3, 0], [4-8/3, -4+8/3+8/3/3, 0], [4-8/3, -4+8/3, 0], [-4+8/3, -4+8/3, 0],
                        fill_opacity=0.4, fill_color=BLUE)
        self.play(GrowFromEdge(rect3, LEFT))
        formula3 = formula.submobjects[4].copy()
        self.play(formula3.animate.scale(1/2).move_to(rect3.get_center_of_mass()))

        line4_1 = DashedLine(start=[-4+8/3+8/3/3, -4+8/3+8/3/3, 0], end=[-4+8/3+8/3/3, -4+8/3+8/3/3+8/3/3, 0])
        line4_2 = line4_1.copy().shift(RIGHT*8/3/3)
        self.play(Create(line4_2), Create(line4_1))

        rect4 = Polygon([-4+8/3+8/3/3, -4+8/3+8/3/3, 0], [-4+8/3+8/3/3, -4+8/3+8/3/3+8/3/3, 0],
                        [-4+8/3, -4+8/3+8/3/3+8/3/3, 0], [-4+8/3, -4+8/3+8/3/3, 0], fill_color=BLUE, fill_opacity=0.4).shift(RIGHT*8/3/3*2)
        self.play(GrowFromEdge(rect4, DOWN))
        formula4 = formula.submobjects[6].copy()
        self.play(formula4.animate.scale(1 / 2).move_to(rect4.get_center_of_mass()))

        line_5_1 = DashedLine(start=[-4+8/3+8/3/3, -4+8/3+8/3/3+8/3/3/3*2, 0],
                              end=[-4+8/3+8/3/3*2, -4+8/3+8/3/3+8/3/3/3*2, 0])
        line_5_2 = line_5_1.copy().shift(DOWN*8/3/3/3)
        self.play(Create(line_5_2), Create(line_5_1))

        rect5 = Polygon([-4+8/3+8/3/3, -4+8/3+8/3/3+8/3/3/3*2, 0], [-4+8/3+8/3/3*2, -4+8/3+8/3/3+8/3/3/3*2, 0],
                        [-4+8/3+8/3/3*2, -4+8/3+8/3/3+8/3/3, 0], [-4+8/3+8/3/3, -4+8/3+8/3/3+8/3/3, 0],
                        fill_opacity=0.4, fill_color=BLUE)
        self.play(GrowFromEdge(rect5, UP))
        formula5 = formula.submobjects[8].copy()
        self.play(formula5.animate.scale(1 / 4).move_to(rect5.get_center_of_mass()))

        formula6 = formula.submobjects[10].copy()
        self.play(formula6.animate.scale(1 / 4).move_to(ORIGIN))

        group1 = VGroup(rect5, rect4, rect3, rect2, rect1)
        group1_1 = VGroup(rect5, rect4, rect3, rect2, rect1,
                          formula6, formula5, formula4, formula3, formula2, formula1)
        group2 = group1.copy().set_fill(PURE_RED)
        self.play(Rotate(group2, PI, about_point=ORIGIN))
        #self.play(group2.animate.rotate(PI, about_point=ORIGIN))

        self.remove(line1_1, line1_2, line2_2, line2_1, line3_1, line3_2, line4_2, line4_1, line_5_2, line_5_1,
                    square_1)
        self.remove(brace_down, brace_left, txt2, txt1)
        self.play(group1_1.animate.shift(UL*3),
                  group2.animate.shift(DR*3))

        txt1_1 = MathTex(r"\frac{1}{2}").scale(3).move_to(group1_1.get_center())
        txt2_2 = txt1_1.copy().move_to(group2.get_center())
        self.play(GrowFromCenter(txt1_1), GrowFromCenter(txt2_2))

        self.play(FadeOut(group2), FadeOut(txt2_2), FadeOut(group1_1))

        #self.play(formula.submobjects[0].animate.move_to(formula.submobjects[0], LEFT))

        equal = MathTex("=").scale(3).next_to(txt1_1, LEFT*2)
        self.play(Write(equal))
        self.play(txt1_1.animate.next_to(equal, RIGHT))

        self.wait(3)