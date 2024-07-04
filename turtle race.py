import random
from turtle import Turtle,Screen
WIDTH,HEIGHT=400,400
color_list=["red","green","pink","orange","black","gray","yellow","blue","pink"]
def num_turtle():

    count=0
    while True:
        count=int(input("Enter Number of Trutle Participate in race (2-10) =>>"))
        if 2<=count<=10:
         return count
        else:
         print("invalid Turtle Number ,plz give turtle number from (2-10)=>> ")
turtles=num_turtle()
print(turtles)
s1=Screen()
s1.setup(400,400)
x_spacing=WIDTH//(turtles+1)
turtle_list=[]
for i in range(1,turtles+1):
  
    new_turtle=Turtle()
    new_turtle.shape("turtle")
    new_turtle.left(90) 
    new_turtle.color(color_list[i-1])
    new_turtle.penup()
    new_turtle.goto(-WIDTH//2+(i *x_spacing),-HEIGHT//2+5)
    turtle_list.append(new_turtle)
def race():
   raceon =True
   while raceon:
      for t in turtle_list:
        distance=random.randrange(1,30)
        t.forward(distance)
        x,y=t.pos()
        if y>=HEIGHT//2:
          print(f"winner is {t.pencolor()} turtle" )
          raceon =False
race()



s1.exitonclick()
