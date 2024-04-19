pipeY = 0
pipeX = 5
birdY = 2
frameRate = 3 * 100

basic.show_string("Bird")
basic.show_leds("""
    . # # . .
    # # . # .
    # # # # #
    # # # # #
    . # # . .
    """)
basic.pause(frameRate)


def drawPipes():
    i = 0

    for i in range(5):
        led.plot(pipeX, i)

    led.unplot(pipeX, pipeY)

def mainLoop():
    global birdY, pipeX, pipeY

    basic.clear_screen()
    drawPipes()
    led.plot(0, birdY)
    birdY += 1

    if birdY > 4:
        birdY = 4
    elif birdY < 0:
        birdY = 0

    pipeX -= 1
    if pipeX < 0:
        pipeY = randint(1, 3)
        pipeX = 5

    if birdX == pipeX and birdY != pipeY:
        basic.show_string("Game Over!")
        game.show_score()
    else:
        game.set_score(game.score += 1)

    basic.pause(frameRate)

def on_button_pressed_a():
    global birdY
    birdY += -1

input.on_button_pressed(Button.A, on_button_pressed_a)


def on_forever():
    mainLoop()

basic.forever(on_forever)
