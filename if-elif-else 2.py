weight = 10
distance = 120
if weight<= 10:
    if distance<= 100:
        shipping_cost= 10
    else:
        shipping_cost= 25
else:
    if distance<= 100:
        shipping_cost = 20
    else:
        shipping_cost = 40
print("The shipping cost is: ",shipping_cost)