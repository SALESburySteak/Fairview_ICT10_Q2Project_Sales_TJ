from pyscript import display, document

def addmember(e):
    a = document.getElementById("firstname").value
    b = document.getElementById("lastname").value 
    # retrieves the inputs of the user

    c = str.upper(a)
    d = str.upper(b) 
    # Capitalized inputs to indicate what was added into the list

    document.getElementById("output").innerHTML = "" # resets the output so that it doesn't stack up

    G7 = {'Albert Pablo', 'Daniel Guzman', 'Arvin dela Cruz', 'Jacob Vasquez'}
    G8 = {'Cristian Reyes', 'Ryan Fajardo', 'Joshua Delos Reyes', 'John Carlo Pimentel'}
    G9 = {'Matthew Ledres', 'Danielle Padilla', 'Elise Garcia'}
    G10 = {'Jilliane Tech', 'Zenrich Lumogdang', 'Lance Bendaña', 'TJ Sales', 'Aryana Vargas'}

    allgrades = G7 | G8 | G9 | G10  # merges all the sets into one set using the union operator 
    addedmember = (c + " " + d)     # merges the first name and the last name along with a space 
    allgrades.add(addedmember)      # adds the full name into the set
    members = "<br>".join(sorted(allgrades))    # arranges them into a neat look and into alphabetical order
    numberofmembers = len(allgrades)    # retrieves the number of students

    e = f"ALL MEMBERS:<br><br>{members}<br><br>"
    document.getElementById("output").innerHTML = e
    # displays the full member list

    f = f"TOTAL NUMBER OF MEMBERS: {numberofmembers}"
    display(f, target = "output")
    # displays the total number of club members

display(target="div1") #literal object