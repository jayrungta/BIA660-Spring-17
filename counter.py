"""
Author: Jay Rungta
Word Counter
- Create a new script named counter.py 

- The script should include a single function run().

- The run() function should accept as input the path to an input file with the same structure as 'textfile'

- The run() function should return the most frequent word in the input file.

- Submit your script through Canvas.

"""
#define a new function
def run(path):
    freq={} # new dictionary. Maps each word to each frequency 

    fin=open(path) # open a connection to the file 
    for line in fin: # read the file line by line 
        # lower() converts all the letters in the string to lower-case
        # strip() removes blank space from the start and end of the string
        # split(c) splits the string on the character c and returns a list of the pieces. For example, "A1B1C1D".split('1')" returns [A,B,C,D]  
        words=line.lower().strip().split(' ')
       
        # use for to go over all the words in the list 
        for word in words: # for each word in the line
            if word in freq:
                freq[word]=freq[word] + 1 # if the word is already in the dictionary increase its count by 1
            else:
                freq[word] = 1 # if it is not in dictionary set its count to 1
    fin.close() # close the connection to the text file 
    
    values=list(freq.values()) # storing all values (word counts) of dictionary 'freq'
    keys=list(freq.keys()) # storing all keys (words) of dictionary 'freq'
    return keys[values.index(max(values))] # returning the word with max word count

# use the function 
print(run('textfile.txt'))
