# 8.  Word Frequency Counter   
#    *Description*: Analyze a text file to count the frequency of each word.  
#    *Skills*: File handling, dictionaries, string manipulation.

import string

def frequency_word_counter(file_path):
    word_frequency={}
    
    with open(file_path,'r') as file:
        contents = file.read()
        # return contents
    
    translation = str.maketrans('','',string.punctuation)
    contents_normalization = contents.translate(translation)
    
    # print(contents_normalization)
    
    words_list=contents_normalization.split()
    print(words_list)
    
    for word in words_list:
        if word in word_frequency:
            word_frequency[word]+=1
        else:
            word_frequency[word]=1
    return word_frequency


words=frequency_word_counter("words.txt")

for word,count in words.items():
    print(f"{word} : {count}")

