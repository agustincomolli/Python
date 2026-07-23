class Dog:
    kennel = 0  # perrera

    def __init__(self, breed: str):
        self.breed = breed  # raza
        Dog.kennel += 1

    def __str__(self) -> str:
        return self.breed + " dice ¡Guau!"


class SheepDog(Dog):
    def __str__(self) -> str:
        return super().__str__() + " ¡No huyas, corderito!"


class GuardDog(Dog):
    def __str__(self) -> str:
        return super().__str__() + " ¡Quédese donde está, intruso!"
    

class LowLandDog(SheepDog):
    def __str__(self) -> str:
        return Dog.__str__(self) + " ¡No me gustan las montañas!"


rocky = SheepDog("Border Collie")
luna = GuardDog("Dobermann")

print(rocky)
print(luna)

print(issubclass(SheepDog, Dog), issubclass(SheepDog, GuardDog))
print(isinstance(rocky, GuardDog), isinstance(luna, GuardDog))

print(luna is luna, rocky is luna)

print(rocky.kennel)