class Player:
    def __init__(self,health,gender,defultWepon,credits,name):
        print("Player Object Created")
        self. health=health
        self. gender=gender
        self.defultWepon=defultWepon
        self.credits=credits
        self. name=name
    
    def playerhurt(self,Damage):
        self.health=self.health-damage
        print("Damage=",damage,"New Health=",self.health)

    def isDead(self):
       if self.health<=0:
          return True
       else:
          return False
       

p1=Player(100,"F")
p2=Player(50,"M")
print (p1.isDead())
print(p2.isDead())
print(p1.health)
print(p1.gender)
print(p2.health)
print(p2.gender)

p1.health=200

p2.health=p2.health-40

print(p1.health)

print(p2.health) 