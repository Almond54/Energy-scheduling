import random
import matplotlib.pyplot as plt

class Appliance():
    """
    This class simulates a household appliance. 
    """
    def __init__(self, name, phases):
        self.name = name
        self.phases = phases
        self.scheduleLength = len(phases)

    def __repr__(self):
        return f"This appliance is a {self.name} and  has a schedule length of {self.scheduleLength}\nThe schedule is "
class Timings():
    def __init__(self, ):
        pass


def cost(S, N, X):
    # Return the cost of solution S with respect to N and X
    assert len(S) == len(N) 
    total = 0
    j = 0
    for i in range(len(S)):
        if S[i] == 1:
            total += N[i] * X[j]
            j += 1
    return total

# Main Program: Ask the user to specify the input file, then read it into memory.

def open_file(infile):
    
    with open(infile, 'r') as f:
        N = eval(f.readline())
        X = eval(f.readline())
    # Do some basic checks to make sure the input is valid
    assert type(N) == list and type(X) == list and len(N) >= len(X), "Error. Invalid input"
    n = len(N)
    x = len(X)
    return N,n,X,x


# Main Program: Ask the user to specify the input file, then read it into memory.
infile = input("Enter problem file name >> ")
with open(infile, 'r') as f:
    N = eval(f.readline())
    X = eval(f.readline())

# Do some basic checks to make sure the input is valid
assert type(N) == list and type(X) == list and len(N) >= len(X), "Error. Invalid input"
n = len(N)
x = len(X)                  #idk but maybe we can get rid of this and then do the cycle over multiple days?




ListOfCosts = []
Cheapest = 100000000000000000000
BestSchedule = {}
numberofruns = 100000
k = 1
for i in range(numberofruns):
    print("we are ", round(i / numberofruns * 100, 2 ), "percent complete")
    S = []
    for i in range(x):
        S.append(1)
    for i in range(n-x):
        S.append(0)
    random.shuffle(S)
    ListOfCosts.append(cost(S, N, X))
    if ListOfCosts[-1] < Cheapest: #checks if this is the new cheapest
        Cheapest = ListOfCosts[-1] #if it is, replaces the old cheapest number with this
        BestSchedule = [S]  #saves the solution to the BestSchedule one
    if (ListOfCosts[-1]) == Cheapest: # if this is as cheap as another soln...
        BestSchedule.append(S)  # adds the new soln to the BestSchedule part
ListOfCosts = sorted(ListOfCosts)
NoDuplicatesListOfCosts = sorted(list(set(ListOfCosts)))
FrequencyOfCosts = []
for i in NoDuplicatesListOfCosts:
    FrequencyOfCosts.append(ListOfCosts.count(i))
print(min(NoDuplicatesListOfCosts))
print(Cheapest)
print(BestSchedule) # checking it worked in registering the cheapest

best_best_schedule = min(BestSchedule) #the shortest and thus most time efficient solution in BestSchedule
print(best_best_schedule)


best_best_schedule_cost = best_best_schedule
j = 0
for i in range(len(best_best_schedule_cost)):
    if best_best_schedule_cost[i] == 1:
        best_best_schedule_cost[i] = X[j]
        j += 1                                  #this is putting the energy cost in the schedule

#if len(best_best_schedule_cost) != len(N):
#    for i in range(1, len(best_best_schedule_cost) // len(N)):      # We dont actually need this cos its just matching them up anyway but it'd be useful if we end up trying to take multiple days for stuff
#        N.append(N)

x_axis = range(1, len(best_best_schedule_cost) + 1)
fig, ax = plt.subplots(figsize = (10, 7))
plt.title("Energy Costs and when to use an Appliance for the lowest cost")
ax_2 = ax.twinx()

ax.bar(x_axis, best_best_schedule_cost, color = "red", width = 0.5)
ax_2.plot(x_axis, N, color = "blue", linewidth = 5)

ax.set_xlabel("Time Period")
ax.set_ylabel("Units Required")
ax_2.set_ylabel("Cost Per Unit")
ax_2.set_yticks(range(max(best_best_schedule_cost)))                #this is to set the amount that the y-axis goes up in, which is good for p1, p2 but not so much for p3

#plt.xticks(x_axis)         #same thign for x-axis only really good for p1
plt.show()
