#Hill climbing
def calfunc(x, y): 
    return 3 - (x*2 + y*2) 
 
def findneighbors(x, y): 
    list2 = [] 
    list2.append([x + 1, y + 1]) 
    list2.append([x - 1, y - 1]) 
    list2.append([x + 1, y - 1]) 
    list2.append([x - 1, y + 1]) 
    return list2 
 
x = int(input("Enter initial value for x: ")) 
y = int(input("Enter initial value for y: ")) 
 
while True: 
    list1 = [] 
    opt = calfunc(x, y) 
    neighbors = findneighbors(x, y) 
    for i in range(len(neighbors)): 
        list1.append(calfunc(neighbors[i][0], neighbors[i][1])) 
    max_val = max(list1) 
    index = list1.index(max_val) 
    x_new, y_new = neighbors[index][0], neighbors[index][1] 
     
    if calfunc(x_new, y_new) <= opt: 
        break 
    x, y = x_new, y_new 
    print(f"New x: {x}, New y: {y}")
