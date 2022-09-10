class County:
    def __init__(self, init_name, init_population, init_voters):
        self.name = init_name
        self.population = init_population
        self.voters = init_voters
        self.percentage = (self.voters/self.population)
def highest_turnout(data) :
    county = data[0]
    turnout = data[0].percentage
    for item in data:
        print(item.name)
        print(item.percentage)
        if item.percentage >= turnout:
            county = item.name
            turnout = item.percentage
    return county, turnout
allegheny = County("allegheny", 1000490, 645469)
philadelphia = County("philadelphia", 1134081, 539069)
montgomery = County("montgomery", 568952, 199591)
lancaster = County("lancaster", 345367, 130278)
delaware = County("delaware", 414031, 184538)
chester = County("chester", 319919, 130823)
bucks = County("bucks", 444149, 119816)
data = [allegheny, philadelphia, montgomery, lancaster, delaware, chester, bucks]
result = highest_turnout(data) # do not change this line!
print(result) # prints the output of the function
# do not remove this line!
