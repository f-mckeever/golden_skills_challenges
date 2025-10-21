# {{PROBLEM}} Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a game player
I want to create a `character` with a cool `name`
So that other players recognise my character

As a game player
I want to see my characters `health`
So that I know when I might need to drink a health potion

As a game player
I want my character to be able to `pick up` `items (potions/weapons)` that they find in the game
So that they can use them when they need

As a game player
I want to be able to `use my health potion` item
So that my character's health goes back to 100

As a game player
I want to `attack` another character
So that they lose the health points associated with an attack by that weapon

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
# EXAMPLE

class Character():

    #Params -> 
        #name: str
    #Returns -> 
        #none
    #Sides -> 
        #set default health to 100
        #empty list for inventory
    def __init__(self, name):
        pass


    #pick_up_item
    #Params -> 
    def pick_up_item(self, item)
        pass

    #attack_character
    def attack(self, target):
        pass

    #use_potion
    #Params
    #   potion: Potion
    #Returns
    #   nothing OR str: "You are already at full health."
    def use_potion(self, potion):
        pass

    #take_damage
    def take_damage(self, damage):
        pass


class Potion():

    #init
    #Params -> 
        #name: str
    #Returns -> 
        #nada
    #Sides -> 
        #becomes self -> exists -> maybe added to a list?
    def __init__(self, name, amount_to_restore):
        pass


class Weapon():

    #init
    #Params -> 
        #name: str 
        #damage: int
    #Returns -> 
        #nada
    #Sides ->
        #becomes self -> exists -> maybe added to a list
    def __init__(self, name, damage):
        pass

```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE


"""
Test, taking damage, reduces health by damage
"""

def test_character_take_damage_takes_damage():
    player = Character("Ben")
    assert player.health == 100

    player.take_damage(35)
    assert player.health == 65

"""
Test, use potion, health should return to 100
"""

def test_character_use_potion_restores_all_health():
    player = Character("Ben")

    player.take_damage(35)
    assert player.health == 65

    player.use_potion(potion)
    assert player.health == 100

"""
Test, use potion at full health
"""

def test_character_use_potion_at_full_health():
    player = Character("Fionn")
    potion = Potion("Health Potion")

    assert player.health == 100

    result = player.use_potion(potion)
    
    assert result == "You are already at full health."
    assert player.health == 100


"""




```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
