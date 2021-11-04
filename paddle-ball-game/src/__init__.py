#! python
#
# PongGame - main.py
# Originally created by following the tutorial at:
# https://kivy.org/doc/stable/tutorials/pong.html
# The main.py file is where the application (the game example) is instantiated
# and invoked.
from kivy.app import App
from kivy.clock import Clock
from src.PaddleBallGame import PaddleBallGame


class PaddleBallApp(App):
    # PongApp is an App class (provided by Kivy) which will be used to
    # instantiate the various widgets that make up the application.
    def build(self):
        game = PaddleBallGame()
        game.serve_ball()
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        return game


from src.PlayerPaddle import PlayerPaddle
from src.GameBall import GameBall
