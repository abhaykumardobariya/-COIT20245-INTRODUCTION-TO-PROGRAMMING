# Task-3
def search_species(city):
    RADIUS = 100000
    coordiantes = gps(city)
    # print(coordiantes)
    species_list = get_species_list(coordiantes, RADIUS)
    return species_list

def display_species(species_list):
    print("\nDetail of species : \n")
    
    for entry in species_list:
        if "AcceptedCommonName" in entry:
            print(
                "TaxonID : " + str(entry["TaxonID"]) + "\n"
                "Name of the species : " + entry["AcceptedCommonName"] + "\n"
                "Pest Status : " + entry["PestStatus"] + "\n")
            print("--"*30+"\n")
        else:
            print(
                "TaxonID : " + str(entry["TaxonID"]) + "\n"
                "Scientific Name of the species : " + entry["ScientificName"] + "\n"
                "Pest Status : " + entry["PestStatus"] + "\n")
            print("--"*30+"\n")
