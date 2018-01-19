class Hero:

    def __init__(self, name, health, armor, skills):
        self.name = name
        self.health = armor
        self.skills = skills

    def cast(self,i):
        print "Skill Name: {0} Damage: {1}".format(self.skills[1]['skill'],self.skills[1]['dmg'])

skills = [
            {'skill':'strike','dmg':1},
            {'skill':'heavy strike','dmg':5}
        ]

emp = Hero("Brian mcKnight", 10, 20, skills)
emp.cast(0)

#DAMAGE MCKNIGHT
emp.health -= 5
#print "McKnight's Health: {0}".format(emp.health)