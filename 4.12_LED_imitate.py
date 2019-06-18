import time
start1 = time.time()

numbers = [
    ['###', '#', '###', '###', '# #', '###', '###', '###', '###', '###'],
    ['# #', '#', '  #', '  #', '# #', '#  ', '#  ', '  #', '# #', '# #'],
    ['# #', '#', '###', '###', '###', '###', '###', '  #', '###', '###'],
    ['# #', '#', '#  ', '  #', '  #', '  #', '# #', '  #', '# #', '  #'],
    ['###', '#', '###', '###', '  #', '###', '###', '  #', '###', '###']
]
separator = ' '
result = [];
str1 = '1234567890123456789012345678901234567890'
# str1 = input()

for i in range(5):
    result_line = separator
    for ch in (str1):
        result_line += numbers[i][int(ch)] + separator
    result.append(result_line)
# print result
for i in range(5):
    print(result[i])

end1 = time.time()

print('')

start2 = time.time()

numbers = {
    0: {'1': '#', '2': '###', '3': '###', '4': '# #', '5': '###', '6': '###', '7': '###', '8': '###', '9': '###', '0': '###'},
    1: {'1': '#', '2': '  #', '3': '  #', '4': '# #', '5': '#  ', '6': '#  ', '7': '  #', '8': '# #', '9': '# #', '0': '# #'},
    2: {'1': '#', '2': '###', '3': '###', '4': '###', '5': '###', '6': '###', '7': '  #', '8': '###', '9': '###', '0': '# #'},
    3: {'1': '#', '2': '#  ', '3': '  #', '4': '  #', '5': '  #', '6': '# #', '7': '  #', '8': '# #', '9': '  #', '0': '# #'},
    4: {'1': '#', '2': '###', '3': '###', '4': '  #', '5': '###', '6': '###', '7': '  #', '8': '###', '9': '###', '0': '###'}
}
separator = ' '
result = [];
str1 = '1234567890123456789012345678901234567890'
# str1 = input()

for i in range(5):
    result_line = separator
    for ch in (str1):
        result_line += numbers[i][ch] + separator
    result.append(result_line)
# print result
for i in range(5):
    print(result[i])

end2 = time.time()

print(f"ARR : {end1 - start1}")
print(f"DICT: {end2 - start2}")
