import argparse
import math
import re
import time

start = time.clock();
def count_lines():
    n_of_l = sum(1 for line in open(args.name))
    return n_of_l


def count_words():
    n_of_w = 0
    for line in open(args.name):
        w = re.findall(r'\S+', line)
        n_of_w = n_of_w + len(w)
    return n_of_w


def count_chars():
    n_of_c = 0
    for line in open(args.name):
        c = re.findall('\S', line)
        n_of_c = n_of_c + len(c)
    return n_of_c


parser = argparse.ArgumentParser()
parser.add_argument("-l", "--lines", action="store_true", help="number of lines in specified text file")
parser.add_argument("-m", "--chars", action="store_true", help="number of characters in specified text file")
parser.add_argument("-w", "--words", action="store_true", help="number of words in specified text file")
parser.add_argument("name", type=str, help="give the name of the text file")
args = parser.parse_args()
if args.chars:
    print(count_chars())
elif args.lines:
    print(count_lines())
elif args.words:
    print(count_words())
print(args.name)
start2 = time.clock();
print(start2-start)