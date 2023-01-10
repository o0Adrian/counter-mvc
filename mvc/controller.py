from flet_mvc import FletController

# Controller
class Controller(FletController):
    def minus_click(e):
        self.model.TextNumber.set_value(str(int(self.model.TextNumber()) - 1))
        self.update()

    def plus_click(e):
        self.model.TextNumber.set_value(str(int(self.model.TextNumber()) - 1))
        self.update()
