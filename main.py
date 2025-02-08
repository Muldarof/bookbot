def main():
    path_to_file = "books/frankenstein.txt"
    with open(path_to_file) as f:
        file_contents = f.read()
        #print(file_contents)
        #print(word_count(file_contents))
        count = character_counter(file_contents)
        print(f"{count}")

def word_count(input):
    words = input.split()
    length = len(words)
    return length

def character_counter(input_string):
    result = {}
    for char in input_string:
        char = char.lower()
        if char in result:
            result[char] = result[char] + 1
        else:
            result[char] = 1
    return result

main()
