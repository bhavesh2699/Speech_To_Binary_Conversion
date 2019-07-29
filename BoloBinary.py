import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)


try:
    s=r.recognize_google(audio)
    print("You said: " +s )
    print(' '.join(map(bin,bytearray(s,encoding='utf-8'))))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))


 
#developed by Bhavesh Solanki and Ashok Chouhan
