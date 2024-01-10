import numpy as np
from manim import *

# configs
config.background_color = BLACK
config.pixel_width = 180 * 2
config.pixel_height = 320 * 2


class SumFrom1Over2To1Over64(Scene):
    def construct(self):
        formula = MathTex(r"\frac{1}{2}+ \frac{1}{4}+\frac{1}{8}+\frac{1}{16}+\frac{1}{32}+\frac{1}{64}",
                          color=BLUE).scale(2)
        self.play(Write(formula), run_time=2)
        question_mark = MathTex("?", color=RED).scale(4).move_to(DOWN * 4)
        self.play(FadeIn(question_mark))
        self.play(FadeOut(question_mark))
        self.play(formula.animate.move_to(UP * 10))

        side_len = 10
        square = Square(side_length=side_len, color=WHITE)
        self.play(Create(square))

        up_brace = BraceBetweenPoints([square.side_length / 2, square.side_length / 2, 0],
                                      [-square.side_length / 2, square.side_length / 2, 0],
                                      color=BLUE, sharpness=0.5)
        up_brace_label = MathTex("1", color=BLUE).scale(2).next_to(up_brace, UP * 2)
        self.play(Create(up_brace))
        self.play(Create(up_brace_label))

        left_brace = BraceBetweenPoints(
            [-square.side_length / 2, square.side_length / 2, 0],
            [-square.side_length / 2, -square.side_length / 2, 0],
            color=BLUE, sharpness=0.5)
        left_brace_label = MathTex("1", color=BLUE).scale(2).next_to(left_brace, LEFT * 2)
        self.play(Create(left_brace))
        self.play(Create(left_brace_label))

        self.remove(up_brace, up_brace_label, left_brace_label, left_brace)

        square_2 = Rectangle(width=side_len, height=side_len / 2, fill_opacity=0.4, fill_color=WHITE)
        square_2.shift(np.array([0, side_len / 4.0, 0]))
        self.play(Create(square_2), run_time=2)
        # self.play(Create(Line(start=[-side_len/2, 0, 0], end=[side_len/2, 0, 0])))

        one_over_two_text = MathTex(r"\frac{1}{2}", color=BLUE).scale(2).move_to([0, side_len / 4.0, 0])
        self.play(Create(one_over_two_text))

        square_4 = (Square(side_length=side_len / 2.0, fill_opacity=0.4, fill_color=WHITE)
                    .shift(np.array([-side_len / 4.0, -side_len / 4.0, 0])))
        self.play(Create(square_4), run_time=2)
        self.play(Create(MathTex(r"\frac{1}{4}", color=BLUE).scale(2)
                         .move_to([-side_len / 4.0, -side_len / 4.0, 0])))

        square_8 = Rectangle(width=side_len / 2.0, height=side_len / 4.0, fill_opacity=0.4, fill_color=WHITE)
        square_8.shift(np.array([side_len / 4.0, -side_len / 8, 0]))

        self.play(Create(square_8), run_time=2)
        self.play(Create(MathTex(r"\frac{1}{8}", color=BLUE).scale(2)
                         .move_to(square_8.get_center())))

        square_16 = Square(side_length=side_len / 4.0, fill_opacity=0.4, fill_color=WHITE)
        square_16.shift(np.array([side_len / 8.0, -side_len * 3 / 8, 0]))

        self.play(Create(square_16), run_time=2)
        self.play(Create(MathTex(r"\frac{1}{16}", color=BLUE).scale(1.3)
                         .move_to(square_16.get_center())))

        square_32 = Rectangle(width=side_len / 4.0, height=side_len / 8.0, fill_opacity=0.4, fill_color=WHITE)
        square_32.shift(np.array([side_len * 3 / 8.0, -side_len * 5 / 16, 0]))

        self.play(Create(square_32), run_time=2)
        self.play(Create(MathTex(r"\frac{1}{32}", color=BLUE).scale(0.9)
                         .move_to(square_32.get_center())))

        square_64 = Square(side_length=side_len / 8.0, fill_opacity=0.4, fill_color=WHITE)
        square_64.shift(np.array([side_len * 5 / 16.0, -side_len * 7 / 16, 0]))

        self.play(Create(square_64), run_time=2)
        last_tex = MathTex(r"\frac{1}{64}", color=BLUE).scale(0.9).move_to(square_64.get_center())
        self.play(Create(last_tex))

        red_tex = MathTex(r"\frac{1}{64}", color=RED, stroke_width=2).scale(0.9).move_to([side_len * 7 / 16.0, -side_len * 7 / 16.0, 0])
        self.play(Create(red_tex))

        answer = MathTex(r"= 1 - ", color=BLUE).scale(2).move_to(UP * 7).align_to(formula, LEFT)
        answer.move_to(UP * 7).align_to(formula, LEFT)
        answer1 = MathTex(r"\frac{1}{64}", color=RED).scale(2).next_to(answer, RIGHT)
        answer2 = MathTex(r" = \frac{63}{64}", color=BLUE).scale(2).next_to(answer1, RIGHT)

        self.play(Write(answer))
        self.play(ReplacementTransform(red_tex, answer1))
        self.play(Write(answer2))

        self.wait(4)
