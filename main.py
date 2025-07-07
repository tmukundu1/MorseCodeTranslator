import sys

# Morse code dictionary for letters, digits, and common symbols
data = {
    "a": ".-",          "b": "-...",            "c": "-.-.",            "d": "-..",             "e": ".",           "f": "..-.",        "g": "--.",
    "h": "....",         "i": "..",             "j": ".---",            "k": "-.-",             "l": ".-..",        "m": "--",          "n": "-.",              
    "o": "---",         "p": ".--.",            "q": "--.-",            "r": ".-.",             "s": "...",         "t": "-",           "u": "..-",         
    "v": "...-",        "w": ".--",             "x": "-..-",            "y": "-.--",            "z": "--..",        "0": "-----",       "1": ".----",           
    "2": "..---",       "3": "...--",           "4": "....-",           "5": ".....",           "6": "-....",       "7": "--...",       "8": "---..",
    "9": "----.",       "&": ".-...",           "'": ".----.",          "@": ".--.-.",          ")": "-.--.-",      "(": "-.--.",       ":": "---...",          
    ",": "--..--",      "=": "-...-",           "!": "-.-.--",          ".": ".-.-.-",          "-": "-....-",      "+": ".-.-.",       '"': ".-..-.",          
    "?": "..--..",      " ": "/",
    }

while True:
    # Prepare dictionaries for encoding and decoding
    dictionary = data
    reverse_dictionary = {value: key for key, value in dictionary.items()}

    # Get user input for mode selection
    proceed = False
    while proceed == False:
        try:
            user_choice = int(input("What would you like to do?\n"
                                    "1. Convert plain text to morse code\n"
                                    "2. Convert morse code to plaintext\n" \
                                    "3. Exit\n"
                                    "Enter your choice (1/2/3): "))

            # Check for valid input
            if user_choice not in (1, 2, 3):
                raise ValueError

            if user_choice != 3:
                input_text = input(f"Enter the message to be translated: \n").lower()
        
        except ValueError:
            print("Invalid input! Please select either 1, 2 or 3 to proceed.\n")
        else:
            proceed = True  # Exit loop on valid input

    # Convert the input text based on user selection
    output_text = ""
    while proceed:
        try:
            match user_choice:
                case 1:
                    # Convert plain text to Morse code
                    converted_chars = [dictionary[key] for key in list(input_text)]
                case 2:
                    # Convert Morse code to plain text
                    converted_chars = [reverse_dictionary[key] for key in input_text.split()]
                case 3:
                    print("Goodbye!")
                    sys.exit()
        except KeyError:
            # Catch invalid characters not found in the dictionary
            print("Invalid character detected! Only use A–Z, 0–9, and valid Morse symbols.")
        else:
            proceed = False  # Exit loop on successful conversion

    # Format the final output based on conversion type
    output_text = " ".join(converted_chars) if user_choice == 1 else "".join(converted_chars)

    # Display the result
    print(f"Here is the translated text: \n{output_text}\n\n")
