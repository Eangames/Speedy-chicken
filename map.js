
map = [
    "ground-left-up",
    "gound-up",
    "ground-up-right",
    "bridge-length-1",
    "bridge-top",
    "bridge-left",
    "bridge-middle",
    "bridge-right",
    "ground-left",
    "ground",
    "ground-right",
    "ground-all",
    "ground-topright",
    "egg-collectable",
    "",
    "",
    "ground-left-down",
    "ground-down",
    "ground-down-right",
    "ground-topleft",
    "ground-bottomleft",
    "ground-bottomright",
    "",
    "",
    "start",
    "button",
    "pressureplate",
    "door-closed",
    "",
    "",
    "",
    "",
    "end",
    "button-pressed",
    "pressureplate-pressed",
    "door-open",
    "",
    "",
    "",
    "",
    "sign-arrow-bottomright",
    "sign-arrow-topright",
    "sign-arrow-topleft",
    "sign-arrow-bottomleft",
    "sign-arrow-down",
    "",
    "",
    "",
    "sign",
    "sign-empty",
    "sign-arrow-right",
    "sign-arrow-left",
    "sign-arrow-up",
    "",
    "",
    "",
    "water-anim-0",
    "water-anim-1",
    "water-anim-2",
    "water-anim-3",
    "water-still",
    "",
    "decoration",
    "decoration"
]

solid_map = [
    2,2,2,1,0,1,1,1,
    2,2,2,2,2,0,0,0,
    2,2,2,2,2,2,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
]

interactions_map = [
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,1,0,0,
    0,0,0,0,0,0,0,0,
    1,1,1,1,0,0,0,0,
    1,1,1,1,0,0,0,0,
    0,0,0,0,0,0,0,0,
    1,1,0,0,0,0,0,0,
    1,1,1,1,1,0,0,0,
]

function getType(index){
    return map[index], solid_map[index], interactions_map[index];
}

function getTilesOfType(type){
    let indexes = []; for(let i=0;i<64;i++){if(map[i]==type){indexes.push(i);}} return indexes;
}

function getTilesOfSolidness(solidness){
    let indexes = []; for(let i=0;i<64;i++){if(solid_map[i]==solidness){indexes.push(i);}} return indexes;
}

function getTilesOfIncteractions(interactions){
    let indexes = []; for(let i=0;i<64;i++){if(interactions_map[i]==interactions){indexes.push(i);}} return indexes;
}
