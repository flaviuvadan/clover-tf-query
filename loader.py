"""
A data loading script that takes in the output of Clover (in text format)
and builds an object that holds the clean data (i.e. without information
not required for querying for genes.)
"""

# packages used in this script
import pandas as pd
import numpy as np
import sys 
import re 
import time 

# global variables 
FIRST_ARGUMENT_INDEX = 1

class Loader():
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

    def load_data(self):
        """
        Load function that takes in the name of the file to load
        via standard input. 
        """
        self.check_file()

        list_of_gene_frames = []
        with open (sys.argv[FIRST_ARGUMENT_INDEX]) as input_file:
            file_line = input_file.readline()
            
            ensembl_code = "" 
            count_codes = 0
            tf_list = []

            while file_line:
                if re.search(">ENS", file_line):
                    if count_codes == 0:
                        ensembl_code = file_line
                        count_codes+=1
                        file_line = input_file.readline()
                    else:
                        # concatenate the dataframes
                        gene_dict = dict()
                        gene_dict[ensembl_code] = tf_list
                        self.genes_dataframe = pd.concat([self.genes_dataframe, \
                                pd.DataFrame(gene_dict)], axis=1)
                        # reset 
                        file_line = input_file.readline()
                        ensembl_code = file_line
                        tf_list = []
                        file_line = input_file.readline()
                        
                elif len(ensembl_code) != 0:   
                    result = re.search("(M\d+)\s([A-Z]+\$\w+)\s([\w+\-\:\(\)]+\w+)", file_line)
                    if result and len(ensembl_code) != 0:
                        tf_list.append(result.group(3).strip().upper())
                        file_line = input_file.readline()
                else:
                    file_line = input_file.readline()

### testing ###
load = Loader()
load.load_data()
print(load.genes_dataframe)
