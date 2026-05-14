import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/HighSchools.csv')


login = input(print("Student Login ID: "))

while login is str:
    print("Your login was successful. Here are the average HSC marks 2023 to 2025.")
    print(df)
    break
else:
    print("You login attempt failed. Try again.")
    input(print("Student Login ID: "))




    
#x = df['Schools']
#y = df['Success Rate(%)']

#graph = plt.figure
#print(graph)