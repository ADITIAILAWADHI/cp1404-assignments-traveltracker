"""
Name: ADITI AILAWADHI
Date started: 17 March 2021
GitHub URL: https://github.com/CP1404-BNE-2020-SP22/cp1404-assignment-1---traveltracker-ADITIAILAWADHI/blob/master/README.md
brief program details:
MENU constant defined globally
def main():
     content from places.csv opened with mode r (only read) and appended to a list (csv_file_list).
     listed_places(list) for storing order of priority from csv_file_list.
     display Travel Tracker 1.0 - by Aditi Ailawadhi
     display total number of places loaded from places.csv stored in csv_file_list
     display MENU
     get user_input and character changed to uppercase
     while user_input not "Q":
           if user_input is "L":
               listed_places = list_places(csv_file_list)
           elif user_input is "A":
               added_place = add_new_place()
               display_added_place(csv_file_list, added_place)
           elif user_input is "M":
                 count = 0
                 for roww in csv_file_list:
                     value = roww.split(",")
                     if (value[3] == "n\n"):
                          count += 1
                 if count == 0:
                     print("No unvisited places")
                 else:
                     listed_places = list_places(csv_file_list)
                     marked_place = marked_place_validation(csv_file_list)
                     place = listed_places[marked_place - 1]
                     already_visited(csv_file_list, place)

           else user_input not from "Q"/"L"/"A"/"M":
               display Invalid menu choice
           display MENU
           get user_input and character changed to uppercase
    num = 0
    updated_csv_file_list = []
    for listt in listed_places:
        for item in csv_file_list:
            rows = item.split(",")
            if (int(rows[2]) == listed_places[num]):
                new_item = str(rows[0]) + "," + str(rows[1]) + "," + str(rows[2]) + "," + str(rows[3])
                updated_csv_file_list.append(new_item)
        num += 1
    updated_csv_file = open("places.csv", "w")
    for item in updated_csv_file_list:
            updated_csv_file.write(item)
    updated_csv_file.close()
    display total number of places saved to places.csv stored in csv_file_list
    display Have a nice day :)


def list_places(csv_file_list):
       lists of priority of non- visited places and visited places created.
       for rows in csv_file_list:
        text = rows.split(",")
        if text[3] == "n\n":
            non_visited.append(int(text[2]))
        else:
            visited.append(int(text[2]))
       combined list of non- visited priority and sorted visited priority lists created with sorted priority of visited visited places.
    display_list(csv_file_list, combined_list)    # display list as per combined list order
    return combined_list

def display_list(csv_file_list, combined_list):
       This prints displays the not visited places with "*" at the starting and visited places with " " at the starting.
       Additionally, if count of non- visited places is 0, it displays {} places. No places left to visit. Why not add
       a new place?".format(len(csv_file_list)).
       else , it displays "{} places. You still want to visit {} places.".format(len(csv_file_list), count).

def display_added_place(csv_file_list, added_place):
    new_row = str(added_place[0]) + "," + str(added_place[1]) + "," + str(added_place[2]) + "," + str(added_place[3])
    csv_file_list.insert(0, new_row)   # new row added at the 0 index of csv_file_list
    display "{} in {} (priority {}) added to Travel Tracker".format(added_place[0], added_place[1], added_place[2])

def add_new_place():
    add_row = ["", "", 0, ""]  # add_row list created.
    content = ""
    # Name and Country input validation in a single for loop.
    # validation for negative, 0 input and invalid value entered for Priority.
    add_row[3] = "n\n"   # add_row[3] will always be "n\n" of csv_file_list
    return add_row

def marked_place_validation(csv_file_list):
        # validation for the number of a place to mark as visited for negative , 0 and greater than len(csv_file_list).
        return user_input

def already_visited(csv_file_list, place):
    i = 0
    for j in csv_file_list:
        item = j.split(",")
        if (item[3] == "v\n") and (int(item[2]) == place):
            print("That place is already visited")
        elif (item[3] == "n\n") and (int(item[2]) == place):
            item[3] = "v\n"
            csv_file_list[i] = item[0] + "," + item[1] + "," + item[2] + "," + item[3]
            print("{} in {} visited!".format(item[0], item[1]))
        i += 1
"""
# MENU constant defined globally
MENU = """
L - List places
A - Add new place
M - Mark a place as visited
Q - Quit"""


def main():
    print("Travel Tracker 1.0 - by Aditi Ailawadhi")

    # content from places.csv opened with mode r (only read) and appended to a list (csv_file_list).
    csv_file = open("places.csv", "r")
    csv_file_list = []
    for content in csv_file:
        csv_file_list.append(content)
    csv_file.close()

    # listed_places for storing order of priority
    listed_places = []
    for rows in csv_file_list:
        text = rows.split(",")
        listed_places.append(int(text[2]))

    print("{} places loaded from places.csv".format(len(csv_file_list)))
    print("Menu: ", MENU)
    user_input = input(">>> ").upper()
    while user_input != "Q":

        if user_input == "L":
            listed_places = list_places(csv_file_list)

        elif user_input == "A":
            added_place = add_new_place()
            display_added_place(csv_file_list, added_place)

        elif user_input == "M":
            count = 0
            # checking count of unvisited places
            for roww in csv_file_list:
                value = roww.split(",")
                if (value[3] == "n\n"):
                    count += 1
            if count == 0:
                print("No unvisited places")
            else:
                listed_places = list_places(csv_file_list)
                marked_place = marked_place_validation(csv_file_list)
                place = listed_places[marked_place - 1]
                already_visited(csv_file_list, place)

        else:
            print("Invalid menu choice")
        print("Menu:", MENU)
        user_input = input(">>> ").upper()

    # finally code for "Q"- Quit runs that overwrites the places.csv with updated_csv_file_list content.
    num = 0
    updated_csv_file_list = []  # new list for adding the content of csv_file_list same as the display_list function sequence.
    for listt in listed_places:
        for value in csv_file_list:
            rows = value.split(",")
            # if value of index 2 of rows from csv_file_list is same as that of index num of the listed_places then the
            # particular row will be added to the updated_csv_file_list. It will run for all values of listed_places.
            if (int(rows[2]) == listed_places[num]):
                new_item = str(rows[0]) + "," + str(rows[1]) + "," + str(rows[2]) + "," + str(rows[3])
                updated_csv_file_list.append(new_item)
        num += 1
    updated_csv_file = open("places.csv", "w")
    for place in updated_csv_file_list:
            updated_csv_file.write(place)
    updated_csv_file.close()
    print("{} places saved to places.csv".format(len(csv_file_list)))
    print("Have a nice day :)")


def list_places(csv_file_list):
    non_visited = []  # list of priority of non- visited
    visited = []  # list of priority of visited
    for rows in csv_file_list:
        text = rows.split(",")
        if text[3] == "n\n":
            non_visited.append(int(text[2]))
        else:
            visited.append(int(text[2]))

    visited.sort()  # priority of visited- sorted

    combined_list = non_visited + visited  # combined list of non- visited priority and sorted visited priority lists

    display_list(csv_file_list, combined_list)    # display list as per combined list order
    return combined_list


def display_list(csv_file_list, combined_list):
    i = 1
    count = 0      # count of non- visited places
    list_index = 0
    for lst in combined_list:
        for rows in csv_file_list:
            text = rows.split(",")
            # if text[3] in csv_file_list == "n\n" and value of text index 2 from csv_file_list is same as that of list_index of the combined_list:
            if (text[3] == 'n\n') and (int(text[2]) == combined_list[list_index]):
                print("*{}. {:<8s} in {:<12s} priority {:2d}".format(i, text[0], text[1], int(text[2])))   # display * at the starting
                count += 1
            elif (text[3] == 'v\n') and (int(text[2]) == combined_list[list_index]):
                print(" {}. {:<8s} in {:<12s} priority {:2d}".format(i, text[0], text[1], int(text[2])))   # display " " at the starting
        list_index += 1
        i += 1

    if count == 0:
        print("{} places. No places left to visit. Why not add a new place?".format(len(csv_file_list)))
    else:
        print("{} places. You still want to visit {} places.".format(len(csv_file_list), count))


def display_added_place(csv_file_list, added_place):
    new_row = str(added_place[0]) + "," + str(added_place[1]) + "," + str(added_place[2]) + "," + str(added_place[3])
    csv_file_list.insert(0, new_row)   # new row added at the 0 index of csv_file_list
    print("{} in {} (priority {}) added to Travel Tracker".format(added_place[0], added_place[1], added_place[2]))


def add_new_place():
    add_row = ["", "", 0, ""]  # add_row list created.
    content = ""
    # Name and Country input validation
    for i in range(2):
        if i == 0:
            content = "Name"
        else:
            content = "Country"
        add_row[i] = str(input("{}: ".format(content)))
        while add_row[i] == "":
            print("Input can not be blank")
            add_row[i] = str(input("{}: ".format(content)))
    # validation for negative, 0 input and invalid value entered for Priority
    while True:
        try:
            add_row[2] = int(input("Priority: "))
            while add_row[2] <= 0:
                print("Number must be > 0")
                add_row[2] = int(input("Priority: "))
            break
        except ValueError:
            print("Invalid input; enter a valid number")
    add_row[3] = "n\n"   # add_row[3] will always be "n\n" of csv_file_list
    return add_row


def marked_place_validation(csv_file_list):
    while True:
        try:
            user_input = int(input("Enter the number of a place to mark as visited\n>>> "))
            while user_input <= 0 or user_input > len(csv_file_list):
                if user_input <= 0:
                    print("Number must be > 0")
                else:
                    print("Invalid place number")
                user_input = int(input("Enter the number of a place to mark as visited\n>>> "))
            return user_input
        except ValueError:
            print("Invalid input; enter a valid number")


def already_visited(csv_file_list, place):
    i = 0
    for j in csv_file_list:
        item = j.split(",")
        if (item[3] == "v\n") and (int(item[2]) == place):
            print("That place is already visited")
        elif (item[3] == "n\n") and (int(item[2]) == place):
            item[3] = "v\n"
            csv_file_list[i] = item[0] + "," + item[1] + "," + item[2] + "," + item[3]
            print("{} in {} visited!".format(item[0], item[1]))
        i += 1


if __name__ == '__main__':
    main()
