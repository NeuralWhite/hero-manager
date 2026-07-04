user = [
    {"name": "Ali", "power": 8, "level": 4, "mission": ["m1", "m2", "m3"]},
    {"name": "Sara", "power": 11, "level": 5, "mission": ["m1", "m2", "m3", "m4"]},
    {"name": "Reza", "power": 6, "level": 2, "mission": ["m1"]},
    {"name": "Nima", "power": 15, "level": 7, "mission": ["m1", "m2", "m3", "m4", "m5"]},
    {"name": "Mina", "power": 9, "level": 3, "mission": ["m1", "m2"]},
    {"name": "Parsa", "power": 18, "level": 8, "mission": ["m1", "m2", "m3", "m4"]},
    {"name": "Hasan", "power": 12, "level": 6, "mission": ["m1", "m2", "m3"]},
    {"name": "Zahra", "power": 7, "level": 2, "mission": []},
    {"name": "Amir", "power": 22, "level": 9, "mission": ["m1", "m2", "m3", "m4", "m5"]},
    {"name": "Maryam", "power": 14, "level": 6, "mission": ["m1","m2", "m3"]},
    {"name": "Hossein", "power": 5, "level": 2, "mission": ["m1"]},
    {"name": "Yasmin", "power": 16, "level": 7, "mission": ["m1", "m2", "m3", "m4"]},
    {"name": "Kiana", "power": 25, "level": 8, "mission": ["m1", "m2", "m3", "m4", "m5", "m6"]},
    {"name": "Rojan", "power": 10, "level": 4, "mission": ["m1", "m2"]},
    {"name": "Artemis", "power": 17, "level": 8, "mission": ["m1", "m2", "m3", "m4"]},
    {"name": "Sina", "power": 6, "level": 3, "mission": []},
    {"name": "Siavash", "power": 13, "level": 5, "mission": ["m1", "m2", "m3"]},
    {"name": "Kataun", "power":20, "level": 1, "mission": ["m1", "m2", "m3", "m4", "m5"]},
    {"name": "Kourosh", "power": 21, "level": 4, "mission": ["m1", "m2", "m3"]},
    {"name": "Fatemeh", "power": 28, "level": 10, "mission": ["m1", "m2", "m3", "m4", "m5", "m6"]}
    
]



def add_hero():
    name_inp = input("Enter the user's name:")
    power_inp = int(input("Enter the user's power:"))
    level_inp = int(input("Enter the user's level:"))
    mission_inp = int(input("How many missions has the user complated? "))

    e = []
    for i in range(mission_inp):
        mission_str = str(i+1)
        mission_write = "m" + mission_str
        e.append(mission_write)

    user.append({"name": name_inp, "power": power_inp, "level": level_inp, "mission": e})

    return f"{name_inp} has been added"

print(add_hero())



def find_strongest():
    x = 0
    empty = []
    text = ''

    for highest in user:
        if highest["level"] > x:
            x = highest["level"]

    for b in user:
        if b["level"] == x:
            empty.append(b['name'])
    if len(empty) == 1:
        return f"{empty[0]} is the strongest."
        
    else:
        for c in range(len(empty)):
            if c == 0:
                text += empty[c]
            elif c > 0:
                text += " and " + empty[c]
        text += " are the Strongest."
    return text

print(find_strongest())



def generate_report():
    for i in user:
        if len(i["mission"]) >= 3:
            print(f"Hero: {i['name']} | mission:{len(i['mission'])}")

generate_report()