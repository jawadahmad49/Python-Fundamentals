# Python has functions for creating, reading , Updating and deleting files

# open a file

myFile = open('myfile.txt', 'w')

# Get some info

print('Name: ', myFile.name)
print('isClosed: ', myFile.closed)
print('Opening Mode: ', myFile.mode)

# Write to file

myFile.write('I love Python')

myFile.write(' and JavaScript')

myFile.close()

# Append to file
myFile = open('myfile.txt', 'a')
myFile.write(' I also like PHP')
myFile.close()

# Read from file
myFile = open('myfile.txt', 'r+')
text = myFile.read(100)

print(text)