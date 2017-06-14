import sys

from PIL import Image


def decode_image(path_to_file):

    encoded_image = Image.open(path_to_file)
    red_channel = encoded_image.split()[0]

    x_size = encoded_image.size[0]
    y_size = encoded_image.size[1]

    decoded_image = Image.new("RGB", encoded_image.size)
    pixels = decoded_image.load()

    for i in range(x_size):
        for j in range(y_size):
            if bin(red_channel.getpixel((i, j)))[-1] == '0':    # last bit from pixel
                pixels[i, j] = (255, 255, 255)
            else:
                pixels[i, j] = (0, 0, 0)

    decoded_image.save("decoded___{}".format(path_to_file.replace("encoded___","")))


if __name__ == '__main__':

    decode_image(sys.argv[1])