from function import load_clean
import keras
from keras.preprocessing.text import Tokenizer

#tokenize text
def tokenize_words(lines):
    tokenizer = keras.preprocessing.text.Tokenizer(filters=" ")
    tokenizer.fit_on_texts(lines)
    return tokenizer

def max_len(lines):
    return max(len(line.split()) for line in lines)
if __name__ == "__main__":
    data = load_clean('../datasets/processed/eng-fra-both.pickle')
    train = load_clean('../datasets/processed/eng-fra-train.pickle')
    test = load_clean('../datasets/processed/eng-fra-test.pickle')

    engl_tokens = tokenize_words(data[:, 0])
    

