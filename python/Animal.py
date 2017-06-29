class Animal(object):

    def __init__(self, name, color, type_):
        self.name = name
        self.color = color
        self.type_ = type_


    def my_color(self):
        return ('I am of color', self.color)


    #anim = Animal('Lion','Green','Carnivor')
    print(my_color('green'))
