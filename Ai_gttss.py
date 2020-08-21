from gtts import gTTS 
from playsound import playsound
import os  
global cnt
cnt = 0
def gttts(mytext):
    global cnt
    k=1
    cnt+=1
    while k==1: 
        try:
            language = 'en-us'
            myobj = gTTS(text=mytext, lang=language, slow=False)
            myobj.save(f"in_prog{cnt}.mp3")
            k=0
        except:
            print('gtts error')
            continue
        try:
            playsound(f'in_prog{cnt}.mp3')
            os.remove(f'in_prog{cnt}.mp3')
        except:
            print('unable to play sound')
            pass
