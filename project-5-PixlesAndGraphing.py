#Daniel Almond project 5
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import time
from IPython.display import display, clear_output

def rgb_to_grayscale(rgb_pixel):
    return int(max(rgb_pixel[0], rgb_pixel[1], rgb_pixel[2]))


def load_png(filename):
    return mpimg.imread(filename)


def convert_to_grayscale(image):
    return [[rgb_to_grayscale(pixel) for pixel in row] for row in image]


class Sprite:
    def __init__(self, image, position=[0,0]):
        self.image = image
        self.position = position
        self.default_position = [0,0]
        self.original_image = [row[:] for row in image]
        self.touched_star = False
        self.touched_mushroom = False

    def resize(self, factor):
        new_image = []
        for row in self.image:
            new_row = []
            for pixel in row:
                new_row.extend([pixel] * factor)
            new_image.extend([new_row] * factor)
        self.image = new_image

    def invert_colors(self):
        self.image = [[1 - pixel for pixel in row] for row in self.image]

    def check_interactions(self):
        if self.touches_star() and not self.touched_star:
            self.invert_colors()
            self.touched_star = True
        if self.touches_mushroom() and not self.touched_mushroom:
            self.resize(2)
            self.touched_mushroom = True

    def touches_star(self):
        # Define the bounding box for the star
        star_y1 = 85 
        star_y2 = 137
        star_x1 = 22
        star_x2 = 69

        # Get the bounding box of the sprite
        sprite_x1, sprite_y1 = self.position
        sprite_x2 = sprite_x1 + len(self.image[0])
        sprite_y2 = sprite_y1 + len(self.image)

        # Check for overlap between the sprite and the star
        return not (sprite_x2 < star_x1 or sprite_x1 > star_x2 or sprite_y2 < star_y1 or sprite_y1 > star_y2)

    def touches_mushroom(self):
        # Define the bounding box for the mushroom
        mushroom_x1 = 66
        mushroom_x2 = 93
        mushroom_y1 = 196
        mushroom_y2 = 222

        # Get the bounding box of the sprite
        sprite_x1, sprite_y1 = self.position
        sprite_x2 = sprite_x1 + len(self.image[0])
        sprite_y2 = sprite_y1 + len(self.image)

        # Check for overlap between the sprite and the mushroom
        return not (
                    sprite_x2 < mushroom_x1 or sprite_x1 > mushroom_x2 or sprite_y2 < mushroom_y1 or sprite_y1 > mushroom_y2)

    def move(self, direction):
        if direction == "1":
            self.position[0] -= 16
        elif direction == "2":
            self.position[0] += 16
        elif direction == "3":
            self.position[1] -= 16
        elif direction == "4":
            self.position[1] += 16
        self.check_interactions()  # this line executes after you move.

    def overlay_on_background(self, background):
        temp_background = [row[:] for row in background]
        for y, row in enumerate(self.image):
            for x, pixel in enumerate(row):
                background_x = self.position[1] + x 
                background_y = self.position[0] + y 
                if 0 <= background_x < len(temp_background[0]) and 0 <= background_y < len(
                        temp_background):  # check for out of bounds
                    # Set the grayscale value for all RGB channels
                    gray_value = (pixel, pixel, pixel)
                    temp_background[background_y][background_x] = gray_value
        return temp_background

    def reset(self):
        # Reset the sprite to its original image and position
        self.image = [row[:] for row in self.original_image]
        self.position = self.default_position
        # Reset the interaction flags
        self.touched_star = False
        self.touched_mushroom = False


def display_image(image_data):
    plt.imshow(image_data)
    plt.axis('off')  # Hide axes
    plt.show()




# Read the background and sprite images
original_background = load_png('background.png')
sprite_image = load_png('face.png')

# If the sprite image should be converted to grayscale
sprite_image = convert_to_grayscale(sprite_image)

# Initialize the sprite
sprite = Sprite(sprite_image, [0, 0])

# User interaction loop
while True:
    background = original_background.copy()
    display_image(sprite.overlay_on_background(background))

    print("__________________________________________________")
    print("1. Move Up")
    print("2. Move Down")
    print("3. Move Left")
    print("4. Move Right")
    print("'R'. Reset")
    print("'E'. End Game")
    print("Choose: ", end='')
    user_choice = input().lower()
    if user_choice == "1" or user_choice == "2" or user_choice == "3" or user_choice == "4":
        sprite.move(user_choice)
    elif user_choice == 'r':
        sprite.reset()
    elif user_choice == 'e':
        print("Thanks for playing")
        break
    else:
        print("oops, try again")

