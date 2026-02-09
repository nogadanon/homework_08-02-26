

# 1
list1 = [1, 3, 5, 1, 7, 9, 2, 2, 8, 5, 10, 5]
list2 = [1, 2, 5]
# Remove all items from list1 that appear in list2
# Print list1 at the end

for item in list2:
    while item in list1:
        list1.remove(item)
print(list1)
print()

# 2
list1 = [1, 2, 9, 88, 0]
list2 = [3, 4, -3]
list3 = [5, 6, 55]
# Create list4 that contains all values from list1, list2, and list3
# Use loops only (no +)

list4 = []
for item in list1:
    list4.append(item)
for item in list2:
    list4.append(item)
for item in list3:
    list4.append(item)
print(list4)
print()

# 3
list1 = [1, 2, 3, 4, 5]
list2 = [2, 4]
# Create a new list that contains items from list1 that do NOT appear in list2

new_list = []
for item in list1:
    if item not in list2:
        new_list.append(item)
print(new_list)
print()

# 4
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 6, 7]
# Create a list with items that appear in both lists No duplicates in the result

new_list = []
for item in list1:
    if item in list2:
        new_list.append(item)
print(new_list)
print()

# 5
list1 = [1, 2, 3, 4, 5, 6, 7]
list2 = [2, 4]
list3 = [5, 6]
# Remove from list1 all items that appear in either list2 or list3 Print list1

for item in list1:
    if item in list2 or item in list3:
        list1.remove(item)
print(list1)
print()

# 6
list1 = [1, 4, 6]
list2 = [2, 5, 7]
# Create list3 that contains all numbers from both lists but keep them sorted
x_list = list1+list2
list3 = []

for i in range(len(x_list)):
    min = x_list[0]
    for item in x_list:
         if item < min:
            min = item
    list3.append(min)
    x_list.remove(min)
print(list3)
print()

# 7
list1 = [1, 2, 3, 4, 5, 2, 2]
list2 = [2, 4]
# Count how many items in list1 appear in list2 Print the count
i = 0
for item in list1:
    if item in list2:
        i += 1
print(f'ther is {i} items in both lists')
print()

# 8
names = ["danny", "moshe", "suzi", "sharon", "avi"]
blacklist = ["moshe", "avi"]
# Remove all blacklisted names from names
for item in names:
    if item in blacklist:
        names.remove(item)
print(names)
print()

# 9
list1 = [1, 2, 3, 4, 5, 6, 7]
# Create:
# list_even → all even numbers
# list_odd → all odd numbers
list_even = []
list_odd = []
for item in list1:
    if item % 2 == 0:
        list_even.append(item)
    else:
        list_odd.append(item)
print(list_even)
print(list_odd)
print()

# 10
list1 = ["HELLO", "World", "PYTHON", "code", "TEST"]
# Create list2
# Copy into list2 only strings that are ALL uppercase
list2 = []
for item in list1:
    if item.isupper():
        list2.append(item)
print(list2)
print()

# 11
# בדיקה לאות ראשונה בלבד ללא title***
list1 = ["Hello", "world", "Python", "java", "Code"]
#Copy to list2 only words that start with uppercase
list2 = []
for item in list1:
    _check = list(item)
    if _check[0].isupper():
        list2.append(item)
print(list2)
print()

# 12 – Split sentence list into words
sentences = [
    "Hello world",
    "Python is fun",
    "I love coding"
]
# Create words list that contains all words. Use split() and loops
list1 = []
for item in sentences:
    list1.extend(item.split())
print(list1)
print()

# 13
# trip spaces and copy non-empty strings
list1 = ["  hello  ", "   ", "python", "  code ", ""]
# Create list2 that contains:
# stripped strings
# ignore empty strings after strip
# hint: use isspace
list2 = []
for item in list1:
    if not item.isspace() and len(item) != 0:
        item = item.strip()
        list2.append(item)
print(list2)
print()

# 14 – Replace letters in all strings
list1 = ["hello", "world", "python"]
# Create list2 where:
# all o letters are replaced with 0
list2 = []
for item in list1:
    item = item.replace("o", "0")
    list2.append(item)
print(list2)
print()

# 15 – Count strings that end with specific word
list1 = ["good morning", "morning sun", "happy morning", "good night"]
# Count how many strings end with "morning"
i = 0
for item in list1:
    if item.endswith("morning"):
        i += 1
print(f'there is {i} strings in the list thet ending with "morning"')
print()

# 16 – Separate numeric strings and text strings
list1 = ["123", "hello", "42", "F114", "python", "007", "A14"]
# Create:
# numbers → numeric strings only
# texts → non-numeric strings
# mixed -> both
_numbers = []
_text = []
mix = []
for item in list1:
    if item.isdigit():
        _numbers.append(item)
    elif item.isalpha():
        _text.append(item)
    else:
        mix.append(item)
print(_numbers)
print(_text)
print(mix)













