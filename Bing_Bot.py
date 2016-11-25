import urllib2
import webbrowser
import random
import os
import telnetlib
import time
from BeautifulSoup import BeautifulSoup

# Debug Variable
debug = False

# Registers FireFox as available browser
ffpath = 'C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe'
webbrowser.register('firefox', None, webbrowser.BackgroundBrowser(ffpath), 1)

# Retrieve Array of Words to use from Long Wikipedia Article
random_words = urllib2.urlopen('https://en.wikipedia.org/wiki/1918_New_Year_Honours').read()
clean_words = BeautifulSoup(random_words).text
words = []
for word in clean_words.split():
    words.append(word)
print("Length of Array of Words is " + str(len(words)))

# Function to search Bing and acquire points
def search_bing():
    word1 = random.randint(0,len(words))
    word2 = random.randint(0,len(words))
    word3 = random.randint(0,len(words))
    #webbrowser.open_new('https://www.bing.com/search?q='+words[word1]+'+'+words[word2]+'+'+words[word3])
    open_curr_tab('https://www.bing.com/search?q='+words[word1]+'+'+words[word2]+'+'+words[word3])
    print("Done")

# Establish TelNet Session to open FireFox so all searches are contained in one tab.
HOST = 'localhost'
PORT = 4242

def open_curr_tab(url):
    tn = telnetlib.Telnet(HOST, PORT)
    cmd = "content.location.href = '{url}'".format(url=url)

    tn.read_until("repl> ")
    tn.write(cmd + "\n")

    tn.write("repl.quit()\n")


#############################################
if debug:
    start_time = time.time()
    print(webbrowser._browsers)
    webbrowser.get('firefox').open('https://www.google.com')
    run_time = time.time() - start_time
    minutes, seconds = divmod(run_time, 60)
    hours, minutes = divmod(minutes, 60)
    print("Seconds Time Format --- %s seconds ---" % (time.time() - start_time))
    print("Normal Time Format --- %d:%02d:%02d ---" % (hours, minutes, seconds))

if __name__ == "__main__":
    iterations = int(raw_input("How many queries do you want to make: "))
    if iterations != 0:
        try:
            webbrowser.get('firefox').open_new_tab('http://www.bing.com/')
        except:
            print("FireFox Failed to start...")
        time.sleep(5)
        try:
            for i in range(iterations):
                search_bing()
                print(str(i+1)+ " queries made...")
            #os.system("TASKKILL /F /IM firefox.exe")
        except:
            print("An error occured while running searches...")

    correct_input = False

    #mobile_go = raw_input("Is your Browser set to Mobile? Proceed y/n: ")

    while not correct_input:
        mobile_go = raw_input("Is your Browser set to Mobile? Proceed y/n: ")
        if mobile_go == "y" or mobile_go == "yes" or mobile_go == "Yes" or mobile_go == "n" or mobile_go == "no" or mobile_go == "No":
            correct_input = True

    if mobile_go == "y" or mobile_go == "yes":
        iterations = int(raw_input("How many queries do you want to make: "))
        if iterations != 0:
            try:
                webbrowser.get('firefox').open_new_tab('http://www.bing.com/')
            except:
                print("FireFox Failed to start...")
            for i in range(iterations):
                search_bing()
                print(str(i + 1) + " queries made...")
            print("Mobile Step Completed...")
            #time.sleep(10)
    else:
        print("Mobile Step Cancelled....")

#webbrowser.open_new('http://www.bing.com/')