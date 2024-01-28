#program:   L3 calorie counter
#programmer:    ethian freyre-mijares
#start date:    1/24/2024
#end date
#purpose: calculate calories for an item

#input
name = input("enter item name: ")
carbs = int(input("how many grams of carbs does this have?: "))
fats = int(input("how many grams of fat does this have?: "))
proteins = int(input("How many grams of protein does this have?:  "))

#process
t_cals = (carbs*4) + (fats*9) + (proteins*4)

#output
print("total calories for: {} are {}".format(name, t_cals))
print("thank you for your patronage")
