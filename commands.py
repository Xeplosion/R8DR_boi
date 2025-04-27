import os
import random

def get_random_verse(input_path):
    verses = []
    with open("./verses.txt", 'r', encoding='utf-8') as f:
        for line in f:
            verses.append(line)

    return random.choice(verses)