import csv
import json5



def get_drugs(filename):
    """ Function that reads the drugs csv file and returns a list of the drugs' names
    """
    with open(filename, mode='r', newline='') as text:
        csv_reader = csv.DictReader(text)
        return [row["drug"].lower() for row in csv_reader]



def read_clinical_trials(filename_trials, drug, dic, journals_list):
    """
    Function that reads the clinical trials csv file and populates the journals_list variable
    and adds  key ("trials") to the dictionnary given in input
    """

    clinical_trials_list = []
    with open(filename_trials, mode='r', newline='') as trials:
        csv_reader = csv.DictReader(trials)
        for row in csv_reader:
            if drug in row['scientific_title'].lower().split(" "):
                clinical_trials_list.append({
                    "name": row['scientific_title'],
                    "date": row["date"]
                })
                if { "name": row['journal'], "date": row["date"] } not in journals_list:
                    journals_list.append({
                        "name": row['journal'],
                        "date": row["date"]
                    })
        dic.update({"trials": clinical_trials_list})


def read_pubmed_csv(filename_pubmed_csv, drug, pubmed_list, journals_list):
    """
    Function that reads the pubmed csv file and populates the journals_list and pubmed_list variables
    """
    with open(filename_pubmed_csv, mode='r', newline='') as articles:
        csv_reader = csv.DictReader(articles)
        for row in csv_reader:
            if drug in row['title'].split(" "):
                pubmed_list.append({"name": row['title'], "date": row["date"]})

                if {  "name": row['journal'].lower(), "date": row["date"] } not in journals_list:
                    journals_list.append({
                        "name": row['journal'],
                        "date": row["date"]
                    })


def read_pubmed_json(filename_pubmed_json, drug, pubmed_list, journals_list, dic):
    """
    Function that reads the pubmed json file and populates the journals_list variable and
    adds 2 new keys (  pubmed and journals ) to the dictionnary given in input
    """

    with open(filename_pubmed_json, mode='r') as text:
        json_reader = json5.load(text)
        for row in json_reader:
            if drug in row['title'].lower().split(" "):
                pubmed_list.append({"name": row['title'], "date": row["date"]})
                if { "name": row['journal'], "date": row["date"] } not in journals_list:
                    journals_list.append({
                        "name": row['journal'],
                        "date": row["date"]
                    })
        dic.update({"pubmed": pubmed_list})
        dic.update({"journals": journals_list})


def most_cited_journal(json_file):
    """
    Get the journal that cites the most drugs
    """
    with open(json_file, mode='r') as text :
        json_reader = json5.load(text)
        journals = dict()
        # loop over the json
        for row in json_reader:
            for r in row["journals"]:
                # add a new key to our dictionnary if that key wasn't present => {'journal_name':['drug_name] }
                if r["name"] not in list(journals.keys()):
                    journals[r["name"]] = [ row["drug_name"] ]
                # if the journal name key was already present, update that key by appending
                # the related drug name if that wasn't already present => {'journal_name':['drug_name1, drug_name_2] }
                if r["name"]  in list(journals.keys()) and row["drug_name"] not in journals[r["name"]]:
                    journals[r["name"]].append(row["drug_name"])

    # get the longest list of different drug names
    m = max(list(journals.values()))
    # In case we have more than one journal having cited the most different drugs, return all those corresponding journals
    return [list(journals.keys())[i] for i, j in enumerate(list(journals.values())) if len(j) == len(m)]
