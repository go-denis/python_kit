colors = ['red', 'green', 'blue']

data = open('text.txt', 'a')
data.writelines(colors)
data.close()

# Либо так:
# with open('text.txt', 'w') as data:
#     data.write('line 1\n')
#     data.write('line 2\n')

# print(56)