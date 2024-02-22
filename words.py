def print_upper_words(words, starting_letters):
    """Prints each word in a list on a separate line and in upper case"""

    for word in words:
        first_letter = word[0]
        if first_letter in set(starting_letters):
            print(word.upper())

print_upper_words(['hello', 'hey', 'goodbye', 'eeeo', 'yes'], ['g'])