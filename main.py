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
    def __init__(self, material, length, monotonous, color):
        self.material = material
        self.length = length
        self.monotonous = monotonous
        self.color = color


class Spatula:
    def __init__(self, material, monotonous, color):
        self.material = material
        self.monotonous = monotonous
        self.color = color


def create_utensil():
    print("Creating utensil: \n")


def choose_utensil():
    options = ['fork', 'spoon', 'knife', 'spatula']
    created = False

    print(', '.join(options))

    utensil = input("Which utensil do you want to buy? ").strip().lower()

    # There we go through the all utensils to make sure User chose the existent utensil
    for option in options:
        if utensil == option:
            created = True
            break

    if created:
        print("You have chosen -", option.capitalize())
        create_utensil()
    else:
        print("Sorry, you chose the wrong option.")


def main():
    choose_utensil()


if __name__ == '__main__':
    main()
