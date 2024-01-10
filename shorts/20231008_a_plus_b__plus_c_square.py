import numpy as np
from manim import *

# configs
config.background_color = BLACK
config.pixel_width = 180 * 2
config.pixel_height = 320 * 2


class APlusBPlusCSquare(Scene):
    def construct(self):
        formula1 = MathTex(r"{{(a+b+c)^{2}}}", color=BLUE).scale(1.5)
        question = Text("?", color=RED).scale(3).next_to(formula1, DOWN * 2)
        self.play(Write(formula1))
        self.play(ShowCreationThenFadeOut(question))
        self.play(formula1.animate.shift(UP * 9 + LEFT * 4))

        scale_value = 1
        run_t = 0.2

        line11 = Line(start=[0, 8, 0], end=[3, 8, 0], color=RED).shift(np.array([-5, -4, 0]))
        label11 = MathTex("a").next_to(line11, UP).scale(scale_value)
        self.play(Create(line11), run_time=run_t)
        self.add(label11)

        line12 = Line(start=[3, 8, 0], end=[6, 8, 0], color=YELLOW).shift(np.array([-5, -4, 0]))
        label12 = MathTex("b").next_to(line12, UP).scale(scale_value)
        self.play(Create(line12), run_time=run_t)
        self.add(label12)

        line13 = Line(start=[6, 8, 0], end=[8, 8, 0], color=BLUE).shift(np.array([-5, -4, 0]))
        label13 = MathTex("c").next_to(line13, UP).scale(scale_value)
        self.play(Create(line13), run_time=run_t)
        self.add(label13)

        line21 = Line(start=[8, 8, 0], end=[8, 5, 0], color=RED).shift(np.array([-5, -4, 0]))
        label21 = MathTex("a").next_to(line21, RIGHT).scale(scale_value)
        self.play(Create(line21), run_time=run_t)
        self.add(label21)

        line22 = Line(start=[8, 5, 0], end=[8, 2, 0], color=YELLOW).shift(np.array([-5, -4, 0]))
        label22 = MathTex("b").next_to(line22, RIGHT).scale(scale_value)
        self.play(Create(line22), run_time=run_t)
        self.add(label22)

        line23 = Line(start=[8, 2, 0], end=[8, 0, 0], color=BLUE).shift(np.array([-5, -4, 0]))
        label23 = MathTex("c").next_to(line23, RIGHT).scale(scale_value)
        self.play(Create(line23), run_time=run_t)
        self.add(label23)

        line31 = Line(start=[8, 0, 0], end=[6, 0, 0], color=BLUE).shift(np.array([-5, -4, 0]))
        label31 = MathTex("c").next_to(line31, DOWN * 2).scale(scale_value)
        self.play(Create(line31), run_time=run_t)
        self.add(label31)

        line32 = Line(start=[6, 0, 0], end=[3, 0, 0], color=YELLOW).shift(np.array([-5, -4, 0]))
        label32 = MathTex("b").next_to(line32, DOWN * 2).scale(scale_value)
        self.play(Create(line32), run_time=run_t)
        self.add(label32)

        line33 = Line(start=[3, 0, 0], end=[0, 0, 0], color=RED).shift(np.array([-5, -4, 0]))
        label33 = MathTex("a").next_to(line33, DOWN * 2).scale(scale_value)
        self.play(Create(line33), run_time=run_t)
        self.add(label33)

        line41 = Line(start=[0, 0, 0], end=[0, 2, 0], color=BLUE).shift(np.array([-5, -4, 0]))
        label41 = MathTex("c").next_to(line41, LEFT * 2).scale(scale_value)
        self.play(Create(line41), run_time=run_t)
        self.add(label41)

        line42 = Line(start=[0, 2, 0], end=[0, 5, 0], color=YELLOW).shift(np.array([-5, -4, 0]))
        label42 = MathTex("b").next_to(line42, LEFT * 2).scale(scale_value)
        self.play(Create(line42), run_time=run_t)
        self.add(label42)

        line43 = Line(start=[0, 5, 0], end=[0, 8, 0], color=RED).shift(np.array([-5, -4, 0]))
        label43 = MathTex("a").next_to(line43, LEFT * 2).scale(scale_value)
        self.play(Create(line43), run_time=run_t)
        self.add(label43)

        line51 = DashedLine(start=[0, 5, 0], end=[3, 5, 0], color=RED).shift(np.array([-5, -4, 0]))
        label51 = MathTex("a").next_to(line51, DOWN).scale(scale_value)
        self.play(Create(line51), run_time=run_t)
        self.add(label51)

        line52 = DashedLine(start=[3, 5, 0], end=[6, 5, 0], color=YELLOW).shift(np.array([-5, -4, 0]))
        label52 = MathTex("b").next_to(line52, DOWN).scale(scale_value)
        self.play(Create(line52), run_time=run_t)
        self.add(label52)

        line53 = DashedLine(start=[6, 5, 0], end=[8, 5, 0], color=RED).shift(np.array([-5, -4, 0]))
        label53 = MathTex("c").next_to(line53, DOWN).scale(scale_value)
        self.play(Create(line53), run_time=run_t)
        self.add(label53)

        line61 = DashedLine(start=[0, 2, 0], end=[3, 2, 0], color=RED).shift(np.array([-5, -4, 0]))
        label61 = MathTex("a").next_to(line61, DOWN).scale(scale_value)
        self.play(Create(line61), run_time=run_t)
        self.add(label61)

        line62 = DashedLine(start=[3, 2, 0], end=[6, 2, 0], color=YELLOW).shift(np.array([-5, -4, 0]))
        label62 = MathTex("b").next_to(line62, DOWN).scale(scale_value)
        self.play(Create(line62), run_time=run_t)
        self.add(label62)

        line63 = DashedLine(start=[6, 2, 0], end=[8, 2, 0], color=RED).shift(np.array([-5, -4, 0]))
        label63 = MathTex("c").next_to(line63, DOWN).scale(scale_value)
        self.play(Create(line63), run_time=run_t)
        self.add(label63)

        line71 = DashedLine(start=[3, 8, 0], end=[3, 5, 0], color=RED).shift(np.array([-5, -4, 0]))
        label71 = MathTex("a").next_to(line71, RIGHT).scale(scale_value)
        self.play(Create(line71), run_time=run_t)
        self.add(label71)

        line72 = DashedLine(start=[3, 5, 0], end=[3, 2, 0], color=YELLOW).shift(np.array([-5, -4, 0]))
        label72 = MathTex("b").next_to(line72, RIGHT).scale(scale_value)
        self.play(Create(line72), run_time=run_t)
        self.add(label72)

        line73 = DashedLine(start=[3, 2, 0], end=[3, 0, 0], color=RED).shift(np.array([-5, -4, 0]))
        label73 = MathTex("c").next_to(line73, RIGHT).scale(scale_value)
        self.play(Create(line73), run_time=run_t)
        self.add(label73)

        line81 = DashedLine(start=[6, 8, 0], end=[6, 5, 0], color=RED).shift(np.array([-5, -4, 0]))
        label81 = MathTex("a").next_to(line81, RIGHT).scale(scale_value)
        self.play(Create(line81), run_time=run_t)
        self.add(label81)

        line82 = DashedLine(start=[6, 5, 0], end=[6, 2, 0], color=YELLOW).shift(np.array([-5, -4, 0]))
        label82 = MathTex("b").next_to(line82, RIGHT).scale(scale_value)
        self.play(Create(line82), run_time=run_t)
        self.add(label82)

        line83 = DashedLine(start=[6, 2, 0], end=[6, 0, 0], color=RED).shift(np.array([-5, -4, 0]))
        label83 = MathTex("c").next_to(line83, RIGHT).scale(scale_value)
        self.play(Create(line83), run_time=run_t)
        self.add(label83)

        new_run_t = 0.5

        s_rect1 = Polygon(line11.start, line11.end, line71.end, line51.start, fill_color=RED, fill_opacity=0.5).shift(
            np.array([-5, -4, 0]))
        self.play(GrowFromEdge(s_rect1, LEFT), run_time=new_run_t)
        self.play(label11.animate.move_to(s_rect1.get_center()), run_time=new_run_t)
        dot1 = MathTex(r"\cdot").next_to(label11, RIGHT)
        self.add(dot1)
        self.play(label71.animate.next_to(dot1, RIGHT), run_time=new_run_t)
        subgroup1 = VGroup(label11, label71, dot1)

        s_rect2 = Polygon(line12.start, line12.end, line81.end, line52.start, fill_color=ORANGE,
                          fill_opacity=0.5).shift(np.array([-5, -4, 0]))
        self.play(GrowFromEdge(s_rect2, LEFT), run_time=new_run_t)
        self.play(label12.animate.move_to(s_rect2.get_center()), run_time=new_run_t)
        dot2 = MathTex(r"\cdot").next_to(label12, RIGHT)
        self.add(dot2)
        self.play(label81.animate.next_to(dot2, RIGHT), run_time=new_run_t)
        subgroup2 = VGroup(label12, dot2, label81)

        s_rect3 = Polygon(line13.start, line13.end, line21.end, line53.start, fill_color=YELLOW,
                          fill_opacity=0.5).shift(np.array([-5, -4, 0]))
        self.play(GrowFromEdge(s_rect3, LEFT), run_time=new_run_t)
        self.play(label13.animate.move_to(s_rect3.get_center()), run_time=new_run_t)
        dot3 = MathTex(r"\cdot").next_to(label13, RIGHT)
        self.add(dot3)
        self.play(label21.animate.next_to(dot3, RIGHT), run_time=new_run_t)
        subgroup3 = VGroup(label21, dot3, label13)

        s_rect4 = Polygon(line22.start, line22.end, line82.end, line82.start, fill_color=GREEN, fill_opacity=0.5).shift(
            np.array([-5, -4, 0]))
        self.play(GrowFromEdge(s_rect4, UP), run_time=new_run_t)
        self.play(label53.animate.move_to(s_rect4.get_center()), run_time=new_run_t)
        dot4 = MathTex(r"\cdot").next_to(label53, RIGHT)
        self.add(dot4)
        self.play(label22.animate.next_to(dot4, RIGHT), run_time=new_run_t)
        subgroup4 = VGroup(label22, dot4, label53)

        s_rect5 = Polygon(line52.start, line52.end, line62.end, line62.start, fill_color=BLUE, fill_opacity=0.5).shift(
            np.array([-5, -4, 0]))
        self.play(GrowFromEdge(s_rect5, RIGHT), run_time=new_run_t)
        self.play(label52.animate.move_to(s_rect5.get_center()), run_time=new_run_t)
        dot5 = MathTex(r"\cdot").next_to(label52, RIGHT)
        self.add(dot5)
        self.play(label82.animate.next_to(dot5, RIGHT), run_time=new_run_t)
        subgroup5 = VGroup(label82, label52, dot5)

        s_rect6 = Polygon(line51.start, line51.end, line61.end, line61.start, fill_color=PURPLE,
                          fill_opacity=0.5).shift(np.array([-5, -4, 0]))
        self.play(GrowFromEdge(s_rect6, RIGHT), run_time=new_run_t)
        self.play(label51.animate.move_to(s_rect6.get_center()), run_time=new_run_t)
        dot6 = MathTex(r"\cdot").next_to(label51, RIGHT)
        self.add(dot6)
        self.play(label72.animate.next_to(dot6, RIGHT))
        subgroup6 = VGroup(label72, dot6, label51)

        s_rect7 = Polygon(line41.start, line41.end, line73.start, line73.end, fill_color=WHITE, fill_opacity=0.5).shift(
            np.array([-5, -4, 0]))
        self.play(GrowFromEdge(s_rect7, UP), run_time=new_run_t)
        self.play(label61.animate.move_to(s_rect7.get_center()), run_time=new_run_t)
        dot7 = MathTex(r"\cdot").next_to(label61, RIGHT)
        self.add(dot7)
        self.play(label73.animate.next_to(dot7, RIGHT))
        subgroup7 = VGroup(label73, label61, dot7)

        s_rect8 = Polygon(line62.start, line62.end, line32.start, line32.end, fill_color=GOLD, fill_opacity=0.5).shift(
            np.array([-5, -4, 0]))
        self.play(GrowFromEdge(s_rect8, LEFT), run_time=new_run_t)
        self.play(label62.animate.move_to(s_rect8.get_center()), run_time=new_run_t)
        dot8 = MathTex(r"\cdot").next_to(label62, RIGHT)
        self.add(dot8)
        self.play(label83.animate.next_to(dot8, RIGHT))
        subgroup8 = VGroup(label83, dot8, label62)

        s_rect9 = Polygon(line63.start, line63.end, line31.start, line31.end, fill_color=PINK, fill_opacity=0.5).shift(
            np.array([-5, -4, 0]))
        self.play(GrowFromEdge(s_rect9, LEFT), run_time=new_run_t)
        self.play(label63.animate.move_to((s_rect9.get_center())), run_time=new_run_t)
        dot9 = MathTex(r"\cdot").next_to(label63, RIGHT)
        self.add(dot9)
        self.play(label23.animate.next_to(dot9, RIGHT))
        subgroup9 = VGroup(label23, dot9, label63)

        brace_down = BraceBetweenPoints(line41.start, line31.start).shift(np.array([-5, -4, 0]))
        self.play(Create(brace_down), run_time=new_run_t)
        down_plus1 = MathTex("+").next_to(label32, LEFT)
        down_plus2 = MathTex("+").next_to(label32, RIGHT)
        self.add(down_plus2, down_plus1)
        self.play(label33.animate.next_to(down_plus1, LEFT), run_time=new_run_t)
        self.play(label31.animate.next_to(down_plus2, RIGHT), run_time=new_run_t)

        brace_left = BraceBetweenPoints(line43.end, line41.start).shift(np.array([-5, -4, 0]))
        self.play(Create(brace_left), run_time=new_run_t)
        left_plus1 = MathTex("+").next_to(label42, UP)
        left_plus2 = MathTex("+").next_to(label42, DOWN)
        self.add(left_plus2, left_plus1)
        self.play(label43.animate.next_to(left_plus1, UP), run_time=new_run_t)
        self.play(label41.animate.next_to(left_plus2, DOWN), run_time=new_run_t)

        equals1 = MathTex("=(").scale(1).move_to(LEFT * 6 + UP * 8)
        self.play(Create(equals1), run_time=new_run_t)
        group_left = VGroup(down_plus2, down_plus1, label31, label32, label33)
        self.play(group_left.animate.next_to(equals1, RIGHT))
        middle = MathTex(r")\cdot(").next_to(group_left)
        self.add(middle)
        # group_right = VGroup(left_plus2, left_plus1, label42, label43, label41)
        # self.play(group_right.animate.next_to(middle, RIGHT))
        self.play(label43.animate.next_to(middle, RIGHT), run_time=new_run_t)
        self.play(left_plus1.animate.next_to(label43, RIGHT), run_time=new_run_t)
        self.play(label42.animate.next_to(left_plus1, RIGHT), run_time=new_run_t)
        self.play(left_plus2.animate.next_to(label42, RIGHT), run_time=new_run_t)
        self.play(label41.animate.next_to(left_plus2, RIGHT), run_time=new_run_t)

        right = MathTex(")").next_to(label41, RIGHT)
        self.add(right)

        equals2 = MathTex("=").scale(1).align_to(equals1, LEFT).shift(UP * 7)
        self.add(equals2)
        self.play(subgroup1.animate.next_to(equals2, RIGHT), run_time=new_run_t)
        plus1 = MathTex("+").scale(1).next_to(subgroup1, RIGHT)
        self.add(plus1)
        self.play(subgroup2.animate.next_to(plus1, RIGHT), run_time=new_run_t)
        plus2 = plus1.copy().next_to(subgroup2, RIGHT)
        self.add(plus2)
        self.play(subgroup3.animate.next_to(plus2, RIGHT), run_time=new_run_t)
        plus3 = plus2.copy().next_to(subgroup3, RIGHT)
        self.add(plus3)
        self.play(subgroup4.animate.next_to(plus3, RIGHT), run_time=new_run_t)
        plus4 = plus3.copy().next_to(subgroup4, RIGHT)
        self.add(plus4)
        self.play(subgroup5.animate.next_to(plus4, RIGHT), run_time=new_run_t)
        plus5 = plus4.copy().next_to(subgroup5, RIGHT)
        self.add(plus5)
        self.play(subgroup6.animate.move_to(LEFT * 5 + UP * 6), run_time=new_run_t)
        plus6 = plus5.copy().next_to(subgroup6, RIGHT)
        self.add(plus6)
        self.play(subgroup7.animate.next_to(plus6, RIGHT), run_time=new_run_t)
        plus7 = plus6.copy().next_to(subgroup7, RIGHT)
        self.add(plus7)
        self.play(subgroup8.animate.next_to(plus7, RIGHT), run_time=new_run_t)
        plus8 = plus7.copy().next_to(subgroup8, RIGHT)
        self.add(plus8)
        self.play(subgroup9.animate.next_to(plus8, RIGHT), run_time=new_run_t)

        result = MathTex(r"={{a}}^2+{{b}}^2+{{c}}^2+2{{a}}{{b}}+2{{a}}{{c}}+2{{b}}{{c}}",
                         ).align_to(equals1, LEFT).shift(UP * 5)
        result.set_color_by_tex("a", RED)
        result.set_color_by_tex("b", YELLOW)
        result.set_color_by_tex("c", BLUE)
        self.play(Write(result))

        self.wait(4)
