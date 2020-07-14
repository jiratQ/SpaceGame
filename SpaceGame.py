import turtle
import os
import math
import random

#Screen
wn = turtle.Screen();
wn.bgcolor("black");
wn.title("SpaceGame");

turtle.register_shape("enermy.gif")

#Score
point = 0;
maxx = 0;
pen = turtle.Turtle();
pen.hideturtle();
pen.color("white");
pen.up();
pen.setposition(0,-295);
pen.down();
pen.write("Score = {} !".format(point),align="center",font=("Arial",14,"normal"));


#Border
border_pen = turtle.Turtle();
border_pen.speed(0)
border_pen.hideturtle();
border_pen.color("white");
border_pen.penup();
border_pen.goto(-300,300);
border_pen.pendown();
border_pen.pensize(3);
for side in range(4):
    border_pen.fd(600);
    border_pen.right(90);

#Player
player = turtle.Turtle();
player.speed(0);
player.color("green");
player.shape("triangle");
player.penup();
player.setposition(0,-250);
player.setheading(90);
playerspeed=15;

#Enermy
enermy = turtle.Turtle();
enermy.color("red");
enermy.shape("enermy.gif");
enermy.penup();
enermy.speed(0);
enermy.setposition(-250,250);
enermy.hideturtle();
enermyspeed=5;

#Choose number of enerny
number_of_enermy=5;
enermies=[];

for i in range(number_of_enermy):
    enermies.append(turtle.Turtle());

for enermy in enermies:
    enermy.color("red");
    enermy.shape("enermy.gif");
    enermy.penup();
    enermy.speed(0);
    x=random.randint(-200,200);
    y=random.randint(0,280);
    enermy.setposition(x,y);

#PlayerWeapons
bullet=turtle.Turtle();
bullet.hideturtle();
bullet.penup();
bullet.color("yellow");
bullet.shape("triangle");
bullet.speed(0);
bullet.setheading(90);
bullet.shapesize(0.5,0.5);
bulletspeed=10;
bulletstate="Ready";

#Function
def move_left():
    x=player.xcor();
    x-=playerspeed;
    if(x<-300):
        x+=600;
    player.setx(x);

def move_right():
    x=player.xcor();
    x+=playerspeed;
    if(x>300):
        x-=600
    player.setx(x);

def fire_bullet():
    global bulletstate
    if(bulletstate=="Ready"):
        bulletstate="Fire";
        x=player.xcor();
        y=player.ycor();
        y+=10;
        bullet.setposition(x,y);
        bullet.showturtle();

def isCollition(t1,t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2));
    if(distance<25):
        return True;
    return False;


#Controll
wn.listen();
wn.onkeypress(move_left,"Left");
wn.onkeypress(move_right,"Right");
wn.onkeypress(fire_bullet,"space")
end=0

while end==0:
    wn.update();
    #EnermyMove
    for enermy in enermies:
        x = enermy.xcor();
        x += enermyspeed;
        enermy.setx(x);
        if enermy.xcor()>270:
            for e in enermies:
                y=e.ycor();
                y-=40;
                e.sety(y);
            enermyspeed *= -1;
        if enermy.xcor()<-270:
            for e in enermies:
                y=e.ycor();
                y-=40;
                e.sety(y);
            enermyspeed *= -1; 
        #BulletMove
        y=bullet.ycor()+bulletspeed;
        bullet.sety(y);
        if(bullet.ycor()>290):
            bullet.hideturtle();
            bulletstate="Ready";
        if(isCollition(bullet,enermy)):
            bullet.hideturtle();
            bullet.setposition(0,400);
            bulletstate="Ready";
            x=random.randint(-200,200);
            y=random.randint(enermy.ycor(),280);
            enermy.setposition(x,y);
            point += 1;
            if enermyspeed<0:
                enermyspeed -= 1;
            else:
                enermyspeed += 1;
            maxx = max(maxx,point)
            pen.clear();
            pen.write("Score = {} !".format(maxx),align="center",font=("Arial",14,"normal"));
        if(player.ycor()>=enermy.ycor()):
            player.hideturtle();
            enermy.hideturtle();
            end=1
            break
for e in enermies:
    e.hideturtle();
bullet.hideturtle();
pen.hideturtle();
pen.clear();
pen.up();
pen.setposition(0,0);
pen.write("Score = {}".format(maxx),font=("Arial",40),align="center");
while end==1:
    wn.update();