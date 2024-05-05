from PIL import Image
import easygui as eg
import os


def main():
    path = eg.fileopenbox(title='Select image', filetypes=[["*.png;*.jpg;*.jpeg;*.webp", "Image files"]])
    convert_to_ascii(path)


def convert_to_ascii(path):
    img = Image.open(path)
    f = open("ascii.txt", "w")

    width, height = img.size
    for y in range(height):
        for x in range(width):
            R, G, B = img.getpixel((x, y))
            brightness = sum([R, G, B])
            if brightness < 127.5:
                char = "$"
            elif brightness < 255:
                char = "@"
            elif brightness < 382.5:
                char = "&"
            elif brightness < 510:
                char = "#"
            elif brightness < 637.5:
                char = "Z"
            elif brightness < 765:
                char = "z"
            else:
                char = "~"
            f.write(char)
        f.write("\n")
    os.startfile('ascii.txt')


if __name__ == '__main__':
    main()
