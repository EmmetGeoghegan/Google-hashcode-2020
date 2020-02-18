import time


def importdata(filename):
    with open(f"./in/{filename}") as inputfile:
        lines = inputfile.readlines()
        target = int(lines[0].strip("\n").split(" ")[0])
        batch_size = int(lines[0].strip("\n").split(" ")[1])

        pizzas = lines[1].strip("\n").split(" ")
        pizzas = [int(i) for i in pizzas]
    return target, batch_size, pizzas


def createoutputfile(num_pizzas, chosenpizzas, filename="sub.txt"):
    timestamp = str(time.time()).replace(".", "")
    with open(f"./submissions/{timestamp}{filename}", "w+") as outputfile:
        outputfile.write(str(num_pizzas)+"\n")
        outputfile.write(" ".join([str(i.id) for i in chosenpizzas]))


class Pizzas:
    all_Pizzas = []

    def __init__(self, id, slices):
        self.slices = slices
        self.id = id
        self.all_Pizzas.append(self)
        self.used = 0

    def __repr__(self):
        return(f"{self.slices}")


# target, batch_size, pizzas = importdata("a.in")       # Completed
# target, batch_size, pizzas = importdata("b.in")       # Completed
# target, batch_size, pizzas = importdata("c.in")       # Completed
target, batch_size, pizzas = importdata("d.in")
# target, batch_size, pizzas = importdata("e.in")

for id, slices in enumerate(pizzas):
    Pizzas(id, slices)
pizzas = Pizzas.all_Pizzas

print(target, batch_size, Pizzas.all_Pizzas)

best_selec = []
print("----")
# print(Pizzas)
print("----")


def recur_sum(pizzas, target, sel_p=[]):
    cus_score = 250554555    # D cus  - 250554555
    # cus_score = 8090664    # E cus score - 8090664
    global best_selec
    curr_sum = sum([i.slices for i in sel_p])

    if curr_sum == target:
        print(f"Perf soln: {sel_p}")
        createoutputfile(len(sel_p), sel_p, "perf.txt")
        return "DONE"
    else:
        if (target - curr_sum > -1) and (curr_sum > sum([i.slices for i in best_selec])) and (sum([i.slices for i in sel_p]) > cus_score):
            print(f"Old Best: {best_selec}")
            print(f"New best: {sel_p}")
            best_selec = sel_p
            print(f"Best Selec:{sum([i.slices for i in best_selec])}   {target-sum([i.slices for i in best_selec])} off\n")
            createoutputfile(len(sel_p), sel_p, "att.txt")

    for i in range(len(pizzas)):
        n = pizzas[i]
        remaining = pizzas[i+1:]
        recur_sum(remaining, target, sel_p + [n])


recur_sum(pizzas, target)
print("Best Soln Found")



# New algo
# Sum all available
# Subtract from target
# find pizzas that come close to the ammount to be removed
# unused pizzas are perfect submission
