
# Step 1: Define periodic table data
periodic_table = [
    {"number": 1, "symbol": "H",  "name": "Hydrogen", "mass": 1.008},
    {"number": 2, "symbol": "He", "name": "Helium",   "mass": 4.0026},
    {"number": 3, "symbol": "Li", "name": "Lithium",  "mass": 6.94},
    {"number": 4, "symbol": "Be", "name": "Beryllium","mass": 9.0122},
    {"number": 5, "symbol": "B",  "name": "Boron",    "mass": 10.81},
    {"number": 6, "symbol": "C",  "name": "Carbon",   "mass": 12.011},
    {"number": 7, "symbol": "N",  "name": "Nitrogen", "mass": 14.007},
    {"number": 8, "symbol": "O",  "name": "Oxygen",   "mass": 15.999},
    {"number": 9, "symbol": "F",  "name": "Fluorine", "mass": 18.998},
    {"number": 10,"symbol": "Ne", "name": "Neon",     "mass": 20.180},
    {"number": 41, "symbol": "Nb", "name": "Niobium", "mass": 92.906},
    {"number": 42, "symbol": "Mo", "name": "Molybdenum", "mass": 95.95},
    {"number": 43, "symbol": "Tc", "name": "Technetium", "mass": 98},
    {"number": 44, "symbol": "Ru", "name": "Ruthenium", "mass": 101.07},
    {"number": 45, "symbol": "Rh", "name": "Rhodium", "mass": 102.91},
    {"number": 46, "symbol": "Pd", "name": "Palladium", "mass": 106.42},
    {"number": 47, "symbol": "Ag", "name": "Silver", "mass": 107.87},
    {"number": 48, "symbol": "Cd", "name": "Cadmium", "mass": 112.41},
    {"number": 49, "symbol": "In", "name": "Indium", "mass": 114.82},
    {"number": 50, "symbol": "Sn", "name": "Tin", "mass": 118.71},
    {"number": 51, "symbol": "Sb", "name": "Antimony", "mass": 121.76},
    {"number": 52, "symbol": "Te", "name": "Tellurium", "mass": 127.60},
    {"number": 53, "symbol": "I", "name": "Iodine", "mass": 126.90},
    {"number": 54, "symbol": "Xe", "name": "Xenon", "mass": 131.29},
    {"number": 55, "symbol": "Cs", "name": "Cesium", "mass": 132.91},
    {"number": 56, "symbol": "Ba", "name": "Barium", "mass": 137.33},
    {"number": 57, "symbol": "La", "name": "Lanthanum", "mass": 138.91},
    {"number": 58, "symbol": "Ce", "name": "Cerium", "mass": 140.12},
    {"number": 59, "symbol": "Pr", "name": "Praseodymium", "mass": 140.91},
    {"number": 60, "symbol": "Nd", "name": "Neodymium", "mass": 144.24},
    {"number": 61, "symbol": "Pm", "name": "Promethium", "mass": 145},
    {"number": 62, "symbol": "Sm", "name": "Samarium", "mass": 150.36},
    {"number": 63, "symbol": "Eu", "name": "Europium", "mass": 151.96},
    {"number": 64, "symbol": "Gd", "name": "Gadolinium", "mass": 157.25},
    {"number": 65, "symbol": "Tb", "name": "Terbium", "mass": 158.93},
    {"number": 66, "symbol": "Dy", "name": "Dysprosium", "mass": 162.50},
    {"number": 67, "symbol": "Ho", "name": "Holmium", "mass": 164.93},
    {"number": 68, "symbol": "Er", "name": "Erbium", "mass": 167.26},
    {"number": 69, "symbol": "Tm", "name": "Thulium", "mass": 168.93},
    {"number": 70, "symbol": "Yb", "name": "Ytterbium", "mass": 173.05},
    {"number": 71, "symbol": "Lu", "name": "Lutetium", "mass": 174.97},
    {"number": 72, "symbol": "Hf", "name": "Hafnium", "mass": 178.49},
    {"number": 73, "symbol": "Ta", "name": "Tantalum", "mass": 180.95},
    {"number": 74, "symbol": "W", "name": "Tungsten", "mass": 183.84},
    {"number": 75, "symbol": "Re", "name": "Rhenium", "mass": 186.21},
    {"number": 76, "symbol": "Os", "name": "Osmium", "mass": 190.23},
    {"number": 77, "symbol": "Ir", "name": "Iridium", "mass": 192.22},
    {"number": 78, "symbol": "Pt", "name": "Platinum", "mass": 195.08},
    {"number": 79, "symbol": "Au", "name": "Gold", "mass": 196.97},
    {"number": 80, "symbol": "Hg", "name": "Mercury", "mass": 200.59},
    {"number": 81, "symbol": "Tl", "name": "Thallium", "mass": 204.38},
    {"number": 82, "symbol": "Pb", "name": "Lead", "mass": 207.2},
    {"number": 83, "symbol": "Bi", "name": "Bismuth", "mass": 208.98},
    {"number": 84, "symbol": "Po", "name": "Polonium", "mass": 209},
    {"number": 85, "symbol": "At", "name": "Astatine", "mass": 210},
    {"number": 86, "symbol": "Rn", "name": "Radon", "mass": 222},
    {"number": 87, "symbol": "Fr", "name": "Francium", "mass": 223},
    {"number": 88, "symbol": "Ra", "name": "Radium", "mass": 226},
    {"number": 89, "symbol": "Ac", "name": "Actinium", "mass": 227},
    {"number": 90, "symbol": "Th", "name": "Thorium", "mass": 232.04},
    {"number": 91, "symbol": "Pa", "name": "Protactinium", "mass": 231.04},
    {"number": 92, "symbol": "U", "name": "Uranium", "mass": 238.03},
    {"number": 93, "symbol": "Np", "name": "Neptunium", "mass": 237},
    {"number": 94, "symbol": "Pu", "name": "Plutonium", "mass": 244},
    {"number": 95, "symbol": "Am", "name": "Americium", "mass": 243},
    {"number": 96, "symbol": "Cm", "name": "Curium", "mass": 247},
    {"number": 97, "symbol": "Bk", "name": "Berkelium", "mass": 247},
    {"number": 98, "symbol": "Cf", "name": "Californium", "mass": 251},
    {"number": 99, "symbol": "Es", "name": "Einsteinium", "mass": 252},
    {"number": 100, "symbol": "Fm", "name": "Fermium", "mass": 257},
    {"number": 101, "symbol": "Md", "name": "Mendelevium", "mass": 258},
    {"number": 102, "symbol": "No", "name": "Nobelium", "mass": 259},
    {"number": 103, "symbol": "Lr", "name": "Lawrencium", "mass": 266},
    {"number": 104, "symbol": "Rf", "name": "Rutherfordium", "mass": 267},
    {"number": 105, "symbol": "Db", "name": "Dubnium", "mass": 270},
    {"number": 106, "symbol": "Sg", "name": "Seaborgium", "mass": 271},
    {"number": 107, "symbol": "Bh", "name": "Bohrium", "mass": 270},
    {"number": 108, "symbol": "Hs", "name": "Hassium", "mass": 277},
    {"number": 109, "symbol": "Mt", "name": "Meitnerium", "mass": 278},
    {"number": 110, "symbol": "Ds", "name": "Darmstadtium", "mass": 281},
    {"number": 111, "symbol": "Rg", "name": "Roentgenium", "mass": 282},
    {"number": 112, "symbol": "Cn", "name": "Copernicium", "mass": 285},
    {"number": 113, "symbol": "Nh", "name": "Nihonium", "mass": 286},
    {"number": 114, "symbol": "Fl", "name": "Flerovium", "mass": 289},
    {"number": 115, "symbol": "Mc", "name": "Moscovium", "mass": 290},
    {"number": 116, "symbol": "Lv", "name": "Livermorium", "mass": 293},
    {"number": 117, "symbol": "Ts", "name": "Tennessine", "mass": 294},
    {"number": 118, "symbol": "Og", "name": "Oganesson", "mass": 294},
]

# Step 2: Define a function to search
def search_element():
    print("\nSearch element by:")
    print("1. Atomic Number")
    print("2. Atomic Symbol")
    print("3. Atomic Mass")
    print("4. Exit")

    choice = input("Enter 1, 2, 3, or 4: ")

    found = None  # Initialize

    if choice == "1":
        try:
            atomic_number = int(input("Enter atomic number: "))
            for element in periodic_table:
                if element["number"] == atomic_number:
                    found = element
                    break
        except ValueError:
            print("Invalid number.")

    elif choice == "2":
        symbol = input("Enter atomic symbol (e.g., H, He, O): ").capitalize()
        for element in periodic_table:
            if element["symbol"] == symbol:
                found = element
                break

    elif choice == "3":
        try:
            mass = float(input("Enter approximate atomic mass: "))
            for element in periodic_table:
                if abs(element["mass"] - mass) <= 0.1:  # tolerance
                    found = element
                    break
        except ValueError:
            print("Invalid mass.")

    elif choice == "4":
        print("Exiting program. Goodbye!")
        return False  # Stop loop

    else:
        print("Invalid choice.")
        return True  # Continue loop

    # Step 3: Display result
    if found:
        print("\nElement Information:")
        print(f"Name          : {found['name']}")
        print(f"Symbol        : {found['symbol']}")
        print(f"Atomic Number : {found['number']}")
        print(f"Atomic Mass   : {found['mass']}")
    else:
        if choice in ["1", "2", "3"]:
            print("Element not found.")

    return True  # Keep running


# Step 4: Run program in loop
while True:
    if not search_element():
        break

