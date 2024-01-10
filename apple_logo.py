from manim import *
import numpy as np
import math
from sympy import symbols, Eq, solve, sin
import sympy

# configs
config.background_color = BLACK

config.pixel_width = 180 * 4
config.pixel_height = 320 * 4

x_shift = 0
y_shift = -4


# curve A and point 2
def first_formula(x):
    return np.array([x + x_shift, 0.48 * pow(x + 2.03, 2) + 0.01 + y_shift, 0])


curve_a_func = ParametricFunction(first_formula, t_range=np.array([-7, 7]), color=RED)
curve_a_title = MathTex("f(x)=0.49(x+2.03)^{2}+0.01", fill_color=GREEN).move_to([-2, 11, 0]).scale(1)
point_2 = [-2.03, 0.48 * pow(-2.03 + 2.03, 2) + 0.01, 0]

point_2_label = DecimalMatrix(
    [point_2], element_to_mobject_config={"num_decimal_places": 2}
).scale(1)


# curve B and point 3
def second_formula(x):
    return np.array([x + x_shift, 1 / 3 * math.cos(x) + 0.1577448 + y_shift, 0])


curve_b_func = ParametricFunction(second_formula, t_range=np.array([-7, 7]), color=RED)
curve_b_title = MathTex(r"g(x)=0.33cos(x)+0.16", fill_color=GREEN).move_to([0, -3, 0])
curve_b = ParametricFunction(second_formula, t_range=np.array([-2.03, 2.03]), color=WHITE)
point_3 = [2.03, 1 / 3 * math.cos(2.03) + 0.1577448, 0]
point_3_label = DecimalMatrix(
    [point_3], element_to_mobject_config={"num_decimal_places": 2}
).scale(1)


# curve function C
def third_formula(x):
    return np.array([x + x_shift, 0.48 * pow(x - 2.03, 2) + 0.01 + y_shift, 0])


curve_c_func = ParametricFunction(third_formula, t_range=np.array([-7, 7]), color=RED)
curve_c_title = MathTex("f(x)=0.49(x-2.03)^{2}+0.01", fill_color=GREEN).move_to([2, 11, 0]).scale(1)

# curve D and point 4 and 5
curve_d_func = ImplicitFunction(lambda x, y: pow(x - 5.58, 2) + pow(y - y_shift - 5.34, 2) - 6.63,
                                x_range=[0, 7],
                                color=RED)
curve_d_title = (MathTex("(x-5.58)^{2}+(y-5.34)^{2}=6.63", fill_color=GREEN)
                 .next_to([5.58 + x_shift, 5.34 + y_shift, 0], LEFT))


def calculate_point_4():
    x, y = symbols('x y', real=True)
    eq1 = Eq(pow(x - 5.58, 2) + pow(y - 5.34, 2), 6.63)
    eq2 = Eq(0.48 * pow(x - 2.03, 2) + 0.01, y)
    results = solve((eq1, eq2), (x, y))

    point_4_x = point_4_y = 0.0
    for p in results:
        if p[0] < 6:
            point_4_x = float(p[0])
            point_4_y = float(p[1])
    return [point_4_x, point_4_y, 0]


point_4 = calculate_point_4()
point_4_label = DecimalMatrix(
    [point_4], element_to_mobject_config={"num_decimal_places": 2}
).scale(1)

# curve C and point 4
curve_c = ParametricFunction(third_formula, t_range=np.array([point_3[0], point_4[0]]), color=WHITE)

# curve function E
curve_e_func = ImplicitFunction(lambda x, y: pow(x - 1.95, 2) + pow(y - y_shift - 5.56, 2) - 9.14,
                                x_range=[-7, 7],
                                y_range=[-8, 16],
                                color=RED)

curve_e_title = (MathTex("(x-1.95)^{2}+(y-5.56)^{2}=9.14", fill_color=GREEN)
                 .next_to([1.95 + x_shift, 5.56 + y_shift, 0], UP * 4))


# point 5 and curve d
def calculate_point_5():
    x, y = symbols('x y', real=True)
    eq1 = Eq(pow(x - 5.58, 2) + pow(y - 5.34, 2), 6.63)
    eq2 = Eq(pow(x - 1.95, 2) + pow(y - 5.56, 2), 9.14)
    result = solve((eq1, eq2), (x, y))
    point = []
    for p in result:
        if p[1] > 5.34:
            point.append(float(p[0]))
            point.append(float(p[1]))
            point.append(0)
    return point


point_5 = calculate_point_5()
point_5_label = DecimalMatrix(
    [point_5], element_to_mobject_config={"num_decimal_places": 2}
).scale(1)

curve_d = ImplicitFunction(lambda x, y: pow(x - 5.58, 2) + pow(y - y_shift - 5.34, 2) - 6.63,
                           x_range=[0, 5],
                           y_range=[point_4[1] + y_shift, point_5[1] + y_shift],
                           color=WHITE)

# curve F
curve_f_func = ParametricFunction(
    lambda x: np.array([x + x_shift, 0.6 * math.sin(x - 1.4) + 8.7 + y_shift, 0]),
    t_range=np.array([-7, 7]), color=RED)
curve_f_title = (MathTex("h(x)=0.6sin(x-1.4)+8.7", fill_color=GREEN)
                 .next_to([2, 6, 0], UP))
point_6 = [0.85, 0.6 * math.sin(0.85 - 1.4) + 8.7, 0]
point_6_label = DecimalMatrix(
    [point_6], element_to_mobject_config={"num_decimal_places": 2}
).scale(1)
curve_e = ImplicitFunction(lambda x, y: pow(x - 1.95, 2) + pow(y - y_shift - 5.56, 2) - 9.14,
                           x_range=[point_6[0], point_5[0]],
                           y_range=[y_shift + 5.56, 14],
                           color=WHITE)

# curve G
curve_g_func = ImplicitFunction(lambda x, y: pow(x + 1.95, 2) + pow(y - y_shift - 5.56, 2) - 9.14,
                                x_range=[-7, 7],
                                y_range=[-8, 16],
                                color=RED)
curve_g_title = (MathTex("(x+1.95)^{2}+(y-5.56)^{2}=9.14", fill_color=GREEN)
                 .next_to([-1.95 + x_shift, 5.56 + y_shift, 0], UP * 4))

point_7_x = math.sqrt(9.14 - (8.577 - 5.58) ** 2) + 0.18 - 1.95
point_7 = [point_7_x, 0.6 * math.sin(point_7_x - 1.4) + 8.7, 0]

point_7_label = DecimalMatrix(
    [point_7], element_to_mobject_config={"num_decimal_places": 2}).scale(1)
curve_f = ParametricFunction(
    lambda x: np.array([x + x_shift, 0.6 * math.sin(x - 1.4) + 8.7 + y_shift, 0]),
    t_range=np.array([point_7[0], point_6[0]]), color=WHITE)

# curve H func
curve_h_func = ImplicitFunction(lambda x, y: pow(x - 0.16, 2) + pow(y - y_shift - 5.14, 2) - 26.68,
                                x_range=[-7, 7],
                                y_range=[-8, 16],
                                color=RED)
curve_h_title = (MathTex("(x-0.16)^{2}+(y-5.14)^{2}=26.68", fill_color=GREEN)
                 .next_to([0.16, 5.14, 0], UP))
point_8 = [-4.9, math.sqrt(9.14 - (-4.9 + 1.95) ** 2) + 5.56, 0]
point_8_label = DecimalMatrix(
    [point_8], element_to_mobject_config={"num_decimal_places": 2}).scale(1)

# curve G
curve_g = ArcBetweenPoints(
    start=list(np.add(point_7, [x_shift, y_shift, 0])), end=list(np.add(point_8, [x_shift, y_shift, 0])),
    stroke_color=WHITE, radius=math.sqrt(9.14)
)

point_9 = [-point_4[0], -math.sqrt(26.68 - (-point_4[0] - 0.16) ** 2) + 5.14, 0]

point_9_label = DecimalMatrix(
    [point_9], element_to_mobject_config={"num_decimal_places": 2}).scale(1)
curve_h = ImplicitFunction(lambda x, y: pow(x - 0.16, 2) + pow(y - y_shift - 5.14, 2) - 26.68,
                           x_range=[-7, 0],
                           y_range=[point_9[1] + y_shift, point_8[1] + y_shift],
                           color=WHITE)

# curve A
curve_a = ParametricFunction(first_formula, t_range=np.array([point_9[0], point_2[0]]), color=WHITE)


class AppleLogo(Scene):
    txt_list = [
        Text("How to draw", font_size=80, fill_opacity=1),
        Text("The Apple logo", font_size=80, fill_opacity=1, color=RED),
        Text("Using", font_size=80, fill_opacity=1),
        Text("Mathematical Formulas", font_size=96, fill_opacity=1, color=BLUE),
    ]

    plane = NumberPlane(
        x_range=[-7, 7, 2],
        y_range=(-8, 16, 2),
        x_length=14,
        y_length=24,
    )

    axes = Axes(
        x_range=[-7, 7, 2],
        y_range=(-8, 16, 2),
        x_length=14,
        y_length=24,
        x_axis_config={"unit_size": 1},
        y_axis_config={"unit_size": 1}
    ).add_coordinates()

    def show_beginning_text(self):
        self.play(AddTextLetterByLetter(self.txt_list[0].move_to(UP * 4)))
        self.play(AddTextLetterByLetter(self.txt_list[1].move_to(UP * 2)))
        self.play(AddTextLetterByLetter(self.txt_list[2].move_to(ORIGIN)))
        self.play(AddTextLetterByLetter(self.txt_list[3].move_to(DOWN * 2)))

    def remove_beginning_text(self):
        self.play(RemoveTextLetterByLetter(self.txt_list[0]), run_time=0.2)
        self.play(RemoveTextLetterByLetter(self.txt_list[1]), run_time=0.2)
        self.play(RemoveTextLetterByLetter(self.txt_list[2]), run_time=0.2)
        self.play(RemoveTextLetterByLetter(self.txt_list[3]), run_time=0.2)

    def draw_leaf(self):
        # draw the smallest part combined with 2 circles
        circle_small_1 = Circle(
            radius=math.sqrt(6.35),
            color=RED
        ).move_to([2.31, 8.77 + y_shift, 0])
        circle_small_1_title = MathTex(
            "(x-2.3)^{2}+(y-8.77)^2=6.35",
            fill_color=GREEN
        ).move_to(circle_small_1.get_center()).scale(1)

        circle_small_2 = Circle(
            radius=math.sqrt(5.58),
            color=RED
        ).move_to([-0.23, 11.02 + y_shift, 0])
        circle_small_2_title = MathTex(
            "(x+0.3)^{2}+(y-11.01)^{2}=5.58",
            fill_color=GREEN
        ).move_to(circle_small_2.get_center()).scale(1)

        intersect_small_12 = Intersection(
            circle_small_1, circle_small_2, color=WHITE
        )
        self.add(circle_small_1_title)
        self.play(Create(circle_small_1))
        self.add(circle_small_2_title)
        self.play(Create(circle_small_2))

        self.play(Create(intersect_small_12))
        self.remove(circle_small_1_title)
        self.remove(circle_small_2_title)
        self.play(Uncreate(circle_small_1))
        self.play(Uncreate(circle_small_2))

    def construct(self):
        self.show_beginning_text()
        self.remove_beginning_text()

        self.play(FadeIn(self.plane))
        self.play(FadeIn(self.axes))

        # curve A
        self.add(curve_a_title)
        self.play(Create(curve_a_func), run_time=2)
        dot_2 = Dot(list(np.add(point_2, [x_shift, y_shift, 0])), color=GREEN)
        point_2_label.next_to(dot_2, DOWN)
        self.add(point_2_label)
        self.add(dot_2)

        self.remove(curve_a_title, dot_2, point_2_label)

        # curve B
        self.add(curve_b_title)
        self.play(Create(curve_b_func))
        dot_3 = Dot(list(np.add(point_3, [x_shift, y_shift, 0])), color=GREEN)
        point_3_label.next_to(dot_3, DOWN)
        self.add(dot_3, point_3_label)
        self.play(Create(curve_b))
        self.remove(dot_3, curve_b_title, point_3_label)
        self.play(Uncreate(curve_b_func))

        # curve C and pint 4
        self.add(curve_c_title)
        self.play(Create(curve_c_func))
        self.remove(curve_c_title)

        dot_4 = Dot(list(np.add(point_4, [x_shift, y_shift, 0])), color=GREEN)
        point_4_label.next_to(dot_4, LEFT)
        self.add(dot_4, point_4_label)
        self.play(Create(curve_c))
        self.remove(dot_4, curve_d_title, point_4_label)
        self.play(Uncreate(curve_c_func))

        # curve D function
        self.add(curve_d_title)
        self.play(Create(curve_d_func))

        # curve E function
        self.add(curve_e_title)
        self.play(Create(curve_e_func), run_time=2)

        # curve D
        dot_5 = Dot(list(np.add(point_5, [x_shift, y_shift, 0])), color=GREEN)
        point_5_label.next_to(dot_5, UP)
        self.add(point_5_label, dot_5)
        print([point_4[1], point_5[1]])
        self.play(Create(curve_d))
        self.remove(curve_d_title, dot_5, point_5_label)
        self.play(Uncreate(curve_d_func))

        # curve F function and curve E
        self.add(curve_f_title)
        self.play(Create(curve_f_func))
        dot_6 = Dot(list(np.add(point_6, [x_shift, y_shift, 0])), color=GREEN)
        point_6_label.next_to(dot_6, UP)
        self.add(dot_6, point_6_label)
        self.play(Create(curve_e))
        self.remove(curve_e_title)
        self.play(Uncreate(curve_e_func))
        self.remove(point_6_label, dot_6)

        # curve G function
        self.add(curve_g_title)
        self.play(Create(curve_g_func))

        # curve F and point 7
        dot_7 = Dot(list(np.add(point_7, [x_shift, y_shift, 0])), color=GREEN)
        point_7_label.next_to(dot_7, UP)
        self.add(dot_7, point_7_label)
        self.play(Create(curve_f))
        self.remove(curve_f_title)
        self.play(Uncreate(curve_f_func))
        self.remove(point_7_label, dot_7)
        self.play(Uncreate(curve_f_func))
        self.remove(curve_f_title)

        # curve H function
        self.add(curve_h_title)
        self.play(Create(curve_h_func))
        dot_8 = Dot(list(np.add(point_8, [x_shift, y_shift, 0])), color=GREEN)
        self.add(dot_8)
        point_8_label.next_to(dot_8, UP)
        self.add(point_8_label)

        # curve G
        self.play(Create(curve_g))
        self.remove(curve_g_title)
        self.play(Uncreate(curve_g_func))
        self.remove(point_8_label, dot_8)

        # point 9
        dot_9 = Dot(list(np.add(point_9, [x_shift, y_shift, 0])), color=GREEN)
        point_9_label.next_to(dot_9, RIGHT)
        self.add(dot_9, point_9_label)

        # curve H
        self.play(Create(curve_h))
        self.play(Uncreate(curve_h_func))
        self.remove(curve_h_title)

        self.remove(point_9_label, dot_9)

        # curve A
        self.play(Create(curve_a))
        self.play(Uncreate(curve_a_func))

        # draw leaf
        self.draw_leaf()

        self.play(FadeOut(self.axes))
        self.play(FadeOut(self.plane))

        self.wait(2)
