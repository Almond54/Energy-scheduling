import random
import matplotlib.pyplot as plt

class Appliance():
    """
    This class simulates a household appliance. 
    """
    def __init__(self, name, phases):
        self.name = name
        self.phases = phases
        self.ScheduleLength = len(phases)

    def __repr__(self):
        return f"This appliance is a {self.name} and  has a schedule length of {self.ScheduleLength}\n The schedule is {self.phases}"

class Timings():
    """
    This class holds the information about engergy timings
    """
    def __init__(self, costPerPeriod):
        self.costPerPeriod = costPerPeriod # This attribute holds the price of electricity at each period of the day 
        self.length = len(costPerPeriod)

class Solution():
    """
    This class acts as a blueprint for a solution to our problem it includes
        > The schedule of the phases of the solution
        > The cost of the solution
        > The object involved in the solution
        > Multiple ways to generate a solution
    """
    def __init__(self, appliance, timings):
        """
        Following code initalizes a solution generated by randomly shuffling the indexs about
        """
        temp = [1 for i in appliance.phases] + [0 for i in range(timings.length - appliance.ScheduleLength)] #Create an array with the energy consupmtion for the appiliance and 0s when its not on
        random.shuffle(temp)
        self.solutionSchedule = []
        appliancePhaseIndex = 0
        for i in temp:
            if i == 1:
                self.solutionSchedule.append(appliance.phases[appliancePhaseIndex])
                appliancePhaseIndex += 1
            else:
                self.solutionSchedule.append(0)
        del temp

        #Here were are just setting some misc attributes
        self.timings = timings
        self.length = timings.length
        self.appliance = appliance
        self.cost = "Unknown"
        self.calcuateCost()

    def calcuateCost(self):
        """
        This methoid sets the cost of the solution object.
        """
        total = 0
        for i in range(self.length):
            total += self.solutionSchedule[i] * self.timings.costPerPeriod[i]
        self.cost = total

    def graph(self):
        """
        Following function graphs out the solution nicely.
        """
        xAxis =[i for i in range(self.length)]
        fig, ax = plt.subplots(figsize = (10, 7))
        plt.title("Energy Costs and when to use an Appliance for the lowest cost")
        ax_2 = ax.twinx()
        ax.bar(xAxis, self.solutionSchedule, color = "red", width = 0.5)
        ax_2.plot(xAxis, self.timings.costPerPeriod, color = "blue", linewidth = 5)

        ax.set_xlabel("Time Period")
        ax.set_ylabel("Units Required")
        ax_2.set_ylabel("Cost Per Unit")
        plt.show()

    def __repr__(self):
        return f"This is a solution for the appliance {self.appliance.name}, with timings for use {self.solutionSchedule} which has a cost of {self.cost}"



def open_file(file):
    """
    This function reads a specific problem and returns the approiate Appliance and Timings objects
    """
    with open(file, 'r') as f:
        timingArray = eval(f.readline())
        applianceName = f.readline()
        applianceArray = eval(f.readline())
    return Appliance(applianceName, applianceArray), Timings(timingArray)

def task1(appliance, timing, numberOfRuns):
    """
    
    """
    ListOfCosts = []
    Cheapest = 10000000000
    for i in range(numberOfRuns):
        print("we are ", round(i / numberOfRuns * 100, 2 ), "percent complete")
        tempSolution = Solution(appliance, timing)
        ListOfCosts.append(tempSolution.cost)
        if ListOfCosts[-1] < Cheapest: #checks if this is the new cheapest
            BestSchedules = []
            Cheapest = ListOfCosts[-1] #if it is, replaces the old cheapest number with this
            BestSchedules.append(tempSolution)  #saves the solution to the BestSchedules one
        if (ListOfCosts[-1]) == Cheapest: # if this is as cheap as another soln...
            BestSchedules.append(tempSolution)  # adds the new soln to the BestSchedule part
    ListOfCosts = sorted(ListOfCosts)
    solutions = BestSchedules
    best_cost = min(ListOfCosts)
    return ListOfCosts, solutions, best_cost

def graph_task_1(ListOfCosts):
    """
    Takes the data found in task1 and gives a graph showing the distribution of the random solutions' cost.
    """
    NoDuplicatesListOfCosts = sorted(list(set(ListOfCosts)))
    FrequencyOfCosts = []
    for i in NoDuplicatesListOfCosts:
        FrequencyOfCosts.append(ListOfCosts.count(i))
    plt.xlabel("Cost")
    plt.ylabel("Frequency")
    plt.bar(NoDuplicatesListOfCosts, FrequencyOfCosts, color = 'white')
    plt.plot(NoDuplicatesListOfCosts, FrequencyOfCosts, color = 'grey')
    plt.show()


testAppliance, testTimings = open_file("p2.txt")
costs, schedules, best_cost = task1(testAppliance, testTimings, 100000)

print(best_cost)
graph_task_1(costs)
print(schedules[0])
schedules[0].graph()
#The things above this are what we want to print off to complete task 1 so thats sorted.



#testTimings.graph(testAppliance)
#print(Solution(testAppliance, testTimings).cost)
