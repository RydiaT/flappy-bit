let pipeY = 0
let pipeX = 5
let birdY = 2
let frameRate = 3 * 100
basic.showString("Bird")
basic.showLeds(`
    . # # . .
    # # . # .
    # # # # #
    # # # # #
    . # # . .
    `)
basic.pause(frameRate)
function drawPipes() {
    let i = 0
    for (i = 0; i < 5; i++) {
        led.plot(pipeX, i)
    }
    led.unplot(pipeX, pipeY)
}

function mainLoop() {
    
    basic.clearScreen()
    drawPipes()
    led.plot(0, birdY)
    birdY += 1
    if (birdY > 4) {
        birdY = 4
    } else if (birdY < 0) {
        birdY = 0
    }
    
    pipeX -= 1
    if (pipeX < 0) {
        pipeY = randint(1, 3)
        pipeX = 5
    }
    
    basic.pause(frameRate)
}

input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    birdY += -1
})
basic.forever(function on_forever() {
    mainLoop()
})
