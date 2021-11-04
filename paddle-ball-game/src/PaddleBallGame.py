from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty


class PaddleBallGame(Widget):
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
