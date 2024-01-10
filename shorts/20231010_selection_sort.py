import numpy
from manim import *
from numpy import *

config.pixel_width = 180 * 2
config.pixel_height = 320 * 2


class SelectSort(Scene):
    def construct(self):
        self.add(Text(r"Selection Sort Algorithm", font_size=64).move_to([0, 9, 0]))
        self.add(Rectangle(width=11, height=1.8, stroke_color=BLACK,
                           fill_color=YELLOW, fill_opacity=0.4).move_to([0, 9, 0]))

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

        rt = 0.4

        txt = Text(r"First Round", font_size=150, color=RED, stroke_width=5)
        self.play(GrowFromCenter(txt))
        self.remove(txt)

        def move_rect(direction, index):
            self.play(VGroup(rect_objs[list.index(index)], txt_objs[list.index(index)]).animate.shift(direction),
                      run_time=rt)

        def wiggle_rect(index):
            self.play(Wiggle(VGroup(rect_objs[list.index(index)], txt_objs[list.index(index)])), run_time=1)

        circle = Circle(radius=0.2, color=RED, fill_color=RED, fill_opacity=1).next_to(rect_objs[list.index(10)], LEFT*5)
        self.add(circle)

        move_rect(LEFT, 10)
        move_rect(LEFT, 8)
        move_rect(RIGHT, 10)
        move_rect(LEFT, 2)
        move_rect(RIGHT, 8)
        move_rect(LEFT, 9)
        wiggle_rect(9)
        move_rect(RIGHT, 9)
        move_rect(LEFT, 1)
        move_rect(RIGHT, 2)
        move_rect(LEFT, 6)
        wiggle_rect(6)
        move_rect(RIGHT, 6)
        move_rect(LEFT, 3)
        wiggle_rect(3)
        move_rect(RIGHT, 3)
        move_rect(LEFT, 5)
        wiggle_rect(5)
        move_rect(RIGHT, 5)
        move_rect(LEFT, 7)
        wiggle_rect(7)
        move_rect(RIGHT, 7)
        move_rect(LEFT, 4)
        wiggle_rect(4)
        move_rect(RIGHT, 4)

        self.play(VGroup(rect_objs[list.index(1)], txt_objs[list.index(1)]).animate.shift(UP*1.5*4),
                  VGroup(rect_objs[list.index(2)], txt_objs[list.index(2)]).animate.shift(DOWN * 1.5 * 1),
                  VGroup(rect_objs[list.index(9)], txt_objs[list.index(9)]).animate.shift(DOWN * 1.5 * 1),
                  VGroup(rect_objs[list.index(10)], txt_objs[list.index(10)]).animate.shift(DOWN * 1.5 * 1),
                  VGroup(rect_objs[list.index(8)], txt_objs[list.index(8)]).animate.shift(DOWN * 1.5 * 1),
                  run_time=rt)
        move_rect(RIGHT, 1)

        txt = Text(r"Second Round", font_size=150, color=RED, stroke_width=5)
        self.play(GrowFromCenter(txt))
        self.remove(txt)

        self.play(circle.animate.shift(DOWN*1.5), run_time=rt)
        move_rect(LEFT, 10)
        move_rect(LEFT, 8)
        move_rect(RIGHT, 10)
        move_rect(LEFT, 2)
        move_rect(RIGHT, 8)
        move_rect(LEFT, 9)
        wiggle_rect(9)
        move_rect(RIGHT, 9)
        move_rect(LEFT, 6)
        wiggle_rect(6)
        move_rect(RIGHT, 6)
        move_rect(LEFT, 3)
        wiggle_rect(3)
        move_rect(RIGHT, 3)
        move_rect(LEFT, 5)
        wiggle_rect(5)
        move_rect(RIGHT, 5)
        move_rect(LEFT, 7)
        wiggle_rect(7)
        move_rect(RIGHT, 7)
        move_rect(LEFT, 4)
        wiggle_rect(4)
        move_rect(RIGHT, 4)

        self.play(VGroup(rect_objs[list.index(2)], txt_objs[list.index(2)]).animate.shift(UP * 1.5 * 2),
                  VGroup(rect_objs[list.index(10)], txt_objs[list.index(10)]).animate.shift(DOWN * 1.5 * 1),
                  VGroup(rect_objs[list.index(8)], txt_objs[list.index(8)]).animate.shift(DOWN * 1.5 * 1),
                  run_time=rt)
        move_rect(RIGHT, 2)

        txt = Text(r"Third Round", font_size=150, color=RED, stroke_width=5)
        self.play(GrowFromCenter(txt))
        self.remove(txt)

        self.play(circle.animate.shift(DOWN * 1.5), run_time=rt)
        move_rect(LEFT, 10)
        move_rect(LEFT, 8)
        move_rect(RIGHT, 10)
        move_rect(LEFT, 9)
        wiggle_rect(9)
        move_rect(RIGHT, 9)
        move_rect(LEFT, 6)
        move_rect(RIGHT, 8)
        move_rect(LEFT, 3)
        move_rect(RIGHT, 6)
        move_rect(LEFT, 5)
        wiggle_rect(5)
        move_rect(RIGHT, 5)
        move_rect(LEFT, 7)
        wiggle_rect(7)
        move_rect(RIGHT, 7)
        move_rect(LEFT, 4)
        wiggle_rect(4)
        move_rect(RIGHT, 4)

        self.play(VGroup(rect_objs[list.index(3)], txt_objs[list.index(3)]).animate.shift(UP * 1.5 * 4),
                  VGroup(rect_objs[list.index(10)], txt_objs[list.index(10)]).animate.shift(DOWN * 1.5 * 1),
                  VGroup(rect_objs[list.index(8)], txt_objs[list.index(8)]).animate.shift(DOWN * 1.5 * 1),
                  VGroup(rect_objs[list.index(9)], txt_objs[list.index(9)]).animate.shift(DOWN * 1.5 * 1),
                  VGroup(rect_objs[list.index(6)], txt_objs[list.index(6)]).animate.shift(DOWN * 1.5 * 1),
                  run_time=rt)
        move_rect(RIGHT, 3)

        txt = Text(r"Forth Round", font_size=150, color=RED, stroke_width=5)
        self.play(GrowFromCenter(txt))
        self.remove(txt)

        self.play(circle.animate.shift(DOWN * 1.5), run_time=rt)
        move_rect(LEFT, 10)
        move_rect(LEFT, 8)
        move_rect(RIGHT, 10)
        move_rect(LEFT, 9)
        wiggle_rect(9)
        move_rect(RIGHT, 9)
        move_rect(LEFT, 6)
        move_rect(RIGHT, 8)
        move_rect(LEFT, 5)
        move_rect(RIGHT, 6)
        move_rect(LEFT, 7)
        wiggle_rect(7)
        move_rect(RIGHT, 7)
        move_rect(LEFT, 4)
        move_rect(RIGHT, 5)

        self.play(VGroup(rect_objs[list.index(4)], txt_objs[list.index(4)]).animate.shift(UP * 1.5 * 6),
                  VGroup(rect_objs[list.index(10)], txt_objs[list.index(10)]).animate.shift(DOWN * 1.5 * 1),
                  VGroup(rect_objs[list.index(8)], txt_objs[list.index(8)]).animate.shift(DOWN * 1.5 * 1),
                  VGroup(rect_objs[list.index(9)], txt_objs[list.index(9)]).animate.shift(DOWN * 1.5 * 1),
                  VGroup(rect_objs[list.index(6)], txt_objs[list.index(6)]).animate.shift(DOWN * 1.5 * 1),
                  VGroup(rect_objs[list.index(5)], txt_objs[list.index(5)]).animate.shift(DOWN * 1.5 * 1),
                  VGroup(rect_objs[list.index(7)], txt_objs[list.index(7)]).animate.shift(DOWN * 1.5 * 1),
                  run_time=rt)
        move_rect(RIGHT, 4)

        txt = Text(r"Fifth Round", font_size=150, color=RED, stroke_width=5)
        self.play(GrowFromCenter(txt))
        self.remove(txt)

        self.play(circle.animate.shift(DOWN * 1.5), run_time=rt)

        move_rect(LEFT, 10)
        move_rect(LEFT, 8)
        move_rect(RIGHT, 10)
        move_rect(LEFT, 9)
        wiggle_rect(9)
        move_rect(RIGHT, 9)
        move_rect(LEFT, 6)
        move_rect(RIGHT, 8)
        move_rect(LEFT, 5)
        move_rect(RIGHT, 6)
        move_rect(LEFT, 7)
        wiggle_rect(7)
        move_rect(RIGHT, 7)

        self.play(VGroup(rect_objs[list.index(5)], txt_objs[list.index(5)]).animate.shift(UP * 1.5 * 4),
                  VGroup(rect_objs[list.index(10)], txt_objs[list.index(10)]).animate.shift(DOWN * 1.5 * 1),
                  VGroup(rect_objs[list.index(8)], txt_objs[list.index(8)]).animate.shift(DOWN * 1.5 * 1),
                  VGroup(rect_objs[list.index(9)], txt_objs[list.index(9)]).animate.shift(DOWN * 1.5 * 1),
                  VGroup(rect_objs[list.index(6)], txt_objs[list.index(6)]).animate.shift(DOWN * 1.5 * 1),
                  run_time=rt)

        move_rect(RIGHT, 5)


        txt = Text(r"Sixth Round", font_size=150, color=RED, stroke_width=5)
        self.play(GrowFromCenter(txt))
        self.remove(txt)

        self.play(circle.animate.shift(DOWN * 1.5), run_time=rt)

        move_rect(LEFT, 10)
        move_rect(LEFT, 8)
        move_rect(RIGHT, 10)
        move_rect(LEFT, 9)
        wiggle_rect(9)
        move_rect(RIGHT, 9)
        move_rect(LEFT, 6)
        move_rect(RIGHT, 8)
        move_rect(LEFT, 7)
        wiggle_rect(7)
        move_rect(RIGHT, 7)

        self.play(VGroup(rect_objs[list.index(6)], txt_objs[list.index(6)]).animate.shift(UP * 1.5 * 3),
                  VGroup(rect_objs[list.index(10)], txt_objs[list.index(10)]).animate.shift(DOWN * 1.5 * 1),
                  VGroup(rect_objs[list.index(8)], txt_objs[list.index(8)]).animate.shift(DOWN * 1.5 * 1),
                  VGroup(rect_objs[list.index(9)], txt_objs[list.index(9)]).animate.shift(DOWN * 1.5 * 1),
                  run_time=rt)

        move_rect(RIGHT, 6)

        txt=Text(r"Seventh Round", font_size=150, color=RED, stroke_width=5)
        self.play(GrowFromCenter(txt))
        self.remove(txt)

        self.play(circle.animate.shift(DOWN * 1.5), run_time=rt)
        move_rect(LEFT, 10)
        move_rect(LEFT, 8)
        move_rect(RIGHT, 10)
        move_rect(LEFT, 9)
        wiggle_rect(9)
        move_rect(RIGHT, 9)
        move_rect(LEFT, 7)
        move_rect(RIGHT, 8)
        self.play(VGroup(rect_objs[list.index(7)], txt_objs[list.index(7)]).animate.shift(UP * 1.5 * 3),
                  VGroup(rect_objs[list.index(10)], txt_objs[list.index(10)]).animate.shift(DOWN * 1.5 * 1),
                  VGroup(rect_objs[list.index(8)], txt_objs[list.index(8)]).animate.shift(DOWN * 1.5 * 1),
                  VGroup(rect_objs[list.index(9)], txt_objs[list.index(9)]).animate.shift(DOWN * 1.5 * 1),
                  run_time=rt)

        move_rect(RIGHT, 7)

        txt = Text(r"Eighth Round", font_size=150, color=RED, stroke_width=5)
        self.play(GrowFromCenter(txt))
        self.remove(txt)

        self.play(circle.animate.shift(DOWN * 1.5), run_time=rt)

        move_rect(LEFT, 10)
        move_rect(LEFT, 8)
        move_rect(RIGHT, 10)
        move_rect(LEFT, 9)
        wiggle_rect(9)
        move_rect(RIGHT, 9)

        self.play(VGroup(rect_objs[list.index(8)], txt_objs[list.index(8)]).animate.shift(UP * 1.5 * 1),
                  VGroup(rect_objs[list.index(10)], txt_objs[list.index(10)]).animate.shift(DOWN * 1.5 * 1),
                  run_time=rt)

        move_rect(RIGHT, 8)


        txt = Text(r"Ninth Round", font_size=150, color=RED, stroke_width=5)
        self.play(GrowFromCenter(txt))
        self.remove(txt)

        self.play(circle.animate.shift(DOWN * 1.5), run_time=rt)
        move_rect(LEFT, 10)
        move_rect(LEFT, 9)
        move_rect(RIGHT, 10)
        self.play(VGroup(rect_objs[list.index(9)], txt_objs[list.index(9)]).animate.shift(UP * 1.5 * 1),
                  VGroup(rect_objs[list.index(10)], txt_objs[list.index(10)]).animate.shift(DOWN * 1.5 * 1),
                  run_time=rt)
        move_rect(RIGHT, 9)

        txt = Text(r"Finish", font_size=150, color=RED, stroke_width=5)
        self.play(GrowFromCenter(txt))
        self.remove(txt)

        self.remove(circle)

        self.wait(3)


