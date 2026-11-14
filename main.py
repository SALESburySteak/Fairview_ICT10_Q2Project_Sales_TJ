from pyscript import display, document


def check(e):
    #list of members
    members = ["Tyler Sales", "Lance Bendana", "Jilliane Tech", "Therese Reyes", "Bianca Ledres", "Carlos Borromeo"]
    document.getElementById("output").innerHTML = "" #reset the input so that it doesn't stack up

    a = document.getElementById("firstname").value #retrieves the inputs of the user
    b = document.getElementById("lastname").value

    name = (a + " " + b) #merges the first name and the last name along with a space
    memberchecker = name in members #checks if the name is in the list, returns a boolean value

    status = [
        (f"Sorry, {name}. You are not included in the club."), #if member is not included, this will be displayed
        (f"Congratulations {name}! You are included in the club.") #if member is included, this will be displayed
        ]

    document.getElementById("output").innerHTML = status[memberchecker]  #output based on memberchecker boolean value