with open("india_housing_prices.csv", 'r') as fp:
    file_data = fp.read()

capitalize_firstword = file_data.title().replace(',','|')

with open ("Updated_india_housing_prices.csv", 'w') as fp:
    fp.write(capitalize_firstword)
print("Updated file ")
