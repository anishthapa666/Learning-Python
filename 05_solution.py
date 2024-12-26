# To chose the mode of transport based on the distance needed to cover
distance= 16

if distance < 3 :
    mode = "walk"
elif distance <=15:
    mode = "bus"
elif distance > 15:
    mode = "train" 
print(mode)