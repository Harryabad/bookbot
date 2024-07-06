path = "books/frankenstein.txt"

def main():
    with open(path) as f:
        file_contents = f.read()
        #print(file_contents)
    return file_contents

def word_count(file_contents):
    words = file_contents.split()
    count = len(words)
    print(f"{count} words in this book \n")

def character_count(file_contents):
    letter_count = {}
    words = file_contents.split()
    for word in words:
        for letter in word:
            if letter.isalpha():
                letter = letter.lower()
                if letter in letter_count:
                    letter_count[letter] += 1
                else:
                    letter_count[letter] = 1
    return letter_count

def sort_on(letter_count):
    return letter_count["count"]

def convert_to_list_of_dicts(counts):
    list_of_dicts = [{"character": char, "count": count} for char, count in counts.items()]
    return list_of_dicts

if __name__ == "__main__":
    print(f"--- Begin report of {path} ---")
    file_contents = main()
    letter_count = character_count(file_contents)
    dicts = convert_to_list_of_dicts(letter_count)
    word_count(file_contents)
    #print(character_count(file_contents), "\n")
    dicts.sort(reverse=True, key=sort_on)
    for i in dicts:
        print(f"The '{i['character']}' character was found {i['count']} times", end=" ")
        print()
    print("--- End report ---")