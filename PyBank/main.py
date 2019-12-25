import csv
import os
import pdb


def reader(path = "D:\GT Data Science and Analytics\Home_work\Python-Challenge\PyBank\Resources", file = "budget_data.csv"):
    """
    function accepts two parameters - the path to the cvs file and the file name, reads the file and returns two lists - date list\
    in month - year format as string and profit loss list in float. 
    """
    budget_csv = os.path.join(path, file)
    date_list = []
    profit_loss_lst = []
    try: # If separately ran, reader function will return None instead of generic error if path or file name is not correct
        with open(budget_csv, newline = '') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter = ',')
            next(csv_reader)    
            for line in csv_reader:
                date_list.append(line[0])
                profit_loss_lst.append(float(line[1]))
    except FileNotFoundError:
        csv_reader = None
    return date_list, profit_loss_lst


def writer(total_months, total, dates_gain, dates_loss, average, loss, gain, loss_index, gain_index):
    """
    Function writes the result to text file and prints out the same result to console.
    """
    with open("bank_results.txt", "w" ) as text:
        text.write(f"Financial Analysis\n--------------------------\nTotal Months: {total_months}\nTotal: {total}\nAverage Change: {average}\nGreatest Increase in Profits: {dates_gain} (${gain})\nGreatest Decrease in Profits: {dates_loss} (${loss})")
        print(f"Financial Analysis\n--------------------------\nTotal Months: {total_months}\nTotal: {total}\nAverage Change: {average}\nGreatest Increase in Profits: {dates_gain} (${gain})\nGreatest Decrease in Profits: {dates_loss} (${loss})")


def average_change(profit_loss):
    """
    Function returns average change of the numbers in the list using formula (last_element - first_element)/(number of elements - 1)
    """
    
    profit_loss_copy = profit_loss[:]
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
    	
    	difference = profit_loss[i+1] - profit_loss[i]

    	if (difference < greatest_loss):
            greatest_loss = profit_loss[i+1] - profit_loss[i]
            index_loss = i + 1
    	elif difference > greatest_gain:	        
            greatest_gain = difference
            index_gain = i + 1
            
    return greatest_loss, greatest_gain, index_loss, index_gain
        


         
def logic():
    """
    This is the main function that runs others. Gets returned values and lastly calls writer function.
    """
    dates, profit_loss = reader()
    average = average_change(profit_loss)
    loss, gain, loss_index, gain_index = greatest(profit_loss)
    total = sum(profit_loss)
    total_months = len(profit_loss)
    dates_gain  = dates[gain_index]
    dates_loss = dates[loss_index]
    
    writer(total_months, total, dates_gain, dates_loss, average, loss, gain, loss_index, gain_index)
    
    
logic()    
    




