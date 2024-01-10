import numpy as np
from manim import *
import math

# configs
config.background_color = BLACK
config.pixel_width = 180 * 2
config.pixel_height = 320 * 2


class Sum2N_1(Scene):
    def construct(self):
        formula = MathTex("1+3+5+...+(2n-1)").scale(1.5).shift(UP*8)
        final_formula = formula.copy()
        self.play(Write(formula), run_time=1)
        question_mark = MathTex("?", font_size=96, color=RED).next_to(formula, DOWN*5)
        self.play(ShowCreationThenFadeOut(question_mark))

        side_len = 0.5
        #1
        square_1 = Square(side_length=side_len, color=BLUE, fill_color=BLUE, fill_opacity=0.5,
                          ) # .shift(UP*5)
        # 2
        square_2 = square_1.copy().next_to(square_1, DOWN, buff=0)
        square_3 = square_2.copy().next_to(square_2, LEFT, buff=0)
        square_4 = square_3.copy().next_to(square_2, RIGHT, buff=0)
        # 3
        square_5 = VGroup(square_2, square_3, square_4).copy().shift(DOWN * side_len)
        square_6 = square_3.copy().next_to(square_5, LEFT, buff=0)
        square_7 = square_3.copy().next_to(square_5, RIGHT, buff=0)
        # 4
        square_8 = VGroup(square_7, square_6, square_5).copy().shift(DOWN * side_len)
        square_9 = square_3.copy().next_to(square_8, RIGHT, buff=0)
        square_10 = square_3.copy().next_to(square_8, LEFT, buff=0)
        # 5
        square_11 = VGroup(square_8, square_9, square_10).copy().shift(DOWN * side_len)
        square_12 = square_3.copy().next_to(square_11, LEFT, buff=0)
        square_13 = square_3.copy().next_to(square_11, RIGHT, buff=0)
        # 6
        square_14 = VGroup(square_11, square_13, square_12).copy().shift(DOWN * side_len)
        square_15 = square_3.copy().next_to(square_14, LEFT, buff=0)
        square_16 = square_3.copy().next_to(square_14, RIGHT, buff=0)
        # 7
        square_17 = VGroup(square_14, square_15, square_16).copy().shift(DOWN * side_len)
        square_18 = square_3.copy().next_to(square_17, LEFT, buff=0)
        square_19 = square_3.copy().next_to(square_17, RIGHT, buff=0)

        self.play(Create(square_1), run_time=0.2)
        self.play(Create(square_2), Create(square_3), Create(square_4), run_time=0.2)
        self.play(Create(square_5), Create(square_6), Create(square_7), run_time=0.2)
        self.play(Create(square_8), Create(square_9), Create(square_10), run_time=0.2)
        self.play(Create(square_11), Create(square_12), Create(square_13), run_time=0.2)
        self.play(Create(square_14), Create(square_15), Create(square_16), run_time=0.2)
        self.play(Create(square_17), Create(square_18), Create(square_19), run_time=0.2)

        txt1 = (MathTex("1").next_to(square_1, UP))
        brace = BraceBetweenPoints(
            [square_18.get_center()[0] - square_18.side_length/2, square_18.get_center()[1], square_18.get_center()[2]],
            [square_19.get_center()[0] + square_19.side_length/2, square_19.get_center()[1], square_19.get_center()[2]],
        ).shift(DOWN*0.5)
        txt2 = MathTex("2n-1").next_to(brace, DOWN)
        self.play(Create(txt1))
        self.play(Create(brace))
        self.play(Create(txt2))

        self.remove(txt1)
        all_group = VGroup(
            square_1, square_2, square_3, square_4, square_5, square_6, square_7,
            square_9, square_10, square_8, square_13, square_12, square_11,
            square_16, square_15, square_14,
            square_17, square_18, square_19,
        )

        all_group_copy1 = all_group.copy().set_fill(RED)
        self.play(Rotate(all_group_copy1, about_point=square_1.get_center(), angle=math.pi/2))
        self.play(all_group_copy1.animate.shift(np.array([square_1.side_length,0,0])))
        formula1 = MathTex(r"2\cdot(1+3+5+...+(2n-1))").scale(1.5).shift(UP * 8)
        self.play(ReplacementTransform(formula, formula1))

        brace1 = BraceBetweenPoints(
            [square_18.get_center()[0] - square_18.side_length / 2, square_18.get_center()[1],
             square_18.get_center()[2]],
            [square_19.get_center()[0] + square_19.side_length *3/ 2, square_19.get_center()[1],
             square_19.get_center()[2]],
        ).shift(DOWN * 0.5)
        txt2_ = MathTex("2n").next_to(brace, DOWN)
        self.play(ReplacementTransform(brace, brace1), ReplacementTransform(txt2, txt2_))

        all_group_copy2 = all_group_copy1.copy().set_fill(YELLOW)
        self.play(Rotate(all_group_copy2, about_point=square_1.get_center(), angle=math.pi/2))
        self.play(all_group_copy2.animate.shift(np.array([square_1.side_length,0,0])))
        formula2 = MathTex(r"3\cdot(1+3+5+...+(2n-1))").scale(1.5).shift(UP * 8)
        self.play(ReplacementTransform(formula1, formula2))

        all_group_copy3 = all_group_copy2.copy().set_fill(PURPLE)
        self.play(Rotate(all_group_copy3, about_point=square_1.get_center(), angle=math.pi/2))
        self.play(all_group_copy3.animate.shift(np.array([square_1.side_length,0,0])))
        formula3 = MathTex(r"4\cdot(1+3+5+...+(2n-1))").scale(1.5).shift(UP * 8)
        self.play(ReplacementTransform(formula2, formula3))

        brace2 = BraceBetweenPoints(
            [square_18.get_center()[0], square_18.get_center()[1] + square_18.side_length * 13.5,
             square_18.get_center()[2]],
            [square_18.get_center()[0], square_18.get_center()[1] - square_18.side_length / 2,
             square_18.get_center()[2]]
        ).shift(LEFT)
        self.play(Create(brace2))
        txt3 = MathTex("2n", sheen_direction=UP).next_to(brace2, LEFT)
        self.play(Write(txt3))

        # play wth formula
        equal_sign = MathTex("=").scale(1.5).shift(UP*6+LEFT*4)
        self.play(Write(equal_sign), run_time=0.5)
        txt4 = txt3.copy()
        self.play(txt4.animate.scale(1.5).next_to(equal_sign, RIGHT))
        dot_sign = MathTex(r"\cdot").scale(1.5).next_to(txt4, RIGHT)
        self.play(Write(dot_sign), run_time=0.1)
        txt5 = txt2_.copy()
        self.play(txt5.animate.scale(1.5).next_to(dot_sign, RIGHT))

        group_ans = VGroup(txt5, dot_sign, txt4)

        final_ans = MathTex(r"n^2").scale(1.5).next_to(equal_sign, RIGHT)
        self.play(ReplacementTransform(formula3,final_formula),
                  ReplacementTransform(group_ans, final_ans),
                  run_time=2)

        self.wait(4)
