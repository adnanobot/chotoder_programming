import pyttsx3
import speech_recognition as sr
import re

voice_engine = pyttsx3.init()
voice_engine.setProperty("rate", 150)
voice_engine.setProperty("voice", "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_enGB_GeorgeM")
voice_engine.setProperty('volume', 1.0) 

recognizer = sr.Recognizer()

print("Bismillah")
print("==================================")
print("  Mayer Doa Hotel & Restaurant")
print("     Matikata, Gorto City")
print("==================================")
print()
print("~*~*~*~*~*~*~*~*~*~*~*~*")
print("        Menu")
print("~*~*~*~*~*~*~*~*~*~*~*~*")
print("1. Kacchi Biryani ... ... ... 180 tk.")
print("2. Morog Polao ... ... ... .. 150 tk.")
print("3. Plain Polao ... ... ... .. 120 tk.")
print("3. Kala Bhuna ... ... ... ... 120 tk.")
print()

# price list
# kacchi = 180
# morog_polao = 150
# plain_polao = 120
# kala_bhuna = 120

price_dict = {"1": 180, "2": 120, "3": 120, "4": 120}
item_dict = {"1": "Kacchi biryani", "2": "Morog Polao", "3": "Plain Polao",
             "4": "Kala bhuna"}
bill = 0

# voice_engine.say("Assalamu alaikum mama.")
# voice_engine.say("I am your robowaiter in Maer Doa Hotel.")
print("Please tell us the item number:")
voice_engine.say("Please tell us the item number.")
# voice_engine.say("Tell me like this: .")
# voice_engine.say("Item number 100")
voice_engine.runAndWait()

while True:
    print("Listening ...")

    with sr.Microphone() as source:
        audio_text = recognizer.listen(source=source)
        user_choice = ""

        try:
            # using google speech recognition
            audio_text = recognizer.recognize_google(audio_text)
            user_choice = audio_text[audio_text.find("number") + len("number") + 1: ]
            print("choice is ", user_choice)
            print("You have selected: ", item_dict[user_choice])
            voice_engine.say("You have selected: " + item_dict[user_choice])
            voice_engine.runAndWait()
        except:
            print("Sorry, I did not get that")

    print("You have selected ", item_dict[user_choice])

    bill =  bill + price_dict[user_choice]
    
    exit_choice = input("Anything else? <Y/N>")
    if exit_choice == "N" or exit_choice == "n":
        print()
        print("Thank you sir. You have a great choice.")
        print("Your total bill is ", bill)
        print("Your food is coming soon. You can do zikir and fikir during this time.")
        print()
        break
    print("\nPlease enter the menu number: ")
