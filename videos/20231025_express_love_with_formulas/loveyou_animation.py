from manim import *
import numpy as np
import math
from colour import Color

# configs
config.background_color = BLACK


class MathLove(Scene):
    def construct(self):
        text = Text('How to express love through mathematical formulas?', font_size=30, fill_opacity=1,

                    ).move_to(ORIGIN)
        for letter in text:
            letter.set_color(random_bright_color())
        self.play(AddTextLetterByLetter(text))
        self.play(RemoveTextLetterByLetter(text), run_time=1)

        plane = NumberPlane()
        axes = Axes()
        self.add(axes)
        self.add(plane)

        def second_formula(x):
            return np.array([x, 1 / (x + 6), 0])

        curve1 = ParametricFunction(second_formula, t_range=np.array([-5.9, -4]), color=RED)
        curve1_back = ParametricFunction(second_formula, color=WHITE)

        formula1 = MathTex(r"y=\frac{1}{x+6}", color=WHITE, font_size=40).next_to(curve1, DOWN).shift(UP)
        self.play(Write(formula1))
        #self.play(Create(curve1_back))
        self.play(Create(curve1))
        #self.play(Uncreate(curve1_back))

        curve2 = ImplicitFunction(lambda x, y: pow(x + 2, 2) + pow(y - 2, 2) - 2,
                                 color=RED)
        formula2 = MathTex(r"(x+2)^2+(y-2)^2=2", color=WHITE, font_size=40).next_to(curve2, DOWN).shift(UP*3)

        self.play(Write(formula2))
        self.play(Create(curve2))

        def forth_formula(x):
            return np.array([x, -2*x, 0])

        def fifth_formula(x):
            return np.array([x, 2*x, 0])

        curve3 = ParametricFunction(forth_formula, color=RED, t_range=np.array([0,1])).shift(UP*3)
        curve4 = ParametricFunction(fifth_formula, color=RED, t_range=np.array([1, 2])).shift(DOWN)
        formula3 = MathTex("y=|2x-2|+1", color=WHITE, font_size=40).next_to(curve4, DOWN)

        self.play(Write(formula3))
        self.play(Create(curve3))
        self.play(Create(curve4))

        curve5 = ImplicitFunction(lambda x, y: -3 * math.sin(math.fabs(3 * (y - 2))) - x + 6, y_range=[1, 3],
                                  color=RED)

        formula5 = MathTex(r"x=-3sin(3|y-2|+6)", color=WHITE, font_size=40).next_to(curve5, DOWN).shift(UP)
        self.play(Write(formula5))
        self.play(Create(curve5))

        def sixth_formula(x):
            return np.array([x, x*x*x*x-3, 0])
        curve6 = ImplicitFunction(lambda x, y: y - math.pow(x, 4) + 3, color=RED, y_range=[-3,0])
        curve6_backup = ImplicitFunction(lambda x, y: y - math.pow(x, 4) + 3, color=WHITE)

        curve6_1 = ParametricFunction(sixth_formula, color=RED, t_range=np.array([-1.2, 1.2]))
        curve6_1_backup = ParametricFunction(sixth_formula, t_range=np.array([-2, 2]), color=WHITE)

        formula6 = MathTex(r"y=x^4-3", color=WHITE, font_size=40).next_to(curve6, RIGHT)

        self.play(Write(formula6))
        self.play(Create(curve6_1_backup))
        self.add(curve6_1)
        self.play(Uncreate(curve6_1_backup))

        self.remove(formula6, formula5, formula3, formula2, formula1)
        self.play(FadeOut(plane), FadeOut(axes))

        self.wait(3)