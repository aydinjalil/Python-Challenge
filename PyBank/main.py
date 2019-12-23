import csv
import os
import pdb
def average_change(profit_loss):
    
    """
    Function returns average change of the numbers in the list using formula (last_element - first_element)/(number of elements - 1)
    """
    
    profit_loss_copy = profit_loss[:]
    print(profit_loss_copy)
    #pr_loss_diff = []
    average_ch = (profit_loss_copy[-1] - profit_loss_copy[0])/(len(profit_loss_copy)-1)
    return round(average_ch, 2)
    
    
def greatest (profit_loss):
    """
    Function iterates through the list of numbers and returns greatest_difference between the two consecutive numbers,\n
    greatest negative difference between the two consecutive numbers and the index of the second element in the sequence. 
    """
    index_loss = 0
    index_gain = 0
    greatest_loss = 0
    greatest_gain = 0
    for i in range(len(profit_loss) - 1):
        if profit_loss[i+1] - profit_loss[i] < greatest_loss:
            greatest_loss = profit_loss[i+1] - profit_loss[i]
            index_loss = i+1
        if profit_loss[i+1] - profit_loss[i] > greatest_gain:
            greatest_gain = profit_loss[i+1] - profit_loss[i]
            index_gain = i+1
    return greatest_loss, greatest_gain, index_loss, index_gain
        

def reader(path = "D:\GT Data Science and Analytics\Home_work\Python-Challenge\PyBank\Resources", file = "budget_data.csv"):
    """
    function accepts two parameters - the path to the cvs file and the file name, reads the file and returns two lists - date list\
    in month - year format as string and profit loss list in float. 
    """
    budget_csv = os.path.join(path, file)
    date_list = []
    profit_loss_lst = []
    with open(budget_csv, newline = '') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = ',')
        next(csv_reader)    
        for line in csv_reader:
            date_list.append(line[0])
            profit_loss_lst.append(float(line[1]))
    return date_list, profit_loss_lst
        
    
    #print(date_list[index])
    
def logic():
    
    """
    This is the main function that runs others
    """
    dates, profit_loss = reader()
    average = average_change(profit_loss)
    loss, gain, loss_index, gain_index = greatest(profit_loss)
    
    print(f"Financial Analysis\n--------------------------\nTotal Months: {len(profit_loss)}\nTotal: {sum(profit_loss)}\nAverage Change: {average}\nGreatest Increase in Profits: {dates[gain_index]} (${gain})\nGreatest Decrease in Profits: {dates[loss_index]} (${loss})")
    

def writer():
    pass
logic()    
    




