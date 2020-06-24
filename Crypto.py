import pyAesCrypt
import base64
# encryption/decryption buffer size - 64K
bufferSize = 64 * 1024

def crypto():
    print("1.Encrypt\n2.Decrypt\n3.Encode a string\n4.Decode a string\n5.Exit")

    choice = input("Select your choice:")

    #encrypt a file
    if choice == '1':
        file1 = input("Enter file path of the file to encrypt:")
        file2 = input("Enter new file path of a file:")
        password = input("Enter password:")
        pyAesCrypt.encryptFile(file1, file2, password, bufferSize)
        print("Encrypted")

    #decrypt a file
    elif choice == '2':
        file1 = input("Enter file path of the file to decrypt:")
        file2 = input("Enter new file path of a file:")
        password = input("Enter password:")
        pyAesCrypt.decryptFile(file1,file2,password,bufferSize)
        print("Decrypted")

    #encode a string
    elif choice == '3':
        message = input("Enter a string: ")
        message_bytes = message.encode('ascii')
        base64_bytes = base64.b64encode(message_bytes)
        base64_message = base64_bytes.decode('ascii')

        print(base64_message)
        def value():
            option = input("Do you want to save it in a file (y/n): ")
            if option == 'y' or option == 'Y':
                File = input("Enter the file with its path: ")
                File1 = open(File,'a')
                File1.write(base64_message)
                File1.close()
                print("File saved successfully")
            elif option == 'n' or option == 'N':
                pass
            else:
                value()
        value()

    #decode a string
    elif choice == '4':
        base64_message = input("Enter the value: ")
        base64_bytes = base64_message.encode('ascii')
        message_bytes = base64.b64decode(base64_bytes)
        message = message_bytes.decode('ascii')

        print(message)

    #To exit the script
    elif choice == '5':
        exit()

    else:
        print("wrong input.Please try again\n")
        #if user selects wrong option we need to run the script until user selects correct option
        crypto() #to call the script again

#calling the function crypto to run the scirpt
crypto()

