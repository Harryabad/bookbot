
def main():
    path = "books/frankenstein.txt"
    book_text = read_book(path)
    num_words = word_count(book_text)
    character_dictionary = character_count(book_text)
    characters_sorted = character_dict(character_dictionary)

    print(f"--- Begin report of {path} ---")
    print(f"{num_words} words was found in {path} \n")

    for i in characters_sorted:
        print(f"The '{i['character']}' character was found {i['count']} times", end=" ")
        print()
    print("--- End report ---")



def word_count(file_contents):
    words = file_contents.split()
    count = len(words)
    return count

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

def character_dict(counts):
    list_of_dicts = [{"character": char, "count": count} for char, count in counts.items()]
    list_of_dicts.sort(reverse=True, key=sort_on)
    return list_of_dicts

def read_book(path):
    with open(path) as f:
        return f.read()
    
if __name__ == "__main__":
    main()