# -*- coding: UTF-8 -*-
"""PyParagraph Homework Solution."""

# Incorporate regular expressions (helpful for splitting by punctuation)
import re
import os

# Files to load and output (Remember to change these)
file_to_load = os.path.join("raw_data", "paragraph_1.txt")
file_to_output = os.path.join("analysis", "paragraph_analysis.txt")

# String variable to hold the paragraph contents
paragraph = ""

# Read the text file
with open(file_to_load) as txt_data:

    # Store the contents as a string (with no new lines)
    paragraph = txt_data.read().replace("\n", " ")

# Split the paragraph based on spaces to calculate word count
word_split = paragraph.split(" ")
print(word_split)
word_count = len(word_split)

# Create a list for holding all the letter counts
letter_counts = []

# Loop through the word array and calculate the length of each word
for word in word_split:

    # Add each letter count into the letter_counts list
    letter_counts.append(len(word))

# Calculate the avg letter count
avg_letter_count = round(sum(letter_counts) / float(len(letter_counts)))

# Re-split the original paragraph based on punctuation (. ? !)
sentence_split = re.split("(?<=[.!?]) +", paragraph)
print(sentence_split)
sentence_count = len(sentence_split)

words_per_sentence = []

# Loop through the sentence array and calculate the number of words in each
for sentence in sentence_split:

    # Calculate the number of words in each sentence and add to the list
    #by splitting up each sentence into a list of its words
    sentence_word_split = sentence.split(" ")
    
    #counting the length of the list
    sentence_word_count = len(sentence_word_split)
   
    #add that value to the list
    words_per_sentence.append(sentence_word_count)
    
# Calculate the avg word count (per sentence)
mean_word_count = sum(words_per_sentence)/sentence_count
    
# Generate Paragraph Analysis Output
'''sample
Paragraph Analysis
-----------------
Approximate Word Count: 122
Approximate Sentence Count: 5
Average Letter Count: 4.6
Average Sentence Length: 24.0
'''

# Print all of the results (to terminal)
print(f'''
      Paragrph Analysis\n
      ----------\n 
      Aproximate Word Count: {word_count}\n
      Approximate Sentence Count: {sentence_count}\n
      Average Letter Count: {avg_letter_count}\n
      Average Sentence Length: {mean_word_count}''')
    
# Save the results to analysis text file
with open(file_to_output, "w", newline = '') as txt_file:
    file = open(file_to_output, "a")
    file.write(f'''
      Paragrph Analysis\n
      ----------\n 
      Aproximate Word Count: {word_count}\n
      Approximate Sentence Count: {sentence_count}\n
      Average Letter Count: {avg_letter_count}\n
      Average Sentence Length: {mean_word_count}''')
    file.close()