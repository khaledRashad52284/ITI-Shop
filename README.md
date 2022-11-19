# ITI-Shop
print("Welcome to ITI shop")
table={
	"Banana":10 ,
	"Apple":20,
	"Tomato":5
}
bill=0
bill=int(bill)
product=["Banana","Apple","Tomato","Ay 7aga"]
while 1:
	x=input ("For customer press one , \nfor owner press two.\n")
	x=int(x)
	if x == 1:
		print("Customer mode ")
		y=input("To show our product press 1 \nTo Buy from our products press 2 \nto print the bill press 3\n")
		y=int(y)
		if y==1:
			print(product)
		if y==2:
			c=input("To sellect banana press 1 \nTo sellect Apple press 2\nTo sellect Tomato press 3\n")
			c=int(y)
			if y==1:
				print("the price of banana is :{}".format(table["Banana"]))
				order=input("To sellect banana enter the ammount in kg\nto print the bill or exit enter 0\n")
				order=int(order)
				if order!=0:
					
					#bill=int(bill)
					bill+=order*table["Banana"]
					z=input("To print the bill press 1\nto exit press 0")
					z=int(z)

					if z==1:
						y=3
					
			if c==2:
				print("the price of Apple is :{}".format(table["Apple"]))
				order=input("To sellect Apple enter the ammount in kg\nto print the bill or exit enter 0")
				order=int(order)
				if order!=0:
					#bill=int(bill)
					bill+=order*table["Apple"]
					z=input("To print the bill press 1\nto exit press 0")
					z=int(z)

					if z==1:
						y=3
			if c==3:
				print("the price of Tomato is :{}".format(table["Tomato"]))
				order=input("To sellect Tomato enter the ammount in kg\nto print the bill or exit enter 0")
				order=int(order)
				if order!=0:
					#bill=int(bill)
					bill+=order*table["Tomato"]
					z=input("To print the bill press 1\nto exit press 0")
					z=int(z)
					if z==1:
						y=3
		if y==3:
			m=1;
			while m==1:
				if y==3:
					ammount=input("please Enter the ammount in kg \n")
					ammount=int(ammount)
					type=input("please isert the type \n")
					bill+=ammount*table[type]
					print("The cost of {} = {}".format(type,cost))
					y=0
				n=input("To add other product Enter one , \nor to print the total cost enter 2\n")
				n=int(n)
				if n==1:
					ammount=input("please Enter the ammount in kg \n")
					ammount=int(ammount)
					type=input("please isert the type \n")
					bill+=ammount*table[type]
				
				else:
					print("The total cost = {}".format(bill));
					m=0;
		else :
			print("Wrong anwer")

	elif x==2:
		print("Owner mode")

	else :
		print("Wrong answer")
