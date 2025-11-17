"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: Kayla Bagley
Date: 10/28/2025

AI Usage (Google Gemini): AI helped me figure out my indentation error, completely understanding how to save a character to a file, how to check the filename.

"""
import os
def create_character(name, character_class):
    # makes sure every character starts at level 1
    level = 1

    # my stat calculation
    strength, magic, health = calculate_stats(character_class, level)

    character = {
        "name": name,
        "class": character_class,
        "level": level,
        "strength": strength,
        "magic": magic,
        "health": health,
        "gold": 100  #  character starts at 100 gold
    }

    return character
   

def calculate_stats(character_class, level):
    # (low,med,high) = (4,7,10); growth rates = (1,2,3,4)

    if character_class == "Warrior":
        base_strength = 10
        base_magic = 4
        base_health = 10
        growth_strngth = 3
        growth_magic = 1
        growth_health = 4
    elif character_class == "Mage":
        base_strength = 4
        base_magic = 10
        base_health = 7
        growth_strngth = 1
        growth_magic = 3
        growth_health = 3
    elif character_class == "Rogue":
        base_strength = 7
        base_magic = 7
        base_health = 10
        growth_strngth = 2
        growth_magic = 2
        growth_health = 4
    elif character_class == "Cleric":
        base_strength = 7
        base_magic = 10
        base_health = 7
        growth_strngth = 2
        growth_magic = 3
        growth_health = 3
    else:
        return (0, 0, 0)  

    strength = base_strength + (level * growth_strngth )
    magic = base_magic + (level * growth_magic )
    health = base_health + (level * growth_health )

    return (strength, magic, health)


def save_character(character, filename):

    if character is None:
        print("Error: No character to save.")
        return False

    if filename == "":
        print("Error: Invalid filename.")
        return False

    if os.path.isdir(filename):
        print("Error: That name is a folder, not a file.")
        return False

    directory = os.path.dirname(filename)
    if directory != "" and not os.path.exists(directory):
        print("Error: Could not save character.")
        return False

    with open(filename, "w", encoding="utf-8") as file:
        file.write(f"Character Name: {character['name']}\n")
        file.write(f"Class: {character['class']}\n")
        file.write(f"Level: {character['level']}\n")
        file.write(f"Strength: {character['strength']}\n")
        file.write(f"Magic: {character['magic']}\n")
        file.write(f"Health: {character['health']}\n")
        file.write(f"Gold: {character['gold']}\n")

    print(f"Character saved to {filename}")
    return True


def load_character(filename):
    if not os.path.exists(filename):
        print("Error: File not found.")
        return None

    character = {}

    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            if ": " in line:
                parts = line.strip().split(": ", 1)
                key = parts[0]
                value = parts[1]

            if key == "Character Name":
                character["name"] = value
            elif key == "Class":
                character["class"] = value
            elif key == "Level":
                character["level"] = int(value)
            elif key == "Strength":
                character["strength"] = int(value)
            elif key == "Magic":
                character["magic"] = int(value)
            elif key == "Health":
                character["health"] = int(value)
            elif key == "Gold":
                character["gold"] = int(value)

    stats = ["name", "class", "level", "strength", "magic", "health", "gold"]
    for key in stats:
        if key not in character:
            print("Error: Missing " + key + " in file.")
            return None

    return character

def display_character(character):
    print("\n=== CHARACTER SHEET ===")
    print(f"Name: {character['name']}")
    print(f"Class: {character['class']}")
    print(f"Level: {character['level']}")
    print(f"Strength: {character['strength']}")
    print(f"Magic: {character['magic']}")
    print(f"Health: {character['health']}")
    print(f"Gold: {character['gold']}")


def level_up(character):
    character["level"] = character.get("level", 1) + 1
    strength, magic, health = calculate_stats(character["class"], character["level"])
    character["strength"] = strength
    character["magic"] = magic
    character["health"] = health

