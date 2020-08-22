import turtle

#👏 Background Check 👏
wn=turtle.Screen()
wn.title("Ping Pong")
wn.bgcolor("Black")
wn.setup(width=800, height=600)
wn.tracer(0)

#👏 Paddle 1 👏
paddle_1 = turtle.Turtle()
paddle_1.speed(0)
paddle_1.shape("square")
paddle_1.shapesize(stretch_wid=5 , stretch_len=1)
paddle_1.color("white")
paddle_1.penup()
paddle_1.goto( -350 ,0 )

#👏 Paddle 2 👏
paddle_2 = turtle.Turtle()
paddle_2.speed(0)
paddle_2.shape("square")
paddle_2.shapesize(stretch_wid=5 , stretch_len=1)
paddle_2.color("white")
paddle_2.penup()
paddle_2.goto( 350 , 0 )

#👏 Ball 👏
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)


#👏 Ball Inertia 👏
ball.dx = 0.1
ball.dy = 0.1


#Score
score_a = 0
score_b = 0

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto( 0 , 260)
pen.write("Player A: 0 | Player B: 0", align="center",font=("Courier", 12, "normal"))




#👏 Paddle Movement Function 👏
def paddle_1_update_up():
    y = paddle_1.ycor()
    y += 20
    paddle_1.sety(y)

def paddle_1_update_down():
    y = paddle_1.ycor()
    y -= 20
    paddle_1.sety(y)

def paddle_2_update_up():
    y = paddle_2.ycor()
    y += 20
    paddle_2.sety(y)

def paddle_2_update_down():
    y = paddle_2.ycor()
    y -= 20
    paddle_2.sety(y)


#👏 Input waiting for paddle 👏
wn.listen()
wn.onkeypress(paddle_1_update_up, "w")
wn.onkeypress(paddle_1_update_down, "s")
wn.onkeypress(paddle_2_update_up, "Up")
wn.onkeypress(paddle_2_update_down, "Down")

#👏 Main game loop 👏
while True:
    wn.update()

    #👏 Inertia 👏 
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    
    #👏Wall Check 👏
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    
     
    if ball.xcor() > 390:
        ball.goto( 0 , 0 )
        ball.dx *= -1
        score_a +=1
        pen.clear()
        pen.write("Player A: {} | Player B: {}".format(score_a,score_b), align="center",font=("Courier", 12, "normal"))

    if ball.xcor() < -390:
        ball.goto( 0 , 0 )
        ball.dx *= -1
        score_b +=1
        pen.clear()
        pen.write("Player A: {} | Player B: {}".format(score_a,score_b), align="center",font=("Courier", 12, "normal")) 
        
    #👏 Paddle Collision Check 👏
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < (paddle_2.ycor() + 40) and ball.ycor() > (paddle_2.ycor()-40)): 
        ball.setx(340)
        ball.dx *= -1
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < (paddle_1.ycor() + 40) and ball.ycor() > (paddle_1.ycor()-40)): 
        ball.setx(-340)
        ball.dx *= -1
