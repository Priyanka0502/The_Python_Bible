'''
pig-latin: It is a simple joke language. It's imaginary thst makes regular words hard
to understand.
pig-> igpay (for consonants->> remove  consonant cluster:put it at the end:and then add ay:::: 'p' -> ig-p-ay )
priyanka-> iyankapray
apple->appleyay   (for vowels ->> just add yay at the end)

We will ask a user for a sentence and then convert entire sentence to pig-latin!!
steps:
1. get sentence from user
2. split sentence into words
3. loop through words and convert to pig latin
    3.1 if words start with vowel,add "yay" at the end
    3.2 else , move the first consonant cluster to end, and add "ay"
4. stick words back together
5. output the final string
'''

user_sentence=input("Enter the sentence you wanna convert!!").strip().lower()
word_list=user_sentence.split()
print(word_list)

new_words=[]
for word in word_list:
    if word[0] in "aeiou":
        word_vowel=word+'yay'
        new_words.append(word_vowel)
    else:
        vowel_pos=0
        for letter in word:
            if letter not in 'aeiou': # we will assume that the vowel is coming next
                vowel_pos=vowel_pos+1
            else:
                break
        cons=word[:vowel_pos]
        the_rest=word[vowel_pos:]
        new_word=the_rest+cons+'ay'
        new_words.append(new_word)

#stick words together
output=" ".join(new_words)
print(output)


