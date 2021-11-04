#! python
#
# PongGame - main.py
# Originally created by following the tutorial at:
# https://kivy.org/doc/stable/tutorials/pong.html
# The main.py file is where the application (the game example) is instantiated
# and invoked.
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty
from kivy.properties import ReferenceListProperty
from kivy.properties import ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock


class PongPaddle(Widget):
    score = NumericProperty(0)

    def bounce_ball(self, ball):
        if self.collide_widget(ball):
            vx, vy = ball.velocity
            offset = (ball.center_y - self.center_y) / (self.height / 2)
            bounced = Vector(-1 * vx, vy)
            vel = bounced * 1.1
            ball.velocity = vel.x, vel.y + offset


class PongBall(Widget):

    # Velocity of the ball on x and y axis
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)

    # Referencelist property so we can use ball.velocity as a shorthand, just
    # like e.g. w.pos for w.x and w.y
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    # move method will move the ball one step. This will be called in equal
    # intervals to animate the ball
    def move(self):
        self.pos = Vector(*self.velocity) + self.pos


class PongGame(Widget):
    # PongGame is a Widget class which will run inside the application.

    ball = ObjectProperty(None)

    # def serve_ball(self):
    #     # Original serve method which used randint
    #     self.ball.center = self.center
    #     self.ball.velocity = Vector(4, 0).rotate(randint(0, 360))

    def serve_ball(self, vel=(4, 0)):
        self.ball.center = self.center
        self.ball.velocity = vel

    def update(self, dt):
        # Game updates, e.g., ball.move, go in this method.
        self.ball.move()

        # Bounce off of paddles
        self.player1.bounce_ball(self.ball)
        self.player2.bounce_ball(self.ball)

        # Bounce off top and bottom
        if (self.ball.y < 0) or (self.ball.top > self.height):
            self.ball.velocity_y *= -1

        # Bounce off left and right - testing only
        # if (self.ball.x < 0) or (self.ball.right > self.width):
        #     self.ball.velocity_x *= -1

        # Counting a scored point when ball touches a side
        if self.ball.x < self.x:
            self.player2.score += 1
            self.serve_ball(vel=(4, 0))
        if self.ball.x > self.width:
            self.player1.score += 1
            self.serve_ball(vel=(-4, 0))

    def on_touch_move(self, touch):
        if touch.x < self.width / 3:
            self.player1.center_y = touch.y
        if touch.x > self.width - self.width / 3:
            self.player2.center_y = touch.y


class PongApp(App):
    # PongApp is an App class (provided by Kivy) which will be used to
    # instantiate the various widgets that make up the application.
    def build(self):
        game = PongGame()
        game.serve_ball()
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        return game


if __name__ == "__main__":
    PongApp().run()
