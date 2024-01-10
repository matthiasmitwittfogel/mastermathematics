import math

from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.azure import AzureService

# configs
config.background_color = BLACK


class SubSum(VoiceoverScene):
    def construct(self):

        self.set_speech_service(
            AzureService(voice="zh-CN-YunxiNeural", style="newscast")
        )
        formula1 = MathTex(r"1^3+2^3+3^3+4^3+...+n^3").scale(2 / 3).shift(UP * 3.2)

        with self.voiceover(
            "数形结合方法推导从1的立方到n的立方之和。"
        ) as tracker:
            self.play(Write(formula1), run_time=tracker.duration)

        formula2 = (MathTex(r"{{=1\cdot1^2}}+{{2\cdot2^2}}+{{3\cdot3^2}}+{{4\cdot4^2}}+{{...}}+{{n\cdot n^2}}").scale(2 / 3)
                    .next_to(formula1, RIGHT))

        sl = 0.3
        square_11 = Square(side_length=sl, fill_color=BLUE, fill_opacity=0.5, stroke_width=0.1).shift(UP*2+LEFT*3)
        square1s = [square_11]
        square_21 = Square(side_length=sl*2, fill_color=BLUE, fill_opacity=0.5, stroke_width=0.1).next_to(square_11, DOWN, buff=0).align_to(square_11, LEFT)
        square_22 = square_21.copy().shift(RIGHT*square_21.side_length)
        square2s = [square_21, square_22]
        square_31 = Square(side_length=sl*3, fill_color=BLUE, fill_opacity=0.5, stroke_width=0.1).next_to(square_21, DOWN, buff=0).align_to(square_21, LEFT)
        square_32 = square_31.copy().shift(RIGHT*square_31.side_length)
        square_33 = square_32.copy().shift(RIGHT*square_32.side_length)
        square3s = [square_31, square_32, square_33]

        square_41 = Square(side_length=sl*4, fill_color=BLUE, fill_opacity=0.5, stroke_width=0.1).next_to(square_31, DOWN, buff=0).align_to(square_31, LEFT)
        square_42 = square_41.copy().shift(RIGHT*square_41.side_length)
        square_43 = square_42.copy().shift(RIGHT*square_42.side_length)
        square_44 = square_43.copy().shift(RIGHT*square_43.side_length)
        square4s = [square_41, square_42, square_43, square_44]

        square_51 = Square(side_length=sl*5, fill_color=BLUE, fill_opacity=0.5, stroke_width=0.1).next_to(square_41, DOWN, buff=0).align_to(square_41, LEFT)
        square5s = [square_51]
        for i in range(1,5):
            square5s.append(square_51.copy().shift(RIGHT*i*square_51.side_length))

        mark1 = MathTex("1").next_to(square_11, LEFT).scale(1 / 2)
        mark2 = MathTex("2").next_to(square_21, LEFT).scale(1 / 2)
        mark3 = MathTex("3").next_to(square_31, LEFT).scale(1 / 2)
        mark4 = MathTex("4").next_to(square_41, LEFT).scale(1 / 2)
        mark_dot1 = Text("...").next_to(mark4, 2 * DOWN).scale(1 / 2)
        mark5 = MathTex("n").next_to(square_51, LEFT).scale(1 / 2)

        with self.voiceover("首先让我们将1的立方拆解为1乘以1的平方，<bookmark mark='A'/> 等于一个边长为1的正方形的面积") as tracker:
            self.play(formula1.animate.to_edge(LEFT))
            self.play(Write(formula2.submobjects[0].next_to(formula1, RIGHT)))
            self.wait_until_bookmark('A')
            self.play(GrowFromEdge(square_11, LEFT))
            self.add(mark1)

        with self.voiceover("然后将2的立方拆解为2乘以2的平方，<bookmark mark='B'/>也就是2个边长为2的正方形的面积。") as tracker:
            self.add(formula2.submobjects[1].next_to(formula2.submobjects[0], RIGHT))
            self.play(Write(formula2.submobjects[2].next_to(formula2.submobjects[1], RIGHT)))
            self.wait_until_bookmark('B')
            for i in range(len(square2s)):
                self.play(GrowFromEdge(square2s[i], LEFT))
            self.add(mark2)

        with self.voiceover("3的立方等于3乘以3的平方，<bookmark mark='C'/>也就是3个边长为3的正方形的面积。") as tracker:
            self.add(formula2.submobjects[3].next_to(formula2.submobjects[2], RIGHT))
            self.play(Write(formula2.submobjects[4].next_to(formula2.submobjects[3], RIGHT)))
            self.wait_until_bookmark("C")
            for i in range(len(square3s)):
                self.play(GrowFromEdge(square3s[i], LEFT))
            self.add(mark3)

        with self.voiceover("4的立方等于4乘以4的平方，<bookmark mark='D'/>等于4个边长为4的正方形的面积。") as tracker:
            self.add(formula2.submobjects[5].next_to(formula2.submobjects[4], RIGHT))
            self.play(Write(formula2.submobjects[6].next_to(formula2.submobjects[5], RIGHT)))
            self.wait_until_bookmark('D')
            for i in range(len(square4s)):
                self.play(GrowFromEdge(square4s[i], LEFT))
            self.add(mark4)

        with self.voiceover("以此类推,<bookmark mark='E'/>直到n的立方，<bookmark mark='F'/>等于n个边长为n的正方形的面积"):

            self.add(formula2.submobjects[7].next_to(formula2.submobjects[6], RIGHT))
            self.add(formula2.submobjects[8].next_to(formula2.submobjects[7], RIGHT))
            self.add(formula2.submobjects[9].next_to(formula2.submobjects[8], RIGHT))
            self.wait_until_bookmark('E')
            self.play(Write(formula2.submobjects[10].next_to(formula2.submobjects[9], RIGHT)))
            self.wait_until_bookmark('F')
            self.add(mark_dot1)
            for i in range(len(square5s)):
                self.play(GrowFromEdge(square5s[i], LEFT), run_time=0.5)
            self.add(mark5)

        line = Line(start=square_11.get_corner(UL), end=square5s[4].get_corner(DR) + [square_51.side_length, 0, 0],
                    color=RED, stroke_width=1)
        line1 = Line(start=square5s[4].get_corner(DR) + [square_51.side_length, 0, 0], end=square5s[4].get_corner(DR),
                     stroke_width=1)
        with self.voiceover("所以从1到n的立方和就等于图中所有小正方形的面积之和。那么应该如何计算正方形的面积呢？<bookmark mark='G'/>我们可以如图所示作一条红色直线，"
                            ):
            self.wait_until_bookmark('G')
            self.play(Create(line))
            self.play(Create(line1))

        triangle5 = Polygon(square5s[4].get_corner(DR) + [square_51.side_length, 0, 0],
                            square_51.get_corner(DL), square_11.get_corner(UL), fill_color=BLUE, fill_opacity=0.5, stroke_width=0.1)
        diffs = []
        for i, square in [(0,square1s), (1,square2s), (2,square3s), (3,square4s), (4,square5s)]:
            diffs.append(
                Difference(square[i], triangle5, fill_color=PURE_RED, fill_opacity=0.5, stroke_width=0.1)
            )

        squares = [square1s, square2s, square3s, square4s, square5s]
        intersects = []
        dicts = list(zip(squares, diffs))
        for d in dicts:
            intersects.append(Intersection((d[0])[-1], d[1], stroke_width=0.1, fill_color=BLACK, fill_opacity=1, color=BLACK, stroke_color=BLACK))
        self.add(*intersects)

        self.add(*diffs)

        with self.voiceover("直线右上方分割出n个红色小三角形。<bookmark mark='X'/>我们把这些红色小正方形顺时针旋转180度，所有的小正方形的面积之和就组成了一个大三角形的面积，计算从1"
                            "到n的立方和就等于计算这个大三角形的面积"):
            for d in diffs:
                self.play(Rotate(d, -PI, about_point=d.get_corner(DR)))
            self.remove(line, line1)

        brace_left = BraceBetweenPoints(square_11.get_corner(UL), square_51.get_corner(DL)).shift(LEFT)
        txt1 = MathTex(r"\frac{n(n+1)}{2}").next_to(brace_left, LEFT)
        brace_down = BraceBetweenPoints(square_51.get_corner(DL),
                                        square_51.get_corner(DL) + 6 * square_51.side_length * RIGHT)
        txt2 = MathTex(r"n(n+1)").next_to(brace_down, DOWN)
        with self.voiceover("这个大三角形的高等于从1到n的等差数列之和，也就是<bookmark mark='H' /> N乘以n加1除以2。"):
            self.play(Create(brace_left))
            self.wait_until_bookmark('H')
            self.play(Write(txt1))

        with self.voiceover("这个大三角形的底边<bookmark mark='I' />等于n乘以n加1"):
            self.play(Create(brace_down))
            self.wait_until_bookmark('I')
            self.play(Write(txt2))

        result_1 = Text(r"=面积(").scale(2/3).align_to(formula2.submobjects[10], LEFT).shift(UP*2+LEFT*2)
        final = MathTex(r"=(\frac{n(n+1)}{2})^2")
        with self.voiceover("所以面积等于二分之一的底乘以高，"):
            self.play(Write(result_1), run_time=0.2)
            result1_2 = triangle5.copy()
            self.play(result1_2.animate.scale(1/10).next_to(result_1, RIGHT), run_time=0.5)
            result_2 = Text(")").scale(2/3).next_to(result1_2, RIGHT, buff=0.1)
            self.play(Write(result_2), run_time=0.2)
            result_3 = MathTex(r"=\frac{1}{2} \cdot ").align_to(result_1, LEFT).shift(UP)
            self.play(Write(result_3), run_time=0.2)
            result_4 = txt1.copy().scale(3 / 4).next_to(result_3, RIGHT)
            self.play(result_4.animate.scale(2 / 3).next_to(result_3, RIGHT), run_time=0.5)
            dot_4 = MathTex(r"\cdot").next_to(result_4, RIGHT)
            self.add(dot_4)
            result_5 = txt2.copy()
            self.play(result_5.animate.scale(2 / 3).next_to(dot_4, RIGHT), run_time=0.5)
            final.scale(4 / 5).align_to(result_3, LEFT).shift(DOWN*0.5)

        with self.voiceover("最终结果等于二分之N乘以N加1的平方。"):
            self.play(Write(final))

        self.wait(3)
