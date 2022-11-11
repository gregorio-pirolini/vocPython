import requests
from bs4 import BeautifulSoup
import re #regex


from marcia import Marcia
from rentrer import Rentrer
from pouppee import Pouppee
from enrose import EnRose
from bb import Bb
from andi import Andi
from maman import Maman

print("Hello, World!")

テキスト  = """importer tous 
                textes aux 
                variables"""

#テキスト  =  Marcia+' '+ Rentrer+' '+ Pouppee+' '+ EnRose+' '+ Bb+' '+Andi+' '+Maman


# regex to cu words and words with -
myRegex = re.compile("[a-zà-ž]+-[a-zà-ž]+|[a-zà-ž]+",re.IGNORECASE)

#cut string into words
言葉= re.findall(myRegex, テキスト)

#remove duplicate from list make set all small letters
unique=set(map(str.lower, 言葉))

#sort alphabeically
alpha=sorted(unique, key=str.casefold)


url = 'https://fr.wiktionary.org/wiki/manger'
r = requests.get(url)
soup = BeautifulSoup(r.content)
findMe =soup.find_all("div", class_="API")
print("findMe")
print(findMe)
# #write to file
# f = open("forMarcia.txt", "a")
# for x in alpha:
#     f.write(x+"\n")  
# f.close()  



# アルファベット = 
# enter text

# create list from words
            #if word exist pass
            # create set from list remove duplicates set(..)
            # alphabeticaly

# create file to print
# write to file as word
