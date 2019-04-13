from PIL import Image

my_image = Image.open("Sunsets.jpg")
image_pixels = my_image.load()
width, height = my_image.size
for i in range(0, width):
    for m in range(0, height):
        current_pixel = image_pixels[i,m]
        blue_component = image_pixels[i,m][0]
        green_component = image_pixels[i,m][1]
        red_component = image_pixels[i,m][2]
        gray_value = (int)(0.07 * blue_component + 0.72 * green_component + 0.21 *
        red_component)
        new_value = (gray_value, gray_value, gray_value, 255)
        if(gray_value < 50):
            new_value = (252, 225, 90)
        elif(gray_value < 50):
                    new_value = (247, 168, 168)
        elif(gray_value < 100):
                    new_value = (149, 249, 249)
        elif(gray_value < 100):
                new_value = (174, 255, 147)
        elif(gray_value < 100):
            new_value = (181, 219, 255)
        elif (gray_value < 200):
            new_value = (249, 158, 144)
        image_pixels[i,m] = new_value
my_image.show()
