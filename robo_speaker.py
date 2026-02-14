# import os

# if __name__ == "__main__":
#    while True:
#     x = input("Enter the word you want me to speak -> ")
#     if(x=="break"):
#       break
#     command = f"say {x}" # works only in macos
#     os.system(command)
import pyttsx3

def speak(text):
    engine = pyttsx3.init("sapi5")  # Initialize SAPI5
    voices = engine.getProperty("voices")  # Get available voices
    engine.setProperty("voice", voices[1].id)  # Select voice (0: Male, 1: Female)
    engine.setProperty("rate", 170)  # Adjust speaking speed
    engine.say(text)
    engine.runAndWait()

# speak("Hello! How are you?")
if __name__ == "__main__":
   while True:
       x = input("Enter what u want me to speak -> ")
       if(x=="break"):
           speak("Bye bye sir")
           break
       speak(x)