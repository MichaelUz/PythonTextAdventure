class Fighter:
    def __init__(self,name,health,damage,weapon):
        self.name = name
        self.health = health
        self.damage = damage
        self.weapon = weapon

    def giveDamage(self):
        if self.weapon == "gun":
            return self.damage * 4
        elif self.weapon == "knife":
            return self.damage *2

        else:
             return self.damage

    def reset(self,health,damage,weapon):
        self.health = health
        self.damage = damage
        self.weapon = weapon
