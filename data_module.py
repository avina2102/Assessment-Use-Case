import pandas as pd
import matplotlib.pyplot as plt
from string import ascii_letters, digits

#Loading CSV

data = pd.read_csv("Data Spreadsheet.csv",encoding='latin-1')

while True:
    login = input("Student Login ID (only alphabet, no spaces): ")
    if not login.isalpha():
        print("Your login attempt has failed. Try again.\n")
    else:
        input("Password: ")
        print("\nYour login was successful.")
        break

student = int(input(("What is the average of your results in school (%) ? ")))

def get_range(student):
    if 90 <= student <= 100:
        return "90-100"
    elif 80 <= student < 90:
        return "80-90"
    elif 70 <= student < 80:
        return "70-80"
    elif 60 <= student < 70:
        return "60-70"
    elif 50 <= student < 60:
        return "50-60"
    elif 40 <= student < 50:
        return "40-50"
    elif 30 <= student < 40:
        return "30-40"
    elif 20 <= student < 30:
        return "20-30"
    elif 10 <= student < 20:
        return "10-20"
    else:
        return "0-10"

student_range = get_range(student)

print("Your range is:", student_range)
filtered_data = data[data["Range"] == student_range]

plt.figure(figsize=(8, 8))

plt.barh(
    filtered_data["School"],
    filtered_data["Success Rate (%)"]
)

plt.xlabel("Percentage")
plt.ylabel("Schools")
plt.title(f"Schools for range {student_range}")
plt.gca().invert_yaxis()
plt.yticks(fontsize=4)
plt.show()

print("Those are the most suitable and recommended schools for you based on your capability. ")
print("See you next time! ")



