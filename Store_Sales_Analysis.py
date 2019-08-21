# Analysis of a Store/Shop Daily Sales
# Coding : Syed Azam Hassan
t = [['17/08/2019', 45000],
     ['18/08/2019', 58000],
     ['19/08/2019', 35000],
     ['20/08/2019', 39500]]
t_max = (max(t, key=lambda x: x[1]))
t_min = (min(t, key=lambda x: x[1]))
print("Max. sale of the day          : ",t_max[1])
print("Date when there was max sale  : ",t_max[0])
print("Min. sale                     : ",t_min[1])
print("Date of min sale              : ",t_min[0])
print("Average daily sale            : ",sum([n[1] for n in t])/len(t))
print("Variation between max/min sale: ",t_max[1] - t_min[1])