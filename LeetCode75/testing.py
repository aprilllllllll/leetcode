def findMinCost(demand):
    print(demand)
    new_demand = []
    count = 1
    new_demand.append(count)

    for i in range(2, len(demand)):
        if demand[i] > demand[i-1]:
            count += 1
        elif demand[i] < demand[i-1]:
            count -= 1
        new_demand.append(count)
    
    print("new_demand:", new_demand)
    
    left = 0
    max_len = 0
    l = []
    
    for right in range(len(new_demand)):
        while new_demand[right] in l:
            l.remove(new_demand[left])
            left += 1
        l.append(new_demand[right])
        max_len = max(max_len, right - left + 1)
    
    return max_len

print(findMinCost(demand=[224819349, 472695727, 813613483, 989158287, 784836922, 878317643, 159430960, 154740056, 311066165, 924351734]))