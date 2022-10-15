

from random import *

from time import *
#import time
# import matplotlib.pyplot as plt
exits = ['q','quit','exit','stop','4']
mobList = ['Skeleton','Slime','Goblin','Zombie','Werewolf','Ogre','Undead Horde','Automaton','Placeholder']
adjList = ['','Golden ','Strong ','Elite ','Forgotten ','Derelict ','Ancient ','Colossal ','Supreme ']
typeList = ['',' Guard',' Warrior',' Brute',' Guard',' Lord']
firstName = ['Johann','Henri','Karl','Johanness','David','Henry','Jhesse','Leucas','Louis','Odrev','Fercingetorix','Torrelegintix','Remy','Alrov','Demol','Omel','Oderhein','Jacob','Emanuel','Perseplomine','Homer','Soa','Charles','Caere','Mason','Helionentrivix','Hok Min','Sinquo','Reginald','Sarge','Ermine','Sargent','Edgar','Odalric']
lastName = [" de Mer"," de l'Occitan",' Hapsbrug',' Eldermeinn',' de la Bourdonnais',' Feudharte',' Champbruggain',' Sasson',' the Bald',' of Arc',' Smithson',' Lemmington',' Tudor',' Greco',' Opilugus Detrimundus',' Avenfeol',' Geraldson',' Sarrot',' Benedict',' Godwinson',' Adalhard',' Flavius',' Fulbert',' Lanzo']
weapons = ["Forgotten Hero's Sword",'Crypt Sword','Claymore','Katana','Naginata',"Assasin's Dagger",'Ogre King Sword']
armors = ["Forgotten Hero's Chainmail", 'Crypt Armor', 'Bony Chestplate','Dungeon Armor','Ogre Armor']
roomList = ['Chamber','Trapped Chamber','Bone Pit','Den','Treasure Chamber','Abandonned Keep','Goblin Sanctuary','Wizard Tower','Ogre Outpost','Ancient Cistren']
bossList = ['Rogue Knight of the Forgotten Kingdom','Goblin King','Werewolf Grand Champion','Great Ogre King','Koloktos, Ancient Automaton','Dark Mage Pelimanntrix','The Last Dragon']
typeIndex = ''
adjIndex = ''
chamber = None
difficulty = 0.6
weapon = 0
armor = 0
money = 40
fightActive = 0
class Mob:
    def __init__(self,mob,strength,type,adjective,health):
        self.health = health
        self.strength = strength
        self.adjective = adjective
        self.type = type
        if typeIndex != 0:
            self.strength += (int(type)+1)**2
            self.health += 10
        if adjIndex != 0:
            self.strength += (int(adjective)+1)**2
            self.health += 12
        if typeIndex != 0 and adjIndex != 0:
            self.name = adjList[adjective] + mob + typeList[type]
        if typeIndex != 0 and adjIndex == 0:
            self.name = mob + typeList[type]
        if typeIndex == 0 and adjIndex != 0:
            self.name = adjList[adjective]+mob
        if typeIndex == 0 and adjIndex == 0:
            self.name = mob
        modifier = round((mobIndex+2)/4)
        if modifier < 1: modifier = 1
        self.strength = round(strength*difficulty)*modifier
        self.health = round(health*difficulty)*modifier
        self.mob = mob
        if self.health < 5:
            self.health = 5
        if self.strength < 5:
            self.strength = 5
class Boss:
    def __init__(self, mob, health, strength, defense, choice):
        self.mob = bossList[mob]
class Player:
    def __init__(self,type,firstname,lastname,health,name,strength,defense):
        self.type = type
        self.firstname = firstname
        self.lastname = lastname
        self.health = health
        self.name = firstname+lastname
        self.strength = strength
        self.defense = defense
def treasureSelect():
    global weapon
    global armor
    global money
    selection = randint(0, 3)
    sleep(0.5)
    if selection == 0 and weapon != len(weapons) - 1:
        print("You find: " + weapons[weapon + 1])
        weapon += 1
        player.strength += 10
    elif selection == 1 and armor != len(armors) - 1:
        print(("You find: " + armors[armor + 1]))
        armor += 1
        player.defense += 10
    elif selection == 2:
        gold = str(randint(10, 100))
        print("You find: " + gold + " Gold!")
        if randint(1, 10) == 4:
            print("Looks like it's unusable however, it has been corroded beyond recognition")
        else:
            money+=int(gold)
    else:
        print("You find: Health Potion")
        player.health += randint(10, 80)
        print(player.name + " healed to " + str(player.health))
    # print(typeIndex,adjIndex)
    #print(enemy.name,enemy.health,enemy.strength)
def launchTrap():
    trap = randint(0,4)
    global running
    global damage
    if trap == 0:
        damage = (randint(1, 70))
        player.health -= damage
        print("A saw trap opens up, dealing " + str(damage))
        if player.health <= 0:
            fightActive = 0
            sleep(0.5)
            print('Blood pools around you. It goes dark...')
            running = False
    elif trap == 1:
        damage = (randint(1, 70))
        player.health -= damage
        print("A trap opens and a massive rock smashes into you, dealing " + str(damage))
        if player.health <= 0:
            fightActive = 0
            sleep(0.5)
            print('Blood pools around you. It goes dark...')
            running = False
    else:
        print("There's nothing inside")
def activateFight():
    global armor
    global money
    global weapon
    global running
    global fightActive
    while fightActive == 1:
        sleep(0.5)
        print('Your Weapon and Armor: ' + weapons[weapon] + ', ' + armors[armor])
        print('Your Health: ' + str(player.health))
        print('Your Defense: ' + str(player.defense))
        print('Your Strength: ' + str(player.strength))
        print('Enemy Health: ' + str(enemy.health))
        print('Enemy Strength: ' + str(enemy.strength))
        playerChoice = input("Attack (1), Defend (2), or Flee? (3)")
        if playerChoice == '1':
            sleep(0.5)
            playerDamage = round(player.strength * round(uniform(0, 3), 2))
            print(player.name + ' attacks the ' + enemy.name + ", dealing " + str(playerDamage))
            enemy.health -= playerDamage
            if enemy.health <= 0:
                sleep(0.5)
                print('The ' + enemy.name + ' falls to the ground. You win!')
                player.strength += 3
                fightActive = 0
                if enemy.mob == "Undead Horde" or enemy.name == "Colossal Goblin Lord" or chamber == 3 or enemy.name == "Supreme Ogre Lord":
                    if enemy.name != "Supreme Ogre Lord":
                        treasureSelect()
                    else:
                        print("Great Enemy Felled!")
                        treasureSelect()
                        treasureSelect()
                        treasureSelect()
                break
        elif playerChoice == '2':
            defense = round(player.defense * uniform(0, 2))
            print('You brace for impact, absorbing ' + str(defense) + ' in damage')
            sleep(0.5)
            damage = (round(enemy.strength * round(uniform(0, 2), 2)))
            if damage != 0:
                damage = (round(enemy.strength * round(uniform(0, 2), 2))) - defense
                if damage < 0:
                    damage = 0
                player.health -= damage
                print('The ' + enemy.name + ' attacks ' + player.name + ', dealing ' + str(damage))
                sleep(0.5)
                if damage == 0:
                    print("Blocked!")
                    sleep(0.5)
                    playerDamage = round((player.strength * round(uniform(0, 2), 2)) / 2)
                    print(player.name + ' counterattacks the ' + enemy.name + ", dealing " + str(playerDamage))
                    enemy.health -= playerDamage
                    if enemy.health <= 0:
                        sleep(0.5)
                        print('The ' + enemy.name + ' falls to the ground. You win!')
                        player.strength += 3
                        fightActive = 0
                        if enemy.mob == "Undead Horde" or enemy.name == "Colossal Goblin Lord" or chamber == 3 or enemy.name == "Supreme Ogre Lord":
                            if enemy.name != "Supreme Ogre Lord":
                                treasureSelect()
                            else:
                                print("Great Enemy Felled!")
                                treasureSelect()
                                treasureSelect()
                                treasureSelect()
                        break

                if damage < 10 and damage != 0 and defense != 0:
                    print('Partially Blocked!')
                    sleep(0.5)
                    playerDamage = round((player.strength * round(uniform(0, 2), 2)) / 3)
                    print(player.name + ' counterattacks the ' + enemy.name + ", dealing " + str(playerDamage))
                    enemy.health -= playerDamage
                    if enemy.health <= 0:
                        sleep(0.5)
                        print('The ' + enemy.name + ' falls to the ground. You win!')
                        player.strength += 3
                        fightActive = 0
                        if enemy.mob == "Undead Horde" or enemy.name == "Colossal Goblin Lord" or chamber == 3 or enemy.name == "Supreme Ogre Lord":
                            if enemy.name != "Supreme Ogre Lord":
                                treasureSelect()
                            else:
                                print("Great Enemy Felled!")
                                treasureSelect()
                                treasureSelect()
                                treasureSelect()
                        break
            else:
                print(enemy.name + " didn't do any damage!")
        elif playerChoice == '3':
            sleep(0.5)
            print(player.name + ' runs for it at the sight of the ' + enemy.name + '!')
            if randint(0, 2) == 1:
                damage = round(enemy.strength * round(uniform(0, 2), 2))
                sleep(0.5)
                print(
                    "However, the " + enemy.name + " lands a hit just as " + player.name + ' escapes, dealing ' + str(
                        damage))
                player.health -= damage
                if player.health <= 0:
                    fightActive = 0
                    sleep(0.5)
                    print('Blood pools around you. It goes dark...')
                    running = False
                else:
                    sleep(0.5)
                    print(player.name + ' manages to escape!')
                    fightActive = 0
                    break
            else:
                sleep(0.5)
                print(player.name + ' escapes unharmed!')
                fightActive = 0
                break
        elif playerChoice in exits:
            exit()
        if playerChoice != '2' and playerChoice != '3':
            damage = round(enemy.strength * round(uniform(0, 2), 2))
            sleep(0.5)
            print('The ' + enemy.name + ' attacks ' + player.name + ', dealing ' + str(damage))
            player.health -= damage
        sleep(0.5)
        if player.health <= 0:
            fightActive = 0
            sleep(0.5)
            print('Blood pools around you. It goes dark...')
            running = False
def roomSelect():
    global chamber
    if difficulty < 1:
        if randint(0,3) == 1:
            chamber = 0
        else:
            chamber = randint(0,randint(3,9))
    elif difficulty < 1.5:
        if randint(0,3) == 1:
            chamber = 0
        else:
            chamber = randint(0, randint(4, 9))
    elif difficulty < 1.7:
        if randint(0,4) == 1:
            chamber = 0
        else:
            chamber = randint(0, randint(7, 9))
    else:
        if randint(0,5) == 1:
            chamber = 0
        else:
            chamber = randint(0,9)

player = Player('Crusader',firstName[randint(0,len(firstName)-1)],lastName[randint(0,len(lastName)-1)],150,...,randint(15,60),randint(30,60))
# player.strength = 4000
# player.health = 4000
# player.defense = 4000
print(player.name,player.health,player.strength,player.defense)
if input("Press any button to begin") in exits:
    exit()
playerDamage = 0
running = True
sleep(0.5)
chamberPrev = -1
while running:
    sleep(0.5)
    if difficulty%10 != 0:
        roomSelect()
        if chamber == 0:
            print("You enter a Chamber")
            sleep(1)
            if randint(0,4) != 1:
                mobIndex = randint(0, randint(0, len(mobList) - 4))
                mob = mobList[mobIndex]
                mobStrength = randint(10, 30)
                if randint(0, 2) == 1:
                    adjIndex = randint(0, len(adjList) - 1)
                else:
                    adjIndex = 0
                adjective = adjList[adjIndex]
                if randint(0, 2) == 1:
                    typeIndex = randint(0, randint(0, len(typeList) - 1))
                else:
                    typeIndex = 0
                mobType = typeList[typeIndex]
                mobHealth = randint(1, randint(5, randint(16, 18))) * (round(mobStrength / 2))
                if adjective == None:
                    adjective = ''
                if mobType == None:
                    mobType = ''
                enemy = Mob(mob, mobStrength, typeIndex, adjIndex, mobHealth)
                sleep(0.5)
                print('A '+enemy.name+' approaches you, showing malicious intent!')
                fightActive = 1
            else:
                print("There's nothing inside")
        elif chamber == 1:#['Goblin Sanctuary','Ogre Outpost','Dragon Den','Ancient Cistren']
            print('You enter a Chamber...')
            sleep(1)
            launchTrap()

        elif chamber == 2:
            print("You enter a Bone Pit")
            sleep(1)
            mobIndex = 0
            mob = mobList[mobIndex]
            mobStrength = randint(20,25)
            mobHealth = randint(1, randint(5, randint(16, 18))) * (round(mobStrength / 2))
            enemy = Mob(mob,mobStrength,0,0,mobHealth)
            print('A ' + enemy.name + ' approaches you, showing malicious intent!')
            fightActive = 1
        elif chamber == 3:
            print("You enter a Den")
            sleep(1)
            mobIndex = randint(4, len(mobList) - 4)
            mob = mobList[mobIndex]
            mobStrength = randint(10, 40)
            if randint(0, 2) == 1:
                adjIndex = randint(0, len(adjList) - 1)
            else:
                adjIndex = 0
            adjective = adjList[adjIndex]
            if randint(0, 2) == 1:
                typeIndex = randint(0, randint(3, len(typeList) - 1))
            else:
                typeIndex = 0
            mobType = typeList[typeIndex]
            mobHealth = randint(1, randint(5, randint(16, 18))) * (round(mobStrength / 2))
            if adjective == None:
                adjective = ''
            if mobType == None:
                mobType = ''
            enemy = Mob(mob, mobStrength, typeIndex, adjIndex, mobHealth)
            print('A ' + enemy.name + ' approaches you, showing malicious intent!')
            fightActive = 1
        elif chamber == 4:
            print('You enter a Treasure Room!')
            treasureSelect()

        elif chamber == 5:#['Abandonned Keep','Goblin Sanctuary','Ogre Outpost','Dragon Den','Ancient Cistren']
            print("You enter an Abandonned Keep...")
            sleep(1)
            print("It's full of undead warriors!")
            sleep(0.5)
            mobIndex = 6
            mob = mobList[mobIndex]
            mobStrength = randint(10, 40)
            if randint(0, 2) == 1:
                adjIndex = randint(0, len(adjList) - 1)
            else:
                adjIndex = 0
            adjective = adjList[adjIndex]
            typeIndex = 0
            mobHealth = randint(1, randint(5, randint(16, 18))) * (round(mobStrength / 2))
            enemy = Mob(mob, mobStrength, typeIndex, adjIndex, mobHealth)
            print('A ' + enemy.name + ' approaches you, showing malicious intent!')
            fightActive = 1
        elif chamber == 6:
            print("You enter a Goblin Sanctuary...")
            sleep(0.5)
            if randint(0,1) == 1:
                print("Surprisingly, they shower you with gifts!")
                treasureSelect()
            else:
                print("The Goblins sound the alarm, and a hulking Colossal Goblin Lord approaches!")
                mobIndex = 2
                mob = mobList[mobIndex]
                mobStrength = randint(20, 60)
                adjIndex = 7
                adjective = adjList[adjIndex]
                typeIndex = 5
                mobHealth = randint(2,20) * (round(mobStrength / 2))
                enemy = Mob(mob, mobStrength, typeIndex, adjIndex, mobHealth)
                fightActive = 1
        elif chamber == 7:
            strengthcost = randint(30, 50)
            cost = randint(20, 40)
            print("You enter a mysterious Wizard Tower...")
            sleep(1)
            print("Wizard: Hello There! Don't really get that many visitors.")
            sleep(2)
            print("Wizard: What can I do for you?")
            sleep(0.8)
            wait = True
            while wait:
                sleep(0.5)
                ask = input("Heal me (1), Strengthen me (2), or Leave (3)?")
                if ask == '1':
                    sleep(0.5)
                    print("Wizard: That'll cost "+str(cost))
                    ask = input("You have "+str(money)+'. Proceed? (1)')
                    if ask == '1':
                        if money >= cost:
                            money -= cost
                            sleep(1)
                            wizardSpeak = ['Alakazam!','Hocus Pocus!','Abrakadabra!','Presto!','Shazaam!']
                            text = randint(0,4)
                            print("Wizard: "+wizardSpeak[text])
                            sleep(1)
                            player.health += randint(10,200)
                            print("Wizard: You now have "+str(player.health)+" health!")
                        else:
                            print("Wizard: You don't have enough...")
                    else:
                        sleep(0.5)
                        print("Wizard: But it's such a cheap price!")
                elif ask == '2':
                    sleep(0.5)
                    print("Wizard: That'll cost " + str(strengthcost))
                    ask = input("You have " + str(money) + '. Proceed? (1)')
                    if ask == '1':
                        if money >= strengthcost:
                            money -= strengthcost
                            sleep(1)
                            wizardSpeak = ['Alakazam!', 'Hocus Pocus!', 'Abrakadabra!', 'Presto!', 'Shazaam!']
                            text = randint(0, 4)
                            print("Wizard: " + wizardSpeak[text])
                            sleep(1)
                            player.strength += randint(40, 60)
                            print("Wizard: You now have " + str(player.strength) + " strength!")
                        else:
                            print("Wizard: You don't have enough...")
                    else:
                        sleep(0.5)
                        print("Wizard: But it's such a cheap price!")
                elif ask == '3':
                    sleep(1)
                    print("Wizard: Ok, farewell I guess")
                    sleep(1)
                    wait = False
        elif chamber == 8:
            print("You enter an Ogre Outpost...")
            if randint(1,4) == 1:
                sleep(1)
                mobIndex = 5
                mob = mobList[mobIndex]
                mobStrength = randint(20, 30)
                adjIndex = randint(0, len(adjList) - 1)
                adjective = adjList[adjIndex]
                typeIndex = 2
                mobType = typeList[typeIndex]
                mobHealth = randint(1, randint(5, randint(16, 18))) * (round(mobStrength / 2))
                enemy = Mob(mob, mobStrength, typeIndex, adjIndex, mobHealth)
                print('A ' + enemy.name + ' approaches you, showing malicious intent!')
                fightActive = 1
            else:
                sleep(1)
                print("You find yourself faced with a Supreme Ogre Lord!")
                sleep(1)
                mobIndex = 5
                mob = mobList[mobIndex]
                mobStrength = randint(25, 40)
                adjIndex = 8
                adjective = adjList[adjIndex]
                typeIndex = 5
                mobType = typeList[typeIndex]
                mobHealth = randint(5, 14) * (round(mobStrength / 2))
                enemy = Mob(mob, mobStrength, typeIndex, adjIndex, mobHealth)
                fightActive = 1

        elif chamber == 9:
            ...
    else:
        ...
    activateFight()
    difficulty += 0.05
    sleep(1)
    chamberPrev = chamber
print("You survived to difficulty: "+str(round(difficulty,3)))
