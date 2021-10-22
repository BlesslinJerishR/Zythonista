import random

# Generating random 8 integers in a array
harray = list(random.randrange(1,100,1) for count in range(8))
print(harray)

high = max(harray)
low  = min(harray)
# print(high)
# print(low)

# Driver Code
driver = list()
driver.append(high)
driver.append(low)
orginal = list(org for org in harray if org not in driver)
print(driver + orginal)