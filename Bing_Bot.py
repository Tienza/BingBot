import urllib2
import webbrowser
import random
import os
import platform
import telnetlib
import time
from unidecode import unidecode
from BeautifulSoup import BeautifulSoup

# Debug Variable
debug = False

# Registers FireFox and Microsoft Edge as available browser
ffpath = 'C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe'
webbrowser.register('firefox', None, webbrowser.BackgroundBrowser(ffpath), 1)

mepath = 'edge.bat'
webbrowser.register('edge', None, webbrowser.BackgroundBrowser(mepath), 2)

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
    open_curr_tab('https://www.bing.com/search?q=' + unidecode(words[word1]) + '+' + unidecode(words[word2]) + '+' + unidecode(words[word3]))
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
    print(webbrowser._tryorder)
    webbrowser.get('firefox').open('https://www.google.com')

if __name__ == "__main__":
    # Does a single search on Microsoft Edge to get Edge Points
    if "Windows" in platform.platform():
        print("Doing Single Search on Microsoft Edge...")
        word1 = random.randint(0,len(words))
        word2 = random.randint(0,len(words))
        word3 = random.randint(0,len(words))
        edge_search = 'start microsoft-edge:https://www.bing.com/search?q=' + unidecode(words[word1]) + '+' + unidecode(words[word2]) + '+' + unidecode(words[word3])
        if debug:
            print("Writing edge.bat...")
        with open('edge.bat', 'w') as edge_bat:
            edge_bat.writelines(edge_search)
        webbrowser.get('edge').open_new_tab('http://www.bing.com/')
        time.sleep(1)
        if debug:
            print("Finished used edge.bat...deleting...")
        os.remove('edge.bat')
        time.sleep(2)
        os.system("TASKKILL /F /IM MicrosoftEdge.exe")
        print("")

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
        except:
            print("An error occured while running searches...")

        print("")

    correct_input = False

    while not correct_input:
        mobile_go = raw_input("Is your Browser set to Mobile? Proceed y/n: ")
        if mobile_go == "y" or mobile_go == "yes" or mobile_go == "Yes" or mobile_go == "n" or mobile_go == "no" or mobile_go == "No":
            correct_input = True

    if mobile_go == "y" or mobile_go == "yes" or mobile_go == "Yes":
        iterations = int(raw_input("How many queries do you want to make: "))
        if iterations != 0:
            for i in range(iterations):
                search_bing()
                print(str(i + 1) + " queries made...")

            print("")
            print("Mobile Step Completed...")
            print("Please switch back to Desktop User Agent if you wish. You have 10 seconds...")
            time.sleep(10)
        open_curr_tab('http://www.bing.com/')
    else:
        print("Mobile Step Cancelled....")
        open_curr_tab('http://www.bing.com/')

#webbrowser.open_new('http://www.bing.com/')
if debug:
    run_time = time.time() - start_time
    minutes, seconds = divmod(run_time, 60)
    hours, minutes = divmod(minutes, 60)
    print("Seconds Time Format --- %s seconds ---" % (time.time() - start_time))
    print("Normal Time Format --- %d:%02d:%02d ---" % (hours, minutes, seconds))