import pymongo
from pymongo import MongoClient

client = MongoClient('mongodb+srv://Zed:Walter@cluster0.jhe6s.mongodb.net/?retryWrites=true&w=majority')
db = client["Books"]
collection = db["Info"]

choice = -1
while choice != "0":
    print("0) Quit Program")
    print("1) Display Books")
    print("2) Add Books")
    print("3) Delete Books")
    print("4) Update Books")
    choice = input("> ")
    if choice == "1":
        #Display a list of all books
        results = collection.find({})
        print("{:>10}  {:>15}  {:>10}  {:>8}".format("Title", "Author", "Status", "Score"))
        for result in results:
            print("{:>10}  {:>15}  {:>10}  ".format(result[0], result[1], result[2]), result[3])
    elif choice == "2":
        #Add a new book
        title = input("Title: ")
        author = input("Author: ")
        status = input("Status: ")
        score = input("Score: ")
        post = {
            "Title": title,
            "Author": author,
            "Status": status,
            "Score": score
        }
        collection.insert_one(post)
    elif choice == "3":
        #Delete a book from the list
        title = input("Title: ")
        collection.delete_one({"Title": title})
    elif choice == "4":
        #Update a book status or score
        print("1) Update Status")
        print("2) Update Score")
        update_choice = input("> ")
        if update_choice == "1":
            title = input("Title: ")
            status = input("Status: ")
            collection.update_one({"Title": title},{"$set": {"status": status}})
        elif update_choice == "2":
            title = input("Title: ")
            score = input("Score: ")
            collection.update_one({"Title": title},{"$set": {"score": score}})

