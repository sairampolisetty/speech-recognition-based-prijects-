import speech_recognition as sr
import pyttsx3

text=pyttsx3.init()
def main():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        text.say("please say something")
        text.runAndWait()

        audio = r.listen(source)

        try:
            print("you have said\n" + r.recognize_google(audio))
            text.say("you have said" + r.recognize_google(audio))
            text.runAndWait()

        except Exception as e:
            print('error' + str(e))

if __name__=="__main__":
    main()
text.say("thank you     so much for using me")
text.runAndWait()