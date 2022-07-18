from googletrans import Translator
import pandas as pd
# opening the file in read mode
my_file = open("list.txt", "r")
# reading the file
data = my_file.read()
# replacing end of line('/n') with ' ' and
# splitting the text it further when '.' is seen.
english_word_list = data.replace('\n', '  ').split("  ")
my_file.close()
print(english_word_list)