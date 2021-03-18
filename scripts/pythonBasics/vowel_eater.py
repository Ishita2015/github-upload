# Prompt the user to enter a word
user_word = input("Enter word: ")
# and assign it to the user_word variable.
user_word = user_word.upper()
vowel_eater = ['A', 'E', 'I', 'O', 'U']
word_without_vowels = ''
for letter in user_word:
    # Complete the body of the for loop.
    if letter in vowel_eater:
        continue
    word_without_vowels += letter
print(word_without_vowels)
