# Task-5
def filter_venomous(species_list):
    venomous_species = []
    for entry in species_list:
        if entry["PestStatus"] == "Venomous":
            venomous_species.append(entry)
    return venomous_species
