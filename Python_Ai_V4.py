try:
    from nltk.tokenize import WordPunctTokenizer
    from nltk.corpus import stopwords
    import os,wikipedia,random,nltk,psutil,webbrowser,win32api
    from playsound import playsound
    import speech_recognition as sr
    from datetime import datetime
    from googlesearch import search

    #user library
    import Ai_gttss,Task
except ModuleNotFoundError:
    print('Please check requirements')
    exit()


class Ai():
    def __init__():
        pass
    
    def wish():
        """
        Wishes Me according to time
        """
        hour = int(datetime.now().hour)
        if(hour>=0) and (hour<12):
            Ai_gttss.gttts('A Very Good Morning')
        elif(hour>=12) and (hour<16):
            Ai_gttss.gttts('Good Afternoon, How\'s your day going?')
        elif(hour>=16) and (hour<20):
            Ai_gttss.gttts('Good Evening, How was your day ?')
        elif(hour>=20) and (hour<24):
            Ai_gttss.gttts('Welcome back!, hope you\'re having a great day!')

    def user_input_mic():
        """
        User input Via Microphone
        """
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.pause_threshold = 0.80
            r.energy_threshold = 1000
            print('Listening...')
            audio = r.listen(source)
            try:
                print('Fetching the string...')
                user_input = r.recognize_google(audio,language="en-in")
                print(f'User said: {user_input}')
            except sr.RequestError:
                playsound('check_internet.mp3')
                print('Check Internet Connection')
                return "None"
            except sr.UnknownValueError:

                return 'None'
                pass
            except:
                print('Some Error Occured')
                return "None"
            return user_input

if __name__ == "__main__":
    Ai.wish()
    while True:
        
        user_input = Ai.user_input_mic().lower()
        t = WordPunctTokenizer()
        user_input_tokened = t.tokenize(user_input)
        filtered_sentence = []
        stopped_sent = []
        stop_words = set(stopwords.words('english'))
        
        greet_list = ['Hello!,how can i help you','Hello!, hope you are doing great','Sending you a warm hello and wishing you a beautiful day!']
        bye_list = ['Good bye!, see you later','It was a great talk!, ,I look forward to seeing you again soon']
        thank_list = ['I am Happy to help you!','My pleasure!','Don\'t Mention it','No worries!','You\'re welcome']
        
        if 'hello' in user_input_tokened or 'hey' in user_input_tokened or 'hi' in user_input_tokened:
            for greet in greet_list:
                greeting = random.choice(greet_list)
                Ai_gttss.gttts(greeting)
                break
        
        elif 'fine' in user_input_tokened or 'i am fine' in user_input_tokened or 'doing good' in user_input_tokened or 'alright' in user_input_tokened or 'nice' in user_input_tokened:
            Ai_gttss.gttts('Great!, Let\'s get started')


        elif 'not good' in user_input_tokened or 'bad' in user_input_tokened or 'worst' in user_input_tokened or 'ok ok' in user_input_tokened:
            Ai_gttss.gttts('Well allow me to make it better')


        elif 'thank you' in user_input or 'thanks' in user_input:
            Ai_gttss.gttts(random.choice(thank_list))


        elif 'good bye' in user_input or 'bye' in user_input or 'shutdown alice' in user_input or 'cya' in user_input:
            Ai_gttss.gttts(random.choice(bye_list)) 
            text = Task.sleep_mode()    
            Ai_gttss.gttts(text)        
        
        else:
            for w in user_input_tokened:    #filters the sentence bringin the important words
                if w not in stop_words: 
                    filtered_sentence.append(w)
                else:
                    stopped_sent.append(w)

            #print(stopped_sent,'\n',filtered_sentence)
            question_words = ['what','when','where','who','which','how']
            for words in question_words:
                if 'what' in stopped_sent :
                    if 'is' in stopped_sent :
                        if 'weather' in filtered_sentence or 'temperature' in filtered_sentence or 'temp' in filtered_sentence:
                            if 'here' in stopped_sent:
                                weather_done = Task.weather('jaipur')
                            else:
                                city = str(filtered_sentence[-2]+" "+filtered_sentence[-1])
                                weather_done = Task.weather(city)    
                            if weather_done:
                                pass
                            else:
                                pass
                            break
                        elif 'time' in filtered_sentence:
                            now = datetime.now()
                            current_time = now.strftime('%I:%M:%p')
                            print(current_time)
                            current_time = 'Time right now is '+current_time 
                            Ai_gttss.gttts(current_time)
                            break
                        elif 'date' in filtered_sentence:
                            today = datetime.today()
                            date_now = today.strftime('%d %B %Y')
                            print(date_now)
                            current_date = 'Today is '+date_now
                            Ai_gttss.gttts(current_date)
                            break
                        elif 'battery' in filtered_sentence:
                            try:
                                battery = psutil.sensors_battery()[0]
                                percent = str(battery)
                                print(percent)
                                sentence = 'Current battery Percent is '+percent
                                Ai_gttss.gttts(sentence)
                                sentence = ''
                            except TypeError:
                                Ai_gttss.gttts('I think You Are on desktop, so I cant check your battery status.')
                            break
                        elif 'computer' in filtered_sentence and 'status' in filtered_sentence:
                            total_ram = psutil.virtual_memory()[0] / 10**9
                            avail_ram = psutil.virtual_memory()[1] / 10**9
                            used_ram = psutil.virtual_memory()[3] / 10**9 
                            total_ram = str(round(total_ram,2))
                            avail_ram = str(round(avail_ram,2))
                            used_ram = str(round(used_ram,2))
                            try:
                                battery = psutil.sensors_battery()[0]
                                percent = str(battery)
                                print(percent)
                                sentence1 = 'Current battery Percent is '+percent+'%.'
                                Ai_gttss.gttts(sentence1)
                            except TypeError:
                                Ai_gttss.gttts('I think You Are on desktop, so I cant check your battery status.')
                            sentence = 'The Total Ram is '+total_ram+' GB'+'.with '+avail_ram+' GB Available Ram, with Usage of '+used_ram+'GB.'
                            Ai_gttss.gttts(sentence)
                            break
                        else:
                            Task.google(user_input)
                            break
                            

                    elif 'are' in stopped_sent :
                        for words in filtered_sentence:
                            sentence = ''.join(words)
                        print(sentence)
                        Task.wiki(sentence)
                        sentence = ''
                        break
                elif 'launch' in filtered_sentence or 'open' in filtered_sentence or 'run' in filtered_sentence:
                    if 'folder' in user_input_tokened:
                        try:
                            if 'open' in user_input_tokened:
                                folder = user_input.replace('open ','')
                            if 'launch' in user_input_tokened:
                                folder = user_input.replace('launch ','')
                            if 'run' in user_input_tokened:
                                folder = user_input.replace('run ','')
                            
                            folder = folder.replace(' folder','')
                        except:
                            print('some error folder')
                            pass
                        os.system('explorer C:\\{}'.format(folder))
                    if 'file' in user_input_tokened:
                        try:
                            if 'open' in user_input_tokened:
                                run_file = user_input.replace('open ','')
                            if 'launch' in user_input_tokened:
                                run_file = user_input.replace('launch ','')
                            if 'run' in user_input_tokened:
                                run_file = user_input.replace('run ','')
                            
                            run_file = run_file.replace(' file','')
                        except:
                            print('some error in running file')
                            pass
                        listt,user_need = Task.runn(run_file)
                        Task.multiple(listt,user_need)
                        break
                    websites = ['google','youtube','facebook','stackoverflow','python','wikipedia','twitter']
                    for words in websites:
                        if words != 'google':
                            if words in filtered_sentence:
                                query = words
                                sentence = 'Opening '+query
                                Ai_gttss.gttts(sentence)
                                for j in search(query,num=1,stop=1):
                                    try:
                                        webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open(j)
                                    except: 
                                        webbrowser.open(j)        
                                break
                        elif 'google' in filtered_sentence:
                            Ai_gttss.gttts('Opening Google')
                            try:
                                webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open('www.google.com')
                            except: 
                                webbrowser.open('www.google.com')        
                            break
                    break