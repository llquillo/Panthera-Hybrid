# Panthera Hybrids Problem
import random


# init function for dynamically created classes
def __init__(self, name, generation, gender):
    self.name = name
    self.generation = generation
    self.gender = gender


# fuction for crossing two (2) pantheras
def cross(panthera1, panthera2):
    gender = ["Female", "Male"]
    random.shuffle(gender)
    if(panthera1.getGender() != panthera2.getGender()):
        gen = 0
        gen = panthera1.generation if (
            panthera1.generation > panthera2.generation) else panthera2.generation
        gen += 1
        if(type(panthera1) != type(panthera2)):
            getHybrid(type(panthera1).__name__, type(panthera2).__name__,
                      gender[0], gen)
        else:
            name = type(panthera1).__name__
            newPanthera = type(panthera1)(
                name if gender[0] == "Male" else name+'ess', gender[0], gen)
            printDetails(newPanthera)
    else:
        print("Cannot cross. Same Gender.")


# function for printing info about the crossed panthera
def printDetails(newPanthera):
    print()
    print(newPanthera)
    print("\tName: ", newPanthera.name)
    print("\tGeneration: ", newPanthera.generation)
    print("\tGender: ", newPanthera.gender)
    print("\tType: ", type(newPanthera).__name__)
    print()


# function for creating the new hybrid class
def createClass(name, generation, gender):
    className = type(name,
                     (Panthera,),
                     {"__init__()": __init__}
                     )
    newPanthera = className(name if gender ==
                            "Male" else name+'ess', generation, gender)

    printDetails(newPanthera)


# function for creating the new hybrid class for the special case: Tiger Hybrid Female
def createClassTigerHybridF(name, generation, gender, femaleName):
    className = type(name,
                     (Panthera,),
                     {"__init__()": __init__}
                     )
    newPanthera = className(name if gender ==
                            "Male" else femaleName+"ss", generation, gender)

    printDetails(newPanthera)


# function for getting the hybrid
def getHybrid(panthera1, panthera2, gender, generation):
    def initPanthera(panthera1):
        return {
            'Tiger': tigerHybrid,
            'Lion': lionHybrid,
            'Jaguar': jaguarHybrid,
            'Leopard': leopardHybrid
        }[panthera1]()

    def tigerHybrid():
        name = panthera1[:3]
        if(panthera2 == "Lion"):
            name += panthera2[-2:]
        else:
            name += panthera2[-3:]

        return createClass(name, generation, gender)

    def lionHybrid():
        name = panthera1[:2]
        if(panthera2 == "Tiger"):

            if(gender == "Female"):
                return createClassTigerHybridF(name + panthera2[-3:], generation, gender, name + panthera2[-3:-
                                                                                                           2] + panthera2[-1:] + panthera2[-2:-1])
            else:
                name += panthera2[-3:]
        elif(panthera2 == "Jaguar"):
            name += panthera2[-4:]
        else:
            name += panthera2[-4:]

        return createClass(name, generation, gender)

    def jaguarHybrid():
        name = panthera1[:3]
        if(panthera2 == "Tiger"):
            if(gender == "Female"):
                return createClassTigerHybridF(name + panthera2[-3:], generation, gender, name + panthera2[-3:-
                                                                                                           2] + panthera2[-1:] + panthera2[-2:-1])
            else:
                name += panthera2[-3:]
        elif(panthera2 == "Leopard"):
            name = panthera1[:4]
            name += panthera2[-4:]
        else:
            name += panthera2[-4:].lower()

        return createClass(name, generation, gender)

    def leopardHybrid():
        name = panthera1[:3]
        if(panthera2 == "Tiger"):
            if(gender == "Female"):
                return createClassTigerHybridF(name + panthera2[-3:], generation, gender, name + panthera2[-3:-
                                                                                                           2] + panthera2[-1:] + panthera2[-2:-1])
            else:
                name += panthera2[-3:]
        elif(panthera2 == "Lion"):
            name = panthera1[:4]
            name += panthera2[-2:]
        elif(panthera2 == "Jaguar"):
            name = panthera1[:2]
            name += panthera2[-4:]
        else:
            name += panthera2[-4:]

        return createClass(name, generation, gender)

    initPanthera(panthera1)


# main panthera classes
class Panthera:
    def __init__(self, name, generation, gender):
        self.name = name
        self.generation = generation
        self.gender = gender

    def getGender(self):
        return self.gender

    def getGeneration(self):
        return self.generation

    def printType(self):
        print(type(self))
        
    def __lt__(self, other):
        if self.generation < other.generation:
            return self.generation < other.generation

    def __eq__(self, other):
        if self.generation == other.generation:
            return self.generation == other.generation

    def __gt__(self, other):
        if self.generation > other.generation:
            return self.generation > other.generation


class Lion(Panthera):
    def __init__(self, name, generation, gender):
        super().__init__(name, generation, gender)


class Tiger(Panthera):
    def __init__(self, name, generation, gender):
        super().__init__(name, generation, gender)


class Jaguar(Panthera):
    def __init__(self, name, generation, gender):
        super().__init__(name, generation, gender)


class Leopard(Panthera):
    def __init__(self, name, generation, gender):
        super().__init__(name, generation, gender)


# Test Cases:

# Different Gender:
# Same Type:
# Tiger
t1 = Tiger("Tiger", 1, "Male")
t2 = Tiger("Tigress", 1, "Female")
cross(t1, t2)

# Lion
l1 = Lion("Lion", 1, "Male")
l2 = Lion("Lioness", 1, "Female")
cross(l1, l2)

# Jaguar
j1 = Jaguar("Jaguar", 1, "Male")
j2 = Jaguar("Jaguaress", 1, "Female")
cross(j1, j2)

# Leopard
le1 = Leopard("Leopard", 1, "Male")
le2 = Leopard("Leopardess", 1, "Female")
cross(le1, le2)


# Different Types:

# Tiger Hybrids:
# Tigon:
t1 = Tiger("Tiger", 1, "Male")
l2 = Lion("Lioness", 1, "Female")
cross(t1, l2)

# Tiguar:
t1 = Tiger("Tiger", 1, "Male")
j2 = Jaguar("Jaguaress", 1, "Female")
cross(t1, j2)

# Tigard:
t1 = Tiger("Tiger", 1, "Male")
le2 = Leopard("Leopardess", 1, "Female")
cross(t1, le2)


# Lion Hybrids:
# Liger:
l1 = Lion("Lion", 1, "Male")
t2 = Tiger("Tigress", 1, "Female")
cross(l1, t2)

# Liguar:
l1 = Lion("Lion", 1, "Male")
j2 = Jaguar("Jaguaress", 1, "Female")
cross(l1, j2)

# Lipard:
l1 = Lion("Lion", 1, "Male")
le2 = Leopard("Leopardess", 1, "Female")
cross(l1, le2)


# Jaguar Hybrids:
# Jagger:
j1 = Jaguar("Jaguar", 1, "Male")
t2 = Tiger("Tigress", 1, "Female")
cross(j1, t2)

# Jaglion:
j1 = Jaguar("Jaguar", 1, "Male")
l2 = Lion("Lioness", 1, "Female")
cross(j1, l2)

# Jagupard:
j1 = Jaguar("Jaguar", 1, "Male")
le2 = Leopard("Leopardess", 1, "Female")
cross(j1, le2)

# Leopard Hybrids:
# Leoger:
le1 = Leopard("Leopard", 1, "Male")
t2 = Tiger("Tigress", 1, "Female")
cross(le1, t2)

# Leopon:
le1 = Leopard("Leopard", 1, "Male")
l2 = Lion("Lioness", 1, "Female")
cross(le1, l2)

# Leguar:
le1 = Leopard("Leopard", 1, "Male")
j2 = Jaguar("Jaguaress", 1, "Female")
cross(le1, j2)


# Same Gender:
t1 = Tiger("Tigeress", 1, "Female")
t2 = Tiger("Tigress", 1, "Female")
cross(t1, t2)

t1 = Tiger("Tigeress", 1, "Female")
l2 = Lion("Lioness", 1, "Female")
cross(t1, l2)


# Different Generation:
t1 = Tiger("Tiger", 1, "Male")
t2 = Tiger("Tigress", 2, "Female")
cross(t1, t2)

t1 = Tiger("Tiger", 2, "Male")
l2 = Lion("Lioness", 1, "Female")
cross(t1, l2)

# Sorting
pantherArray = []

for i in range(1, 10):
    tigerInstance = Tiger("Tiger", i, "Male")
    pantherArray.append(tigerInstance)

random.shuffle(pantherArray)

print("\n===UNSORTED===")
for i in pantherArray:
    print("Name: ", i.name, "Generation: ", i.generation)

pantherArray.sort()

print("\n===SORTED===")
for i in pantherArray:
    print("Name: ", i.name, "Generation: ", i.generation)
