# The Morse Code dictionary stored as 'data'
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
    # Load the dictionary and create a reversed version for decoding
    dictionary = data
    reverse_dictionary = {value: key for key, value in dictionary.items()}

    # Prompt the user until a valid option and message are received
    proceed = False
    while proceed == False:
        try:
            # Options for display purposes only
            choices = ("Morse Code", "Plain Text")

            # Ask the user to select conversion direction
            user_choice = int(input("What would you like to do?\n"
                                    "1. Convert plain text to morse code\n"
                                    "2. Convert morse code to plaintext\n"
                                    "Select 1. or 2.: "))

            # Check for valid input
            if user_choice not in (1, 2):
                raise ValueError

            # Prompt user to enter text to convert
            input_text = input(f"Enter the message to be converted to {choices[user_choice-1]}: \n").lower()
        
        except ValueError:
            # Catch invalid menu selection or non-integer input
            print("Invalid input! Please select either 1. or 2. to proceed.\n")
        else:
            proceed = True  # Exit loop on valid input

    # Prepare for conversion
    output_text = ""
    proceed = False
    while proceed == False:
        try:
            # Match the user's choice and perform the appropriate conversion
            match user_choice:
                case 1:
                    # Convert plain text to Morse code
                    input_text = list(input_text)  # Split text into characters
                    converted_chars = [dictionary[key] for key in input_text]  # Translate each character
                case 2:
                    # Convert Morse code to plain text
                    input_text = input_text.split()  # Split Morse code into individual codes
                    converted_chars = [reverse_dictionary[key] for key in input_text]  # Translate each code
        except KeyError:
            # Catch invalid characters not found in the dictionary
            print("You entered some invalid characters! You can only translate the letters A-Z and numbers 0-9: ")
        else:
            proceed = True  # Exit loop on successful conversion

    # Format the final output based on conversion type
    if user_choice == 1:
        output_text = " ".join(converted_chars)  # Separate Morse codes with spaces
    else:
        output_text = "".join(converted_chars)  # Join plaintext letters into a full message

    # Display the result
    print(f"Here is the translated text: \n{output_text}\n\n")
