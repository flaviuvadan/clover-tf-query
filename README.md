# Clover query script
Clover is a program for identifying functional sites in DNA sequences. If you 
give it a set of DNA sequences that share a common function, it will compare 
them to a library of sequence motifs (e.g. transcription factor binding 
patterns), and identify which, if any, of the motifs are statistically 
overrepresented in the sequence set. (source: http://cagt.bu.edu/page/Clover_about)

In some instances, it may be desirable to query the text output of Clover to
identify a set of genes that share a common transcription factor binding site.
For instance, if you are interested in FOX3, you may query the Clover output 
for FOX3 and get a list of genes that have FOX3 as a statistically 
overrepresented transcription factor binding pattern.

## Usage
python3 query.py <clover_file.txt>
	Enter TF: <TF_name>

The output is a CSV file with a list of all Ensembl IDs of genes that 
have <TF_name> as a statistically over-represented TF. 

The query does not perform a regular expression search. Instead,
it looks for the name of the TF exactly as specified by the user. There are 
transcriptions factors that have variations in their name (e.g. FOXO3A, FOXO3B).
