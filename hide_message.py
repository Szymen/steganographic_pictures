from builtins import bin

import sys
from PIL import Image, ImageFont, ImageDraw
import textwrap


def write_text(text_to_write, image_size):
    image_text = Image.new("RGB", image_size)
    font = ImageFont.load_default().font
    drawer = ImageDraw.Draw(image_text)

    margin = offset = 10
    for line in textwrap.wrap(text_to_write, width=60):
        drawer.text((margin,offset), line, font=font)
        offset += 10
    return image_text


def encode_image(text_to_encode, template_image):
    name = "encoded___{}".format(template_image)
    template_image = Image.open(template_image)
    red_template = template_image.split()[0]
    green_template = template_image.split()[1]
    blue_template = template_image.split()[2]

    x_size = template_image.size[0]
    y_size = template_image.size[1]

    image_text = write_text(text_to_encode, template_image.size)
    bw_encode = image_text.convert('1')

    encoded_image = Image.new("RGB", (x_size, y_size))
    pixels = encoded_image.load()
    for i in range(x_size):
        for j in range(y_size):
            red_template_pix = bin(red_template.getpixel((i,j)))
            old_pix = red_template.getpixel((i,j))
            tencode_pix = bin(bw_encode.getpixel((i,j)))

            if tencode_pix[-1] == '1':
                red_template_pix = red_template_pix[:-1] + '1'
            else:
                red_template_pix = red_template_pix[:-1] + '0'
            pixels[i, j] = (int(red_template_pix, 2), green_template.getpixel((i,j)), blue_template.getpixel((i,j)))
    encoded_image.save(name)

if __name__ == '__main__':
    encode_image( sys.argv[1], sys.argv[2])
