from art import text
prices = {
 "Crisps": 50,
 "Crisps2": 50,
 "Chocolate": 75,
 "Chocolate2": 80,
 "Sweets": 40,
 "Sweets2": 60,
 "Sandwich": 120,
 "Sandwich2": 140,
 "Drink": 95,
 "Drink2": 150
}
print(text)
for key, value in prices.items():
    print(key, ":", value)
choice = input("what item:")
print("----",choice ,"selected----")
cost = prices.get(choice)
insert=int(input("insert money:"))
print("------",insert,"inserted------")
if cost < insert:
 change = insert-cost
 print("thank you for your purchase you will recieve ",change,"p in change")
elif insert < cost:
 print("not enough money has been inserted please try again")
else: 
 print("thank you for your purchase")
