from pyscript import display, document


#database for nonmetal elements, their atomic numbers, and their masses
nonmetal_elements = {
    'H':'Hydrogen',
    'He':'Helium',
    'C': 'Carbon',
    'N':'Nitrogen',
    'O':'Oxygen',
    'F':'Fluorine',
    'Ne':'Neon',
    'P':'Phosphorus',
    'S':'Sulfur',
    'Cl':'Chlorine',
    'Ar':'Argon',
    'Se':'Selenium',
    'Br':'Bromine',
    'Kr':'Krypton',
    'I':'Iodine',
    'Xe':'Xenon',
    'Rn':'Radon',
}
atomic_numbers = {
    'H':'1',
    'He':'2',
    'C': '6',
    'N':'7',
    'O':'8',
    'F':'9',
    'Ne':'10',
    'P':'15',
    'S':'16',
    'Cl':'17',
    'Ar':'18',
    'Se':'34',
    'Br':'35',
    'Kr':'36',
    'I':'53',
    'Xe':'54',
    'Rn':'86',
}
atomic_mass = {
    'H':'1.0078',
    'He':'4.0026',
    'C': '12.011',
    'N':'14.007',
    'O':'15.999',
    'F':'18.998',
    'Ne':'20.180',
    'P':'30.974',
    'S':'32.065',
    'Cl':'35.453',
    'Ar':'39.948',
    'Se':'78.960',
    'Br':'79.904',
    'Kr':'83.798',
    'I':'126.90',
    'Xe':'131.29',
    'Rn':'222',
}

def check_element (e):
    entered_element = document.getElementById("element_symbol").value #checks if it is an existing nonmetal element

    display(f"Symbol: {entered_element} \n Element: {nonmetal_elements.get(entered_element, 'Not found')} \n Atomic Number: {atomic_numbers.get(entered_element)} \n Atomic Mass: {atomic_mass.get(entered_element)}", target='result') #displays the result