from random import randrange
print("Wanna see your pets...Let's go...")

class Pet():
    brdm_dec = 4
    hunger_dec = 6
    brdm_threshold = 5
    hunger_threshold = 10
    sounds = ['Whoof']

    def __init__(self, name):
        self.name = name
        self.hunger = randrange(self.hunger_threshold)
        self.brdm = randrange(self.brdm_threshold)
        self.sounds = self.sounds[:]
    def clock_tick(self):
        self.brdm += 1
        self.hunger += 1

    def mood(self):
        if self.hunger <= self.hunger_threshold and self.brdm <= self.brdm_threshold:
            return "happy"
        elif self.hunger > self.hunger_threshold:
            return "hungry"
        else:
            return "bored"

    def __str__(self):
        state = "     I'm " + self.name + ". "
        state += " I feel " + self.mood() + ". "

        return state

    def hi(self):
        print(self.sounds[randrange(len(self.sounds))])
        self.reduce_brdm()

    def teach(self, word):
        self.sounds.append(word)
        print(self.sounds[-1])
        self.reduce_brdm()

    def feed(self):
        print(self.sounds[randrange(len(self.sounds[:]))]+' and cuddled')
        self.reduce_hunger()

    def reduce_hunger(self):
        self.hunger = max(0, self.hunger - self.hunger_dec)

    def reduce_brdm(self):
        self.brdm = max(0, self.brdm - self.brdm_dec)

avl_name=['Kyle','Felin','Fido','Sissel']
print("Do you wish to see any of the existing pets or add a new one?")

game_on=True
while game_on:
    option = int(input("Type (1) if you want to add one and type (2) to interact with the existing pets: "))
    if(option==1):
        print(f'{avl_name} are the list of existing pets')
        petname=input('Enter the name of the new pet: ')
        avl_name.append(petname)
        print(f"{avl_name} is the new list of pets")
        p1=Pet(petname)
    elif(option==2):
        print('You can 1.greet,2.teach or 3.feed the pet')
        interact=int(input('Choose 1,2 or 3: '))
        p=int(input('Enter the number of the pet you wanna interact with'))
        if interact==1:
            petname=avl_name[p-1]
            p1=Pet(petname)
            p1.hi()
        elif(interact==2):
            petname=avl_name[p-1]
            p1 = Pet(petname)
            word=input('Teach a new word: ')
            p1.sounds[:].append(word)
            p1.teach(word)
        elif(interact==3):
            petname=avl_name[p-1]
            p1=Pet(petname)
            p1.feed()
        else:
            print('Invalid choice')
    else:
        print('Invalid choice')

    for i in avl_name:
        name=Pet(i)
        name.clock_tick()
        print(name)
    game=input('Enter y to continue the game else type n: ')
    if (game=='y'):
        game_on = True
    else:
        game_on = False
    print('Hope you have enjoyed!')
