from pyscript import display, document


comarts_members = {'Cedric Visorde', 'Georgina Sarmiento', 'Alexa Agnote', 'Macy Panela', 'Santiago Valdez', 'Carl Rufo', 'Balian Guardacasa', 'Carl Ang', 'Vivienne Dimayacyac', 'Zuri Asgari', 'Claire Dayawon', 'Jade Patawaran', 'Mikee Ore'} #list of all members

def update_list(e): #function triggered by py-click
    first_name = str(document.getElementById('fname').value) #gets value from input
    last_name = str(document.getElementById('lname').value) #gets value from input
    new_member = first_name + " " + last_name #gets the member's full name by combining inputs
    comarts_members.add(new_member) #adds new member's name to the member list
    display(f'Current Members: {comarts_members}', target='output') #displays the list of all members
    display(f'Total member count: {len(comarts_members)}', target='output') #displays the number of members