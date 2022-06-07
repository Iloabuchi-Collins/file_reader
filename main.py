# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

# author: Iloabuchi Collins
# I4G-ZURI scholarship task
import re  #i need it to split my text in the count function

def read_file_content(filename):
    with open(filename) as file:
        content = file.read()
    return f"{str(content)}"


def count_words():
    text = read_file_content("./story.txt")
    text = re.split(' |\?|\n|\.|,',text) #i did not use .split() because i want to split all punctuations to avoid things like 'word, :count'
    count = {}
    for word in text:
            if word != "":  #prevents my code from counting space as a word
                if word in count.keys():
                    count[word] += 1
                else:
                    count[word] = 1
    return count

count = count_words()    
print(count)

