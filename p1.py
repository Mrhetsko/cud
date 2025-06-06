import pandas as pd
from setuptools.extern import names

# load file
df = pd.read_csv("assignment-database.csv")


issues = {
    "Missing values": [],
    "Names with blank spaces": [],
    "Non numeric prices": [],
    "Duplicate ids": []
}

def get_column_letter(index):
    return chr(65 + index)


#check missing values
for row in range(len(df)):
    for column in range(len(df.columns)):
        value = df.iat[row, column]
        if pd.isnull(value):
            cell = f'{get_column_letter(column)}{row + 2}' # +2 because first row is a header
            issues['Missing values'].append(cell)


# check non numeric
for row in range(len(df)):
    price = df.at[row, "Price"]
    # print(price)
    if not str(price).replace('.', '').isdigit():
        cell = f"D{row + 2}" #PRIce is D column
        issues['Non numeric prices'].append(cell)

# spaces
for row in range(len(df)):
    name = str(df.at[row, 'Product Name'])
    if name.startswith(" "):
        cell = f'B{row + 2}'
        issues['Names with blank spaces'].append(cell)

# Check duplicates
seen_ids = {}
for i in range(len(df)):
    pid = df.at[i, "Product ID"]
    if pid in seen_ids:
        issues["Duplicate ids"].append(f'A{seen_ids[pid]+2}')
        issues["Duplicate ids"].append(f'A{i+2}')
    else:
        seen_ids[pid] = i

if __name__ == '__main__':
    for issue_type, cells in issues.items():
        print(f'{issue_type}: {cells}')