from sympy import symbols, solve, Eq
from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.azure import AzureService

# configs
config.background_color = BLACK
config.pixel_width = 180 * 2
config.pixel_height = 320 * 2


class FindShadedArea(VoiceoverScene):
    def find_critical_point_on_circle(self):
        a, b = symbols('a b', real=True)
        eq1 = Eq(a ** 2 + b ** 2, pow(self.circle_radius, 2))
        eq2 = Eq(a ** 2 + (b - self.critical_len) ** 2 + (a - self.critical_len) ** 2 +
                 b ** 2, 2 * pow(self.critical_len, 2))
        result = solve((eq1, eq2), (a, b))
        point_x = point_y = 0.0
        for p in result:
            if self.circle_radius / 2 < p[0] < self.circle_radius:
                point_x = float(p[0])
                point_y = float(p[1])
        return [point_x, point_y, 0]

    def __init__(self):
        super().__init__()

        # define the circle
        circle_origin = ORIGIN
        self.circle_scale = 2
        self.circle_radius = 2 * self.circle_scale

        # define the critical point
        self.critical_len = 1.55 * self.circle_scale
        self.up_point_in_between = [0, self.critical_len, 0]
        right_point_in_between = [self.critical_len, 0, 0]

        self.point_on_circle = self.find_critical_point_on_circle()
        print("point_on_circle:", self.point_on_circle)

        line1 = Line(start=self.up_point_in_between, end=self.point_on_circle)
        line2 = Line(start=right_point_in_between, end=self.point_on_circle)

        self.right_angle_on_circle = RightAngle(
            Line(start=self.up_point_in_between, end=self.point_on_circle),
            Line(start=right_point_in_between, end=self.point_on_circle),
            length=0.2, quadrant=[-1, -1], color=RED
        )

        self.right_angle_origin = RightAngle(
            Line(start=self.up_point_in_between, end=circle_origin),
            Line(start=circle_origin, end=right_point_in_between),
            length=0.2, quadrant=[-1, 1], color=RED
        )

        # sector
        intersection = Intersection(
            Circle(radius=self.circle_radius),
            Square(side_length=2 * self.circle_radius).shift(UR * self.circle_radius)
        )

        # polygon-OACB
        polygon = Polygon(
            circle_origin, self.up_point_in_between, self.point_on_circle, right_point_in_between
        )

        # blue area
        diff = Difference(
            intersection, polygon, color=BLUE, fill_opacity=1, stroke_color=WHITE
        )
        self.group = VGroup(
            diff, intersection
        )

    def conditions_display(self):
        condition1 = MathTex("r = 4, OA = OB = 3", color=WHITE).scale(1.5)
        condition2 = MathTex(r"\angle AOB = \angle ACB = \frac{\pi }{2} ").scale(1.5)
        cond_group = VGroup( condition2, condition1).arrange(UP).move_to([0,7,0])
        self.add(cond_group)
        circum_rect = (Rectangle(width=cond_group.width*1.1, height=cond_group.height*1.1,
                                 stroke_color=BLACK, color=BLACK, fill_color=WHITE, fill_opacity=0.4)
                       .move_to(cond_group.get_center()))
        self.add(circum_rect)

    def construct(self):
        self.set_speech_service(
            AzureService(
                voice="en-US-RyanMultilingualNeural",
                # style="newscast-casual",
            )
        )
        shift_scale = 0.3
        radius_brace = BraceBetweenPoints([0, self.circle_radius, 0], ORIGIN)
        radius_text = MathTex("4").next_to(radius_brace, LEFT)

        c_label = Text("C", color=RED).move_to(self.find_critical_point_on_circle() + UR * shift_scale)

        with self.voiceover(
                text="""Following is a sector which is one forth of a circle with <bookmark mark='A'/>radius of 4 and 
                <bookmark mark='B'/>C is a point on the circle."""
        ) as tracker:
            self.add(self.group)
            self.conditions_display()

            self.wait_until_bookmark("A")
            self.play(Create(radius_brace))
            self.add(radius_text)
            self.wait_until_bookmark("B")
            self.play(Create(Dot(point=self.point_on_circle, color=RED)))
            self.add(c_label)

        with self.voiceover(text="""The Angle <bookmark mark='C'/>A O B and A C B are both <bookmark mark='D'/>right 
        angles."""
                            ) as tracker:
            self.wait_until_bookmark("C")
            self.add(Text("O", color=RED).move_to(ORIGIN + DL * shift_scale))
            self.add(Text("A", color=RED).move_to([0, self.critical_len, 0] + DR * shift_scale))
            self.add(Text("B", color=RED).move_to([self.critical_len, 0, 0] + UL * shift_scale))
            self.wait_until_bookmark("D")
            self.add(self.right_angle_origin)
            self.add(self.right_angle_on_circle)

        circle_equation = MathTex(r"x^2+y^2=r^2").scale(1.4).move_to(DOWN * 5)
        with self.voiceover(text="""Do you know how to calculate <bookmark mark='E'/>area of the blue part with 
        condition that <bookmark mark='F'/>O A equals O B and equals 3？ With the traditional way, we can set the 
        coordinates of C to be <bookmark mark='G'/>x y. Since point C is on the circle, <bookmark mark='H'/>x square 
        plus y square equals square of radius."""
                            ) as tracker:
            self.wait_until_bookmark("G")
            c_coordinates = MathTex(r"(x,y)").next_to(c_label, RIGHT)

            self.play(Create(c_coordinates))
            self.wait_until_bookmark("H")
            self.play(Write(circle_equation))

        second_equation = MathTex(r"OA^2+OB^2=AC^2+BC^2").scale(1).move_to(DOWN * 7)
        with self.voiceover(text="""Since A O B and A C B are both right angles, <bookmark mark='I'/>square of OA plus 
        square of OB equals square of AC plus square of BC. 
            With these two equations, it's easy to calculate the two unknowns x and y.
            But, it there any easier way? Yes! By rotating."""
                            ) as tracker:
            self.wait_until_bookmark("I")
            self.add(DashedLine(start=[0, self.critical_len, 0], end=[self.critical_len, 0, 0]))
            self.play(Write(second_equation))

        with self.voiceover(text="""First, we rotate the sector counterclockwise by 90 degrees, <bookmark 
        mark='J'/>then by another 90 degrees, and then <bookmark mark='K'/>by another 90 degrees. Finally we can find 
        out that <bookmark mark='L'/>4 times of the blue area equals the area difference of the circle and the 
        square in the middle. <bookmark mark='M'/>With the radius we can get the area of the circle. With the length 
        of OC which equals radius,we can derive the area of inner square.
            
        """) as tracker:
            self.remove(radius_brace, radius_text)
            self.remove(second_equation, circle_equation)
            group1 = self.group.copy()
            self.play(Rotate(group1, angle=PI * 1 / 2, about_point=ORIGIN, run_time=2, rate_func=smooth))

            group2 = group1.copy()
            self.wait_until_bookmark("J")
            self.play(Rotate(group2, angle=PI * 1 / 2, about_point=ORIGIN, run_time=2, rate_func=smooth))

            group3 = group2.copy()
            self.wait_until_bookmark("K")
            self.play(Rotate(group3, angle=PI * 1 / 2, about_point=ORIGIN, run_time=2, rate_func=smooth))

            final_equation = MathTex(r"4S_{blue\_area}=S_{circle}-S_{square}").move_to(DOWN*6)
            final_equation_1 = MathTex(r"S_{blue\_area} &= \frac{S_{circle}-S_{square}}{4} \\ &=\frac{\pi\cdot  4^{2} "
                                       r"- (4\cdot2\cdot sin\frac{\pi}{4})^{2}}{4}  \\ &= 4\pi - 8").scale(
                1.1).move_to(DOWN * 7)
            self.wait_until_bookmark("L")
            self.play(Create(final_equation))
            self.wait_until_bookmark("M")
            self.remove(final_equation)
            self.play(Create(final_equation_1), run_time=0.5)

        self.wait(3)

