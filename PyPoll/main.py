import csv
import os

def reader(path = "D:/GT Data Science and Analytics/Home_work/Python-Challenge/PyPoll/Resources", file = "election_data.csv"):
    """
    function accepts two parameters - the path to the cvs file and the file name, reads the file and returns two lists - voters' list\
    in as int candidates list in string format. 
    """
    election_csv = os.path.join(path, file)
    voters_list = []
    candidate_votes = []
    try: # If separately ran, reader function will return None instead of generic error if path or file name is not correct
        with open(election_csv, newline = '') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter = ',')
            next(csv_reader)   
            for line in csv_reader:
                voters_list.append(int(line[0]))
                candidate_votes.append(str(line[2]))
    except FileNotFoundError:
        csv_reader = None
    #print(len(voters_list)) # This and following print statement is to check for duplicate ids that will indicate
                            #that one or more people voted more than once. After I made sure that there are no
                            #duplicate votes I commented these print functions.
    #print(len(set(voters_list))) 
    return voters_list, candidate_votes

def writer(total, khan, correy, li, tooley, winner):
    """
    Function writes the results to text file and prints out the same result to console.
    """
    with open("election_results.txt", "w" ) as text:
        text.write(f"Election Results\n-----------------------------------\nTotal Votes: {total}\nKhan: {round(khan/total *100, 3)}% {khan}\nCorrey: {round(correy/total*100, 3)}% {correy}\nLi: {round(li/total*100, 3)}% {li}\nO'Tooley: {round(tooley/total*100,3)}% {tooley}\n-----------------------------------\nWinner: {winner}\n-----------------------------------")
        print(f"Election Results\n-----------------------------------\nTotal Votes: {total}\nKhan: {round(khan/total *100, 3)}% {khan}\nCorrey: {round(correy/total*100, 3)}% {correy}\nLi: {round(li/total*100, 3)}% {li}\nO'Tooley: {round(tooley/total*100,3)}% {tooley}\n-----------------------------------\nWinner: {winner}\n-----------------------------------")


def election_results(candidates):
    """
    This function iterates through the votes and adds 1 for each candidate every time their name appears in the dictionary and returns the final results in dictionary.
    """
    _results = {}
    for candidate in candidates:
    	if candidate not in _results:
    		_results[candidate] = 1
    	else:
    		_results[candidate] += 1
 
    return _results
   
     

def logic():
    """
    This is the main function that calls reader and based on the returned values calls election_results function. Then necessary values are sent to writer function.
    """
    votes_final = {}
    ids, votes = reader()
    final_results = election_results(votes)

    winner = max(final_results, key = lambda k: final_results[k])
    khan  = final_results['Khan']
    correy = final_results['Correy'] 
    li = final_results['Li']
    tooley = final_results["O'Tooley"]
    total = khan + correy + li + tooley
 
    writer(total, khan, correy, li, tooley, winner)



logic()