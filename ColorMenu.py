import matplotlib


class ColorMenu:
    """class to get python specific color val"""

    def __init__(self, colors):
        """initialize ColorMenu"""
        self.colors = colors.split()

    def get_color(self):
        """converts color name to python color equivalent"""
        output_colors = []

        # based off user input color return hex name
        for color in self.colors:
            output_colors.append(matplotlib.colors.cnames[color])
        return output_colors
