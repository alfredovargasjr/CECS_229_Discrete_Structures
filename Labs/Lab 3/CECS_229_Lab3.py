# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 16:16:28 2018

@author: Alfredo Vargas

CECS 229
Lab 3 / HW 5

Vectors: Policy Comparison
"""

# read the file
f = open('voting_record_dump109.txt')
votes = list(f)

# split string in votes into vectors
for i in range(len(votes)):
    line = votes[i]
    votes[i] = line.split()
   
# =============================================================================
# Task 2.12.1: Write a procedure create voting dict(strlist) that, given a list of
# strings (voting records from the source file), returns a dictionary that maps the last name
# of a senator to a list of numbers representing that senator’s voting record. You will need to
# use the built-in procedure int(·) to convert a string representation of an integer (e.g. ‘1’)
# to the actual integer (e.g. 1).
# =============================================================================

#    returns a list of list as a list:sublist    
def create_voting_dict(strlist): return { senator[0]:charListToIntList(senator[3:]) for senator in strlist}
#   returns list of char as a list of int
def charListToIntList(st): return [int(c) for c in st]

votes_Dict = create_voting_dict(votes)

# =============================================================================
# Task 2.12.2: Write a procedure policy compare(sen a, sen b, voting dict) that,
# given two names of senators and a dictionary mapping senator names to lists representing
# voting records, returns the dot-product representing the degree of similarity between two
# senators’ voting policies.
# =============================================================================

def policy_compare(sen_a, sen_b, voting_dict): return sum([voting_dict[sen_a][i] * voting_dict[sen_b][i] for i in range(len(voting_dict[sen_a]))])

# =============================================================================
# Task 2.12.3: Write a procedure most similar(sen, voting dict) that, given the name
# of a senator and a dictionary mapping senator names to lists representing voting records,
# returns the name of the senator whose political mindset is most like the input senator
# (excluding, of course, the input senator him/herself).
# =============================================================================

def most_similar(sen, voting_dict):
    senators = voting_dict.keys()
#   most_agreed[name, score]
    most_agreed = ['', -1]
    for senb in senators:
        if senb != sen:
            score = policy_compare(sen,senb,voting_dict)
            if score > most_agreed[1]:
                most_agreed[0] = senb
                most_agreed[1] = score
    return most_agreed[0]
            
# =============================================================================
# Task 2.12.4: Write a very similar procedure least similar(sen, voting dict) that
# returns the name of the senator whose voting record agrees the least with the senator whose
# name is sen.
# =============================================================================
def least_similar(sen, voting_dict):
    senators = voting_dict.keys()
#   least_agreed[name, score]
    least_agreed = ['', 100]
    for senb in senators:
        if senb != sen:
            score = policy_compare(sen,senb,voting_dict)
            if score < least_agreed[1]:
                least_agreed[0] = senb
                least_agreed[1] = score
    return least_agreed[0]

# =============================================================================
# Task 2.12.5: Use these procedures to figure out which senator is most like Rhode Island
# legend Lincoln Chafee. Then use these procedures to see who disagrees most with Pennsylvania’s
# Rick Santorum. Give their names.
# =============================================================================
print("Senator ", most_similar('Chafee', votes_Dict), " is most similar to Senator Chafee.\n","Senator ", least_similar('Santorum', votes_Dict), " is least similar to Santorum.")

# =============================================================================
# Task 2.12.6: How similar are the voting records of the two senators from your favorite
# state?
# =============================================================================

print("Senator Boxer and Senator Feinstein score: ",policy_compare('Boxer', 'Feinstein', votes_Dict))