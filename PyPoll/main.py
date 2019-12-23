import csv
import os

def reader(path = "D:\GT Data Science and Analytics\Home_work\Python-Challenge\PyPoll\Resources", file = "election_data.csv"):
    """
    function accepts two parameters - the path to the cvs file and the file name, reads the file and returns two lists - voters' list\
    in as int candidates list in string format. 
    """
    election_csv = os.path.join(path, file)
    voters_list = []
    candidate_votes = []
    try:
        with open(election_csv, newline = '') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter = ',')
            next(csv_reader)   
            for line in csv_reader:
                voters_list.append(int(line[0]))
                candidate_votes.append(str(line[2]))
    except FileNotFoundError:
        csv_reader = None
    #print(len(voters_list)) # This and following print statement is to check for duplicate ids that will indicate
                            #that one or more people voted more than once
    #print(len(set(voters_list))) 
    return voters_list, candidate_votes

def writer(total, khan, correy, li, tooley, winner):
    with open("election_results.txt", "w" ) as text:
        text.write(f"Election Results\n-----------------------------------\nTotal Votes: {total}\nKhan: {round(khan/total *100, 3)}% {khan}\nCorrey: {round(correy/total*100, 3)}% {correy}\nLi: {round(li/total*100, 3)}% {li}\nO'Tooley: {round(tooley/total*100,3)}% {tooley}\n-----------------------------------\nWinner: {winner}\n-----------------------------------")
        print(f"Election Results\n-----------------------------------\nTotal Votes: {total}\nKhan: {round(khan/total *100, 3)}% {khan}\nCorrey: {round(correy/total*100, 3)}% {correy}\nLi: {round(li/total*100, 3)}% {li}\nO'Tooley: {round(tooley/total*100,3)}% {tooley}\n-----------------------------------\nWinner: {winner}\n-----------------------------------")


def election_results(candidates):
    """This function iterates through the votes and adds 1 for each candidate every time their name appears in the list and returns votes for each candidate"""
    khan_count = 0
    correy_count = 0
    li_count = 0
    otooley_count = 0
    
    for i in candidates:
        if i == 'Khan':
            khan_count += 1
        elif i == 'Li': 
            li_count += 1
        elif i == 'Correy':
            correy_count += 1
        else:
            otooley_count += 1
    
    return khan_count, correy_count, li_count, otooley_count
     

def logic():
    """
    This is the main function that calls reader and based on the returned values calls election_results function. The function prints put the final results.
    """
    votes_final = {}
    ids, votes = reader()
    khan, correy, li, tooley = election_results(votes)
    votes_final["Khan"] = khan
    votes_final["Correy"] = correy
    votes_final["Li"] = li
    votes_final["O'Tooley"] = tooley
    winner = max(votes_final, key = lambda k: votes_final[k])
    total = khan + correy + li + tooley
    writer(total, khan, correy, li, tooley, winner)



logic()