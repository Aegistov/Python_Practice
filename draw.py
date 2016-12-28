from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.widget import Widget
from kivy.graphics import Line

class Painter(Widget):
	def on_touch_down(self, touch):
		with self.canvas:
			touch.ud["line"] = Line(points = (touch.x, touch.y))

	def on_touch_move(self, touch):
		touch.ud["line"].points += [touch.x, touch.y]


class Main_Screen(Screen):
	pass

class Canvas_Screen(Screen):
	pass

class Manager(ScreenManager):
	pass

view = Builder.load_file("ref.kv")

class Draw(App):
	def build(self):
		return view

Draw().run()