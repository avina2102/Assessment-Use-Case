import pandas as pd
import matplotlib.pyplot as plt

#Change for testing

df = pd.read_excel('Book 1.xlsx')

x = df['Schools']
y = df['Success Rate(%)']

plt.figure