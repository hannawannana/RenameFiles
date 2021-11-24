import os

def main ():

    print ("Change the names of files in a folder")
    index = 0
    path = input(str ("Enter diretory path with forward slash: "))
    #path = "C:/Users/ahona/Desktop/Academics/Rename files/"

    for filename in os.listdir(path):

        rename = "Cat Picture" + str(index) + ".jpg"
        mySource = path +filename
        rename = path + rename
        os.rename (mySource, rename)
        index += 1

if __name__ == "__main__":
    main()
