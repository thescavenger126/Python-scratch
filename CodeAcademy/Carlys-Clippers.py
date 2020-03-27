# Types of hairstyles
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

# Original prices given, find avg price of all
prices = [30, 25, 40, 20, 20, 35, 50, 35]
total_price = 0
for cost in prices:
  total_price += cost

avg_price = total_price/len(prices)
print("Average Haircut Price: "+ str(avg_price))
# Drop all prices by $5 to drop avg by $5
new_prices = [(cost-5) for cost in prices]
print(new_prices)

# Number of haircuts completed in order by type of cut
last_week = [2, 3, 5, 8, 4, 4, 6, 2]
# Find total revenue based on number of cuts of each type and cost of cuts
total_revenue = 0
for i in range(len(hairstyles)):
  total_revenue += (last_week[i])*(prices[i])
print("Total Revenue: "+ str(total_revenue))

# Revenue per day
avg_dly_rev = total_revenue/7
print(avg_dly_rev)

# Find out which cuts are under $30 for advertising purposes
cuts_under_30 = [hairstyles[i] for i in range(len(new_prices)-1) if new_prices[i]<30]
print(cuts_under_30)