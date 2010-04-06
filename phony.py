# phony.py - generates lists of words that can be made using 
#            a touchtone phone using the same numbers
#
# Austin G. Davis-Richardson
#   harekrishna@gmail.com

from itertools import *
import sys

MAX = 1000000
MAX_LENGTH = 8
try:
    DICTIONARY = sys.argv[1]
except:
    DICTIONARY = '/usr/share/dict/words' 

def main():
    words = load_dictionary()
    dialpad = {
        '0': (),
        '1': (),
        '2': ('a','b','c'),
        '3': ('d','e','f'),
        '4': ('g','h','i'),
        '5': ('j','k','l'),
        '6': ('m','n','o'),
        '7': ('p','q','r','s'),
        '8': ('t','u','v'),
        '9': ('w','x','y','z')
    }
    

    for i in range(999, MAX):
        numbers = str(i)
        digits = dialpad.keys()
        hits = [ word for word in make_words(numbers, words, digits, dialpad) ] 
        if len(hits)>10:
            print '%s: %s' % (numbers, ' '.join(hits))


def make_words(numbers, words, digits, dialpad):
    letters = [ dialpad[num] for num in numbers ]
    for n in product(*letters):
        word = ''.join(n)
        if word in words:
            yield word
            

def load_dictionary():  
    words = []
    try:
        h_words = open(DICTIONARY, 'r')
    except:
        raise IOError
    finally:
        for line in h_words:
            words.append(line.strip().lower())
        h_words.close()
    return set(words)   
    

if __name__ == '__main__':
    main()