import pickle

print('pickle')

memory = ['Hello', 'files', '!!']
file = open('fileTest.txt', 'wb')
pickle.dump(memory, file)
file.close()

file = open('fileTest.txt', 'rb')
fileMemory = pickle.load(file)
file.close()
print(fileMemory)

