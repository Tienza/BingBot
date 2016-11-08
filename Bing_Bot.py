import urllib2
import webbrowser
import random
from BeautifulSoup import BeautifulSoup

random_words = urllib2.urlopen('https://en.wikipedia.org/wiki/1918_New_Year_Honours').read()
clean_words = BeautifulSoup(random_words).text
words = []
for word in clean_words.split():
    words.append(word)
print("Length of Array of Words is " + str(len(words)))

def search_bing():
    word1 = random.randint(0,len(words))
    word2 = random.randint(0,len(words))
    word3 = random.randint(0,len(words))
    webbrowser.open_new_tab('https://www.bing.com/search?q='+words[word1]+'+'+words[word2]+'+'+words[word3])
    print("Done")

for i in range(30):
    search_bing()