
file = open("test.csv", "w")
for i in range(15):
    for j in range(25):
        file.write("1,")
    file.write("\n")
file.close()