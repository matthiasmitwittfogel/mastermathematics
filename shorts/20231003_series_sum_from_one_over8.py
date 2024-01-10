import numpy as np
from manim import *
import math

# configs
config.background_color = BLACK
config.pixel_width = 180 * 12
config.pixel_height = 320 * 12


class SeriesSumFromOneOver8(Scene):
    def construct(self):
        formula = MathTex(r"{{\frac{1}{8}}} +{{\frac{1}{16}}} +{{\frac{1}{32}}} +{{\frac{1}{64}}}+{{\frac{1}{128}}} + "
                          r"...").scale(1.5).shift(UP * 8)

        self.play(Write(formula), run_time=1)
        question_mark = MathTex("?", font_size=200, color=RED).next_to(formula, DOWN * 10)
        self.play(ShowCreationThenFadeOut(question_mark))

        run_t = 0.5
        square_1 = Square(side_length=8)
        self.play(Create(square_1), run_time=run_t)

        brace_left = BraceBetweenPoints([-4, 4, 0], [-4, -4, 0])
        txt1 = MathTex("1").next_to(brace_left, LEFT)
        brace_down = BraceBetweenPoints([-4, -4, 0], [4, -4, 0])
        txt2 = txt1.copy().next_to(brace_down, DOWN)
        self.play(Create(brace_left), Create(txt1), Create(brace_down), Create(txt2), run_time=1)

        square_2 = square_1.copy()
        self.play(square_2.animate.rotate(PI / 4).scale(1 / math.sqrt(2)), run_time=run_t)

        triangle1 = Polygon([-4, -4, 0], [-4, 0, 0], [0, -4, 0], fill_color=RED, fill_opacity=0.5)
        self.play(Create(triangle1), run_time=run_t)
        f1 = formula.submobjects[0].copy()
        self.play(f1.animate.move_to(triangle1.get_center_of_mass()), run_time=run_t)

        square_3 = square_2.copy()
        self.play(square_3.animate.rotate(PI / 4).scale(1 / math.sqrt(2)), run_time=run_t)

        triangle2 = Polygon([0, -4, 0], [-2, -2, 0], [2, -2, 0], fill_color=RED, fill_opacity=0.5)
        self.play(Create(triangle2), run_time=run_t)
        f2 = formula.submobjects[2].copy()
        self.play(f2.scale(0.8).animate.move_to(triangle2.get_center_of_mass()), run_time=run_t)

        square_4 = square_3.copy()
        self.play(square_4.animate.rotate(PI / 4).scale(1 / math.sqrt(2)), run_time=run_t)

        triangle3 = Polygon([0, -2, 0], [2, 0, 0], [2, -2, 0], fill_color=RED, fill_opacity=0.5)
        self.play(Create(triangle3), run_time=run_t)
        f3 = formula.submobjects[4].copy()
        self.play(f3.scale(0.5).animate.move_to(triangle3.get_center_of_mass()), run_time=run_t)

        square_5 = square_4.copy()
        self.play(square_5.animate.rotate(PI / 4).scale(1 / math.sqrt(2)), run_time=run_t)

        triangle4 = Polygon([1, 1, 0], [1, -1, 0], [2, 0, 0], fill_color=RED, fill_opacity=0.5)
        self.play(Create(triangle4), run_time=run_t)
        f4 = formula.submobjects[6].copy()
        self.play(f4.scale(0.4).animate.move_to(triangle4.get_center_of_mass()), run_time=run_t)

        square_6 = square_5.copy()
        self.play(square_6.animate.rotate(PI / 4).scale(1 / math.sqrt(2)), run_time=run_t)

        triangle5 = Polygon([0, 1, 0], [1, 0, 0], [1, 1, 0], fill_color=RED, fill_opacity=0.5)
        self.play(Create(triangle5), run_time=run_t)
        f5 = formula.submobjects[8].copy()
        self.play(f5.scale(0.2).animate.move_to(triangle5.get_center_of_mass()), run_time=run_t)

        square_7 = square_6.copy()
        self.play(square_7.animate.rotate(PI / 4).scale(1 / math.sqrt(2)), run_time=run_t)

        triangle6 = Polygon([0, 1 / 2, 0], [1 / 2, 0, 0], [-1 / 2, 0, 0], fill_color=RED, fill_opacity=0.5).shift(
            UP / 2)
        self.play(Create(triangle6), run_time=run_t)

        square_8 = square_7.copy()
        self.play(square_8.animate.rotate(PI / 4).scale(1 / math.sqrt(2)), run_time=run_t)

        triangle7 = Polygon([0, 1 / 2, 0], [-1 / 2, 0, 0], [-1 / 2, 1 / 2, 0], fill_color=RED, fill_opacity=0.5)
        self.play(Create(triangle7), run_time=run_t)

        square_9 = square_8.copy()
        self.play(square_9.animate.rotate(PI / 4).scale(1 / math.sqrt(2)), run_time=run_t)

        triangle8 = Polygon([-1 / 4, 1 / 4, 0], [-1 / 4, -1 / 4, 0], [-1 / 2, 0, 0], fill_opacity=0.5, fill_color=RED)
        self.play(Create(triangle8), run_time=run_t)

        square10 = square_9.copy()
        self.play(square10.animate.rotate(PI / 4).scale(1 / math.sqrt(2)), run_time=run_t)

        triangle9 = Polygon([-1 / 4, -1 / 4, 0], [0, -1 / 4, 0], [-1 / 4, 0, 0], fill_color=RED, fill_opacity=0.5)
        self.play(Create(triangle9), run_time=run_t)

        group1 = VGroup(triangle9, triangle8, triangle7, triangle6, triangle5,
                        triangle4, triangle3, triangle2, triangle1, f1, f2, f3, f4, f5)
        group1_ = VGroup(triangle9, triangle8, triangle7, triangle6, triangle5,
                         triangle4, triangle3, triangle2, triangle1)
        group2 = group1_.copy().set_fill(GREEN)
        self.play(group2.animate.rotate(PI / 2, about_point=[0, -2, 0]).shift((RIGHT + UP) * 2))

        group3 = group2.copy().set_fill(BLUE)
        self.play(group3.animate.rotate(PI / 2).shift(UP * 2.5 + LEFT * 0.5))

        group4 = group3.copy().set_fill(WHITE)
        self.play(group4.animate.rotate(PI / 2).shift(LEFT * 2.5 + DOWN * 0.5))

        self.remove(square10, square_9, square_8, square_7, square_6, square_5, square_4, square_3,
                    square_2, square_1)
        self.remove(brace_down, brace_left, txt2, txt1)
        self.play(group4.animate.shift(LEFT * 2 + UP * 2), group3.animate.shift(RIGHT * 2 + UP * 2),
                  group2.animate.shift(DOWN * 2 + RIGHT * 2), group1.animate.shift(LEFT * 2 + DOWN * 2))

        quarter_txt1 = MathTex(r"{{\frac{1}{4}}}").scale(5).move_to(group4.get_center())
        self.play(GrowFromCenter(quarter_txt1))
        quarter_txt2 = MathTex(r"{{\frac{1}{4}}}").scale(5).move_to(group3.get_center())
        self.play(GrowFromCenter(quarter_txt2))
        quarter_txt3 = MathTex(r"{{\frac{1}{4}}}").scale(5).move_to(group2.get_center())
        self.play(GrowFromCenter(quarter_txt3))
        quarter_txt4 = MathTex(r"{{\frac{1}{4}}}").scale(5).move_to(group1.get_center())
        self.play(GrowFromCenter(quarter_txt4))

        self.play(FadeOut(group4), FadeOut(quarter_txt1), run_time=0.5)
        self.play(FadeOut(group3), FadeOut(quarter_txt2), run_time=0.5)
        self.play(FadeOut(group2), FadeOut(quarter_txt3), run_time=0.5)

        eq = MathTex("=").scale(2).move_to(UP*5+LEFT*5)
        self.play(Write(eq), run_time=0.5)

        self.play(quarter_txt4.animate.scale(1/5*2).set_color(RED).next_to(eq, RIGHT))

        self.wait(4)
