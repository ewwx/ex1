import argparse
import math

parser = argparse.ArgumentParser()
parser.add_argument("-l", "--lines", action="store_true",  help="number of lines")
parser.add_argument("-m", "--chars", action="store_true",  help="number of characters")
parser.add_argument("-w", "--words", action="store_true",  help="number of words")
parser.add_argument("name", type=str,  help="give the name of the text file")
args = parser.parse_args()
if args.chars :
    print('c')
elif args.lines :
    print('l')
elif args.words :
    print('w')
print(args.name)


