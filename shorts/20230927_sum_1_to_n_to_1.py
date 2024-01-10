import numpy as np
from manim import *

# configs
config.background_color = BLACK
config.pixel_width = 180 * 12
config.pixel_height = 320 * 12


class SumFrom1ToNTo1(Scene):
    def construct(self):
        run_t = 0.2
        formula = MathTex("1+2+3+...+n+...+3+2+1").scale(1.5).shift(UP * 8)
        self.play(Write(formula), run_time=1)
        question_mark = MathTex("?", font_size=96, color=RED).next_to(formula, DOWN * 5)
        self.play(ShowCreationThenFadeOut(question_mark), run_time=1)

        rect1 = Square(side_length=0.5, fill_color=PURPLE, fill_opacity=0.5).move_to(LEFT * 4 + UP * 6)
        self.play(Create(rect1), run_time=run_t)
        txt1 = MathTex("1").next_to(rect1, LEFT)
        self.add(txt1)

        rect2_1 = Square(side_length=0.5, fill_color=PURPLE, fill_opacity=0.5).next_to(rect1, DOWN, buff=0)
        rect2_2 = rect2_1.copy().next_to(rect2_1, RIGHT, buff=0)
        self.play(Create(rect2_2), Create(rect2_1), run_time=run_t)
        txt2 = MathTex("2").next_to(rect2_1, LEFT)
        self.add(txt2)

        rect3_1 = Square(side_length=0.5, fill_color=PURPLE, fill_opacity=0.5).next_to(rect2_1, DOWN, buff=0)
        rect3_2 = VGroup(rect2_1, rect2_2).copy().next_to(rect3_1, RIGHT, buff=0)
        self.play(Create(rect3_1), Create(rect3_2), run_time=run_t)
        txt3 = MathTex("3").next_to(rect3_1, LEFT)
        self.add(txt3)

        rect4_1 = Square(side_length=0.5, fill_color=PURPLE, fill_opacity=0.5).next_to(rect3_1, DOWN, buff=0)
        rect4_2 = VGroup(rect3_1, rect3_2).copy().next_to(rect4_1, RIGHT, buff=0)
        self.play(Create(rect4_1), Create(rect4_2), run_time=run_t)
        txt4 = MathTex("4").next_to(rect4_1, LEFT)
        self.add(txt4)

        rect5_1 = Square(side_length=0.5, fill_color=PURPLE, fill_opacity=0.5).next_to(rect4_1, DOWN, buff=0)
        rect5_2 = VGroup(rect4_1, rect4_2).copy().next_to(rect5_1, RIGHT, buff=0)
        self.play(Create(rect5_1), Create(rect5_2), run_time=run_t)
        txt5 = MathTex("5").next_to(rect5_1, LEFT)
        self.add(txt5)

        rect6_1 = Square(side_length=0.5, fill_color=PURPLE, fill_opacity=0.5).next_to(rect5_1, DOWN, buff=0)
        rect6_2 = VGroup(rect5_1, rect5_2).copy().next_to(rect6_1, RIGHT, buff=0)
        self.play(Create(rect6_1), Create(rect6_2), run_time=run_t)
        txt6 = MathTex("6").next_to(rect6_1, LEFT)
        self.add(txt6)

        rect7_1 = Square(side_length=0.5, fill_color=PURPLE, fill_opacity=0.5).next_to(rect6_1, DOWN, buff=0)
        rect7_2 = VGroup(rect6_1, rect6_2).copy().next_to(rect7_1, RIGHT, buff=0)
        self.play(Create(rect7_1), Create(rect7_2), run_time=run_t)
        txt7 = MathTex("7").next_to(rect7_1, LEFT)
        self.add(txt7)

        rect8_1 = Square(side_length=0.5, fill_color=PURPLE, fill_opacity=0.5).next_to(rect7_1, DOWN, buff=0)
        rect8_2 = VGroup(rect7_1, rect7_2).copy().next_to(rect8_1, RIGHT, buff=0)
        self.play(Create(rect8_1), Create(rect8_2), run_time=run_t)
        txt8 = MathTex("...").next_to(rect8_1, LEFT)
        self.add(txt8)

        rect9_1 = Square(side_length=0.5, fill_color=PURPLE, fill_opacity=0.5).next_to(rect8_1, DOWN, buff=0)
        rect9_2 = VGroup(rect8_1, rect8_2).copy().next_to(rect9_1, RIGHT, buff=0)
        self.play(Create(rect9_1), Create(rect9_2), run_time=run_t)
        txt9 = MathTex("n-1").next_to(rect9_1, LEFT)
        self.add(txt9)

        rectn_1 = Square(side_length=0.5, fill_color=PURPLE, fill_opacity=0.5).next_to(rect9_1, DOWN, buff=0).set_fill(
            GREEN)
        rectn_2 = VGroup(rect9_1, rect9_2).copy().next_to(rectn_1, RIGHT, buff=0).set_fill(GREEN)
        self.play(Create(rectn_1), Create(rectn_2), run_time=run_t)
        txtn = MathTex("n").next_to(rectn_1, LEFT)
        self.add(txtn)

        rect_9_ = VGroup(rect9_1, rect9_2, txt9).copy().shift(DOWN).set_fill(GREEN)
        self.play(Create(rect_9_), run_time=run_t)

        rect_8_ = VGroup(rect8_1, rect8_2, txt8).copy().shift(DOWN * 2).set_fill(GREEN)
        self.play(Create(rect_8_), run_time=run_t)

        rect_7_ = VGroup(rect7_1, rect7_2, txt7).copy().shift(DOWN * 3).set_fill(GREEN)
        self.play(Create(rect_7_), run_time=run_t)

        rect_6_ = VGroup(rect6_1, rect6_2, txt6).copy().shift(DOWN * 4).set_fill(GREEN)
        self.play(Create(rect_6_), run_time=run_t)

        rect_5_ = VGroup(rect5_1, rect5_2, txt5).copy().shift(DOWN * 5).set_fill(GREEN)
        self.play(Create(rect_5_), run_time=run_t)

        rect_4_ = VGroup(rect4_1, rect4_2, txt4).copy().shift(DOWN * 6).set_fill(GREEN)
        self.play(Create(rect_4_), run_time=run_t)

        rect_3_ = VGroup(rect3_1, rect3_2, txt3).copy().shift(DOWN * 7).set_fill(GREEN)
        self.play(Create(rect_3_), run_time=run_t)

        rect_2_ = VGroup(rect2_1, rect2_2, txt2).copy().shift(DOWN * 8).set_fill(GREEN)
        self.play(Create(rect_2_), run_time=run_t)

        rect_1_ = VGroup(rect1, txt1).copy().shift(DOWN * 9).set_fill(GREEN)
        self.play(Create(rect_1_), run_time=run_t)

        self.remove(txt1, txt2, txt3, txt4, txt5, txt6, txt7, txt8, txt9)
        up_group = VGroup(rect1, rect2_1, rect2_2, rect3_1, rect3_2, rect4_1, rect4_2,
                          rect5_1, rect5_2, rect6_1, rect6_2, rect7_1,
                          rect7_2, rect8_1, rect8_2, rect9_1, rect9_2)

        self.play(up_group.animate.shift(RIGHT * 5))

        self.play(up_group.animate.shift(DOWN * 10 / 2))
        self.play(Rotate(up_group, PI / 2))
        self.play(up_group.animate.shift(LEFT * 4.5))

        down_brace = BraceBetweenPoints(LEFT*4 + RIGHT*0.25 + DOWN*4, RIGHT + RIGHT*0.25 +DOWN*4).shift(LEFT*0.5+UP*0.5)
        right_brace = BraceBetweenPoints(RIGHT*1.2+DOWN*3.5 + UP * 0.25, RIGHT*1.2+UP*1.5 + UP * 0.25)

        self.add(down_brace)
        down_num = MathTex("n").next_to(down_brace, DOWN)
        self.play(Write(down_num))
        self.add(right_brace)
        right_num = MathTex("n").next_to(right_brace, RIGHT)
        self.play(Write(right_num))

        equal = MathTex("=").scale(1.5).move_to(UP*6 + LEFT * 5.5)
        self.play(Write(equal))
        n_ = down_num.copy().scale(1.5)
        self.play(n_.animate.next_to(equal, RIGHT))
        dot = MathTex(r"\cdot").scale(1.5).next_to(n_, RIGHT)
        self.add(dot)
        self.play(right_num.copy().scale(1.5).animate.next_to(dot, RIGHT))

        result = MathTex("=n^2").scale(1.5).move_to(UP*4 + LEFT * 5)
        self.play(Write(result))

        self.wait(4)
