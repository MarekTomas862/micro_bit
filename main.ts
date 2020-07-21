let Losowa = 0
basic.showIcon(IconNames.Happy)
basic.forever(function on_forever() {
    
    basic.showString("Czy parzysta?")
    Losowa = randint(1, 100)
    if (Losowa % 2 == 0) {
        basic.showString("True")
    } else {
        basic.showString("False")
    }
    
    basic.pause(1000)
})
