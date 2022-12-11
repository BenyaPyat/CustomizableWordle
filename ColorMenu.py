class ColorMenu:
    """class to get python specific color val"""

    def __init__(self, colors):
        """initialize ColorMenu"""
        self.colors = colors.split()

    def get_color(self):
        """converts color name to python color equivalent"""
        output_colors = []

        # based off user input color return python specific name
        for color in self.colors:
            if 'green' == color:
                output_colors.append('#76EEC6')
            elif 'yellow' == color:
                output_colors.append('#E3CF57')
            elif 'black' == color:
                output_colors.append('#483D8B')
            elif 'white' in color:
                output_colors.append('#F8F8FF')
            elif 'blue' in color:
                output_colors.append('#0000EE')
            elif 'red' in color:
                output_colors.append('#EE3B3B')
            else:
                pass
        return output_colors
