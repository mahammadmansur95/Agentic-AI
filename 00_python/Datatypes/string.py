name = 'mansur'

#accessing elements
print(name[0])
print(name[-1]) #last element
print(name[0:2]) # slicing elements
print(len(name)) #length

print('Chat' in 'ChatGPT')
print('Claude' not in 'ChatGPT')  

#string formating
company = 'Google'
field = 'AI'

message = f'{company} is an {field} company.'
print(message)

#methods
sentence = "i love PYTHON"
capitalized_string = sentence.capitalize()
print("capitalized" + capitalized_string)
centered = sentence.center(16, "$")
print("centered", centered)
casefold = sentence.casefold() #similar to lower()
print('casefold', casefold)
count = sentence.count('O', 0, -1) #returns num of occurence of substring in a given string 
#string.count(substring, start=..., end=...)
print("count", count)
print("endsWith fun :",sentence.endswith('fun'))
print("startsWith fun :", sentence.startswith('fun'))

#The find() method returns the index of first occurrence of the substring (if found). 
# If not found, it returns -1.
print("find method : ",sentence.find('me'))

#The index() method returns the index of a substring inside the string (if found). 
# If the substring is not found, it raises an exception.
result = sentence.index('is')
print(result)


#The string join() method returns a string by joining all the elements 
# of an iterable (list, string, tuple), separated by the given separator.
text = ['Python', 'is', 'a', 'fun', 'programming', 'language']
# join elements of text with space
print(' '.join(text))

#The replace() method replaces each matching occurrence of a substring with another string.
replaced_text = sentence.replace('i', 'You')
print(replaced_text)

#The split() method breaks down a string into a list of substrings using a chosen separator.
print(sentence.split())

