path = r'D:\OneDrive\Desktop\Python_Projects\Pixel Manipulation Encrypt_decrypt\Photos\night-camp-forest-tents-campfire-600nw-2304185023.jpg'

key = int(input('Enter Key for encryption of image : '))

print('The path of file: ',path)
print('key for encryption : ',key)

fin = open(path,'rb')

image = fin.read()
fin.close()

image = bytearray(image)

for index, values in enumerate(image):
    image[index] = values ^ key


fin = open(path, 'wb')

fin.write(image)
fin.close()
print('Encryption done...')