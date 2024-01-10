import numpy
from manim import *
from numpy import *

config.pixel_width = 180 * 2
config.pixel_height = 320 * 2


class BubbleSort(Scene):
    def construct(self):
        self.add(Text("Bubble Sort Algorithm", font_size=64).move_to([0, 9, 0]))
        self.add(Rectangle(width=9.5, height=1.8, stroke_color=BLACK,
                           fill_color=GREEN, fill_opacity=0.4).move_to([0, 9, 0]))

        groups = []
        j = 6.5
        scale = 0.8
        list = [10, 8, 2, 9, 1, 6, 3, 5, 7, 4]
        for i in list:
            group = VGroup(Rectangle(width=i, height=1, fill_color=BLUE, fill_opacity=0.4)
                           .move_to([-4 + i / 2.0, j, 0]),
                           Text(str(i)).move_to([-4 + i / 2.0, j, 0])
                           )
            groups.append(group)
            j = j - 1.5

        self.add(*groups)

        # self.play(groups[len(groups) - 1].animate.set_fill(RED))

        brace = BraceBetweenPoints(
            [-4, 7, 0], [-4, 4.5, 0], color=PURPLE, sharpness=2.0, stroke_width=10
        )
        txt = Text(r"First Round", font_size=200, color=RED, stroke_width=5)
        self.play(FadeIn(brace), GrowFromCenter(txt))
        self.remove(txt)

        self.play(groups[list.index(10)].animate.shift(numpy.array([0, -1.5, 0])),
                  groups[list.index(8)].animate.shift(numpy.array([0, +1.5, 0]))
                  )
        self.play(brace.animate.shift(numpy.array([0, -1.5, 0])))
        self.play(groups[list.index(10)].animate.shift(numpy.array([0, -1.5, 0])),
                  groups[list.index(2)].animate.shift(numpy.array([0, +1.5, 0]))
                  )
        self.play(brace.animate.shift(numpy.array([0, -1.5, 0])))
        self.play(groups[list.index(10)].animate.shift(numpy.array([0, -1.5, 0])),
                  groups[list.index(9)].animate.shift(numpy.array([0, +1.5, 0]))
                  )
        self.play(brace.animate.shift(numpy.array([0, -1.5, 0])))
        self.play(groups[list.index(10)].animate.shift(numpy.array([0, -1.5, 0])),
                  groups[list.index(1)].animate.shift(numpy.array([0, +1.5, 0]))
                  )
        self.play(brace.animate.shift(numpy.array([0, -1.5, 0])))
        self.play(groups[list.index(10)].animate.shift(numpy.array([0, -1.5, 0])),
                  groups[list.index(6)].animate.shift(numpy.array([0, +1.5, 0]))
                  )
        self.play(brace.animate.shift(numpy.array([0, -1.5, 0])))
        self.play(groups[list.index(10)].animate.shift(numpy.array([0, -1.5, 0])),
                  groups[list.index(3)].animate.shift(numpy.array([0, +1.5, 0]))
                  )
        self.play(brace.animate.shift(numpy.array([0, -1.5, 0])))
        self.play(groups[list.index(10)].animate.shift(numpy.array([0, -1.5, 0])),
                  groups[list.index(5)].animate.shift(numpy.array([0, +1.5, 0]))
                  )
        self.play(brace.animate.shift(numpy.array([0, -1.5, 0])))
        self.play(groups[list.index(10)].animate.shift(numpy.array([0, -1.5, 0])),
                  groups[list.index(7)].animate.shift(numpy.array([0, +1.5, 0]))
                  )
        self.play(brace.animate.shift(numpy.array([0, -1.5, 0])))
        self.play(groups[list.index(10)].animate.shift(numpy.array([0, -1.5, 0])),
                  groups[list.index(4)].animate.shift(numpy.array([0, +1.5, 0]))
                  )

        txt = Text(r"Second Round", font_size=200, color=RED, stroke_width=5)
        self.play(GrowFromCenter(txt))
        self.remove(txt)
        self.play(brace.animate.shift(numpy.array([0, 1.5 * 8, 0])))
        self.play(groups[list.index(8)].animate.shift(numpy.array([0, -1.5, 0])),
                  groups[list.index(2)].animate.shift(numpy.array([0, +1.5, 0]))
                  )
        self.play(brace.animate.shift(numpy.array([0, -1.5, 0])))
        self.play(brace.animate.shift(numpy.array([0, -1.5, 0])))
        self.play(groups[list.index(9)].animate.shift(numpy.array([0, -1.5, 0])),
                  groups[list.index(1)].animate.shift(numpy.array([0, +1.5, 0]))
                  )
        self.play(brace.animate.shift(numpy.array([0, -1.5, 0])))
        self.play(groups[list.index(9)].animate.shift(numpy.array([0, -1.5, 0])),
                  groups[list.index(6)].animate.shift(numpy.array([0, +1.5, 0]))
                  )
        self.play(brace.animate.shift(numpy.array([0, -1.5, 0])))
        self.play(groups[list.index(9)].animate.shift(numpy.array([0, -1.5, 0])),
                  groups[list.index(3)].animate.shift(numpy.array([0, +1.5, 0]))
                  )
        self.play(brace.animate.shift(numpy.array([0, -1.5, 0])))
        self.play(groups[list.index(9)].animate.shift(numpy.array([0, -1.5, 0])),
                  groups[list.index(5)].animate.shift(numpy.array([0, +1.5, 0]))
                  )
        self.play(brace.animate.shift(numpy.array([0, -1.5, 0])))
        self.play(groups[list.index(9)].animate.shift(numpy.array([0, -1.5, 0])),
                  groups[list.index(7)].animate.shift(numpy.array([0, +1.5, 0]))
                  )
        self.play(brace.animate.shift(numpy.array([0, -1.5, 0])))
        self.play(groups[list.index(9)].animate.shift(numpy.array([0, -1.5, 0])),
                  groups[list.index(4)].animate.shift(numpy.array([0, +1.5, 0]))
                  )

        txt = Text(r"Third Round", font_size=200, color=RED, stroke_width=5)
        self.play(GrowFromCenter(txt))
        self.remove(txt)
        self.play(brace.animate.shift(numpy.array([0, 1.5 * 7, 0])))
        self.play(brace.animate.shift(numpy.array([0, -1.5, 0])))
        self.play(groups[list.index(8)].animate.shift(numpy.array([0, -1.5, 0])),
                  groups[list.index(1)].animate.shift(numpy.array([0, +1.5, 0]))
                  )

        for val in [6, 3, 5, 7, 4]:
            self.play(brace.animate.shift(numpy.array([0, -1.5, 0])))
            self.play(groups[list.index(8)].animate.shift(numpy.array([0, -1.5, 0])),
                      groups[list.index(val)].animate.shift(numpy.array([0, +1.5, 0]))
                      )

        txt = Text(r"Forth Round", font_size=200, color=RED, stroke_width=5)
        self.play(GrowFromCenter(txt))
        self.remove(txt)
        self.play(brace.animate.shift(numpy.array([0, 1.5 * 6, 0])))
        self.play(groups[list.index(2)].animate.shift(numpy.array([0, -1.5, 0])),
                  groups[list.index(1)].animate.shift(numpy.array([0, +1.5, 0]))
                  )
        self.play(brace.animate.shift(numpy.array([0, -1.5, 0])))
        self.play(brace.animate.shift(numpy.array([0, -1.5, 0])))
        self.play(groups[list.index(6)].animate.shift(numpy.array([0, -1.5, 0])),
                  groups[list.index(3)].animate.shift(numpy.array([0, +1.5, 0]))
                  )
        self.play(brace.animate.shift(numpy.array([0, -1.5, 0])))
        self.play(groups[list.index(6)].animate.shift(numpy.array([0, -1.5, 0])),
                  groups[list.index(5)].animate.shift(numpy.array([0, +1.5, 0]))
                  )
        self.play(brace.animate.shift(numpy.array([0, -1.5, 0])))
        self.play(brace.animate.shift(numpy.array([0, -1.5, 0])))
        self.play(groups[list.index(7)].animate.shift(numpy.array([0, -1.5, 0])),
                  groups[list.index(4)].animate.shift(numpy.array([0, +1.5, 0]))
                  )

        txt = Text(r"Fifth Round", font_size=200, color=RED, stroke_width=5)
        self.play(GrowFromCenter(txt))
        self.remove(txt)
        self.play(brace.animate.shift(numpy.array([0, 1.5 * 5, 0])))

        self.play(brace.animate.shift(numpy.array([0, -1.5, 0])))
        self.play(brace.animate.shift(numpy.array([0, -1.5, 0])))
        self.play(brace.animate.shift(numpy.array([0, -1.5, 0])))

        self.play(brace.animate.shift(numpy.array([0, -1.5, 0])))
        self.play(groups[list.index(6)].animate.shift(numpy.array([0, -1.5, 0])),
                  groups[list.index(4)].animate.shift(numpy.array([0, +1.5, 0]))
                  )

        txt = Text(r"Sixth Round", font_size=200, color=RED, stroke_width=5)
        self.play(GrowFromCenter(txt))
        self.remove(txt)
        self.play(brace.animate.shift(numpy.array([0, 1.5 * 4, 0])))

        self.play(brace.animate.shift(numpy.array([0, -1.5, 0])))
        self.play(brace.animate.shift(numpy.array([0, -1.5, 0])))
        self.play(brace.animate.shift(numpy.array([0, -1.5, 0])))
        self.play(groups[list.index(5)].animate.shift(numpy.array([0, -1.5, 0])),
                  groups[list.index(4)].animate.shift(numpy.array([0, +1.5, 0]))
                  )

        txt = Text(r"Seventh Round", font_size=200, color=RED, stroke_width=5)
        self.play(GrowFromCenter(txt))
        self.remove(txt)
        self.play(brace.animate.shift(numpy.array([0, 1.5 * 3, 0])))
        self.play(brace.animate.shift(numpy.array([0, -1.5, 0])))
        self.play(brace.animate.shift(numpy.array([0, -1.5, 0])))

        txt = Text(r"Eighth Round", font_size=200, color=RED, stroke_width=5)
        self.play(GrowFromCenter(txt))
        self.remove(txt)
        self.play(brace.animate.shift(numpy.array([0, 1.5 * 2, 0])))
        self.play(brace.animate.shift(numpy.array([0, -1.5, 0])))

        txt = Text(r"Ninth Round", font_size=200, color=RED, stroke_width=5)
        self.play(GrowFromCenter(txt))
        self.remove(txt)
        self.play(brace.animate.shift(numpy.array([0, 1.5 * 1, 0])))

        self.remove(brace)

        self.wait(3)
