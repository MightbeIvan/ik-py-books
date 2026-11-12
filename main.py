import csv
import matplotlib.pyplot as plt
import numpy as np
#csv means Comma separated Values

with open("YA_Books.csv", mode = "r") as bookfile:
    # Mode "r" means read

    books = csv.reader(bookfile)
    #skip header row
    next(books)

    

    for book in books:
        title = book[0]
        author = book[1]
        year = int(book[2])
        number_of_pages = int(book[5])
        rating = float(book[6])
        

        ratings_ph = 0
        n_o_p_ph = 0
        
        #Highest rating book
        if ratings_ph < rating:
            ratings_ph = rating
            
    

        #How many different publishers are represented in the dataset
        publisher_count= 0

        for book in books:
            publisher_count += 1
               
    
    

print (f" The highest rating for any book in the dataset is {rating}")
print(f"There are {publisher_count} publishers represented in this dataset")


x = ["Highest Rating ", "Publisher Count"]
y= [rating,publisher_count]
plt.bar(x,y)
plt.show()