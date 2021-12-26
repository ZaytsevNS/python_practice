def hex_to_rgb(hex_str: str) -> tuple:
    return (int(hex_str[0:2], 16), int(hex_str[2:4], 16), int(hex_str[4:6], 16))
