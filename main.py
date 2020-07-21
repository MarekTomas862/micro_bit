Losowa = 0
basic.show_icon(IconNames.HAPPY)

def on_forever():
    global Losowa
    basic.show_string("Czy parzysta?")
    Losowa = randint(1, 100)
    if Losowa % 2 == 0:
        basic.show_string("True")
    else:
        basic.show_string("False")
    basic.pause(1000)
basic.forever(on_forever)
