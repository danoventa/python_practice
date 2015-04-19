#write to a file
writeMe = 'Example text'

saveFile = open('exampleWrite.txt', 'w')
saveFile.write(writeMe)
saveFile.close()

#append to a file
appendMe = 'Some more Text'

saveFile = open('exampleFile.txt', 'a')
saveFile.write(appendMe)
saveFile.close()

readMe = open('exampleFile.txt', 'r').read()
print(readMe)

splitMe = readMe.split('\n')
print(splitMe)

readMe2 = open('exampleFile.txt', 'r').readlines()
print(readMe2)