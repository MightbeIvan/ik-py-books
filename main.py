import csv
#csv means Comma separated Values

with open("YA_Books.csv", mode = "r") as bookfile:
    # Mode "r" means read

    books = csv.reader(bookfile)
    #skip header row
    next(books)

    most_recent_published = 0 #starting low so that we get the first book
    ratings_ph = 5
    

    for book in books:
        title = book[0]
        author = book[1]

        #print all the authors who's names start with "M"
        #if author.startswith("M"):
        #   print(author)

        #get most recently publishes book
        year = int(book[2])
        rating = float(book[6])

        # if year > most_recent_published:
            # most_recent_published = year
            # most_recent_book = book

            #Get the boo with the worst rating and print it out

        if rating < ratings_ph:
            ratings_ph = rating

    # print(f"Most recently published: {most_recent_book}")
    # print (f"the worst rating is: {ratings_ph}")




#what is the highest rating for any book
    ratings_ph = 0
    


