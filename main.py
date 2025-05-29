import speech_recognition as sr
import webbrowser as web
import pyttsx3
import music_library
from  openai import OpenAI

engine = pyttsx3.init()
client=OpenAI(
    api_key="your-openAI-api-key--HERE",
)
def speak(text): # this function is for converting text to audio using pyttx3 module
    engine.say(text)
    engine.runAndWait()
def OpenAI_request(command):
    response = client.chat.completions.create(
    model="gpt-3.5-turbo",  
    messages=[
        {"role": "system", "content": "you are virtual assistant name beta."},
        {"role": "user", "content": command}
    ]
)
    return response.choices[0].message.content

def process_command(c):  # here the audio converted to text is being process as we command and web.open helps to open sepecific URL 
    if "open youtube" in c.lower():
        web.open("https://youtube.com") 
    elif "open google" in c.lower():
        web.open("https://google.com")
    elif "open facebook" in c.lower():
        web.open("https://facebook.com")
    elif "open github" in c.lower():
        web.open("https://github.com/Abhishek456321")
    elif "who am i" in c.lower():
        speak(" Your  name  is  Abhiishek khaadka  currently  studying  Computer Science  in  Amrit Science Campus. And also the creater of  BETA  that is  me.")
    elif c.lower().startswith("play"):
        key=c.lower().split(" ")[1]
        link=music_library.music[key]
        web.open(link)
    else:
        OpenAI_Response = OpenAI_request(c)
        speak(OpenAI_Response)
   


    

if __name__=="__main__":
    # web.open("www.youtube.com")
    speak("Initializing....Beta")
    # wake word beta
    while True:
        r=sr.Recognizer()
        try:
            with sr.Microphone() as source: # this is microphone for audio input
                print("listening....")
                r.adjust_for_ambient_noise(source, duration=1) # canceling background noise
                audio = r.listen(source,timeout=2,phrase_time_limit=1)
            wake=r.recognize_google(audio) # converting audio into text
            if wake.lower()=="beta": # proceeding only if we say beta 
                speak("Yes! How can i help you . ")
                with sr.Microphone() as source:
                    # print("Beta is Active....")  
                    audio = r.listen(source)  # here recognizer is listening as we speak 
                    command=r.recognize_google(audio) # converting into text 
                process_command(command) #passing to function 
        except Exception as e:
            print(" Time Out....")  
                    
                


            

        
            
             
            
          


           
        
            


                         
         


