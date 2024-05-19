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

print("Assalamu alaikum mama.")
voice_engine.say("Assalamu alaikum mama.")
voice_engine.runAndWait()

print("I am your robowaiter in Maayer Doa Hotel.")
voice_engine.say("I am your robowaiter in Maayer Doa Hotel.")
voice_engine.runAndWait()

print("Assurance City, Gortopuri, Golakata Road.")
voice_engine.say("Assurance City, Gortopuri, Golakata Road.")
voice_engine.runAndWait()

print("Please write the item number.")
voice_engine.say("Please write the item number.")
voice_engine.runAndWait()

print("I can't hear well.")
voice_engine.say("I can't hear well.")
voice_engine.runAndWait()

while True:
    user_choice = input("Please enter the item number: ")
    print("You have selected ", item_dict[user_choice])
    voice_engine.say("You have selected: " + item_dict[user_choice])
    voice_engine.runAndWait()    

    bill =  bill + price_dict[user_choice]
    
    print("Ar kisu lagbo naki mama?")
    voice_engine.say("Ar kisu lagbo naki mama?")
    voice_engine.runAndWait()

    print("I mean anything else?")
    voice_engine.say("I mean anything else?")
    voice_engine.runAndWait()

    exit_choice = input("Anything else? <Y/N>")
    if exit_choice == "N" or exit_choice == "n":
        print()
        print("Thank you sir. You have a great choice.")
        voice_engine.say("Thank you sir. You have a great choice.")
        voice_engine.runAndWait()

        print("Your total bill is "+ bill)
        voice_engine.say("Your total bill is "+ str(bill))
        voice_engine.runAndWait()
        
        print("Your food is coming soon. You can do ziikir and fiikir during this time.")
        voice_engine.say("Your food is coming soon. You can do ziikir and fiikir during this time.")
        voice_engine.runAndWait()
        print()
        break
