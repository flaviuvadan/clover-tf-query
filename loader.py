"""
A data loading script that takes in the output of Clover (in text format)
and builds an object that holds the clean data (i.e. without information
not required for querying for transcription factors.)
"""

# packages used in this script
import pandas as pd
import sys 
import re

# global variables 
FIRST_ARGUMENT_INDEX = 1


class Loader:
    """
    Loader class that takes in the Clover ouput and "cleans" it by 
    selecting for the important features from the file. 
    """
    genes_dataframe = pd.DataFrame()

    def check_file(self):
        """
        Check if the user provided a file to be opened. If provided,
        continue, die otherwise.
        """
        if len(sys.argv) == 1:
            print("\n\nNo input file provided.\nRequired format: python3 " \
                    "<clover_file.txt>\n\n")
            exit()
        else:
            with open (sys.argv[FIRST_ARGUMENT_INDEX]) as input_file:
                first_line = input_file.readline()
                if "Clover: Cis-eLement OVERrepresentation" not in first_line:
                    print("\nNot a Clover file.\nRequired format: python3" \
                            "<clover_file.txt>\n\n")
                    exit()

    def add_genes(self, code, tf_list):
        """
        Add genes to the main dataframe.
        :param code: the ensembl code.
        :param tf_list: the transcription factors associated with the given code.
        """
        gene_dict = dict()
        gene_dict[code] = tf_list
        self.genes_dataframe = pd.concat([self.genes_dataframe, pd.DataFrame(gene_dict)],
                                         axis=1)

    def load_data(self):
        """
        Load function that takes in the name of the file to load
        via standard input. 
        """
        self.check_file()

        with open(sys.argv[FIRST_ARGUMENT_INDEX]) as input_file:

            curr_code = ""
            tf_list_of_curr_code = []
            code_count = 0

            for line in input_file:
                if ">ENS" in line:
                    if code_count == 0:
                        curr_code = line[1:].strip()
                        code_count += 1
                    else:
                        self.add_genes(curr_code, tf_list_of_curr_code)
                        curr_code = ""
                        tf_list_of_curr_code = []
                    curr_code = line[1:].strip()
                elif curr_code != "":
                    result = re.search("(M\d+)\s([A-Z]+\$\w+)\s([\w+\-:()]+\w+)", line)
                    if result:
                        tf_list_of_curr_code.append(result.group(3).strip().upper())
            self.add_genes(curr_code, tf_list_of_curr_code)
