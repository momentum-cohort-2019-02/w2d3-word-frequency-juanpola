

import re
import string

STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'format', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]


frequency = {}
document = open('seneca_falls.txt', 'r')
# opening the seneca_falls.txt and 'r' reads the file, also asigning the file to a variable.
text_string = document.read().lower()
# creating a new variable to to asign the document value to it, the .read() reads the file and the .lower() makes the words in the
# in the document.
find_word = re.findall(r'\b[a-z]{3,15}\b', text_string)
# filtering out the words in the text_string variable

# word_filter = []
# for words in STOP_WORDS:
#     if words =! '' and
stop = []
for itmes in STOP_WORDS:
    if itmes != '' and find_word not in STOP_WORDS:
        stop.append(stop)
        # print(words)
        # return words
    # down below this is going to count every word in the Seneca_falls.txt and filter out the STOP WORDS!
for word in find_word:
    count = frequency.get(word, 0)
    frequency[word] = count + 1
frequency_list = frequency.keys()

for words in frequency_list:
    print words, frequency[words]


# import string
# import re
# STOP_WORDS = [
#     'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
#     'i', 'in', 'is','format', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
#     'will', 'with'
# ]

# frequency = {}
# document= open('seneca_falls.txt', 'r')
# text_string = seneca_falls.txt().lower()
# text_word = re.findall(r'\b[a-z]{3,15}\b', text_string)

# for word in text_word:
#     count = frequency.get(word, 0) not in STOP_WORDS
#     frequency[word] = count + 1

# frequency_list = frequency.keys()

# for words in frequency_list:
#     print words, frequency[words]


# # def print_word_freq(file):
# #     """Read in `file` and print out the frequency of words in that file."""
# #     pass


# # if __name__ == "__main__":
# #     import argparse
# #     from pathlib import Path

# #     parser = argparse.ArgumentParser(
# #         description='Get the word frequency in a text file.')
# #     parser.add_argument('file', help='file to read')
# #     args = parser.parse_args()

# #     file = Path(args.file)
# #     if file.is_file():
# #         print_word_freq(file)
# #     else:
# #         print(f"{file} does not exist!")

# #         exit(1)
