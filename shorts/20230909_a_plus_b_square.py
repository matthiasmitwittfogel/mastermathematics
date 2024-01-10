from manim import *

# configs
config.background_color = BLACK
config.pixel_width = 180 * 12
config.pixel_height = 320 * 12


class APlusBSquare(Scene):
    def construct(self):
        formula1 = MathTex(r"(a+b)^{2}=?", color=BLUE).scale(4)
        self.play(ShowCreationThenFadeOut(formula1), run_time=2)

        scale_value = 1.5

        line1 = Line(start=[-5, 5, 0], end=[1, 5, 0], color=RED)
        label1 = MathTex("a").next_to(line1, UP).scale(scale_value)
        self.play(Create(line1))
        self.add(label1)

        line2 = Line(start=line1.end, end=[5, 5, 0], color=GREEN)
        self.play(Create(line2))
        label2 = MathTex("b").next_to(line2, UP).scale(scale_value)
        self.add(label2)

        line3 = Line(start=line2.end, end=[5, -1, 0], color=RED)
        self.play(Create(line3))
        label3 = MathTex("a").next_to(line3, RIGHT).scale(scale_value)
        self.add(label3)

        line4 = Line(start=line3.end, end=[5, -5, 0], color=GREEN)
        self.play(Create(line4))
        label4 = MathTex("b").next_to(line4, RIGHT).scale(scale_value)
        self.add(label4)

        line5 = Line(start=line4.end, end=[1, -5, 0], color=GREEN)
        self.play(Create(line5))
        label5 = MathTex("b").next_to(line5, DOWN).scale(scale_value)
        self.add(label5)

        line6 = Line(start=line5.end, end=[-5, -5, 0], color=RED)
        self.play(Create(line6))
        label6 = MathTex("a").next_to(line6, DOWN).scale(scale_value)
        self.add(label6)

        line7 = Line(start=line6.end, end=[-5, -1, 0], color=GREEN)
        self.play(Create(line7))
        label7 = MathTex("b").next_to(line7, LEFT).scale(scale_value)
        self.add(label7)

        line8 = Line(start=line7.end, end=[-5, 5, 0], color=RED)
        self.play(Create(line8))
        label8 = MathTex("a").next_to(line8, LEFT).scale(scale_value)
        self.add(label8)

        formula_part1 = MathTex("(").scale(scale_value).move_to([-5, 10, 0])
        self.play(Write(formula_part1))
        formula_part2 = label1.copy()
        self.play(formula_part2.animate.scale(scale_value).next_to(formula_part1))
        formula_part3 = MathTex("+").scale(scale_value).next_to(formula_part2, RIGHT)
        self.play(Write(formula_part3))
        formula_part4 = label2.copy()
        self.play(formula_part4.animate.scale(scale_value).next_to(formula_part3, RIGHT))
        formula_part5 = MathTex(r")\cdot(").scale(scale_value).next_to(formula_part4, RIGHT)
        self.play(Write(formula_part5))
        formula_part6 = label3.copy()
        self.play(formula_part6.animate.scale(scale_value).next_to(formula_part5, RIGHT))
        formula_part7 = MathTex("+").scale(scale_value).next_to(formula_part6, RIGHT)
        self.play(Write(formula_part7))
        formula_part8 = label4.copy()
        self.play(formula_part8.animate.scale(scale_value).next_to(formula_part7, RIGHT))
        formula_part9 = MathTex(")").scale(scale_value).next_to(formula_part8, RIGHT)
        self.play(Write(formula_part9))

        formula_part5_ = MathTex(r")^{2}").scale(scale_value).next_to(formula_part4, RIGHT)
        formula_part10 = MathTex(r"(a+b)^{2}", color=WHITE).scale(scale_value).move_to([-5, 8, 0])
        self.play(*[FadeOut(mob) for mob in [formula_part6, formula_part7, formula_part8, formula_part9]],
                  TransformMatchingTex(formula_part5, formula_part5_), run_time=2
                  )

        equal = MathTex("=").scale(scale_value).move_to([-5, 8, 0])
        self.play(Write(equal))

        dash_line1 = DashedLine(start=line8.start, end=line3.end)
        dash_line2 = DashedLine(start=line1.end, end=line5.end)
        self.play(Create(dash_line1), Create(dash_line2))

        opacity_val = 0.5
        # 1st rectangle
        self.play(DrawBorderThenFill(Square(side_length=6, fill_color=RED, fill_opacity=opacity_val).move_to([-2, 2, 0])
                                     )
                  ,run_time=0.5)
        self.play(label8.animate.move_to([-2, 2, 0]))
        dot1 = MathTex(r"\cdot ").next_to(label8, RIGHT)
        self.add(dot1)
        self.play(label1.animate.next_to(dot1, RIGHT))
        group1 = VGroup(label8, dot1, label1)
        # 2nd rectangle
        self.play(DrawBorderThenFill(Rectangle(width=4, height=6, fill_color=GREEN, fill_opacity=opacity_val).move_to([3, 2, 0])
                                     )
                  ,run_time=0.5)
        self.play(label2.animate.move_to([3, 2, 0]))
        dot2 = MathTex(r"\cdot ").next_to(label2, RIGHT)
        self.add(dot2)
        self.play(label3.animate.next_to(dot2, RIGHT))
        group2 = VGroup(label2, dot2, label3)
        # 3rd rectangle
        self.play(DrawBorderThenFill(Square(side_length=4, fill_color=YELLOW, fill_opacity=opacity_val).move_to([3, -3, 0])
                                     )
                  ,run_time=0.5)
        self.play(label4.animate.move_to([3, -3, 0]))
        dot3 = MathTex(r"\cdot ").next_to(label4, RIGHT)
        self.add(dot3)
        self.play(label5.animate.next_to(dot3, RIGHT))
        group3 = VGroup(label4, dot3, label5)
        # 4th rectangle
        self.play(DrawBorderThenFill(Rectangle(width=6, height=4, fill_color=BLUE, fill_opacity=opacity_val)
                                     .move_to([-2, -3, 0])
                                     )
                  ,run_time=0.5)
        self.play(label6.animate.move_to([-2, -3, 0]))
        dot4 = MathTex(r"\cdot ").next_to(label6, RIGHT)
        self.add(dot4)
        self.play(label7.animate.next_to(dot4, RIGHT))
        group4 = VGroup(label6, dot4, label7)

        self.play(group1.animate.scale(1).next_to(equal, RIGHT))
        plus1 = MathTex(" + ").next_to(group1, RIGHT*1.5).scale(scale_value)
        self.add(plus1)
        self.play(group2.animate.scale(1).next_to(plus1, RIGHT*1.5))
        plus2 = plus1.copy().next_to(group2, RIGHT*1.5)
        self.add(plus2)
        self.play(group3.animate.scale(1).next_to(plus2, RIGHT*1.5))
        plus3 = plus2.copy().next_to(group3, RIGHT*1.5)
        self.add(plus3)
        self.play(group4.animate.scale(1).next_to(plus3, RIGHT*1.5))

        equal_ = MathTex("=").scale(scale_value).move_to([-5, 6, 0])
        result = MathTex(
                                r"a^2 + 2ab + b^2", color=WHITE
        ).scale(scale_value).next_to(equal_, RIGHT)
        self.add(equal_)
        self.play(Write(result))

        self.wait(4)
