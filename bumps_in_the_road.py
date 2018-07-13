def bumps(road):
    bump = 0
    for char in road:
        if char == "n":
            bump += 1
    return "Woohoo!" if bump <= 15 else "Car Dead"


bumps("_nnnnnnn_n__n______nn__nn_nnn")
