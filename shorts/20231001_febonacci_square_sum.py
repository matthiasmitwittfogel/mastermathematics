import numpy as np
from manim import *
import math

# configs
config.background_color = BLACK
config.pixel_width = 180 * 12
config.pixel_height = 320 * 12


class FebonacciSquareSum(Scene):
    def construct(self):
        formula = MathTex(
            "{{1^2}}+{{1^2}}+{{2^2}}+{{3^2}}+{{5^2}}+{{8^2}}+{{13^2}}+{{21^2}}+{{34^2}}+{{55^2}}+{{89^2}}").scale(
            1).shift(UP * 8)
        final_formula = formula.copy()
        self.play(Write(formula), run_time=1)
        question_mark = MathTex("?", font_size=96, color=RED).next_to(formula, DOWN * 5)
        self.play(ShowCreationThenFadeOut(question_mark))

        side_len = 1
        square_1 = Square(side_length=side_len, color=BLUE
                          )
        self.play(Create(square_1))

        square_1_formula = formula.submobjects[0].copy()
        self.play(square_1_formula.animate.move_to(square_1.get_center()))

        formula.submobjects[0].set_color(RED)

        square_2 = square_1.copy().next_to(square_1, DOWN, buff=0)
        self.play(Create(square_2))

        square_2_formula = formula.submobjects[2].copy()
        self.play(square_2_formula.animate.move_to(square_2.get_center()))

        formula.submobjects[2].set_color(RED)

        group = VGroup(square_1, square_1_formula, square_2, square_2_formula)

        square_3 = Square(side_length=2, color=BLUE).next_to(group, RIGHT, buff=0)
        self.play(Create(square_3))

        square_3_formula = formula.submobjects[4].copy()
        self.play(square_3_formula.animate.move_to(square_3.get_center()))

        formula.submobjects[4].set_color(RED)

        group.add(square_3, square_3_formula)

        square_4 = Square(side_length=3, color=BLUE).next_to(group, DOWN, buff=0)
        square_4_formula = formula.submobjects[6].copy()
        self.play(Create(square_4))
        self.play(square_4_formula.animate.move_to(square_4.get_center()))

        formula.submobjects[6].set_color(RED)
        group.add(square_4, square_4_formula)

        self.play(group.animate.shift(UP * 4 + LEFT * 4))

        square_5 = Square(side_length=5, color=BLUE).next_to(group, RIGHT, buff=0)
        square_5_formula = formula.submobjects[8].copy()
        self.play(Create(square_5))
        self.play(square_5_formula.animate.move_to(square_5.get_center()))
        formula.submobjects[8].set_color(RED)

        group.add(square_5, square_5_formula)

        square_6 = Square(side_length=8, color=BLUE).next_to(group, DOWN, buff=0)
        square_6_formula = formula.submobjects[10].copy()
        self.play(Create(square_6))
        self.play(square_6_formula.animate.move_to(square_6.get_center()))
        formula.submobjects[10].set_color(RED)

        group.add(square_6, square_6_formula)

        self.play(group.animate.scale(0.5).shift(LEFT * 3 + UP * 4))

        square_7 = Square(side_length=13, color=BLUE).scale(0.5).next_to(group, RIGHT, buff=0)
        square_7_formula = formula.submobjects[12].copy()
        self.play(Create(square_7))
        self.play(square_7_formula.animate.move_to(square_7.get_center()))
        formula.submobjects[12].set_color(RED)
        group.add(square_7, square_7_formula)

        square_8 = Square(side_length=21, color=BLUE).scale(0.5).next_to(group, DOWN, buff=0)
        square_8_formula = formula.submobjects[14].copy()
        self.play(Create(square_8))
        self.play(square_8_formula.animate.move_to(square_8.get_center()))
        formula.submobjects[14].set_color(RED)
        group.add(square_8, square_8_formula)

        self.play(group.animate.scale(0.3).shift(UP * 2 + LEFT * 2))

        square_9 = Square(side_length=34, color=BLUE).scale(0.5 * 0.3).next_to(group, RIGHT, buff=0)
        square_9_formula = formula.submobjects[16].copy()
        self.play(Create(square_9))
        self.play(square_9_formula.animate.move_to(square_9.get_center()))
        formula.submobjects[16].set_color(RED)
        group.add(square_9, square_9_formula)

        square_10 = Square(side_length=55, color=BLUE).scale(0.5 * 0.3).next_to(group, DOWN, buff=0)
        square_10_formula = formula.submobjects[18].copy()
        self.play(Create(square_10))
        self.play(square_10_formula.animate.move_to(square_10.get_center()))
        formula.submobjects[18].set_color(RED)
        group.add(square_10, square_10_formula)

        self.play(group.animate.scale(0.5).shift(LEFT * 4 + UP * 3))
        self.play(square_10_formula.animate.scale(2))

        square_11 = Square(side_length=89, color=BLUE).scale(0.5 * 0.3 * 0.5).next_to(group, RIGHT, buff=0)
        square_11_formula = formula.submobjects[20].copy()
        self.play(Create(square_11))
        self.play(square_11_formula.animate.move_to(square_11.get_center()))
        formula.submobjects[20].set_color(RED)
        group.add(square_11, square_11_formula)

        brace1 = BraceBetweenPoints(
            group.get_center() + [-group.width / 2.0, -group.height / 2.0, 0],
            group.get_center() + [group.width / 2.0 - group.width * 89.0/(55+89), -group.height / 2.0, 0])
        txt1 = MathTex("55").next_to(brace1, DOWN)
        self.play(Create(brace1),Create(txt1))

        brace2 = BraceBetweenPoints(
            group.get_center() + [group.width / 2.0 - group.width * 89.0/(55+89), -group.height / 2.0, 0],
            group.get_center() + [group.width / 2.0, -group.height / 2.0, 0])
        txt2 = MathTex("89").next_to(brace2, DOWN)
        self.play(Create(brace2),Create(txt2))

        brace3 = BraceBetweenPoints(
            group.get_center() + [group.width/2.0, -group.height/2.0, 0],
            group.get_center() + [group.width/2.0, group.height/2.0, 0]
        )
        txt3 = MathTex("89").next_to(brace3, RIGHT)
        self.play(Create(brace3), Create(txt3))

        equals = MathTex("=(").shift(UP * 6 + LEFT * 4)
        self.play(Write(equals))
        f1 = txt1.copy()
        self.play(Write(f1))
        self.play(f1.animate.next_to(equals, RIGHT))
        f2 = MathTex("+")
        self.play(f2.animate.next_to(f1, RIGHT))
        f3 = txt2.copy()
        self.play(f3.animate.next_to(f2, RIGHT))
        f4 = MathTex(r")\cdot").next_to(f3,RIGHT)
        self.add(f4)
        f5 = txt3.copy()
        self.play(f5.animate.next_to(f4, RIGHT))

        equals1 = MathTex("=").align_to(equals, LEFT).shift(UP*4)
        self.play(Write(equals1))
        result = MathTex("12816").next_to(equals1, RIGHT)
        self.play(Write(result))


        self.wait(4)
