import string
import re
import unicodedata
from unicodedata import normalize
from pickle import dump
from pickle import load
import numpy as np
from numpy.random import rand
from numpy.random import shuffle

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
    with open(filename, 'wb') as f:
        dump(clean_txt, f)


def load_clean(filename):
    with open(filename, 'rb') as f:
        data = load(f)
    return data

def reduce_size(raw_data):
    num_sentences = 15000
    data = raw_data[0:num_sentences]
    data = np.array(data)
    return data

def shuffle_rand(data):
    return shuffle(data)

def create_train(data):
    return data[:12000]

def create_test(data):
    return data[12000:]


if __name__ == "__main__":

    text = get_text('../datasets/external/fra1.txt')
    pairs = to_pairs(text)
    min_max = max_min_length(pairs)
    type = what_type(pairs)
    clean = clean_txt(pairs)
    # clean_data = save_words(clean, 'engl-fra.pickle')
    raw_data = load_clean('../datasets/interim/engl-fra.pickle')
    small_data = reduce_size(raw_data)
    train = create_train(small_data)
    test = create_test(small_data)
    # small_save  = save_words(small_data, 'eng-fra-both.pickle')
    save_train = save_words(train, 'eng-fra-train.pickle')
    save_test = save_words(test, 'eng-fra-test.pickle')