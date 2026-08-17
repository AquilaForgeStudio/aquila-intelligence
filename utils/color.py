def hex_to_rgb(hex_color):
    """
    Convert a hex color string to an RGB tuple.

    Args:
        hex_color (str): A hex color string (e.g., "#RRGGBB" or "RRGGBB").

    Returns:
        tuple: A tuple representing the RGB values (R, G, B).
    """
    hex_color = hex_color.lstrip("#")
    r = hex_color[0:2]
    g = hex_color[2:4]
    b = hex_color[4:6]

    return (int(r,16), int(g,16), int(b,16))

def rgb_to_hex(rgb):
    """
    Convert RGB values to a hex color string.

    Args:
        rgb (tuple): A tuple representing the RGB values (R, G, B).

    Returns:
        str: A hex color string (e.g., "#RRGGBB").
    """
    r, g, b = rgb
    return "#{:02x}{:02x}{:02x}".format(r, g, b)

def interpolate_color(start, end, progress):
    r = start[0] + (end[0] - start[0]) * progress
    g = start[1] + (end[1] - start[1]) * progress
    b = start[2] + (end[2] - start[2]) * progress

    return (round(r), round(g), round(b))