
# 1
list1 = [1, 2, 3, 4, 5, 6, 7]
list_even = []
list_odd = []
for item in list1:
    if item % 2 == 0:
        list_even.append(item)
    else:
        list_odd.append(item)
print(list_even)
print(list_odd)

# 2
list1 = ["HELLO", "World", "PYTHON", "code", "TEST"]
upper_list = []
for item in list1:
    if item.isupper():
        upper_list.append(item)
print(upper_list)

# 3
list1 = ["Hello", "world", "Python", "java", "Code"]
title_list = []
for item in list1:
    if item.istitle():
        title_list.append(item)
print(title_list)

# 4
sentences = [
    "Hello world",
    "Python is fun",
    "I love coding"
]
words_list = []
for item in sentences:
    item.split()
    words_list.extend(item.split())
print(words_list)

# 5
list1 = ["HELLO", "World", "PYTHON", "code"]
new_list = []
for item in list1:
    if item.isupper():
        new_list.append(item[::-1])
    else:
        new_list.append(item)
print(new_list)


