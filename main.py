# Read text from a file, and count the occurrence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here 
    with open(filename) as file:
        file_content = file.read()
    return file_content


def count_words():
    text = read_file_content("./story.txt").lower()
    # [assignment] Add your code here
    # Formatting text
    special_chars = '?,.'
    for char in special_chars:
        text = text.replace(char, "")
    text = text.replace("\n", " ")

    words = text.split(" ")
    word_count = {}
    for word in words:
        if word in word_count.keys():
            count = word.count(word)
            word_count[word] += count
        else:
            word_count[word] = word.count(word)
    return word_count


print(count_words())
