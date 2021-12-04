#start implementation from 11-nov-2021
#import modules
import hashlib
import time 

#Banner

def banner():
    print('''
         __  __                  __              _______                        __  ___
        / / / /                 / /             / _____/                       / / / / 
       / /_/ / ____    _____   / /___          / /    _  __   ____     _____  / /_/ /  
      /  _  / / _  |  / ___/  / __  /         / /    | |/ _| / _  |   / ___/ /   _ /   
     / / / / | |/  | |___  | / / / / ______  / /____ |  /   | |/  |  / /__  / /\ \     
    /_/ /_/  \__/|_| /____/ /_/ /_/ /_____/ /______/ |_|    \__/|_| /____/ /_/  \_\    
   
    ''')

banner()

#inputes

hash_string=input("enter hash string :")
wordlist=input("wordlist:")

#file read
wordlistlines=open(wordlist,'r',errors='ignore').readlines()

#md5 cheacking
starting_time=time.time()
for i in range(0,len(wordlistlines)):
    hash_cheack=hashlib.md5(wordlistlines[i].replace('\n','').encode()).hexdigest()
    
    if hash_string==hash_cheack:
        print("password="+wordlistlines[i].replace('\n',''))
        ending_time=time.time()
        print("time:"+str(ending_time-starting_time))
        exit()
        
print("password not found!!")

ending_time=str(time.time())
print("time:"+str(ending_time-starting_time))
