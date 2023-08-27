from unidecode import unidecode
import sys

alphanum_to_morse = {
    "1" : "1 3 3 3 3",
    "2" : "1 1 3 3 3",
    "3" : "1 1 1 3 3",
    "4" : "1 1 1 1 3",
    "5" : "1 1 1 1 1",
    "6" : "3 1 1 1 1",
    "7" : "3 3 1 1 1",
    "8" : "3 3 3 1 1",
    "9" : "3 3 3 3 1",
    "0" : "3 3 3 3 3",
    " " : "       ",

    "B" : "3 1 1 1",
    "C" : "3 1 3 1",
    "F" : "1 1 3 1",
    "H" : "1 1 1 1",
    "J" : "1 3 3 3",
    "L" : "1 3 1 1",
    "P" : "1 3 3 1",
    "Q" : "3 3 1 3",
    "V" : "1 1 1 3",
    "X" : "3 1 1 3",
    "Y" : "3 1 3 3",
    "Z" : "3 3 1 1",

    "D" : "3 1 1",
    "G" : "3 3 1",
    "K" : "3 1 3",
    "O" : "3 3 3",
    "R" : "1 3 1",
    "S" : "1 1 1",
    "U" : "1 1 3",
    "W" : "1 3 3",

    "A" : "1 3",
    "I" : "1 1",
    "M" : "3 3",
    "N" : "3 1",

    "E" : "1",
    "T" : "3"
}

morse_to_alphanum = {value : key for key, value in alphanum_to_morse.items()}

intro_txt = '''
┌────────────────────────────────────────────────────┐
│          Welcome to Morse Code Converter!          │
│ You can convert text to Morse Code and vice-versa! │
└────────────────────────────────────────────────────┘
'''

reminders = '''
┌─────────────────────────────────────────────────────────────────────────┐
│ Friendly reminders:                                                     │
│ * use only spaces, dot (.) and dash (—) characters                      │
│ * three spaces to separate two letters or digits                        │
│ * seven spaces to separate two words.                                   │
│                                                                         │
│ Example given (Translates to "MORSE CODE"):                             │
│ — —   — — —   . — .   . . .   .             — . — .   — — —   — . .   . │
└─────────────────────────────────────────────────────────────────────────┘

Please insert Morse code for conversion:
'''

run = '''
┌─────────────────────────────┐
│           OPTIONS           │
│ For text to Morse code:   1 │
│ For Morse code to text:   2 │
│ Exit program:             0 │
└─────────────────────────────┘

Please select a number and press Enter key: '''

def morse_converter(option, string):
    if option == "1":
        user_input = input("\nPlease insert text for conversion (letters, numbers and spaces only):\n")
        for char in user_input:
            try: 
                string = f"{string}{alphanum_to_morse[unidecode(char).upper()]}   "
            except:
                continue
        morse_string = string.replace("1", ".").replace("3", "—")
        return morse_string

    elif option == "2":
        def letter_converter(current_word):
            alpha_string = string
            for letter in current_word:
                try: 
                    alpha_string = f"{alpha_string}{morse_to_alphanum[letter]}"
                except:
                    continue
            return alpha_string

        user_input = input(reminders).replace(".", "1").replace("—", "3").split("       ")

        if len(user_input) == 1:
            word = user_input[0].split("   ")
            string = letter_converter(word)
        else:
            for item in range(len(user_input)):
                word = user_input[item].strip().split("   ")
                string = f"{letter_converter(word)} "
        return string

    else: 
        return None


option_select = input(intro_txt + run).strip()
new_string = ""
result = morse_converter(option_select, new_string)

while option_select != "0":
    if option_select not in ["1", "2"]:
        option_select = input("\nPlease try again. Your option:\n").strip()
        result = morse_converter(option_select, new_string)

    print(f"\n__________\n\nConverted result:\n\n{result}\n")
    option_select = input(run).strip()
    result = morse_converter(option_select, new_string)

sys.exit()