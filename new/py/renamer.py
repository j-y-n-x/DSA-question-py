import os

def main():
    i = 0
    path = "D:/00yt/ax/"
    for filename in os.listdir(path):
        change_name = "image" + str(i) + ".png"
        from_source = path + filename
        change_name = path + change_name
        os.rename(from_source, change_name)
        i += 1

if name == 'main':
    main()