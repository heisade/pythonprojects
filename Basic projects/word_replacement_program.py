# For the sentence the user wants to input
user_sentence = input("Enter sentence: ")
print(user_sentence)

# For the old word the user replace
old_word = input("Enter word to replace: ")

# The new word
new_word = input("Enter new word: ")

if old_word in user_sentence:
    new_sentence = user_sentence.replace(old_word, new_word)
    
print(new_sentence)



