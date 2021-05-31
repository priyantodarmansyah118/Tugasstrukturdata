
def minmax(data):
    smallest = largest = data[0]
    for entry in data:
        if smallest > entry:
            smallest = entry
        if largest < entry:
            largest = entry
    return (smallest, largest)


print(minmax([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]))
