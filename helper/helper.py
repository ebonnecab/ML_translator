import string
import re
import unicodedata
from unicodedata import normalize
import nltk
from nltk.tokenize import word_tokenize

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
    line = normalize('NFD', line).encode('ascii', 'ignore')
    line = line.decode('UTF-8')
    return line

def lower_case(line):
    line = [word.lower() for word in line]
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
            clean_pair.append(" ".join(line))
        cleaned.append(clean_pair)
    return cleaned

if __name__ == "__main__":
    
    #previewing file
    text = get_text('../datasets/external/fra1.txt')
    #print total count of sequences
    print(text.count('') +1)
    #print first few lines of text
    # print(text[1:2000])
    #print last few lines of text
    # print(text[490000:500000])
    pairs = to_pairs(text)
    # print(pairs[0:50])
    # min_max = max_min_length(pairs)
    # print(min_max)
    type = what_type(pairs)
    print(type)

    strip = clean_txt(pairs)
    print(strip[0:50])
    # print(all_words)