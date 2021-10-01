print("\nWelcome!\n")
pet_names={'dogs':[],'cats':[]}
class Pets():
    def __init__(self,species,name):
        self.species=species
        self.name=name
        while self.species not in ['dog','cat','horse','hamster']:
            return 'ERROR'
    def __str__(self):
        if self.name!=[]:
            return f"Species of: {self.species} and {self.name} is the name."
        else:
            return f"Species of: {self.species} ,unnamed."

class Dog(Pets):
    def __init__(self,name="Dan",chases='Cats'):
        super().__init__(species,name)
        self.chases=chases
    def __str__(self):
        if self.name!=[]:
            return f"Species of :Dog ,named {self.name},chases {self.chases}"
        else:
            return f"Species of : Dog,unnamed,chases {self.chases}"

class Cat(Pets):
    def __init__(self,name='Tiya',hates='Dogs'):
        super().__init__(species,name)
        self.hates=hates
    def __str__(self):
        if self.name!=[]:
            return f"Species of:Cat,named {self.name},hates {self.hates}"
        else:
            return f"Species of :Cat,unnamed,hates {self.hates}"

class mains(Pets):
    def __init__(self):
        super().__init__(species, name)
        for i in zip(newpet,petsspecies):
            if i[1]=='cat':
                pet_names['cats']=newpet[i[0]]
            elif (i[1]=='dog'):
                pet_names['dogs']=newpet[i[0]]

petname=[]
petspecies=[]
p=Pets(species,name)
game=True
while game:
    addpet=input('Enter the name of the pet: ')
    pettype=input('Enter the species of the pet: ')
    petname.append(addpet)
    petspecies.append(pettype)
    m=mains(Pets)



