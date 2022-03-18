def color(r, g, b, msg):
    return "\033[38;2;{};{};{}m{} \033[38;2;0;0;0m".format(r, g, b, msg)
