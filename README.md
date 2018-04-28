# Clover query script
Clover is a program for identifying functional sites in DNA sequences. If you 
give it a set of DNA sequences that share a common function, it will compare 
them to a library of sequence motifs (e.g. transcription factor binding 
patterns), and identify which, if any, of the motifs are statistically 
overrepresented in the sequence set. (sourec: http://cagt.bu.edu/page/Clover_about)

In some instances, it may be desirable to query the text output of Clover to
identify a set of genes that share a common transcription factor binding site.
For instance, if you are interested in FOX3, you may query the Clover output 
for FOX3 and get a list of genes that have FOX3 as a statistically 
overrepresented transcription factor binding pattern.
