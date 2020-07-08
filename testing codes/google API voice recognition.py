
import speech_recognition as speech

def captainIdSpeech():
    recognizing=speech.Recognizer()
    
    with speech.Microphone() as source:
        audio=recognizing.listen(source)
    
    try:
        variable1=recognizing.recognize_google(audio)
        captainIdSpeechSet(variable1) 
    except Exception:
        print("Couldn't reach you, Please try again")
        
    
"""CaptainIdSpeechSet() function shows the spoken words in ENTRY field of Captain ID"""
def captainIdSpeechSet(text):
    print(text)
    return

captainIdSpeech()
