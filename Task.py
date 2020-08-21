import webbrowser,wikipedia
import requests,json
import Ai_gttss
import speech_recognition as sr
import os
import win32api

def sleep_mode():
    """
    Code went into sleep mode
    """
    user_input1 = False
    while user_input1 == False:
        """
        User input Via Microphone
        """
        r = sr.Recognizer()
        with sr.Microphone() as source:
            global user_input
            r.pause_threshold = 0.95
            r.energy_threshold = 1000
            print('.')
            audio = r.listen(source)
            try:
                user_input = r.recognize_google(audio,language="en-in")
            except sr.RequestError:
                print('Check Internet Connection')
            except sr.UnknownValueError:
                pass
            except WaitTimeoutError:
                pass
            except:
                pass
            try:
                user_input = user_input.lower()
                #print(user_input)
            except:
                pass
            wake_list = ['wake up alice','hey alice','hello alice','ok alice','wake up','anybody there']
            for wake in wake_list:
                try:
                    if wake in user_input:
                        return 'Hello!, How can I help you?'
                        user_input1 = True
                    else:
                        pass
                except:
                    pass


def weather(city_ai):
    """
    Weather search using open weather map api 
    """
    city = ''
    if 'weather' in city_ai :
        city = city_ai.replace('weather','')
    elif 'temperature' in city_ai:
        city = city_ai.replace('temperature','')
    elif 'temp' in city_ai:
        city = city_ai.replace('temp','')
    else:
        city = city_ai
    try:
        url = 'http://api.openweathermap.org/data/2.5/weather?q='+city+'&units=metric&appid=792bc022607eea550d5f59aa9114554c'
        result = requests.get(url)
        result = result.json() 
        print('Temp: '+str(result['main']['temp'])+' C')
        print('Weather: '+result['weather'][0]['description'])
        print('Min Temp: ',result['main']['temp_min'])
        print('Max Temp: ',result['main']['temp_max'])
        Ai_gttss.gttts('The Temperature In'+city+' is '+str(result['main']['temp'])+'Degree Celcius with '+result['weather'][0]['description']+', And Humidity of '+str(result['main']['humidity'])+'% ')
        return True
    except KeyError:
        Ai_gttss.gttts('Some thing is wrong with the weather api. Please wait a moment ,or you can try searching on google by saying, , search weather of (YOUR CITY NAME) using google')
        print('Weather API problem please wait a moment or you can search on Google')
        return False
    except:
        Ai_gttss.gttts('Some error occured during searching weather. Please try again later')



def google(user_input):
        """
        Search in Google by opening a web browser
        """
        Ai_gttss.gttts('Let\'s find Your answer\'s on Google')
        try:
            webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open(f'https://www.google.com/search?q='+user_input)
        except:
            webbrowser.open('https://www.google.com/search?q='+user_input)



def wiki(user_input):
        """
        Searching in wikipedia 
        """
        Ai_gttss.gttts('Searching on Wikipedia.')
        result = wikipedia.summary(user_input, sentences = 3)
        Ai_gttss.gttts('According to Wikipedia.')
        print('Result:',result)
        Ai_gttss.gttts(result)



def multiple(files_list,user_need):
    for x in files_list:
        if(len(files_list) == 1):
            sentence = 'Opening '+user_need
            Ai_gttss.gttts(sentence)
            os.startfile(os.path.join(x))
            break
        else:
            Ai_gttss.gttts('Since There are multiple files of same name, kindly choose the file by entering the number ')
            for x in files_list:
                print(x)
            ch = int(input('which file would like to open'))
            ch = ch-1
            try:
                sentence = 'Opening '+user_need
                Ai_gttss.gttts(sentence)
                os.startfile(os.path.join(files_list[ch]))
            except:
                Ai_gttss.gttts('file not found in any drives')
            break


def runn(user_need):
    drives = win32api.GetLogicalDriveStrings()#getting drives
    drives = drives.split('\000')[:-1]
    #print(drives)#printing existing drives on system
    user_need = user_need.replace(' ','')
    cnt = 0
    files_list = []
    for drive in drives:
        if cnt == 0:
            dir_path = os.path.dirname(drive) 
            for root, dirs, files in os.walk(dir_path): 
                for file in files:
                    file = (root+'\\'+str(file)).lower() 
                    if file.endswith(user_need+'.exe'): 
                        files_list.append(file)
                        cnt+=1
                        break
        else:
            pass
    return files_list,user_need