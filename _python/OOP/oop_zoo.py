class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.zoo_name = zoo_name
    
    def add_animal(self, animal_name, animal_type):
        animal = {"name": animal_name, "type": animal_type}
        self.animals.append(animal)
        return self
    
    def list_animals (self):
        print("\n", "*"*30, "\n")
        print(f"Welcome to {self.zoo_name} Zoo!")
        print("Here are the animals you will find while you are visiting:\n")
        for animal in animals:
            for key in animal.items():
                print("Name:", key)
                print("Animal Type:", key)
        return self



class Animal():
    def __init__(self, name, age, health, happiness):
        self.name = name
        self.age = age
        self.health = health
        self.happiness = 50
        self.movement = 20
        self.hunger = 20
    
    #run this whenever animal is fed
    def feed_animal (self, food_amount):
        if self.hunger >10:
            self.happy_animals("hunger")
        self.health += food_amount/2
        self.hunger -= food_amount
        self.happiness += 10
        return self
    
    #run this to age animal by one year
    def animal_age (self, max_age=10):
        self.age += 1
        young = max_age*.3
        senior = max_age*.6
        if self.age <= young:
            self.movement += 10
        elif self.age >= senior:
            self.movement -= 10
        else:
            pass
        return self
    
    #run this after each activity
    def happy_animals (self, activity):
        if self.happiness > 20:
            if activity == "nothing":
                self.happiness -= 10
            elif activity == "play":
                self.happiness += 10
            # elif activity == "train":
            #     self.happiness += 20
            elif activity == "fear":
                self.happiness -= 20
            else:
                pass
        else:
            self.movement +=20
        return self
    
    #run this based on circumstances animal is in
    def animal_health (self, circumstance):
        if self.health < 5:
            self.movement = self.movement/2
        return self
    
    def display_info (self):
        print("\n", "*"*30, "\n")
        print(f"Name: {self.name}")
        print(f"Health Level: {self.health}")
        print(f"Age: {self.age}")
        print(f"Happiness Level: {self.happiness}")
        return self
            
            
class Lion(Animal):
    def __init__(self, name, age, health=50, happiness=20):
        super().__init__(name, age, health, happiness)
    
    #when the lion roars see what the crowd does
    def lion_roar (self, roar):
        if roar:
            print(f"{self.name} roars and the crowd cheers!")
            self.happy_animals("play")
        else:
            print("The crowd is disappointed")
        return self
    


class Seal(Animal):
    def __init__(self, name, age, health=30, happiness=30):
        super().__init__(name, age, health, happiness)
        self.can_swim = True
    
    def do_tricks(self, num_of_fish):
        while (num_of_fish != 0):
            print(f"{self.name} does a trick")
            self.happy_animals("play")
            self.hunger +=2
            num_of_fish -=1
        return self


class Chicken(Animal):
    def __init__(self, name, age, health=5, happiness=50):
        super().__init__(name, age, health, happiness)
        self. lays_eggs = True
    
    def startle_chicken (self, scare_times):
        while (scare_times != 0):
            print(f"{self.name} the chicken laid an egg")
            self.happy_animals("fear")
            self.hunger += 2
            scare_times -=1
        return self


zoo1 = Zoo("Bob's")
leo = Lion("Leo", 3, 50, 40).display_info().lion_roar(True).display_info()
sally = Seal("Sally", 3, 20).display_info().do_tricks(5).display_info()
clucky = Chicken("Clucky", 1).display_info().startle_chicken(5).display_info()