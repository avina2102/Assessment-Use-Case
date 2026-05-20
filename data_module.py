import pandas as pd
import matplotlib.pyplot as plt
from string import ascii_letters, digits

#Loading CSV
df = pd.read_csv('Data Spreadsheet(Sheet1) (1).csv')

while True:
    login = input("Student Login ID: ")
    if not login.isalpha():
        print("Your login attempt has failed. Try again.\n")
    else:
        print(input("Password: "))
        print("\nYour login was successful.")
        break

student = int(input(("What is the average of your results in school (%) ? ")))

if 90<= student <=100:
    print("Choosing one of these schools is recommended. Here is a visualisation.")
    print()
elif 80<= student <90:
    print("Choosing one of these schools is recommended. Here is a visualisation.")
    print()
elif 70<= student <80:
    print("Choosing one of these schools is recommended. Here is a visualisation.")
    print()
elif 60<= student <70:
    print("Choosing one of these schools is recommended. Here is a visualisation.")
    print()
elif 50<= student <60:
    print("Choosing one of these schools is recommended. Here is a visualisation.")
    print()
elif 40<= student <50:
    print("Choosing one of these schools is recommended. Here is a visualisation.")
    print()
elif 30<= student <40:
    print("Choosing one of these schools is recommended. Here is a visualisation.")
    print()
elif 20<= student <30:
    print("Choosing one of these schools is recommended. Here is a visualisation.")
    print()
elif 10<= student <20:
    print("Choosing one of these schools is recommended. Here is a visualisation.")
    print()
elif 0<= student <10:
    print("Choosing one of these schools is recommended. Here is a visualisation.")
    print()

print("See you next time! ")




#graph = df.plot(x='Schools', y='Success Rate(%)', kind='line')
#plt.show(graph)