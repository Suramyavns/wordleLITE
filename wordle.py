from nltk.corpus import words
import random #run this using python 3.9.9 64-bit
from colorama import Fore
def computation(numchances,numletters,answer,ar):
    chances=1
    result=str()
    while chances<=numchances:
        entry=input(Fore.WHITE + 'Enter your word: ')
        chances=chances+1
        if entry in ar:
            for i in range(numletters):
                if entry[i] in answer:
                    if entry[i]==answer[i]:
                        result += (Fore.GREEN + entry[i])
                    if entry[i]!=answer[i]:
                        result += (Fore.YELLOW + entry[i])
                if entry[i] not in answer:
                    result += (Fore.WHITE + entry[i])
            print(result)
            result += " , "
        if entry==answer:
            print(Fore.GREEN + entry)
            break
        elif entry not in ar: 
            print('Not in the wordlist')
            chances=chances-1
    print('WordleLITE ',answer," ",chances-1,'/6',sep='')

wordlist = words.words()
ar=[]
for i in range(len(wordlist)):
    if len(wordlist[i])==5:
        ar.append(wordlist[i])
answer=random.choice(ar)
computation(6,5,answer,ar)
