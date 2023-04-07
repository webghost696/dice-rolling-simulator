# this code renames your images ending with .jpg into wallpaper1,wallpaper2,... just add the path where you want to rename the images and run the code
import os
path=input("enter the path:\n")
path.replace('\\','/')
def main():
    i=0
    for j in os.listdir(path):
        dest=path+"Wallpaper"+str(i)+".jpg"
        source=path+j
        os.rename(source,dest)
        i+=1
main()