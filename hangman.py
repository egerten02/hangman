import random

cluster = ['Tiger', 'Lion', 'Elephant', 'Leopard', 'Panther', 'Cheetah',
           'Wolf', 'Jaguar', 'Hyena', 'Giraffe', 'Deer', 'Zebra', 'Gorilla',
           'Monkey', 'Chimpanzee', 'Bear', 'Wild', 'Boar', 'Hippopotamus',
           'Kangaroo', 'Rhino', 'Crocodile', 'Panda', 'Squirrel', 'Mongoose',
           'Porcupine', 'Koala', 'Bear', 'Wombat', 'Meerkat', 'Otter', 'Puma',
           'Hedgehog', 'Possum', 'Chipmunk', 'Raccoon', 'Jackal', 'Hare',
           'Mole', 'Rabbit', 'Alligator', 'Oryx', 'Elk', 'Badger', 'Pangolin',
           'Okapi', 'Camel', 'Coyote', 'Bison', 'Elephant', 'Aardvark',
           'Antelope', 'Goat', 'Eagle', 'Eel', 'Armadillo', 'Beaver',
           'Penguin', 'Baboon', 'Bat', 'Chameleon', 'Bull', 'Panda', 'Marten',
           'Chihuahua', 'Orangutan', 'Chinchillas', 'Hawk', 'Iguana', 'Ibex',
           'Cobra', 'Jellyfish', 'Goose', 'Walrus', 'Seal', 'Falcon', 'Shark',
           'Owl', 'Bobcat', 'Pig', 'Yak', 'Reindeer', 'Moose', 'Caracal']

# Main variables
answer = random.choice(cluster).lower()
word = list(answer)
letter_count = len(word)
guessed = letter_count * "_"
guessed = list(guessed)
if letter_count > 8:
    life = 16
else:
    life = 10

def guess():
    """It takes user input and evaluates it."""
    global word, guessed, life, letter_count
    letter = input("Guess a letter\n>")
    found = False

    for i in word:
        if i == letter:
            index = word.index(i)
            guessed[index] = letter
            word[index] = "_"
            letter_count -= 1
            found = True

    if not found:
        life -= 1
        print("Doesn't exist")
        print(life, "guess remained.\n")

def main():
    while life > 0 and letter_count != 0:
        guess()

        for j in guessed:
            print(j)
    if life == 0:
        print("Game over. The man was hanged.\nThe word was ", answer)
    if letter_count == 0:
        print("Well done. You saved the man.")

main()