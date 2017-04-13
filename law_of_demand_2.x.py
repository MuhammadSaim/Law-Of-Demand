#import matplotlib and time module
import matplotlib.pyplot as plt
import time


# 
# Project        :   Economics Law of demand
# Author         :   Muhammad Saim
# Email          :   muhammadsaim494@gmail.com
# version        :   1.0v
# Python Version : 	 2.7v
# 

# print "Project        : Economics Law Of Demand"
# print "Author         : Muhammad Saim"
# print "Email          : muhammadsaim494@gmail.com"
# print "Version        : 1.0v"
# print "Python Version : 2.7v\n\n"


# decalring all veriables 
points_of_demand = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
price = []
demand = []
totallPrices = 0
number_of_pricess = 0
number = 0


# making graph
def making_graph(price, demand):
	plt.plot(price,demand,'ro')
	plt.ylabel('Price')
	plt.xlabel('Demand')
	plt.show()


# show the result
def show(price, demand, points_of_demand):
	print "\n\n"
	print "\tP\tD\tPoint of Demand"
	totallPrices = len(price)
	for show in range(0, totallPrices):
		print "\t",price[show],"|\t",demand[show],"|\t",points_of_demand[show]
	making_graph(price, demand)



# making demand list
def making_demand(price):
	for d in reversed(price):
		demand.append(d)
	show(price, demand, points_of_demand)



# check input is an intiger
def check_input():
	try:
		p = int(raw_input("Enter Price Value: "))
		price.append(p)
	except ValueError:
		print "Please Type Only Number"
		time.sleep(2)
		input_pricess(totallPrices)



# input function for pricess
def input_pricess(number_of_pricess):
	number_of_pricess = number_of_pricess + 1
	for input in range(1,number_of_pricess):
		check_input()
	making_demand(price)



# input function for input tottal numbers of prices
def input_total_price_number(message):
	try:
		totallPrices = int(raw_input(message))
		input_pricess(totallPrices)
	except ValueError:
		print "Please Type Only Number"
		time.sleep(2)
		input_total_price_number(message)



# Calling the function for execute programme 
input_total_price_number("Enter a Totall Number of Prices: ")