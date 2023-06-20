from flet_mvc import data, FletModel


# Model
class Model(FletModel):
    @data
    def TextNumber(self):
        return "0"