def week__3(myChar):

    import turtle , random
    from turtle import Turtle, Screen

    print(''' Django 볼을 획득하라!
    노란색 Django볼을 획득하면 Mission clear 됩니다.''')
    screen = Screen()
    screen.setup(1200, 500)
    Django = Turtle()
    Django.shape('circle')
    Django.color('yellow')
    Django.up()
    point_x = random.randint(-500,500)
    point_y = random.randint(-250,250) 
    Django.goto(point_x,point_y)
    player = Turtle()
    player.speed('fastest')
    PlayerY = 0
    PlayerX = 0
    
    def play():
        if player.distance(Django) < 25:
            turtle.clear()
            turtle.write("Mission Clear",False,"center",font=("Arial",50,"normal"))
            myChar.controlPiro(5)
            myChar.controlCoding(10)

        
        if player.distance(Django) > 25:
            turtle.clear()
            turtle.write("Game Over",False,"center",font=("Arial",50,"normal"))
            myChar.controlPiro(5)
            myChar.controlMoney(-2)

    def moveX():
        nonlocal PlayerX
        screen.onkeypress(None, "Right") 
        player.clear()
        player.penup()
        player.goto(PlayerX, PlayerY)
        player.pendown()
        player.shape('turtle')
        player.color('blue')
        PlayerX += 10
        screen.onkeypress(moveX, "Right") 
        
    def moveY():
        nonlocal PlayerY
        screen.onkeypress(None, "Up") 
        player.clear()
        player.penup()
        player.goto(PlayerX, PlayerY)
        player.pendown()
        player.shape('turtle')
        player.color('blue')
        PlayerY += 10
        screen.onkeypress(moveY, "Up")

    def move_X():
        nonlocal PlayerX
        screen.onkeypress(None, "Left") 
        player.clear()
        player.penup()
        player.goto(PlayerX, PlayerY)
        player.pendown()
        player.shape('turtle')
        player.color('blue')
        PlayerX -= 10
        screen.onkeypress(move_X, "Left")

    def move_Y():
        nonlocal PlayerY
        screen.onkeypress(None, "Down") 
        player.clear()
        player.penup()
        player.goto(PlayerX, PlayerY)
        player.pendown()
        player.shape('turtle')
        player.color('blue')
        PlayerY -= 10
        screen.onkeypress(move_Y, "Down")

    screen.listen()
    turtle.ontimer(play, 9000)
    moveY()
    moveX()
    move_X()
    move_Y()

    screen.mainloop()
