from manim import *
import numpy as np
import math
from colour import Color
# configs
config.background_color = BLACK

config.pixel_width = 180 * 12
config.pixel_height = 320 * 12

x_shift = 0
y_shift = -4


class ByteDanceLogo(Scene):
    txt_list = [
        Text("How to use", font_size=80, fill_opacity=1),
        Text("math formulas", font_size=80, fill_opacity=1, color=RED),
        Text("to draw", font_size=80, fill_opacity=1),
        Text("TikTok logo", font_size=96, fill_opacity=1, color=BLUE),
    ]


    plane = NumberPlane(
        x_range=[-7, 7, 2],
        y_range=(-8, 16, 2),
        x_length=14,
        y_length=24,
    )

    axes = Axes(
        x_range=[-7, 7, 2],
        y_range=(-8, 16, 2),
        x_length=14,
        y_length=24,
        x_axis_config={"unit_size": 1},
        y_axis_config={"unit_size": 1},
        color=YELLOW
    ).add_coordinates()

    def show_beginning_text(self):
        self.play(AddTextLetterByLetter(self.txt_list[0].move_to(UP * 4)))
        self.play(AddTextLetterByLetter(self.txt_list[1].move_to(UP * 2)))
        self.play(AddTextLetterByLetter(self.txt_list[2].move_to(ORIGIN)))
        self.play(AddTextLetterByLetter(self.txt_list[3].move_to(DOWN * 2)))

    def remove_beginning_text(self):
        self.play(RemoveTextLetterByLetter(self.txt_list[0]), run_time=0.2)
        self.play(RemoveTextLetterByLetter(self.txt_list[1]), run_time=0.2)
        self.play(RemoveTextLetterByLetter(self.txt_list[2]), run_time=0.2)
        self.play(RemoveTextLetterByLetter(self.txt_list[3]), run_time=0.2)

    def construct(self):
        self.show_beginning_text()
        self.remove_beginning_text()

        rt=0.5
        self.play(FadeIn(self.plane), run_time=rt)
        self.play(FadeIn(self.axes), run_time=rt)

        formula1 = MathTex(r"(x+3)^2+y^2=16", font_size=65, color=YELLOW).move_to(UP * 0.5 + 3 * LEFT)
        self.play(Write(formula1), run_time=rt)
        circle1 = Circle(radius=4, color=WHITE).move_to(4 * DOWN + 3 * LEFT)
        self.play(Create(circle1))

        circle2 = Circle(radius=2, color=WHITE).move_to(4 * DOWN + 3 * LEFT)
        formula2 = MathTex(r"(x+3)^2+y^2=4", font_size=65, color=YELLOW).next_to(circle2, UP)
        self.play(Write(formula2), run_time=rt)
        self.play(Create(circle2))

        line1 = DashedLine(start=LEFT * 1 + DOWN * 17, end=LEFT * 1 + UP * 17, color=WHITE)
        formula3 = MathTex("x=-1", font_size=65, color=YELLOW).next_to(line1, LEFT * 2).shift(UP * 6)
        self.play(Write(formula3), run_time=rt)
        self.play(Create(line1))

        line2 = DashedLine(start=DOWN * 17 + RIGHT, end=UP * 17 + RIGHT, color=WHITE)
        formula4 = MathTex("x=1", font_size=65, color=YELLOW).next_to(line2, RIGHT * 2).shift(UP * 8)
        self.play(Write(formula4), run_time=rt)
        self.play(Create(line2))

        line3 = DashedLine(start=LEFT * 10 + UP * 4, end=RIGHT * 10 + UP * 4, color=WHITE)
        formula5 = MathTex("y=8", font_size=65, color=YELLOW).next_to(line3, DOWN)
        self.play(Write(formula5), run_time=rt)
        self.play(Create(line3))

        self.play(Unwrite(formula5), Unwrite(formula4), Unwrite(formula3), Unwrite(formula2), Unwrite(formula1))

        circle3 = Circle(radius=5, color=WHITE).move_to(UP * 4 + RIGHT * 4)
        formula6 = MathTex(r"(x-4)^2+(y-8)^2=25", font_size=50, color=YELLOW).next_to(circle3, UP).shift(LEFT)
        self.play(Write(formula6), run_time=rt)
        self.play(Create(circle3))
        self.play(Unwrite(formula6), run_time=0.1)

        circle4 = Circle(radius=3, color=WHITE).move_to(UP * 4 + RIGHT * 4)
        formula7 = MathTex(r"(x-4)^2+(y-8)^2=9", font_size=50, color=YELLOW).next_to(circle4, UP).shift(LEFT)
        self.play(Write(formula7), run_time=rt)
        self.play(Create(circle4))
        self.play(Unwrite(formula7), run_time=0.1)

        line4 = DashedLine(start=DOWN * 17 + RIGHT * 4, end=UP * 17 + RIGHT * 4, color=WHITE)
        formula8 = MathTex(r"x=4", font_size=50, color=YELLOW).next_to(line4, RIGHT).shift(DOWN * 5)
        self.play(Write(formula8), run_time=rt)
        self.play(Create(line4))

        line5 = DashedLine(start=DOWN * 17 + LEFT * 2.2, end=UP * 17 + LEFT * 2.2, color=WHITE)
        formula9 = MathTex(r"x=-2.2", font_size=50, color=YELLOW).next_to(line5, LEFT).shift(DOWN * 5)
        self.play(Write(formula9), run_time=rt)
        self.play(Create(line5))

        line5_part = Line(start=[-2.2, math.sqrt(4 - math.pow(-2.2 + 3, 2)), 0],  # (x+3)^2+y^2=16
                          end=[-2.2, math.sqrt(16 - math.pow(-2.2 + 3, 2)), 0], color=WHITE).shift(
            DOWN * 4)  # (x+3)^2+y^2=4
        self.add(line5_part)

        line1_part = Line(start=[-1, -4, 0], end=[-1, 4, 0], color=WHITE)
        self.add(line1_part)

        line2_part = Line(start=[1, -4, 0], end=[1, 4, 0], color=WHITE)
        self.add(line2_part)

        line3_part = Line(start=[-1, 4, 0], end=[1, 4, 0], color=WHITE)
        self.add(line3_part)

        # (x-2)^2+(y-8)^2=9
        # (x-2)^2+(y-8)^2=25
        line4_part = Line(start=[4, 1, 0], end=[4, -1, 0], color=WHITE)
        self.add(line4_part)

        self.play(Uncreate(line5), Uncreate(line1), Uncreate(line2), Uncreate(line3), Uncreate(line4), run_time=1.5)
        self.remove(formula8, formula9)

        circle1_ = circle1.copy().set_color(PURE_RED)
        circle2_= circle2.copy().set_color(PURE_RED)
        intersection1 = Difference(circle1_, circle2_, fill_color=PURE_RED, fill_opacity=1, color=PURE_RED, stroke_color=PURE_RED)
        rect1 = Rectangle(width=1.2, height=4, fill_color=PURE_RED, color=PURE_RED, fill_opacity=1).shift(np.array([-1.6, -2, 0]))
        # self.play(Create(rect1))
        diff1 = Difference(intersection1, rect1, color=PURE_RED, fill_color=PURE_RED, fill_opacity=1)
        self.play(FadeIn(diff1), run_time=2)

        rect2 = Rectangle(width=2, height=8, fill_color=PURE_RED, color=PURE_RED,  fill_opacity=1)
        self.play(GrowFromEdge(rect2, UP), run_time=1)

        self.remove(circle1, circle2)

        intersection2 = Difference(circle3, circle4, fill_color=PURE_RED, fill_opacity=1, color=PURE_RED)
        square = Square(side_length=5, fill_color=WHITE, fill_opacity=1).shift(RIGHT * 1.5 + UP * 1.5)
        diff2 = Intersection(intersection2, square, fill_color=PURE_RED, color=PURE_RED, fill_opacity=1)
        self.play(FadeIn(diff2))
        self.play(Uncreate(circle4), Uncreate(circle3), run_time=rt)

        self.remove(line4_part, line3_part, line5_part, line2_part, line1_part)

        group = VGroup(diff2, diff1, rect2).set_color(PURE_RED)

        rect_a = Rectangle(width=2, height=8).shift(RIGHT*2+UP)
        rect_b = rect_a.copy().shift(LEFT*0.6+UP*0.6)
        intersect_1 = Intersection(rect_b, rect_a, fill_color=WHITE, color=WHITE, fill_opacity=1)

        sector = AnnularSector(inner_radius=2, outer_radius=4, angle=2*PI, color=WHITE, fill_opacity=1).move_to(4 * DOWN + 3 * LEFT)
        rect_c = Rectangle(width=1.2, height=4, fill_color=WHITE, color=WHITE, fill_opacity=1).shift(np.array([-1.6, -2, 0]))
        diff_a = Difference(sector, rect_c, fill_color=WHITE, color=WHITE, fill_opacity=1).shift(RIGHT*2+UP)
        diff_b = diff_a.copy().shift(LEFT*0.6+UP*0.6)
        inter_a_b = Intersection(diff_a, diff_b, fill_color=WHITE, color=WHITE, fill_opacity=1)
        sector_1 = AnnularSector(inner_radius=3, outer_radius=5, angle=PI/2, start_angle=PI, color=WHITE, fill_opacity=1)
        sector_2 = sector_1.copy().shift(LEFT*0.6+UP*0.6)
        inter_c_d = Intersection(sector_2, sector_1,fill_color=WHITE, color=WHITE, fill_opacity=1).shift(UP*5+RIGHT*6)

        blue = group.copy().set_color(r"#00FFFF")

        inter = Intersection(group, blue, color=WHITE, fill_opacity=1, fill_color=WHITE)
        self.add(inter)

        self.play(blue.animate.shift(RIGHT*2+UP).shift(LEFT * 0.6 + UP * 0.6))

        self.play(group.animate.shift(RIGHT*2+UP))

        self.play(FadeIn(intersect_1), FadeIn(inter_a_b), FadeIn(inter_c_d))

        self.play(FadeOut(self.axes), run_time=0.2)
        self.play(FadeOut(self.plane), run_time=0.2)

        self.wait(3)
