""" Create a class for the LED """

import time
import neopixel
import board


class LED:
    """Create a class for the LED"""

    def __init__(self):
        """Initialize the LED"""
        self.pixels = neopixel.NeoPixel(board.D18, 1, brightness=100, auto_write=False)
        self.pixels.fill((0, 0, 0))
        self.pixels.show()

    def set_color(self, red, green, blue):
        """Set the color of the LED"""
        self.pixels.fill((red, green, blue))
        self.pixels.show()

    def fade(self, red, green, blue, duration):
        """Fade the LED to the specified color over the specified duration"""
        current_color = self.pixels[0]
        current_red = current_color[0]
        current_green = current_color[1]
        current_blue = current_color[2]
        red_step = (red - current_red) / duration
        green_step = (green - current_green) / duration
        blue_step = (blue - current_blue) / duration
        for i in range(duration):
            self.pixels.fill(
                (
                    int(current_red + (red_step * i)),
                    int(current_green + (green_step * i)),
                    int(current_blue + (blue_step * i)),
                )
            )
            self.pixels.show()
            time.sleep(1)
        self.pixels.fill((red, green, blue))
        self.pixels.show()

    def rainbow_cycle(self, wait):
        """Draw rainbow that uniformly distributes itself across all pixels."""
        for j in range(255):
            for i in range(len(self.pixels)):
                idx = int((i * 256 / len(self.pixels)) + j)
                self.pixels[i] = self.wheel(idx & 255)
            self.pixels.show()
            time.sleep(wait)


if __name__ == "__main__":
    # strip = LED()
    # strip.set_color(255, 0, 0)
    # Configuration

    pixels1 = neopixel.NeoPixel(board.D18, 30, brightness=0.1)
    x = 0
    pixels1.fill((0, 220, 0))
    pixels1[10] = (255, 0, 0)

    # Sleep for three seconds, You should now have all LEDs showing light with the first node
    # Showing a different colour
    time.sleep(4)

    # Little Light slider script, will produce a nice loading bar effect that goes all the way up a small Strip
    # and then all the way back
    # This was created using a While Loop taking advantage of that arbitrary variable to determine
    # which LED Node we will target/index with a different colour

    # Below will loop until variable x has a value of 35
    while x < 35:
        pixels1[x] = (255, 0, 0)
        pixels1[x - 5] = (255, 0, 100)
        pixels1[x - 10] = (0, 0, 255)
        # Add 1 to the counter
        x = x + 1
        # Add a small time pause which will translate to 'smoothly' changing colour
        time.sleep(0.05)

    # Below section is the same process as the above loop just in reverse
    while x > -15:
        pixels1[x] = (255, 0, 0)
        pixels1[x + 5] = (255, 0, 100)
        pixels1[x + 10] = (0, 255, 0)
        x = x - 1
        time.sleep(0.05)

    # Add a brief time delay to appreciate what has happened
    time.sleep(4)

    # Complete the script by returning all the LED to off
    pixels1.fill((0, 0, 0))

    # Function to set a solid color on the entire strip
    # def set_color(color):
    #     pixels.fill(color)
    #     pixels.show()

    # # Function to create a rainbow effect on the strip
    # def rainbow_cycle(wait):
    #     for j in range(255):
    #         for i in range(num_pixels):
    #             pixel_index = (i * 256 // num_pixels) + j
    #             pixels[i] = wheel(pixel_index & 255)
    #         pixels.show()
    #         time.sleep(wait)

    # # Function to generate rainbow colors
    # def wheel(pos):
    #     if pos < 85:
    #         return (int(pos * 3), int(255 - pos * 3), 0)
    #     elif pos < 170:
    #         pos -= 85
    #         return (int(255 - pos * 3), 0, int(pos * 3))
    #     else:
    #         pos -= 170
    #         return (0, int(pos * 3), int(255 - pos * 3))

    # # Main loop
    # try:
    #     while True:
    #         set_color((255, 0, 0))  # Set to red
    #         time.sleep(2)

    #         set_color((0, 255, 0))  # Set to green
    #         time.sleep(2)

    #         set_color((0, 0, 255))  # Set to blue
    #         time.sleep(2)

    #         rainbow_cycle(0.01)  # Rainbow effect

    # except KeyboardInterrupt:
    #     # Turn off the NeoPixels when the script is interrupted
    #     pixels.fill((0, 0, 0))
    #     pixels.show()
