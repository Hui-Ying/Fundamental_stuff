# String
# Q1: return a dictionary for the times of the use of words.
import collections
from collections import Counter
from statistics import mode

filename = "Macbeth.txt"

with open(filename) as f:
    contents = f.read()
    num_of_words = collections.Counter(contents.split())
    dict_items = num_of_words.keys()
    first_four = list(dict_items)[0:4] 
    
    
    split_it = contents.split()
    Counter = Counter(split_it)
    most_occur = Counter.most_common(4)
    print(most_occur)
    
# Q2: find the total times "Macbeth" shows in the file.
def count_words(word, list_name):
    num_of_word = 0 
    for i in num_of_words:
        if word in i:
            num_of_word += num_of_words[i]
    return num_of_word 
print(count_words("Macbeth", num_of_words))
        

# Q3: Count the time of the lines that appear "Macbeth"
with open(filename) as f:
   lines = f.readlines()
   print(len([line for line in lines if "Macbeth" in line]))

# Q4: find the time of the line that appear both "Banquo" and "Macbeth"
with open(filename) as f:
   lines = f.readlines()
   print(len([line for line in lines if "Macbeth" in line and "Banquo" in line]))
   