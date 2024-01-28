#program:   L2 calorie counter
#programmer:    ethian freyre-mijares
#start date:    1/17/2024
#end date
#purpose: calculate calories for an item

#input
name = "sushi"
carbs = 20
fats = 10
proteins = 15

#process
t_cals = (carbs*4) + (fats*9) + (proteins*4)

#output
print("total calories for:", name, "are", t_cals)
print("total calories for: {} are {}".format(name, t_cals))
print("thank you for your patronage")
