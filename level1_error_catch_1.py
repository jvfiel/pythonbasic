#Variables
name = "Ranger"
health = "10"
armor = 5

#Print
print "Name: {0}".format(name)
print "Health: {0}".format(health)
print "Armor: {0}".format(armor)
print "-----------------"
print "Name: ", name
print "Health: ", health
print "Armor: ", armor

#BASIC OPERATIONS
rank = "Rookie"
print rank + " " + name
try:
    print "Health: ", health +10 #ERROR
except Exception,e:
    print e, " critical error!"
    print "-------------------"
    print "Health: ", int(health) + 10  # ERROR