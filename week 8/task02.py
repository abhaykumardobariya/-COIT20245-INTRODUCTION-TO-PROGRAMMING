# Task-2
def main():

    display_menu()

    while True:
        user_input = input("wildlife > ")

        if user_input.lower() == "help":
            display_menu()

        elif user_input.lower() == "exit":
            print("\nExiting the program.")
            break

        elif user_input.lower().startswith("species"):
            parts = user_input.split(" ")
            if len(parts) < 2:
                print("Invalid command format. Please use 'species <city>' or 'species <city> venomous'")
            else:
                city = parts[1]
                if len(parts) > 2 and parts[2].lower() == "venomous":
                    species_list = search_species(city)
                    venomous_species = filter_venomous(species_list)
                    
                    if venomous_species:
                        display_species(venomous_species)
                    else:
                        print("Venomous Species not found!")

                else:
                    species_list = search_species(city)
                    display_species(species_list)

        elif user_input.lower().startswith("sighting"):
            parts = user_input.split(" ")
            if len(parts) != 3:
                print("\nInvalid command format. Please enter the command in the format: sighting <city name> <Taxon ID>")
            else:
                _, city, taxonid = parts
                sightings = search_sightings(taxonid, city)
                display_sightings(sightings)
            
        else:
            print("Error: Invalid command")

if _name_ == "_main_":
    main()
