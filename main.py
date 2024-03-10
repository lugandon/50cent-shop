class Fork:
    def __init__(self, material, length, color):
        self.material = material
        self.length = length
        self.color = color

class Spoon:
    def __init__(self, material, length, color):
        self.material = material
        self.length = length
        self.color = color

class Knife:
    def __init__(self, material, length, color):
        self.material = material
        self.length = length
        self.color = color

class Spatula:
    def __init__(self, material, monotonous, color):
        self.material = material
        self.monotonous = monotonous
        self.color = color

def fork_options():
    pass

def spoon_options():
    pass

def knife_options():
    pass

def spatula_options():
    pass


def choose_utensil():
    print('Fork, ', 'Spoon, ', 'Knife, ', 'Spatula')
    utensil = input("Which utensil You want to buy? ").strip().lower()
    match utensil:
        case 'fork':
            fork_options()
        case 'spoon':
            spoon_options()
        case 'knife':
            knife_options()
        case 'spatula':
            spatula_options()
        case _:
            print("You have to choose one from given options.")


def main():
    choose_utensil()


if __name__ == '__main__':
    main()