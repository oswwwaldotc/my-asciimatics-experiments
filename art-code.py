import random
import uuid
# Universal Unique Identifier, is a python library which helps in generating random objects of 128 bits as ids. 

from PIL import Image, ImageDraw

run_id = uuid.uuid1()

print(f'Processing run_id: {run_id}')

image = Image.new('RGB', (2000, 2000))
width, height = image.size

rectangle_width = 100
rectangle_height = 100

number_of_squares = random.randint(10, 50)

draw_image = ImageDraw.Draw(image)
for i in range(number_of_squares):
    rectangle_x = random.randint(0, width)
    rectangle_y = random.randint(0, height)

    rectangle_shape = [
        (rectangle_x, rectangle_y),
        (rectangle_x + rectangle_width, rectangle_y + rectangle_height)]
    draw_image.rectangle(
        rectangle_shape,
        fill=(
            random.randint(0, 50),
            random.randint(51, 100),
            random.randint(101, 150)
        )
    )

image.save(f'{run_id}.png')