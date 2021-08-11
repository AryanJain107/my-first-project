import turtle as trtl
import random as rand
import time
import winsound

wn = trtl.Screen()
wn.bgpic( "spacetest.gif" )
wn.title( "The Saviour of Earth" )
wn.screensize( 500 , 500 )

easyButton = trtl.Turtle()
easyButton.fillcolor( "Black" )
easyButton.begin_fill()
easyButton.shape( "square" )
easyButton.color( "black" )
easyButton.penup()
easyButton.goto(- 150 , 50 )
easyButton.pendown()
easyButton.shapesize( 5 )

hardButton = trtl.Turtle()
hardButton.fillcolor( "Black" )
hardButton.begin_fill()
hardButton.shape( "square" )
hardButton.color( "black" )
hardButton.penup()
hardButton.goto( 150 , 50 )
hardButton.pendown()
hardButton.shapesize( 5 )
easyButton.end_fill() 

def easyButton_clicked ( x , y ): 
    #Can add this command here -- asteroid.hideturtle()
    if easyButton_clicked:
        winsound.PlaySound( "blast.wav" , winsound.SND_ASYNC)
        print ( "Hello!" )
        wn.clearscreen()
        wn.bgpic( "spacetest.gif" )
        wn.register_shape( "2.gif" )
        wn.register_shape( "3.gif" )
        wn.register_shape( "4.gif" )
        wn.register_shape( "5.gif" )

        # Intial Score and Lives
        global score
        score = 0
        lives = 3

        # writer
        # Will help write and update the score and lives
        writer = trtl.Turtle()
        writer.speed( 0 )
        writer.shape( "square" )
        writer.color( "white" )
        writer.penup()
        writer.hideturtle()
        writer.goto( 0 , 250 )
        writer.write( "Score: {} Lives: {} " .format(score, lives), align = "center" , font =( "Courier" , 24 , "normal" ))
        
        # Earth
        # This is the what the user will try to save in this game
        Earth = trtl.Turtle()
        Earth.hideturtle()
        
        #Asteroids
        # User will try to save the Earth from these asteroids 
        asteroids = []
        asteroid = trtl.Turtle()
        sizes = [ "2.gif" , "3.gif" , "4.gif" , "5.gif" ]
        asteroid.speed( 0 )
        asteroid.shape(rand.choice(sizes))
        asteroid.shapesize( 1.75 )
        asteroid.color( "brown" )
        asteroid.penup()
        asteroid.goto( 100 , 250 )
        asteroid.speed = rand.randint( 2 , 3 )
        asteroids.append(asteroid)
        
        # This is the function that will happen when the user clicks on the asteroid 
        
        def spot_clicked ( x , y ):
        #Can add this command here -- asteroid.hideturtle()
            if spot_clicked:
                asteroid.speed = rand.randint( 2 , 3 )
                asteroid.shape(rand.choice(sizes))
                winsound.PlaySound( "blast.wav" , winsound.SND_ASYNC)
                new_xpos = rand.randint (- 300 , 300 )
                new_ypos = rand.randint ( 200 , 200 )
                asteroid.goto (new_xpos, new_ypos)
                if asteroid.ycor() < 11111111111200 :
                    global score
                    score += 10
                    print ( "Score: {} Lives: {} " .format(score, lives))
                    writer.clear()
                    writer.write( "Score: {} Lives: {} " .format(score,
                    lives), align = "center" , font =( "Courier" , 24 , "normal" ))
                    print ( "Asteroid Destroyed" ) 
                  
        # User will have to click on the asteroid to destroy them
        # Event of this program/game
        asteroid.onclick(spot_clicked) 

        # Something that happens over and over again until the game is over
        while True :
            wn.update()
            for asteroid in asteroids:
                # Asteroid Movements, including dropping it from the top of the screen
                asteroid.sety(asteroid.ycor() - asteroid.speed)
                if asteroid.ycor() < - 300 :
                    asteroid.goto(rand.randint(- 300 , 800 ))
                if asteroid.ycor() < - 150 :
                    # Lives Update
                    asteroid.speed = rand.randint( 2 , 3 )
                    asteroid.shape(rand.choice(sizes))
                    winsound.PlaySound( "sound.wav" , winsound.SND_ASYNC)
                    lives -= 1
                    print ( "Score: {} Lives: {} " .format(score, lives))
                    writer.clear() 
                    writer.write( "Score: {} Lives: {} " .format(score,
                    lives), align = "center" , font =( "Courier" , 24 , "normal" ))
                    print ( "Uh Oh!" )
                    if lives == 0 :
                        wn.clearscreen()
                        asteroid.hideturtle()
                        wn.bgcolor( "White" )
                        writer.color( "Red" )
                        writer.penup()
                        writer.hideturtle()
                        writer.goto( 0 , 0 )
                        writer.pendown()
                        writer.write( "GAME OVER!" , align = "center" ,
                        font =( "Courier" , 85 , "normal" ))
                        writer.penup()
                        writer.goto( 0 ,- 50 )
                        writer.pendown()
                        winsound.PlaySound( "gameover.wav" ,
                        winsound.SND_ASYNC)
                        writer.write( "Score: {} " .format(score),
                        align = "center" , font =( "Courier" , 24 , "normal" ))
                        print ( "GAME OVER!" )
                        trtl.done()
                    time.sleep( 1 )
                    # Asteroid Movement
                    for asteroid in asteroids:
                        asteroid.goto(rand.randint(- 300 , 300 ), rand.randint( 400 , 800 )) 

def hardButton_clicked ( x , y ): 
    #Can add this command here -- asteroid.hideturtle()
    if hardButton_clicked:
        winsound.PlaySound( "blast.wav" , winsound.SND_ASYNC)
        print ( "Hello!" )
        wn.clearscreen()
        wn.bgpic( "spacetest.gif" )
        wn.register_shape( "2.gif" )
        wn.register_shape( "3.gif" )
        wn.register_shape( "4.gif" )
        wn.register_shape( "5.gif" )

        # Intial Score and Lives
        global score
        score = 0
        lives = 3

        # writer
        # Will help write and update the score and lives
        writer = trtl.Turtle()
        writer.speed( 0 )
        writer.shape( "square" )
        writer.color( "white" )
        writer.penup()
        writer.hideturtle()
        writer.goto( 0 , 250 )
        writer.write( "Score: {} Lives: {} " .format(score, lives), align = "center" , font =( "Courier" , 24 , "normal" ))
        
        # Earth
        # This is the what the user will try to save in this game
        Earth = trtl.Turtle()
        Earth.hideturtle()
        
        #Asteroids
        # User will try to save the Earth from these asteroids 
        asteroids = []
        asteroid = trtl.Turtle()
        sizes = [ "2.gif" , "3.gif" , "4.gif" , "5.gif" ]
        asteroid.speed( 0 )
        asteroid.shape(rand.choice(sizes))
        asteroid.shapesize( 1.75 )
        asteroid.color( "brown" )
        asteroid.penup()
        asteroid.goto( 100 , 250 )
        asteroid.speed = rand.randint( 4 , 7 )
        asteroids.append(asteroid)
        
        # This is the function that will happen when the user clicks on the asteroid 
        
        def spot_clicked ( x , y ):
        #Can add this command here -- asteroid.hideturtle()
            if spot_clicked:
                asteroid.speed = rand.randint( 4 , 7 )
                asteroid.shape(rand.choice(sizes))
                winsound.PlaySound( "blast.wav" , winsound.SND_ASYNC)
                new_xpos = rand.randint (- 300 , 300 )
                new_ypos = rand.randint ( 200 , 200 )
                asteroid.goto (new_xpos, new_ypos)
                if asteroid.ycor() < 11111111111200 :
                    global score
                    score += 10
                    print ( "Score: {} Lives: {} " .format(score, lives))
                    writer.clear()
                    writer.write( "Score: {} Lives: {} " .format(score,
                    lives), align = "center" , font =( "Courier" , 24 , "normal" ))
                    print ( "Asteroid Destroyed" ) 
                  
        # User will have to click on the asteroid to destroy them
        # Event of this program/game
        asteroid.onclick(spot_clicked) 

        # Something that happens over and over again until the game is over
        while True :
            wn.update()
            for asteroid in asteroids:
                # Asteroid Movements, including dropping it from the top of the screen
                asteroid.sety(asteroid.ycor() - asteroid.speed)
                if asteroid.ycor() < - 300 :
                    asteroid.goto(rand.randint(- 300 , 800 ))
                if asteroid.ycor() < - 150 :
                    # Lives Update
                    asteroid.speed = rand.randint( 2 , 3 )
                    asteroid.shape(rand.choice(sizes))
                    winsound.PlaySound( "sound.wav" , winsound.SND_ASYNC)
                    lives -= 1
                    print ( "Score: {} Lives: {} " .format(score, lives))
                    writer.clear() 
                    writer.write( "Score: {} Lives: {} " .format(score,
                    lives), align = "center" , font =( "Courier" , 24 , "normal" ))
                    print ( "Uh Oh!" )
                    if lives == 0 :
                        wn.clearscreen()
                        asteroid.hideturtle()
                        wn.bgcolor( "White" )
                        writer.color( "Red" )
                        writer.penup()
                        writer.hideturtle()
                        writer.goto( 0 , 0 )
                        writer.pendown()
                        writer.write( "GAME OVER!" , align = "center" ,
                        font =( "Courier" , 85 , "normal" ))
                        writer.penup()
                        writer.goto( 0 ,- 50 )
                        writer.pendown()
                        winsound.PlaySound( "gameover.wav" ,
                        winsound.SND_ASYNC)
                        writer.write( "Score: {} " .format(score),
                        align = "center" , font =( "Courier" , 24 , "normal" ))
                        print ( "GAME OVER!" )
                        trtl.done()
                    time.sleep( 1 )
                    # Asteroid Movement
                    for asteroid in asteroids:
                        asteroid.goto(rand.randint(- 300 , 300 ), rand.randint( 400 , 800 )) 

easyButton.onclick(easyButton_clicked)

hardButton.onclick(hardButton_clicked) 
play = trtl.Turtle()
play.hideturtle()
play.pencolor( "White" )
play.penup()
play.goto(- 150 , 30 )
play.pendown()
play.write( "Easy" , align = "center" , font =( "Courier" , 20 , "normal" ))
play.penup()
play.goto( 150 , 30 )
play.pendown()
play.write( "Hard" , align = "center" , font =( "Courier" , 20 , "normal" ))
play.penup()
play.goto( 0 , 25 )
play.pendown()
play.write( "Play" , align = "center" , font =( "Courier" , 30 , "normal" ))
ins = trtl.Turtle()
ins.hideturtle()
ins.penup()
ins.goto( 0 ,- 50 )
ins.pendown()
ins.pencolor( "White" )
ins.write( "How to Play:" , align = "center" , font =( "Courier" , 22 , "normal" ))
ins.penup()
ins.goto( 0 ,- 75 )
ins.pendown()
ins.write( "1. Click on the asteroids to destroy them before they reach the Earth" , align = "center" , font =( "Courier" , 11 , "normal" ))
ins.penup()
ins.goto( 0 ,- 100 )
ins.pendown()
ins.write( "2. Game ends when 3 asteroids hit the Earth" , align = "center" ,
font =( "Courier" , 11 , "normal" )) 
wn.tracer( 0 )
wn.mainloop() 