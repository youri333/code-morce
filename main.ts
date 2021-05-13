input.onButtonPressed(Button.A, function () {
    code_morse = "" + code_morse + "1"
})
input.onButtonPressed(Button.B, function () {
    code_morse = "" + code_morse + "2"
})
input.onGesture(Gesture.Shake, function () {
    basic.showString("" + (morce[CODE.indexOf(code_morse)]))
})
let CODE: string[] = []
let morce: string[] = []
let code_morse = ""
code_morse = ""
morce = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
CODE = ["12", "2111", "2121", "211", "1", "1121", "221", "1111", "11", "1222", "212", "1211", "22", "21", "222", "1221", "2212", "121", "111", "2", "112", "1112", "122", "2112", "2122", "2211"]
