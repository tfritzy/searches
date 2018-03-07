import webbrowser
import time
import random
searches = ["rhino foods", "rhino foods stock", "rhino foods revenue", "rhino foods value", "rhino foods news"]

while (1):
    search = searches[random.randrange(0,4)]
    webbrowser.open('https://www.google.com/search?ei=bjefWvvAHMzLjwSMyrbgBA&q=' + search + '&oq=' + search)
    time.sleep(1)
