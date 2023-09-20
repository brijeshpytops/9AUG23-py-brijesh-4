import pandas as pd

data = pd.read_json('data.json')
print(data.columns)
lis_data = []
for i in data.iterrows():
    prepdict = {}
    print("=========")
#     print(type(i))
    prepdict['name'] = i[1]['name']
    prepdict['email'] = i[1]['email']
    prepdict['phone'] = i[1]['phone']
    prepdict['date'] = i[1]['date']
    print(prepdict)
    lis_data.append(prepdict)
#     print("=========")
# print(data['name'].tolist())
# print(data)

# Create a DataFrame from the list of dictionaries
df = pd.DataFrame(lis_data)

# Create an Excel writer object
writer = pd.ExcelWriter('users.xlsx', engine='xlsxwriter')

# Convert the DataFrame to an Excel object
df.to_excel(writer, sheet_name='Sheet1', index=False)

# Save the Excel file
writer._save()

print("Excel file 'users.xlsx' has been created.")