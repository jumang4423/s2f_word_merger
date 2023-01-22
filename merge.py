import sys
import re
import os
import json
from os.path import exists

def main():
    # get args
    original_word_dict_filepath = sys.argv[1]
    metadata_jsonl_filepath = sys.argv[2]

    # dict and each word has array of string word
    original_word_dict = {}
    # array<{ image_file_path: string, text: string }>
    metadata_jsonl = []


    # if original_word_dict_filepath is empty, create a new word dict
    if not exists(original_word_dict_filepath):
        with open(original_word_dict_filepath, 'w') as f:
            json.dump({}, f)

    # load original word dict, with read, write
    with open(original_word_dict_filepath, 'r+') as f:
        original_word_dict = json.load(f)

    # load metadata jsonl, with read
    with open(metadata_jsonl_filepath, 'r') as f:
        for line in f:
            metadata_jsonl.append(json.loads(line))


    # merge
    for metadata in metadata_jsonl:
        # translate "cute ambient, shiny, future" into ["cute", "ambient", "shiny", "future"]
        # and remove duplicates
        words = list(set(re.split(r'\W+', metadata['text'])))
        for index, word in enumerate(words):
            if word == '':
                continue
            if word not in original_word_dict:
                original_word_dict[word] = []
            if index < len(words) - 1 and word != "":
                original_word_dict[word].append(words[index + 1])
            if index > 0 and word != "":
                original_word_dict[word].append(words[index - 1])

            # remove duplicates
            original_word_dict[word] = list(set(original_word_dict[word]))

    # write to original word dict
    with open(original_word_dict_filepath, 'w') as f:
        json.dump(original_word_dict, f)


if __name__ == '__main__':
    main()
