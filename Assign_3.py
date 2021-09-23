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
    option = input("Type (y) if you want to add one or else type (n)..(y/n) :")
    if option[0].lower() == 'y':
        new_pet = input('Enter the name of the new pet: ')
        avl_name.append(new_pet)
        choice = avl_name.index(new_pet)+1
    elif option[0].lower() =='n':
        print(avl_name)
        choice = int(input('Choose from 1-4 to interact with any of the pets shown: '))
        game_on = False
    else:
        print("Sorry,I dont understand..Please enter y or n")
        continue
    break

petname=avl_name[choice-1]
p1 = Pet(petname)
new_word = input('Enter a new word to teach them :')
p1.sounds[:].append(new_word)
interact= int(input('How long do ypu wanna interact with(1-15 preferable): '))
for i in range(interact):
    p1.clock_tick()
    print(p1)
    if p1.mood()=='hungry':
        print(f"{petname} is hungry..Feed him to quench the hunger")
        hungr_opt= input("Are you gonna feed it?(y/n)")
        if hungr_opt=='y':
            p1.feed()
        else:
            print(f"{petname} is hungry...feed him")
            continue
    elif p1.mood()=='bored':
        print(f"{petname} is bored..Teach him or say hi to reduce its boredom")
        brd_opt=input('What do you opt--to teach(t) or greet(g) :')
        if brd_opt[0].lower =='t':
            rlx_word=input('Enter a new word to teach : ')
            p1.sounds[:].append(rlx_word)
            p1.teach(rlx_word)
        elif brd_opt[0]=='g':
            p1.hi()
        else:
            print("The pet is bored")
    else:
        continue
