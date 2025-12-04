
from turtle import Turtle,Screen
timmy = Turtle()
my_screen = Screen()
timmy.shape("turtle")
timmy.color("coral")
timmy.forward(100)
print(timmy)
print(my_screen.canvheight)
my_screen.exitonclick()
from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name",["Pikachu","sqirtle","Charmander"])
table.add_column("Type",["electric","power","jeeto"])
print(table)
table.align = "l"
print(table.align)