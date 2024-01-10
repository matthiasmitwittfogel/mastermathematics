from manim import *
from numpy import sqrt, sin, cos
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.azure import AzureService
import math


class ChinaFlag(VoiceoverScene):
    def construct(self):
        self.set_speech_service(
            AzureService(style="newscast")
        )
        with self.voiceover(
                """Do you understand the mathematical knowledge in the Chinese national flag?"""
        ) as tracker:
            text = Text("Do you understand the mathematical").shift(UP)
            text1 = Text("knowledge in the Chinese national flag?").next_to(text, DOWN)
            self.play(AddTextLetterByLetter(text), run_time=tracker.duration/2)
            self.play(AddTextLetterByLetter(text1), run_time=tracker.duration/2)
            self.remove(text, text1)

        flag = Rectangle(width=9, height=6, color=rgb_to_color([238 / 255.0, 28 / 255.0, 37 / 255.0]),
                         stroke_color=rgb_to_color([238 / 255.0, 28 / 255.0, 37 / 255.0]))
        line1 = DashedLine(start=(flag.get_corner(UL) + flag.get_corner(DL)) / 2,
                           end=(flag.get_corner(UR) + flag.get_corner(DR)) / 2,
                           color=WHITE
                           )
        line2 = DashedLine(start=(flag.get_corner(UL) + flag.get_corner(UR)) / 2,
                           end=(flag.get_corner(DL) + flag.get_corner(DR)) / 2,
                           color=WHITE
                           )

        lines1 = []
        for i in range(1, 15):
            line = DashedLine(start=(flag.get_corner(UL) + flag.get_corner(DL)) / 2 + [i * flag.width / 2 / 15, 0, 0],
                              end=flag.get_corner(UL) + [i * flag.width / 2 / 15, 0, 0],
                              stroke_width=1)
            lines1.append(line)

        lines2 = []
        for j in range(1, 10):
            line = DashedLine(start=flag.get_corner(UL) - [0, j * flag.height / 10 / 2, 0],
                              end=(flag.get_corner(UL) + flag.get_corner(UR)) / 2 - [0, j * flag.height / 10 / 2, 0],
                              stroke_width=1
                              )
            lines2.append(line)
        ax = Axes(x_range=[0, 15], y_range=[0, 10], x_length=flag.width / 2, y_length=flag.height / 2,
                  color=BLUE, tips=True)
        ax_orig = ax.get_origin()
        ax.shift((flag.get_corner(UL) + flag.get_corner(DL)) / 2 - ax_orig)

        brace_left = BraceBetweenPoints(flag.get_corner(UL), flag.get_corner(DL))
        txt1 = MathTex("2").next_to(brace_left, LEFT).scale(0.7)
        brace_down = BraceBetweenPoints(flag.get_corner(DL), flag.get_corner(DR))
        txt2 = MathTex("3").next_to(brace_down, DOWN, buff=0).scale(0.7)
        with self.voiceover(
                "The ratio of length to height of the Chinese national flag is 3 to 2. We first draw a rectangle with an aspect ratio of 3 to 2.<bookmark mark='A' /> "
                "Divide this rectangle into four equal parts,<bookmark mark='B' /> 。"
                "Set the vertex at the bottom left of the small rectangle in the upper right corner as the origin, with the right direction as the x-axis, and the line on the left side of the flag as the y-axis, to construct a planar Cartesian coordinate system.<bookmark mark='C' />"
                "Then divide the rectangle in the upper left corner into 10 equal parts, and 15 equal parts on the left and right sides."
        ):
            self.play(Create(flag))
            self.play(Create(brace_down), Create(brace_left))
            self.play(Write(txt1), Write(txt2))
            self.wait_until_bookmark('A')
            self.play(Create(line1), Create(line2))
            self.wait_until_bookmark('B')
            self.play(FadeIn(ax))
            self.wait_until_bookmark('C')

            create_lines1 = []
            create_lines2 = []
            for l in lines1:
                create_lines1.append(Create(l))
            for l in lines2:
                create_lines2.append(Create(l))

            self.play(*create_lines1, run_time=2)
            self.play(*create_lines2, run_time=2)

        def create_dot(x, y):
            return Dot(point=(flag.get_corner(UL) + flag.get_corner(DL)) / 2 + [flag.width / 2 / 15 * x,
                                                                                flag.height / 10 / 2 * y, 0],
                       radius=0.04, color=YELLOW)

        dot_big = create_dot(5, 5)
        dot_big_label = MathTex(r"(5,5)").next_to(dot_big, DOWN)
        # (10,18）、（12,16）、（12,13）、（10,11）
        dot_small = [
            create_dot(10, 8),
            create_dot(12, 6),
            create_dot(12, 3),
            create_dot(10, 1)
        ]
        # self.add(*dot_small)
        dot_small_labels = [
            MathTex(r"(10,8)").next_to(dot_small[0], UP),
            MathTex(r"(12,6)").next_to(dot_small[1], RIGHT),
            MathTex(r"(12,3)").next_to(dot_small[2], RIGHT),
            MathTex(r"(10,1)").next_to(dot_small[3], RIGHT)
        ]
        # self.add(*dot_small_labels)

        self.add(dot_big)

        big_circle = Circle(radius=flag.width / 2 / 15 * 3, color=WHITE).shift(dot_big.get_center())
        big_star = RegularPolygram(5, radius=flag.width / 2 / 15 * 3, color=YELLOW, stroke_color=YELLOW,
                        ).shift(dot_big.get_center())
        small_circles = []

        small_stars = []
        small_stars_helper = []
        for i in range(0, len(dot_small)):
            small_stars.append(
                RegularPolygram(5, radius=flag.width / 2 / 15, color=YELLOW, stroke_color=YELLOW).shift(
                    dot_small[i].get_center())
            )
            small_stars_helper.append(
                Star(outer_radius=flag.width / 2 / 15, color=YELLOW, stroke_color=YELLOW).shift(
                    dot_small[i].get_center())
            )

            small_circles.append(
                Circle(radius=flag.width / 2 / 15, color=WHITE).shift(dot_small[i].get_center())
            )
        with self.voiceover("Find the center points of 5 pentagrams, with the center points of the large pentagram located 5 times above and 5 times below the rectangle, 5 times to the left and 10 times to the right.<bookmark mark='D' />The center points of the four small pentagrams are located 2 times above and 8 times below the rectangle, respectively,"
                            "10 on the left and 5 on the right,<bookmark mark='E' />Up 4, down 6, left 12, right 3，<bookmark mark='F' />Up 7, down 3, left 12, right 3,<bookmark mark='G' />"
                            "9 up and 1 down, 10 left and 5 right.<bookmark mark='H' />Then draw a circle with the center point of the big pentagram as the center and a radius of 3 equal divisions."):
            self.play(Create(dot_big))
            self.add(dot_big_label)
            self.wait_until_bookmark('D')
            self.add(dot_small[0], dot_small_labels[0])
            self.wait_until_bookmark('E')
            self.add(dot_small[1], dot_small_labels[1])
            self.wait_until_bookmark('F')
            self.add(dot_small[2], dot_small_labels[2])
            self.wait_until_bookmark('G')
            self.add(dot_small[3], dot_small_labels[3])
            self.wait_until_bookmark('H')
            self.play(Create(big_circle))

        with self.voiceover("Draw a circle with the center points of four small pentagrams as the center points and a radius of one equal part."):
            creates = []
            for s in small_circles:
                creates.append(Create(s))
            self.play(*creates)

        vert = small_stars_helper[0].get_vertices()[2]
        angle_x = -math.atan(
            (vert[1] - small_stars_helper[0].get_center()[1]) / (vert[0] - small_stars_helper[0].get_center()[0])
        )
        print(angle_x * 180 / math.pi)
        for i in range(0, len(dot_small)):
            slope = (dot_small[i].get_center()[1] - dot_big.get_center()[1]) / (
                    dot_small[i].get_center()[0] - dot_big.get_center()[0])
            angle = math.atan(slope)
            print(angle)
            small_stars[i].rotate(angle_x + angle)

        four_lines = []
        for i in range(0, len(dot_small)):
            four_lines.append(DashedLine(start=big_star.get_center(), end=dot_small[i].get_center()))
        with self.voiceover("Divide the big circle into 5 equal parts. We need to use a ruler and ruler for drawing, and we will not explain it further. Connect the five equal points of a large circle.<bookmark mark='AA' />Draw as a pentagram.<bookmark "
                            "mark='K' />"
                            "Connect the center point of the large circle with the center points of the four small circles, and the intersection point of the line and each small circle is the vertex for drawing a small pentagram.<bookmark mark='L' "
                            "/>Also draw 4 more points on each of the 4 small circles, divide the 4 small circles into 5 equal parts, and draw a pentagram."):
            self.wait_until_bookmark('AA')
            self.play(Create(big_star))
            self.wait_until_bookmark('K')
            self.play(Create(four_lines[0]), Create(four_lines[1]), Create(four_lines[2]), Create(four_lines[3]))
            self.wait_until_bookmark('L')
            for i in range(0, 4):
                self.play(Create(small_stars[i]), run_time=1)

        with self.voiceover("Next, we will remove the excess auxiliary lines.<bookmark mark='M' />Fill the interior of the five pentagrams with yellow."):
            self.wait_until_bookmark('M')
            self.remove(*small_circles, big_circle, *four_lines, ax, *lines1, *lines2, line1, line2, dot_big_label,
                        *dot_small_labels)
            self.remove(brace_left, brace_down, txt2, txt1)
            for star in [*small_stars, big_star]:
                self.play(star.animate.set_fill(YELLOW, 1).set_color(YELLOW))

        with self.voiceover("Fill in the remaining parts in red.<bookmark mark='N' />The five star red flag is already made."):
            flag1 = Polygon(ORIGIN, ORIGIN + [0, flag.height / 2, 0],
                            ORIGIN + [-flag.width / 2, flag.height / 2, 0], ORIGIN - [flag.width / 2, 0, 0],
                            stroke_color=rgb_to_color([238 / 255.0, 28 / 255.0, 37 / 255.0]),
                            fill_color=rgb_to_color([238 / 255.0, 28 / 255.0, 37 / 255.0]), fill_opacity=1)
            diff = flag1
            for star in [*small_stars, big_star]:
                diff = Difference(diff, star, fill_color=rgb_to_color([238 / 255.0, 28 / 255.0, 37 / 255.0]),
                                  fill_opacity=1,
                                  stroke_color=rgb_to_color([238 / 255.0, 28 / 255.0, 37 / 255.0]))
            self.play(FadeIn(diff))
            #self.add(*small_stars, big_star)

            polygon1 = Polygon(ORIGIN + [0, flag.height / 2, 0], ORIGIN,
                              ORIGIN + [flag.width/2, 0, 0], flag.get_corner(UR),
                              fill_color=rgb_to_color([238 / 255.0, 28 / 255.0, 37 / 255.0]), fill_opacity=1,
                              stroke_color=rgb_to_color([238 / 255.0, 28 / 255.0, 37 / 255.0])
                              )
            polygon2 = Polygon( ORIGIN - [flag.width / 2, 0, 0],
                               flag.get_corner(DL), flag.get_corner(DR), ORIGIN + [flag.width / 2, 0, 0],
                               fill_color=rgb_to_color([238 / 255.0, 28 / 255.0, 37 / 255.0]), fill_opacity=1,
                               stroke_color=rgb_to_color([238 / 255.0, 28 / 255.0, 37 / 255.0])
                               )
            self.play(GrowFromEdge(polygon1, UP), run_time=3)
            self.play(GrowFromEdge(polygon2, LEFT), run_time=3)
            self.wait_until_bookmark('N')

        self.wait(3)
