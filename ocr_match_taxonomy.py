import requests

#
import sys
sys.stdout = open(1, 'w', encoding='utf-8', closefd=False)
#

def get_GBIF_taxonomic_lookup(candidate_name, output_dict={}):
    # A simple function to get the 'GBIF interpreted taxonomic lookup' for a given name string
    api_url = 'https://api.gbif.org/v1/species/match?name={}'.format(candidate_name)
    response = requests.get(api_url)
    rson = response.json()

    if rson['matchType'] != "NONE":
        print(rson['matchType'], 'match for:', candidate_name)
        output_dict['submitted_string'] = candidate_name
        output_dict['scientific_name'] = rson['scientificName']
        output_dict['rank'] = rson['rank']
        output_dict['status'] = rson['status']
        output_dict['confidence_score'] = rson['confidence']
    return output_dict

def look_up_species_names(labels, confidence_score=80):
    '''Based on the label list from the read_specimen_text module, this function looks up each element from the list in the GBIF taxonomic API via
     the get_GBIF_taxonomic_lookup() function.
    '''
    result_list = []
    for elem in labels:
        api_res = get_GBIF_taxonomic_lookup(elem)

        if ((len(api_res)>0) and (api_res['confidence_score'] > confidence_score)):

            result_list.append(api_res)
    return result_list


def check_for_api_cache_issues(results):
    #API servers can have cache issues so that different API requests return the exact same response.
    #This function mitigates that issue. I see this as a bandaid rather than a solid solution.
    result_list = [elem for elem in results]

    set_res = [dict(s) for s in set(frozenset(d.items()) for d in result_list)]
    # Removes duplicates in the API result coming from API server caching issues
    return set_res

