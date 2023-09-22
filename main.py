# Morse-code project #

# TODO 1: make dictionary where key is letter, value is code

morse_code = {
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "'": ".----.",
    "!": "-.-.--",
    "/": "-..-.",
    "(": "-.--.",
    ")": "-.--.-",
    "&": ".-...",
    ":": "---...",
    ";": "-.-.-.",
    "=": "-...-",
    "+": ".-.-.",
    "-": "-....-",
    "_": "..--.-",
    "@": ".--.-.",
    " ": " ",
}



wanna_code = True

while wanna_code:

    # TODO 2: demande input, split characters and save in list.
    response = input("Type 1 for encoding, 2 for decrypting, quit to quit: ").lower()
    if response == "quit":
        wanna_code = False

    elif response == "1":
        to_code = input("What would you like to code into morse code?: ").lower()

        # TODO 3: Translate list to code.
        morse = []
        for character in to_code:
            code = morse_code[character]
            morse.append(code)

        # TODO 4: Return code.
        print(morse)
    elif response == "2":
        to_code = input("What would you like to decipher?: ")
        code_list = to_code.split()
        print(code_list)
        full_message = []
        for code in code_list:
            message = [key for key, value in morse_code.items() if value == code]
            full_message.append(message)
        if full_message == [[]]:
            print("Only enter morse code please")
        print(full_message)

    else:
        print("Invalid input, try again!")
