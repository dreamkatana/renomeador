# Python 3 code to rename multiple
# files in a directory or folder

# importing os module
import os

# Function to rename multiple files
def main():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    folder = "."
    for count, filename in enumerate(os.listdir(folder)):
        #dst = f"{filename.split('.')[0]}_{str(count)}.jpg"
        src =f"{folder}/{filename}"  # foldername/filename, if .py file is outside folder
        #dst =f"{folder}/{dst}"
        if filename.endswith("~"):
            #get the alphabet based on the count done by --backup=numbered command
            letter = alphabet[int(filename.split('~')[1])-1]          
            dst = f"{filename.split('.')[0]}{letter}.{filename.split('.')[1]}"
            dst =f"{folder}/{dst}"
            print (f"numero: {str(count)} - {src} -> {dst}")
            # rename() function will
            # rename all the files
            os.rename(src, dst)

# Driver Code
if __name__ == '__main__':

    # Calling main() function
    main()
