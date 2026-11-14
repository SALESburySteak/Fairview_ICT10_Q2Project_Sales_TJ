from pyscript import display, document

#about me variables

name = "Tyler John M. Sales"  # string
age = 15  # int
height = 160.02  # float
pronouns = "he/him"  # string
location = "Philippines"  # string
occupation = "Student"  # string
relationship_status = "Taken"  # string



#my interests variables

sports = ["Badminton", "Pickleball", "Volleyball"]
cozy = ["Webtoon & Manga", "Video Games", "Music"]
creative = ["Poetry", "Digital Art", "Photography"]
science = ["Electromagnetic waves", "Quantum Numbers", "Stoichiometry", "Computer Science"]

#my hobbies variables

chill = ["Listening to music", "Watching anime", "Reading webtoons", "Playing Video Games"]
creative1 = ["Writing poetry", "Drawing Digital Art", "Taking Photographs"]
outdoor = ["Playing badminton", "Playing pickleball", "Playing volleyball"]

#outputs

display("Name: " + name, target="div1")
display("Age: " + str(age), target="div1")
display("Height: " + str(height) + " cm", target="div1")
display("Pronouns: " + pronouns, target="div1")
display("Location: " + location, target="div1")
display("Occupation: " + occupation, target="div1")
display("Relationship Status: " + relationship_status, target="div1")

#div2

display("Sports: " + ", ".join(sports), target="div2")
display("Cozy Activities: " + ", ".join(cozy), target="div2")
display("Creative Activities: " + ", ".join(creative), target="div2")
display("Science Topics: " + ", ".join(science), target="div2")

#div3

display("Chill Hobbies: " + ", ".join(chill), target="div3")
display("Creative Hobbies: " + ", ".join(creative1), target="div3")
display("Outdoor Hobbies: " + ", ".join(outdoor), target="div3")