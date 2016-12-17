import os


def get_planet_images():
    script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
    return [os.path.join(script_dir, "Images/planet0.png"),
            os.path.join(script_dir, "Images/planet1.png"),
            os.path.join(script_dir, "Images/planet2.png"),
            os.path.join(script_dir, "Images/planet3.png"),
            os.path.join(script_dir, "Images/planet4.png"),
            os.path.join(script_dir, "Images/planet5.png"),
            os.path.join(script_dir, "Images/planet6.png"),
            os.path.join(script_dir, "Images/planet7.png"),
            os.path.join(script_dir, "Images/planet8.png"),
            os.path.join(script_dir, "Images/planet9.png")]


def get_spacecraft_image():
    script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
    return os.path.join(script_dir, "Images/Spacecraft.png")


def get_destroyer_image():
    script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
    return os.path.join(script_dir, "Images/Destroyer.png")


def get_background_image():
    script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
    return os.path.join(script_dir, "Images/Background.png")


def get_space_station_image():
    script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
    return [os.path.join(script_dir, "Images/station.png")]


def get_explosion_gif():
    script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
    return os.path.join(script_dir, "Images/explode.gif")
