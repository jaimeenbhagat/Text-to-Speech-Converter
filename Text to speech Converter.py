import pyttsx3
engine = pyttsx3.init()
a=input("Enter the text: ")
engine.say(a)
engine.runAndWait()
