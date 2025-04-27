import os
import random

def get_random_verse(input_path):
    verses = []
    with open("./verses.txt", 'r', encoding='utf-8') as f:
        for line in f:
            verses.append(line)

    return random.choice(verses)

def load_info(filepath):
    info = {}
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            if "=" in line:
                key, value = line.strip().split("=", 1)
                info[key] = value
    
    return info
 