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
            in_file = open(sys.argv[FIRST_ARGUMENT_INDEX], 'r')
            first_line = in_file.readline()
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
        return 0

    
### testing ###
load = Loader()
load.load_data()


