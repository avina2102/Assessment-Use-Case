import pandas as pd
import matplotlib.pyplot as plt
from string import ascii_letters, digits

df = pd.read_csv('data/HighSchools.csv')

login = input("Student Login ID: ")

while any(char.isdigit() for char in login):
    print("Your login attempt has failed. Try again.")
    input("Student Login ID: ")
    if set(login).difference(ascii_letters + digits):
        print("Your login attempt has failed. Try again.")
        input("Student Login ID: ")
    elif isinstance(login, str):
        print("Your login was successful. Here are the average HSC marks 2023 to 2025.")
        print(df)
        break
    else:
        print("Your login attempt has failed. Try again.")
        input("Student Login ID: ")

#graph = df.plot(x='Schools', y='Success Rate(%)', kind='line')
#plt.show(graph)