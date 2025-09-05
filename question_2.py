paragraph = input("Enter paragraph (max 100 words): ")
words = paragraph.split() #splitting text into individual words
palindromes = []

for word in words:
    cleaned = word.lower().strip('.,!?:;"\'') #strip() is used so that punctuation marks doesn't cause false negatives
    if len(cleaned) > 0 and cleaned == cleaned[::-1]: #slicing is used to reverse the string(word)
        palindromes.append(cleaned)

if palindromes:
    print(' '.join(palindromes)) #joins all palindrome words present in the list into a single string
else:
    print(0) #prints 0 if no palindrome words are found