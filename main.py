def main():
    word_count = wordcounter()
    letter_count = lettercounter()
    sorted_letter_list = sort_letters(letter_count)
    createreport(word_count, sorted_letter_list)
def printbook():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    print(file_contents)
def wordcounter():    
    with open("books/frankenstein.txt") as f:
        words = f.read().split()
    number_of_words = (len(words))
    return number_of_words
def lettercounter():
    with open("books/frankenstein.txt") as f:
        letters = f.read()
        letters_lowered = letters.lower()
        all_letters = {}
        for letter in letters_lowered:
            if letter not in all_letters:
                all_letters[letter] = 1
            else:
                all_letters[letter] +=1
    return(all_letters)
def sort_on(all_letters):
    return all_letters["num"]
def sort_letters(all_letters):
    sorted_letters = []
    for letter, count in all_letters.items():
        if letter.isalpha():
            sorted_letters.append({"letter": letter, "num": count})
    sorted_letters.sort(key=sort_on, reverse=True)
    return sorted_letters
    
def createreport(word_count, sorted_letter_list):
    print(" --- Begin report of books/frankenstein.txt ---")
    print(word_count, " words found in the document")
    for letter_dict in sorted_letter_list:
        letter = letter_dict['letter']
        count = letter_dict['num']
        print(f"The '{letter}' character was found {count} times")
    print(" --- End of report --- ")
    
        
        
main()