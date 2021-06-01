#import necessary modules
import os
os.getcwd
import pandas as pd

#Import csv and read csv file
import csv
csvpath = os.path.join('election_data.csv')

election_data_df = pd.read_csv('election_data.csv')
election_data_df.head()

#The total number of votes cast
print("Total Votes:" , election_data_df['Voter ID'].count())

#A complete list of candidates who received votes
print("List of Candidates:" , election_data_df['Candidate'].unique())

#The percentage of votes each candidate won
votes_candidate =election_data_df.groupby('Candidate')['Voter ID'].count().reset_index(name='Count').sort_values('Count',ascending=False)

votes_candidate['Percent']=round(votes_candidate.Count/votes_candidate.Count.sum()*100,5)
votes_candidate

#print results
print("Election Results", file=open("outputpoll.txt", "a"))
print("-------------------------", file=open("outputpoll.txt", "a"))
print ("Total Votes:" ,election_data_df['Voter ID'].count(), file=open("outputpoll.txt", "a"))
print("-------------------------", file=open("outputpoll.txt", "a"))
for index, row in votes_candidate.iterrows():
    print (row['Candidate']+": ",str('%.3f'%row['Percent'])+"% ","("+str(row['Count'])+")", file=open("outputpoll.txt", "a"))
print("-------------------------", file=open("outputpoll.txt", "a"))
print("Winner: ", votes_candidate['Candidate'][votes_candidate['Percent'] == votes_candidate['Percent'].max()].iloc[0], file=open("outputpoll.txt", "a"))
print("-------------------------", file=open("outputpoll.txt", "a"))

#print to terminal
f = open('outputpoll.txt', 'r')
file_contents = f.read()
print (file_contents)