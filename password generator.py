#https://xkcd.com/936/

import random

#maybe use an nltk corpus instead and filter common words
words = ['the', 'and', 'for', 'are', 'but', 'not', 'all', 'any', 'can', 'had', 'was', 'one', 'out', 'day', 'get', 'has', 'how', 'new', 'now', 'old', 'see', 'two', 'way', 'who', 'did', 'its', 'let', 'put', 'say', 'too', 'use'
         'that', 'with', 'have', 'this', 'will', 'your', 'from', 'they', 'know', 'want', 'been', 'good', 'much', 'some', 'time', 'very', 'when', 'come', 'here', 'just', 'like', 'long', 'make', 'many', 'more', 'only', 'over', 'such', 'take', 'than', 'them', 'well', 'were'
           	'today', 'about', 'after', 'other', 'being', 'first', 'great', 'found', 'people', 'still', 'under', 'while', 'years', 'before', 'large']


#shoulda used import string, whatever
allcharsnonpunct = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowercase = 'abcdefghijklmnopqrstuvwxyz'
uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbe = '1234567890'
punct = '!@#?'

numberofletters = 8
numberofpasswords = 8


def makerandompassword(numberofletters, numberofpasswords):
    for each in range(numberofpasswords):
        password = ''
        #make passwords with the format similar to 7?ZYz7nOkr - number, punctuation, then a bunch of letters 
        password += numbe[random.randrange(0,len(numbe))]
        password += punct[random.randrange(0,len(punct))]
        for each in range(numberofletters):
            password += lowercase[random.randrange(0,len(lowercase))]
        print password
makerandompassword(numberofletters,numberofpasswords)

print '\n'


wordstogenerate = 4

def xkcdpassword(wordstogenerate, numberofpasswords):
    for each in range(numberofpasswords):
        password2 = ''
        for each in range(wordstogenerate):
            password2 += words[random.randrange(0,len(words))]
        print password2

xkcdpassword(wordstogenerate, numberofpasswords)
