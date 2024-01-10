import math

import numpy as np
from manim import *

# configs
config.background_color = BLACK

config.pixel_width = 180 * 5
config.pixel_height = 320 * 5
config.frame_width = 9*3
config.frame_height = 16*3


class DifferenceOfSquares(Scene):
    def construct(self):
        title1 = Text("Visual Proof",
                      font_size=80,
                      gradient=(RED, BLUE, GREEN)
                      )

        title2 = MarkupText(
            f'<span underline="single" underline_color="green">Difference of Squares</span>',
            gradient=(RED, BLUE, GREEN),
            font_size=80,
        ).next_to(title1, DOWN * 2)

        self.play(FadeIn(title1), FadeIn(title2))
        self.play(title1.animate.move_to([0, 10, 0]),
                  title2.animate.move_to([[0, 8, 0]])
                  )

        scale_val = 2
        square_a = Square(side_length=8, fill_color=RED, fill_opacity=0.4, color=BLACK)
        self.play(Create(square_a))
        up_brace = BraceBetweenPoints([4, 4, 0], [-4, 4, 0],
                                      color=BLUE, sharpness=0.5)
        up_brace_label = MathTex("a", color=BLUE).scale(scale_val).next_to(up_brace, UP)
        self.play(Create(up_brace_label), Create(up_brace), run_time=1)

        left_brace = BraceBetweenPoints(
            [-4, 4, 0], [-4, -4, 0], color=BLUE, sharpness=0.5
        )

        left_brace_label = MathTex("a", color=BLUE).scale(scale_val).next_to(left_brace, LEFT)
        self.play(Create(left_brace_label), Create(left_brace), run_time=1)

        group_a = VGroup(up_brace_label.copy(), left_brace_label.copy())
        a_square = MathTex(r"a^2", color=BLUE).scale(scale_val).move_to([-4, -8, 0])
        self.play(ReplacementTransform(group_a, a_square))

        square_b = Square(side_length=3, fill_color=GREEN, fill_opacity=0.4).move_to([-2.5, -2.5, 0])
        self.play(DrawBorderThenFill(square_b))

        left_brace_b = BraceBetweenPoints(
            [-4, -1, 0], [-4, -4, 0], color=BLUE, sharpness=0.5
        )
        left_brace_b_label = MathTex("b", color=BLUE).scale(scale_val).next_to(left_brace_b, LEFT)
        left_brace_a_b_ = BraceBetweenPoints(
            [-4, 4, 0], [-4, -1, 0], color=BLUE, sharpness=0.5
        )
        left_brace_a_b_label = MathTex("a-b", color=BLUE).scale(scale_val).next_to(left_brace_a_b_, LEFT)
        self.play(Transform(left_brace, left_brace_a_b_),
                  Transform(left_brace_label, left_brace_a_b_label),
                  Create(left_brace_b), Create(left_brace_b_label),
                  )

        bottom_brace_b = BraceBetweenPoints([-4, -4, 0], [-1, -4, 0],
                                            color=BLUE, sharpness=0.5)
        bottom_brace_b_label = MathTex("b", color=BLUE).scale(scale_val).next_to(bottom_brace_b, DOWN)

        self.add(bottom_brace_b_label, bottom_brace_b)

        bottom_brace_a_b = BraceBetweenPoints([-1, -4, 0], [4, -4, 0],
                                              color=BLUE, sharpness=0.5
                                              )
        bottom_brace_a_b_label = MathTex("a-b", color=BLUE).scale(scale_val).next_to(bottom_brace_a_b, DOWN)
        self.add(bottom_brace_a_b_label, bottom_brace_a_b)

        group_b = VGroup(left_brace_b_label.copy(), bottom_brace_b_label.copy())

        equal_notation = MathTex("-", color=BLUE).scale(scale_val).next_to(a_square)
        self.add(equal_notation)
        b_square = MathTex(r"b^2 = ", color=BLUE).scale(scale_val).next_to(equal_notation, RIGHT)
        self.play(ReplacementTransform(group_b, b_square))

        square_b_ = Square(side_length=4, fill_color=BLACK, stroke_color=BLACK, color=BLACK, fill_opacity=1).move_to(
            [-3, -3, 0])
        self.add(square_b_)
        self.remove(bottom_brace_b, bottom_brace_b_label, left_brace_b_label, left_brace_b)

        dot_line = Line(start=[-1, -1, 0], end=[4, -1, 0])
        self.play(Create(dot_line))

        right_b_brace = BraceBetweenPoints([4, -4, 0], [4, -1, 0],
                                           color=BLUE, sharpness=0.5
                                           )
        right_b_brace_label = MathTex("b", color=BLUE).scale(scale_val).next_to(right_b_brace, RIGHT)
        self.play(Create(right_b_brace_label), Create(right_b_brace))

        rect_mask = Rectangle(width=5, height=3, fill_color=BLACK, fill_opacity=1, stroke_color=BLACK,
                              color=BLACK).move_to([1.5, -2.5, 0])

        rect_tmp = Rectangle(width=5, height=3, fill_color=RED, fill_opacity=0.4, color=BLACK).move_to(
            [-1 + 5 / 2.0, -4 + 3 / 2.0, 0])
        self.add(rect_mask)
        self.add(rect_tmp)

        # group_ = VGroup(rect_tmp, bottom_brace_a_b_label, bottom_brace_a_b, right_b_brace_label, right_b_brace)
        self.remove(bottom_brace_a_b_label,
                    bottom_brace_a_b, right_b_brace, right_b_brace_label)
        self.play(Rotate(rect_tmp, about_point=[4, -1, 0], angle=PI / 2))

        rect_tmp_up_brace = BraceBetweenPoints([7, -1, 0], [4, -1, 0],
                                               color=BLUE, sharpness=0.5
                                               )
        rect_tmp_up_brace_label = MathTex("b", color=BLUE).scale(scale_val).next_to(rect_tmp_up_brace, UP)
        rect_tmp_right_brace = BraceBetweenPoints([7, -6, 0], [7, -1, 0],
                                                  color=BLUE, sharpness=0.5
                                                  )
        rect_tmp_right_brace_label = (MathTex("a-b", color=BLUE).scale(scale_val)
                                      .next_to(rect_tmp_right_brace, RIGHT))

        self.add(rect_tmp_up_brace, rect_tmp_up_brace_label, rect_tmp_right_brace, rect_tmp_right_brace_label)

        rect_tmp_group = VGroup(rect_tmp, rect_tmp_up_brace, rect_tmp_up_brace_label, rect_tmp_right_brace,
                                rect_tmp_right_brace_label)
        self.play(rect_tmp_group.animate.shift(np.array([0, 5, 0])))

        left_pan = MathTex("(", color=BLUE).scale(scale_val).next_to(b_square, RIGHT)
        self.add(left_pan)
        math_a = up_brace_label.copy()
        self.play(math_a.animate.next_to(left_pan, RIGHT))
        math_plus = MathTex("+", color=BLUE).scale(scale_val).next_to(math_a, RIGHT)
        self.add(math_plus)
        math_b = rect_tmp_up_brace_label.copy()
        self.play(math_b.animate.next_to(math_plus, RIGHT))
        right_pan = MathTex(r")(", color=BLUE).scale(scale_val).next_to(math_b, RIGHT)
        self.add(right_pan)
        math_a_b = left_brace_a_b_label.copy()
        self.play(math_a_b.animate.next_to(right_pan, RIGHT))

        self.add(MathTex(")", color=BLUE).scale(scale_val).next_to(math_a_b, RIGHT))

        self.wait(4)
