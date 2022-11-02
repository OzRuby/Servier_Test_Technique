from data_pipeline.utils import get_drugs, read_clinical_trials, read_pubmed_csv, read_pubmed_json, most_cited_journal
import json
import os


def create_drugs_graph(filename_trials, filename_pubmed_csv,
                       filename_pubmed_json, drugs_list, drug_graph_filename):
    """
    Function that creates a json file where we can read the infos between every single
    drug and the articles and journals they are linked to

    """
    json_dump = []

    # Loop over all the drugs
    for drug in drugs_list:
        dic = dict()
        dic.update({"drug_name": drug})
        pubmed_list = []
        journals_list = []

        # Read Clinical trials csv file and add a "trials" key to dic
        read_clinical_trials(filename_trials, drug, dic, journals_list)

        # Read Pubmed  csv file and update pubmed_list and journals_list
        read_pubmed_csv(filename_pubmed_csv, drug, pubmed_list, journals_list)

        # Read Pubmed json file and add 2 keys ( "pubmed" and "journals" key to dic )
        read_pubmed_json(filename_pubmed_json, drug, pubmed_list,
                         journals_list, dic)

        # Append the dic containing all the info related to this specific drug into the variable json_dump
        json_dump.append(dic)

    with open(drug_graph_filename, "w") as json_file:
        json.dump(json_dump, json_file, indent=4, sort_keys=True)
    return json_dump


if __name__ == "__main__":

    drugs_file_csv_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "raw_data", "drugs.csv")
    trials_file_csv_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "raw_data", "clinical_trials.csv")
    pubmed_file_csv_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "raw_data", "pubmed.csv")
    pubmed_file_json_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "raw_data", "pubmed.json")
    drug_graph_filename_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "data", "drugs_tree.json")

    drugs_list = get_drugs(drugs_file_csv_path)

    # The json file produced is located in data_pipeline/data/
    create_drugs_graph(trials_file_csv_path, pubmed_file_csv_path,
                       pubmed_file_json_path, drugs_list,
                       drug_graph_filename_path)

    zejournal = most_cited_journal(drug_graph_filename_path)
