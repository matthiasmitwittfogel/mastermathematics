import numpy
from manim import *
from numpy import *

config.pixel_width = 180 * 2
config.pixel_height = 320 * 2


class InsertSort(Scene):
    def construct(self):
        self.add(Text(r"Insertion Sort Algorithm", font_size=64).move_to([0, 9, 0]))
        self.add(Rectangle(width=11, height=1.8, stroke_color=BLACK,
                           fill_color=RED, fill_opacity=0.4).move_to([0, 9, 0]))

        txt_objs = []
        rect_objs = []
        j = 6.5
        scale = 0.8
        list = [10, 8, 2, 9, 1, 6, 3, 5, 7, 4]
        for i in list:
            txt_objs.append(Text(str(i)).move_to([-4 + i / 2.0, j, 0]))
            rect_objs.append(Rectangle(width=i, height=1, fill_color=BLUE, fill_opacity=0.4)
                             .move_to([-4 + i / 2.0, j, 0]))
            j = j - 1.5

        self.add(*txt_objs, *rect_objs)

        rt = 0.5

        txt = Text(r"First Round", font_size=150, color=RED, stroke_width=5)
        self.play(GrowFromCenter(txt))
        self.remove(txt)

        circle = Circle(radius=0.2, color=RED, fill_color=RED, fill_opacity=1).next_to(rect_objs[list.index(8)], LEFT*5)
        self.add(circle)

        self.play(VGroup(rect_objs[list.index(8)], txt_objs[list.index(8)]).animate.shift(LEFT),
                  VGroup(rect_objs[list.index(10)], txt_objs[list.index(10)]).animate.shift(LEFT),
                  run_time=rt)

        self.play(VGroup(rect_objs[list.index(8)], txt_objs[list.index(8)]).animate.shift(UP*1.5),
                  VGroup(rect_objs[list.index(10)], txt_objs[list.index(10)]).animate.shift(DOWN*1.5),
                  run_time=rt)
        self.play(VGroup(rect_objs[list.index(8)], txt_objs[list.index(8)]).animate.shift(RIGHT),
                  VGroup(rect_objs[list.index(10)], txt_objs[list.index(10)]).animate.shift(RIGHT),
                  run_time=rt)

        txt = Text(r"Second Round", font_size=150, color=RED, stroke_width=5)
        self.play(GrowFromCenter(txt))
        self.remove(txt)

        self.play(circle.animate.shift(DOWN*1.5), run_time=rt)

        self.play(VGroup(rect_objs[list.index(2)], txt_objs[list.index(2)]).animate.shift(LEFT),
                  VGroup(rect_objs[list.index(10)], txt_objs[list.index(10)]).animate.shift(LEFT),
                  run_time=rt)
        self.play(
                  VGroup(rect_objs[list.index(8)], txt_objs[list.index(8)]).animate.shift(LEFT),
                  run_time=rt)

        self.play(VGroup(rect_objs[list.index(2)], txt_objs[list.index(2)]).animate.shift(UP*1.5*2),
                  VGroup(rect_objs[list.index(8)], txt_objs[list.index(8)]).animate.shift(DOWN*1.5),
                  VGroup(rect_objs[list.index(10)], txt_objs[list.index(10)]).animate.shift(DOWN * 1.5),
                  run_time=rt)

        self.play(VGroup(rect_objs[list.index(2)], txt_objs[list.index(2)]).animate.shift(RIGHT),
                  VGroup(rect_objs[list.index(8)], txt_objs[list.index(8)]).animate.shift(RIGHT),
                  VGroup(rect_objs[list.index(10)], txt_objs[list.index(10)]).animate.shift(RIGHT),
                  run_time=rt)

        txt = Text(r"Third Round", font_size=150, color=RED, stroke_width=5)
        self.play(GrowFromCenter(txt))
        self.remove(txt)

        self.play(circle.animate.shift(DOWN * 1.5), run_time=rt)
        self.play(VGroup(rect_objs[list.index(9)], txt_objs[list.index(9)]).animate.shift(LEFT),
                  VGroup(rect_objs[list.index(10)], txt_objs[list.index(10)]).animate.shift(LEFT),
                  run_time=rt)
        self.play(
                  VGroup(rect_objs[list.index(8)], txt_objs[list.index(8)]).animate.shift(LEFT),
                  run_time=rt)
        self.play(Wiggle(VGroup(rect_objs[list.index(8)], txt_objs[list.index(8)])), run_time=1)
        self.play(
            VGroup(rect_objs[list.index(8)], txt_objs[list.index(8)]).animate.shift(RIGHT),
            run_time=rt)
        self.play(
                  VGroup(rect_objs[list.index(9)], txt_objs[list.index(9)]).animate.shift(UP * 1.5),
                  VGroup(rect_objs[list.index(10)], txt_objs[list.index(10)]).animate.shift(DOWN * 1.5),
                  run_time=rt)
        self.play(
            VGroup(rect_objs[list.index(9)], txt_objs[list.index(9)]).animate.shift(RIGHT),
            VGroup(rect_objs[list.index(10)], txt_objs[list.index(10)]).animate.shift(RIGHT),
            run_time=rt)

        txt = Text(r"Forth Round", font_size=150, color=RED, stroke_width=5)
        self.play(GrowFromCenter(txt))
        self.remove(txt)

        self.play(circle.animate.shift(DOWN * 1.5), run_time=rt)

        self.play(VGroup(rect_objs[list.index(1)], txt_objs[list.index(1)]).animate.shift(LEFT),
                  VGroup(rect_objs[list.index(10)], txt_objs[list.index(10)]).animate.shift(LEFT),
                  run_time=rt)
        self.play(VGroup(rect_objs[list.index(9)], txt_objs[list.index(9)]).animate.shift(LEFT),
                  run_time=rt)
        self.play(VGroup(rect_objs[list.index(8)], txt_objs[list.index(8)]).animate.shift(LEFT),
                  run_time=rt)
        self.play(VGroup(rect_objs[list.index(2)], txt_objs[list.index(2)]).animate.shift(LEFT),
                  run_time=rt)
        self.play(
            VGroup(rect_objs[list.index(1)], txt_objs[list.index(1)]).animate.shift(UP*1.5*4),
            VGroup(rect_objs[list.index(2)], txt_objs[list.index(2)]).animate.shift(DOWN * 1.5),
            VGroup(rect_objs[list.index(8)], txt_objs[list.index(8)]).animate.shift(DOWN * 1.5),
            VGroup(rect_objs[list.index(9)], txt_objs[list.index(9)]).animate.shift(DOWN * 1.5),
            VGroup(rect_objs[list.index(10)], txt_objs[list.index(10)]).animate.shift(DOWN * 1.5),
            run_time=rt)

        self.play(
            VGroup(rect_objs[list.index(1)], txt_objs[list.index(1)]).animate.shift(RIGHT),
            VGroup(rect_objs[list.index(2)], txt_objs[list.index(2)]).animate.shift(RIGHT),
            VGroup(rect_objs[list.index(8)], txt_objs[list.index(8)]).animate.shift(RIGHT),
            VGroup(rect_objs[list.index(9)], txt_objs[list.index(9)]).animate.shift(RIGHT),
            VGroup(rect_objs[list.index(10)], txt_objs[list.index(10)]).animate.shift(RIGHT),
            run_time=rt)

        txt = Text(r"Fifth Round", font_size=150, color=RED, stroke_width=5)
        self.play(GrowFromCenter(txt))
        self.remove(txt)

        self.play(circle.animate.shift(DOWN * 1.5), run_time=rt)

        self.play(VGroup(rect_objs[list.index(6)], txt_objs[list.index(6)]).animate.shift(LEFT),
                  VGroup(rect_objs[list.index(10)], txt_objs[list.index(10)]).animate.shift(LEFT),
                  run_time=rt)
        self.play(VGroup(rect_objs[list.index(9)], txt_objs[list.index(9)]).animate.shift(LEFT),
                  run_time=rt)
        self.play(VGroup(rect_objs[list.index(8)], txt_objs[list.index(8)]).animate.shift(LEFT),
                  run_time=rt)
        self.play(VGroup(rect_objs[list.index(2)], txt_objs[list.index(2)]).animate.shift(LEFT),
                  run_time=rt)
        self.play(Wiggle(VGroup(rect_objs[list.index(2)], txt_objs[list.index(2)])), run_time=1)
        self.play(VGroup(rect_objs[list.index(2)], txt_objs[list.index(2)]).animate.shift(RIGHT),
                  run_time=rt)

        self.play(
            VGroup(rect_objs[list.index(6)], txt_objs[list.index(6)]).animate.shift(UP*1.5*3),
            VGroup(rect_objs[list.index(10)], txt_objs[list.index(10)]).animate.shift(DOWN*1.5),
            VGroup(rect_objs[list.index(8)], txt_objs[list.index(8)]).animate.shift(DOWN*1.5),
            VGroup(rect_objs[list.index(9)], txt_objs[list.index(9)]).animate.shift(DOWN*1.5),
            run_time=rt)

        self.play(
            VGroup(rect_objs[list.index(6)], txt_objs[list.index(6)]).animate.shift(RIGHT),
            VGroup(rect_objs[list.index(10)], txt_objs[list.index(10)]).animate.shift(RIGHT),
            VGroup(rect_objs[list.index(8)], txt_objs[list.index(8)]).animate.shift(RIGHT),
            VGroup(rect_objs[list.index(9)], txt_objs[list.index(9)]).animate.shift(RIGHT),
            run_time=rt)

        txt = Text(r"Sixth Round", font_size=150, color=RED, stroke_width=5)
        self.play(GrowFromCenter(txt))
        self.remove(txt)

        self.play(circle.animate.shift(DOWN * 1.5), run_time=rt)
        self.play(VGroup(rect_objs[list.index(3)], txt_objs[list.index(3)]).animate.shift(LEFT),
                  VGroup(rect_objs[list.index(10)], txt_objs[list.index(10)]).animate.shift(LEFT),
                  run_time=rt)
        self.play(VGroup(rect_objs[list.index(9)], txt_objs[list.index(9)]).animate.shift(LEFT),
                  run_time=rt)
        self.play(VGroup(rect_objs[list.index(8)], txt_objs[list.index(8)]).animate.shift(LEFT),
                  run_time=rt)
        self.play(VGroup(rect_objs[list.index(6)], txt_objs[list.index(6)]).animate.shift(LEFT),
                  run_time=rt)
        self.play(VGroup(rect_objs[list.index(2)], txt_objs[list.index(2)]).animate.shift(LEFT),
                  run_time=rt)
        self.play(Wiggle(VGroup(rect_objs[list.index(2)], txt_objs[list.index(2)])), run_time=1)
        self.play(VGroup(rect_objs[list.index(2)], txt_objs[list.index(2)]).animate.shift(RIGHT),
                  run_time=rt)
        self.play(VGroup(rect_objs[list.index(3)], txt_objs[list.index(3)]).animate.shift(UP*1.5*4),
                  VGroup(rect_objs[list.index(10)], txt_objs[list.index(10)]).animate.shift(DOWN * 1.5),
                  VGroup(rect_objs[list.index(8)], txt_objs[list.index(8)]).animate.shift(DOWN * 1.5),
                  VGroup(rect_objs[list.index(9)], txt_objs[list.index(9)]).animate.shift(DOWN * 1.5),
                  VGroup(rect_objs[list.index(6)], txt_objs[list.index(6)]).animate.shift(DOWN * 1.5),
                  run_time=rt)
        self.play(VGroup(rect_objs[list.index(3)], txt_objs[list.index(3)]).animate.shift(RIGHT),
                  VGroup(rect_objs[list.index(10)], txt_objs[list.index(10)]).animate.shift(RIGHT),
                  VGroup(rect_objs[list.index(8)], txt_objs[list.index(8)]).animate.shift(RIGHT),
                  VGroup(rect_objs[list.index(9)], txt_objs[list.index(9)]).animate.shift(RIGHT),
                  VGroup(rect_objs[list.index(6)], txt_objs[list.index(6)]).animate.shift(RIGHT),run_time=rt)

        txt=Text(r"Seventh Round", font_size=150, color=RED, stroke_width=5)
        self.play(GrowFromCenter(txt))
        self.remove(txt)

        self.play(circle.animate.shift(DOWN * 1.5), run_time=rt)
        self.play(VGroup(rect_objs[list.index(5)], txt_objs[list.index(5)]).animate.shift(LEFT),
                  VGroup(rect_objs[list.index(10)], txt_objs[list.index(10)]).animate.shift(LEFT),
                  run_time=rt)
        self.play(VGroup(rect_objs[list.index(9)], txt_objs[list.index(9)]).animate.shift(LEFT),
                  run_time=rt)
        self.play(VGroup(rect_objs[list.index(8)], txt_objs[list.index(8)]).animate.shift(LEFT),
                  run_time=rt)
        self.play(VGroup(rect_objs[list.index(6)], txt_objs[list.index(6)]).animate.shift(LEFT),
                  run_time=rt)
        self.play(VGroup(rect_objs[list.index(3)], txt_objs[list.index(3)]).animate.shift(LEFT),
                  run_time=rt)
        self.play(Wiggle(VGroup(rect_objs[list.index(3)], txt_objs[list.index(3)])), run_time=1)
        self.play(VGroup(rect_objs[list.index(3)], txt_objs[list.index(3)]).animate.shift(RIGHT),
                  run_time=rt)
        self.play(VGroup(rect_objs[list.index(5)], txt_objs[list.index(5)]).animate.shift(UP * 1.5 * 4),
                  VGroup(rect_objs[list.index(10)], txt_objs[list.index(10)]).animate.shift(DOWN * 1.5),
                  VGroup(rect_objs[list.index(8)], txt_objs[list.index(8)]).animate.shift(DOWN * 1.5),
                  VGroup(rect_objs[list.index(9)], txt_objs[list.index(9)]).animate.shift(DOWN * 1.5),
                  VGroup(rect_objs[list.index(6)], txt_objs[list.index(6)]).animate.shift(DOWN * 1.5),
                  run_time=rt)
        self.play(VGroup(rect_objs[list.index(5)], txt_objs[list.index(5)]).animate.shift(RIGHT),
                  VGroup(rect_objs[list.index(10)], txt_objs[list.index(10)]).animate.shift(RIGHT),
                  VGroup(rect_objs[list.index(8)], txt_objs[list.index(8)]).animate.shift(RIGHT),
                  VGroup(rect_objs[list.index(9)], txt_objs[list.index(9)]).animate.shift(RIGHT),
                  VGroup(rect_objs[list.index(6)], txt_objs[list.index(6)]).animate.shift(RIGHT), run_time=rt)

        txt = Text(r"Eighth Round", font_size=150, color=RED, stroke_width=5)
        self.play(GrowFromCenter(txt))
        self.remove(txt)

        self.play(circle.animate.shift(DOWN * 1.5), run_time=rt)
        self.play(VGroup(rect_objs[list.index(7)], txt_objs[list.index(7)]).animate.shift(LEFT),
                  VGroup(rect_objs[list.index(10)], txt_objs[list.index(10)]).animate.shift(LEFT),
                  run_time=rt)
        self.play(VGroup(rect_objs[list.index(9)], txt_objs[list.index(9)]).animate.shift(LEFT),
                  run_time=rt)
        self.play(VGroup(rect_objs[list.index(8)], txt_objs[list.index(8)]).animate.shift(LEFT),
                  run_time=rt)
        self.play(VGroup(rect_objs[list.index(6)], txt_objs[list.index(6)]).animate.shift(LEFT),
                  run_time=rt)
        self.play(Wiggle(VGroup(rect_objs[list.index(6)], txt_objs[list.index(6)])), run_time=1)
        self.play(VGroup(rect_objs[list.index(6)], txt_objs[list.index(6)]).animate.shift(RIGHT),
                  run_time=rt)
        self.play(VGroup(rect_objs[list.index(7)], txt_objs[list.index(7)]).animate.shift(UP*3*1.5),
                  VGroup(rect_objs[list.index(10)], txt_objs[list.index(10)]).animate.shift(DOWN*1.5),
                  VGroup(rect_objs[list.index(8)], txt_objs[list.index(8)]).animate.shift(DOWN*1.5),
                  VGroup(rect_objs[list.index(9)], txt_objs[list.index(9)]).animate.shift(DOWN*1.5),
                  run_time=rt)
        self.play(VGroup(rect_objs[list.index(7)], txt_objs[list.index(7)]).animate.shift(RIGHT),
                  VGroup(rect_objs[list.index(10)], txt_objs[list.index(10)]).animate.shift(RIGHT),
                  VGroup(rect_objs[list.index(8)], txt_objs[list.index(8)]).animate.shift(RIGHT),
                  VGroup(rect_objs[list.index(9)], txt_objs[list.index(9)]).animate.shift(RIGHT),
                  run_time=rt)

        txt = Text(r"Ninth Round", font_size=150, color=RED, stroke_width=5)
        self.play(GrowFromCenter(txt))
        self.remove(txt)

        self.play(circle.animate.shift(DOWN * 1.5), run_time=rt)
        self.play(VGroup(rect_objs[list.index(4)], txt_objs[list.index(4)]).animate.shift(LEFT),
                  VGroup(rect_objs[list.index(10)], txt_objs[list.index(10)]).animate.shift(LEFT),
                  run_time=rt)
        self.play(VGroup(rect_objs[list.index(9)], txt_objs[list.index(9)]).animate.shift(LEFT),
                  run_time=rt)
        self.play(VGroup(rect_objs[list.index(8)], txt_objs[list.index(8)]).animate.shift(LEFT),
                  run_time=rt)
        self.play(VGroup(rect_objs[list.index(7)], txt_objs[list.index(7)]).animate.shift(LEFT),
                  run_time=rt)
        self.play(VGroup(rect_objs[list.index(6)], txt_objs[list.index(6)]).animate.shift(LEFT),
                  run_time=rt)
        self.play(VGroup(rect_objs[list.index(5)], txt_objs[list.index(5)]).animate.shift(LEFT),
                  run_time=rt)
        self.play(VGroup(rect_objs[list.index(3)], txt_objs[list.index(3)]).animate.shift(LEFT),
                  run_time=rt)
        self.play(Wiggle(VGroup(rect_objs[list.index(3)], txt_objs[list.index(3)])), run_time=1)
        self.play(VGroup(rect_objs[list.index(3)], txt_objs[list.index(3)]).animate.shift(RIGHT),
                  run_time=rt)

        self.play(VGroup(rect_objs[list.index(4)], txt_objs[list.index(4)]).animate.shift(UP * 6 * 1.5),
                  VGroup(rect_objs[list.index(10)], txt_objs[list.index(10)]).animate.shift(DOWN * 1.5),
                  VGroup(rect_objs[list.index(8)], txt_objs[list.index(8)]).animate.shift(DOWN * 1.5),
                  VGroup(rect_objs[list.index(9)], txt_objs[list.index(9)]).animate.shift(DOWN * 1.5),
                  VGroup(rect_objs[list.index(7)], txt_objs[list.index(7)]).animate.shift(DOWN * 1.5),
                  VGroup(rect_objs[list.index(6)], txt_objs[list.index(6)]).animate.shift(DOWN * 1.5),
                  VGroup(rect_objs[list.index(5)], txt_objs[list.index(5)]).animate.shift(DOWN * 1.5),
                  run_time=rt)
        self.play(VGroup(rect_objs[list.index(7)], txt_objs[list.index(7)]).animate.shift(RIGHT),
                  VGroup(rect_objs[list.index(10)], txt_objs[list.index(10)]).animate.shift(RIGHT),
                  VGroup(rect_objs[list.index(8)], txt_objs[list.index(8)]).animate.shift(RIGHT),
                  VGroup(rect_objs[list.index(9)], txt_objs[list.index(9)]).animate.shift(RIGHT),
                  VGroup(rect_objs[list.index(6)], txt_objs[list.index(6)]).animate.shift(RIGHT),
                  VGroup(rect_objs[list.index(5)], txt_objs[list.index(5)]).animate.shift(RIGHT),
                  VGroup(rect_objs[list.index(4)], txt_objs[list.index(4)]).animate.shift(RIGHT),
                  run_time=rt)

        txt = Text(r"Finish", font_size=150, color=RED, stroke_width=5)
        self.play(GrowFromCenter(txt))
        self.remove(txt)

        self.remove(circle)

        self.wait(3)


