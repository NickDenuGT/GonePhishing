import pandas as pd
df = pd.read_csv("dataset.csv")

column_items = df.url

for item in column_items:
    digits = 0
    subdomains = 0
    for character in item:
        if character.isnumeric():
            digits += 1
        if character == ".":
            subdomains += 1
    print(subdomains)
