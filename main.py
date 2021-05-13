def on_button_pressed_a():
    global code_morse
    code_morse = "" + code_morse + "1"
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global code_morse
    code_morse = "" + code_morse + "2"
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    basic.show_string("" + (morce[CODE.index(code_morse)]))
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

CODE: List[str] = []
morce: List[str] = []
code_morse = ""
code_morse = ""
morce = ["A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z"]
CODE = ["12",
    "2111",
    "2121",
    "211",
    "1",
    "1121",
    "221",
    "1111",
    "11",
    "1222",
    "212",
    "1211",
    "22",
    "21",
    "222",
    "1221",
    "2212",
    "121",
    "111",
    "2",
    "112",
    "1112",
    "122",
    "2112",
    "2122",
    "2211"]