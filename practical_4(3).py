"""
Write a program that inputs a text file. The program should print the unique words in the 
file in alphabetical order
"""
text_file = open('text.txt', 'r')
text = text_file.read()
text = text.lower()
words = text.split()
words = [word.strip('.,!;()[]') for word in words]
unique = []
for word in words:
    if word not in unique:
        unique.append(word)
unique.sort()
print(unique)
