import string
import re
import unicodedata
from unicodedata import normalize
import nltk
from nltk.tokenize import word_tokenize
from pickle import dump, load

#function to read text file
def get_text(file):
#load in the file
    with open(file, mode="rt", encoding="utf-8") as f:
#read the file
        data = f.read() 
#return text from file
        return data

def to_pairs(txt):   
    lines = txt.strip().split('\n')
    pairs = [pairs.split('\t') for pairs in lines]

    return pairs

def max_min_length(pairs):    
    for sentence in pairs:
        length = [len(s.split()) for s in sentence]
    return min(length), max(length)

def what_type(pairs):
    for sentence in pairs:
        dt = [type(s) for s in sentence]
    return dt

def split_line(line):
    line = line.split()
    return line 

def remove_punct(line):    
    table = str.maketrans("", "", string.punctuation)
    line = [word.translate(table) for word in line]
    return line

def norma_uni(line):
    line = normalize("NFD", line).encode("ascii", "ignore")
    line = line.decode('UTF-8')
    return line

def lower_case(line):
    line = [word.lower() for word in line]
    return line

def non_print(line):
    re_print = re.compile("[^%s]" % re.escape(string.printable))
    line = [re_print.sub("", word) for word in line]
    return line

def clean_txt(lines):
    cleaned = []
    for pair in lines:
        clean_pair = []
        for line in pair:
            line = norma_uni(line)
            line = split_line(line)
            line = lower_case(line)
            line = remove_punct(line)
            line = non_print(line)
            clean_pair.append(" ".join(line))
        cleaned.append(clean_pair)
    return cleaned

def save_words(clean_txt, filename):
    dump(clean_txt, open(filename, 'wb'))


def load_clean(filename):
    data = load(open(filename, 'rb'))
    return data

if __name__ == "__main__":

    text = get_text('../datasets/external/fra1.txt')
    pairs = to_pairs(text)
    min_max = max_min_length(pairs)
    type = what_type(pairs)
    clean = clean_txt(pairs)
    # clean_data = save_words(clean, 'engl-fra.pickle')