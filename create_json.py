
#16x10

level = [
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

file = open("level0.json", "w")
file.write("{\n")
file.write("\t\"level-name\":\"Tutorial\",\n")
file.write("\t\"level-map\":{\n")
for i in range(len(level)):
    if(i<len(level)-1):
        file.write(f"\t\t\"{i}\":\"{type_map[level[i]]}\",\n")
    else:
        file.write(f"\t\t\"{i}\":\"{type_map[level[i]]}\"\n")
file.write("\t}\n")
file.write("}\n")
file.close()
