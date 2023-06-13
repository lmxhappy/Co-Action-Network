import random

fi = open("local_test", "r")
ftrain = open("local_train_splitByUser", "w")
ftest = open("local_test_splitByUser", "w")

while True:
    rand_int = random.randint(1, 10)
    noclk_line = fi.readline().strip()
    clk_line = fi.readline().strip()
    if noclk_line == "" or clk_line == "":
        break
    if rand_int == 2:
        ftest.write(noclk_line + "\n")
        ftest.write(clk_line + "\n")
    else:
        ftrain.write(noclk_line + "\n")
        ftrain.write(clk_line + "\n")
