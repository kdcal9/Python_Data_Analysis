#import necessary modules
import os
os.getcwd
import pandas as pd

#Import csv and read csv file
import csv
csvpath = os.path.join('budget_data.csv')

budget_data_df = pd.read_csv('budget_data.csv')
budget_data_df.head()


#get number of months
month_count = len(budget_data_df["Date"].unique())
month_count

#get total profit and losses
total_profitloss = budget_data_df["Profit/Losses"].sum()
print(total_profitloss)


# Greatest Increase & Decrease
budget_data_df['Profit/Loss_Shifted']=budget_data_df['Profit/Losses'].shift(1)

#create a column to record the chnage between shifted value(previous month) and the current month
budget_data_df['Change']=budget_data_df['Profit/Losses']-budget_data_df['Profit/Loss_Shifted']
print("Average Change: $"+str(round(budget_data_df['Change'].mean(),2)))

#print the maximum positive change 
print("Greatest Increase in Profits: " +budget_data_df['Date'][budget_data_df['Change'] == budget_data_df['Change'].max()].iloc[0]+ " ($"+str(int(budget_data_df['Change'].max()))+")")

#print the maximum negative change  
print("Greatest Increase in Profits: " +budget_data_df['Date'][budget_data_df['Change'] == budget_data_df['Change'].min()].iloc[0]+ " ($"+str(int(budget_data_df['Change'].min()))+")")

#Print Summary Table to text file

print("Financial Analysis", file=open("outputpybank.txt", "a"))
print("----------------------------", file=open("outputpybank.txt", "a"))
print ("Total Months:" ,budget_data_df['Date'].nunique(), file=open("outputpybank.txt", "a"))
print("Total: $"+str(budget_data_df['Profit/Losses'].sum()), file=open("outputpybank.txt", "a"))
print("Average Change: $"+str(round(budget_data_df['Change'].mean(),2)), file=open("outputpybank.txt", "a"))
print("Greatest Increase in Profits: " +budget_data_df['Date'][budget_data_df['Change'] == budget_data_df['Change'].max()].iloc[0]+ " ($"+str(int(budget_data_df['Change'].max()))+")", file=open("outputpybank.txt", "a"))
print("Greatest Increase in Profits: " +budget_data_df['Date'][budget_data_df['Change'] == budget_data_df['Change'].min()].iloc[0]+ " ($"+str(int(budget_data_df['Change'].min()))+")", file=open("outputpybank.txt", "a"))

#print to terminal
f = open('outputpybank.txt', 'r')
file_contents = f.read()
print (file_contents)