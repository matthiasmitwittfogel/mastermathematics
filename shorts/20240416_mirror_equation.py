import numpy as np
from manim import *
import math

# configs
config.background_color = BLACK
config.pixel_width = 180 * 12
config.pixel_height = 320 * 12


class SeriesSumFromOneOver3(Scene):
    def construct(self):
        self.add(Line(start=ORIGIN+DOWN*10, end=ORIGIN+UP*10))
        eq1 = MathTex(r"10^2=100", font_size=60).shift(UP*10).to_edge(LEFT).shift(RIGHT*3)
        eq1_ = MathTex(r"001=01^2", font_size=60).shift(UP * 10).to_edge(RIGHT).shift(LEFT*3)
        self.play(Write(eq1))
        self.play(CounterclockwiseTransform(eq1.copy(), eq1_))

        eq2 = MathTex(r"11^2=121", font_size=60).shift(UP*8).align_to(eq1, RIGHT)
        eq2_ = MathTex(r"121=11^2", font_size=60).shift(UP * 8).align_to(eq1_, LEFT)
        self.play(Write(eq2))
        self.play(CounterclockwiseTransform(eq2.copy(), eq2_))

        eq3 = MathTex("12^2=144", font_size=60).shift(UP*6).align_to(eq2, RIGHT)
        eq3_ = MathTex("441=21^2", font_size=60).shift(UP*6).align_to(eq2_, LEFT)
        self.play(Write(eq3))
        self.play(CounterclockwiseTransform(eq3.copy(), eq3_))

        eq4 = MathTex(r"13^2=169", font_size=60).shift(UP*4).align_to(eq3, RIGHT)
        eq4_ = MathTex(r"961=31^2", font_size=60).shift(UP*4).align_to(eq3_, LEFT)
        self.play(Write(eq4))
        self.play(CounterclockwiseTransform(eq4.copy(), eq4_))

        eq5 = MathTex(r"102^2=10404", font_size=60).shift(UP * 2).align_to(eq4, RIGHT)
        eq5_ = MathTex(r"40401=201^2", font_size=60).shift(UP * 2).align_to(eq4_, LEFT)
        self.play(Write(eq5))
        self.play(CounterclockwiseTransform(eq5.copy(), eq5_))

        eq6 = MathTex(r"103^2=10609", font_size=60).align_to(eq5, RIGHT)
        eq6_ = MathTex(r"90601=301^2", font_size=60).align_to(eq4_, LEFT)
        self.play(Write(eq6))
        self.play(CounterclockwiseTransform(eq6.copy(), eq6_))

        eq7 = MathTex(r"1002^2=1004004", font_size=60).shift(DOWN*2).align_to(eq5, RIGHT)
        eq7_ = MathTex(r"4004001=2001^2", font_size=60).shift(DOWN*2).align_to(eq4_, LEFT)
        self.play(Write(eq7))
        self.play(CounterclockwiseTransform(eq7.copy(), eq7_))

        eq8 = MathTex(r"1003^2=1006009", font_size=60).shift(DOWN*4).align_to(eq5, RIGHT)
        eq8_ = MathTex(r"9006001=3001^2", font_size=60).shift(DOWN*4).align_to(eq4_, LEFT)
        self.play(Write(eq8))
        self.play(CounterclockwiseTransform(eq8.copy(), eq8_))

        eq9 = MathTex(r"10002^2=100040004", font_size=55).shift(DOWN * 6).align_to(eq5, RIGHT)
        eq9_ = MathTex(r"400040001=20001^2", font_size=55).shift(DOWN * 6).align_to(eq4_, LEFT)
        self.play(Write(eq9))
        self.play(CounterclockwiseTransform(eq9.copy(), eq9_))

        eq10 = MathTex(r"10003^2=100060009", font_size=55).shift(DOWN * 8).align_to(eq5, RIGHT)
        eq10_ = MathTex(r"900060001=30001^2", font_size=55).shift(DOWN * 8).align_to(eq4_, LEFT)
        self.play(Write(eq10))
        self.play(CounterclockwiseTransform(eq10.copy(), eq10_))

        self.wait(3)