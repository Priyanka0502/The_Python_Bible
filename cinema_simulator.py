films={
    "titanic":{"age_limit":16,"Tickets":2},
    "fault in our stars":{"age_limit":14,"Tickets":8},
    "little women":{"age_limit":12,"Tickets":5},
    "avengers":{"age_limit":8,"Tickets":15},
     }

while True:
    choice=input("Which film you want to see?").lower()
    if choice in films:
        age=int(input("how old are you").strip())
        if age>=films[choice]["age_limit"]:
            num_seats=films[choice]["Tickets"]
            if num_seats>0:
                print("enjoy the film!!")
                films[choice]["Tickets"]=films[choice]["Tickets"]-1
            else:
                print("Ooops Sorry,We are sold out!!")

        else:
            print("you are too old to watch the film")
    else:
        print("we donot have that film....")


