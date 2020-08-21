import os
import win32api
import Ai_gttss

print('enterred')
def multiple(files_list, user_need):
    for x in files_list:
        if(len(files_list) == 1):
            print(x)
            #os.startfile(os.path.join(x))
            break
        else:
            for x in files_list:
                print(x)
            ch = int(input('which file would like to open: '))
            ch = ch-1
            try:
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
            print('searching drive '+drive)
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
        
print('out of functions')
listt,user_input = runn('python')
multiple(listt,user_input)
print('eof')