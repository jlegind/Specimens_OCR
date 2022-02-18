import requests
import json
from time import sleep

def get_GBIF_taxonomic_lookup(candidate_name, output_dict={}):
    # A simple function to get the ''
    api_url = 'https://api.gbif.org/v1/species/match?name={}'.format(candidate_name)
    response = requests.get(api_url)
    rson = response.json()
    print(candidate_name)
    if rson['matchType'] != "NONE":
        print(rson['matchType'], type(rson['matchType']))
        output_dict['scientific_name'] = rson['scientificName']
        output_dict['rank'] = rson['rank']
        output_dict['status'] = rson['status']
        output_dict['confidence_score'] = rson['confidence']
    return output_dict
# res = get_GBIF_taxonomic_lookup('Dactylorhiza maculata')
# print(res)
labels = ['CLF104120', 'HERBIERS UNIVERSITAIRES DE CLERMONT-FERRAND CLF104120.', 'Dactylorhiza maculata', '(L.) SOÓ', 'subsp. maculata', 'Famille Orchidaceae', 'Identification Thébaud G.', 'Récolteur Thomas M.', 'Date 2012', 'Date 6/7/2012', 'Pays France', 'Départerment Puy-de-Dôme', 'Commune Le Monestier', 'Virennes (Le Monestier, 63), PSET n°2.', 'note', 'RECOLNAT', '']

def pick_out_species_name(label_list):
    '''Based on the label list from the read_specimen_text module, this function looks up each element from the list in the GBIF taxonomic API via
     the get_GBIF_taxonomic_lookup() function.
    '''
    result_list = []
    for elem in labels:
        # sleep(3)
        api_res = get_GBIF_taxonomic_lookup(elem)
        # print('for loop', api_res, len(api_res))

        if ((len(api_res)>0) and (api_res['confidence_score'] > 80)):
            print('High confidence result: ', api_res)
            result_list.append(api_res)
    return result_list

race = pick_out_species_name(labels)

def check_for_api_cache_issues(results):
    #API servers can have cache issues so that different API requests return the exact same response.
    #This function mitigates that issue. I see this as a bandaid rather than a solid solution.
    result_list = [json.dumps(elem) for elem in race]
    setres = list(set(result_list))
    return setres.

res = check_for_api_cache_issues(race)
print('final res = ', res)