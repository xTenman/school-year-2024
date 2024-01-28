#program: lab 2 week 2
#programmer: ethian
#date: 1/17/2024
#purpose: create a basic order form and demonstrate basic input-output processes
#
#input
#explicit
apple_item = str ("apple")
banana_item = str ("banana")
cabbage_item = str ("cabbage")
apple_qty = int (1)
banana_qty = int (5)
cabbage_qty = int (3)
#implicit
apple_price = 0.60
banana_price = 1.5
cabbage_price = 2.0
order_total = 0.0
name = "ethian freyre-mijares"

#process
apple_total = apple_qty * apple_price
banana_total = banana_qty * banana_price
cabbage_total = cabbage_qty * cabbage_price
order_total = apple_total + banana_total + cabbage_total

#output
print("Order for: {}".format(name))
print()
print("item# name     price qty   total")
print("1.-      {}     ${}   {}     ${}".format(apple_item, apple_price, apple_qty, apple_total))
print("2.-      {}  ${}   {}     ${}".format(banana_item, banana_price, banana_qty, banana_total))
print("3.-      {} ${}   {}     ${}".format(cabbage_item, cabbage_price, cabbage_qty, cabbage_total))
print("your total is: ${}".format(order_total))
