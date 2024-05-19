def filter_venomous(species_list):
    venomous_species = []
    for species in species_list:
        if species["Species"]["PestStatus"] == "Venomous":
            venomous_species.append(species)
    return venomous_species

def test_filter_venomous(venomous_species):
    assert venomous_species == [{"Species":{"TaxonID":1040,"AcceptedCommonName":"snake","PestStatus":"Venomous"}}]
    return True
