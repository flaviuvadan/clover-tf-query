"""
Query module that takes in user input and outputs the result of the queried
transcription factor for a given file.
"""

from loader import Loader
import pandas as pd

class Query():
    """
    Query class that handles user input and the query.
    """

    result = []
    loader = Loader()
    loader.load_data()

    def query(self):
        """
        Ask the user for the transcription factor and output all the genes to
        a CSV file
        :return: a CSV file.
        """
        query = input("\n\n\tEnter TF (capitalized): ")

        for col in self.loader.genes_dataframe.columns:
            s = set(pd.Series(self.loader.genes_dataframe[col]))
            if query in s:
                self.result.append(col)

        codes = dict()
        codes['Ensembl IDs'] = self.result
        df = pd.DataFrame(codes)
        df.to_csv(query + '_result.csv', sep='\t', encoding='utf-8')


def main():
    q = Query()
    q.query()


if __name__ == '__main__':
    main()