import os

dir = 'C:\\Users\\Arthurzinho\\Documents'

for root, dirs, filenames in os.walk(dir):
    for file in filenames:
        print(os.path.join(root, file))