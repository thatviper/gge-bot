towers = []
file = "./towers/greentowers.txt"
with open(file) as f:
    for line in f:
        x_cord,y_cord = line.split(":")
        towers.append((x_cord,y_cord))
        
print(towers)
                
