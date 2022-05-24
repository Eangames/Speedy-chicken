
#16x10

level_names = [
    "Tutorial",
    "Level 1",
    "Level 2",
]

levels = [
    [
        64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,
        64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,
        64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,
        64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,
        64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,
        64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,
        64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,
        64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,
        24,64,64,64,64,64,64,64,64,64,64,64,64,64,64,32,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1
    ],
    [
        64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,
        64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,
        64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,
        64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,
        64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,
        64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,
        64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,
        64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,
        24,64,64,64,64,64,64,64,64,64,64,64,64,64,64,32,
        1,1,1,1,1,64,1,1,64,1,64,64,1,1,1,1
    ]
]

type_map = [
    "ground-left-up", #0
    "gound-up",
    "ground-up-right",
    "bridge-length-1",
    "bridge-top",
    "bridge-left",
    "bridge-middle",
    "bridge-right",
    "ground-left", #8
    "ground",
    "ground-right",
    "ground-all",
    "ground-topright",
    "egg-collectable",
    "",
    "",
    "ground-left-down", #16
    "ground-down",
    "ground-down-right",
    "ground-topleft",
    "ground-bottomleft",
    "ground-bottomright",
    "",
    "",
    "start", #24
    "button",
    "pressureplate",
    "door-closed",
    "",
    "",
    "",
    "",
    "end", #32
    "button-pressed",
    "pressureplate-pressed",
    "door-open",
    "",
    "",
    "",
    "",
    "sign-arrow-bottomright", #40
    "sign-arrow-topright",
    "sign-arrow-topleft",
    "sign-arrow-bottomleft",
    "sign-arrow-down",
    "",
    "",
    "",
    "sign", #48
    "sign-empty",
    "sign-arrow-right",
    "sign-arrow-left",
    "sign-arrow-up",
    "",
    "",
    "",
    "water-anim-0", #56
    "water-anim-1",
    "water-anim-2",
    "water-anim-3",
    "water-still",
    "",
    "decoration7",
    "decoration8",
    "" #64
]

file = open("test.js", "r")
content = file.read()
file.close()

file = open("test.js", "w")
file.write(content + "\n\n")
for id in range(len(levels)):
    file.write(f"const level{id} = '")
    file.write("{" + f"\"level_id:\":{id},\"level_name\":\"{level_names[id]}\",")
    file.write("\"level_map\":{")
    for i in range(len(levels[id])):
        if(i<len(levels[id])-1):
            file.write(f"\"{i}\":\"{type_map[levels[id][i]]}\",")
        else:
            file.write(f"\"{i}\":\"{type_map[levels[id][i]]}\"")
    file.write("}")
    file.write("}';\n")
file.close()
