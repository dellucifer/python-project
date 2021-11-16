#start implementation from 11-nov-2021
#import modules
import hashlib
import time       

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
