In 2017, Dr. Cao proposed ProLanGO which uses AI to predict protein functions, see https://www.mdpi.com/1420-3049/22/10/1732. He proposes that protein sequences are similar to human language, so we should be able to find out "words" in the protein sequence, although by nature all amino acids are connected to each other, and we could directly translate the protein sequence as a language to protein functions as another language. Please take a look at the publication for understanding the background. 

For this project, Dr. Cao already provided data in the data folder. F_4_Uniprot_functionDATABASE.DAT is parsed from the Uniprot database, each line is seprated by '|', the first part is protein sequence, and second part is protein function "word", each "word" could map to a protein GO term in another file: F_3_GO_table.DAT. In addition, Dr. Cao also provided the protein sequence "word" in the file: New_Balanced_FragDATABASE_34567_top2000.txt. Finally, you may want to use the file New_filtered_balanced_protein_language_data_34567_top2000 instead of F_4_Uniprot_functionDATABASE.DAT since it only keeps the protein sequence and function "word".

Now this is the method part, from New_filtered_balanced_protein_language_data_34567_top2000, we should be able to analyze how likely a protein sequence "word" would be related to a protein function "word". If you have taken Dr. Cao's AI course, you could try to use Naive Bayesian algorithm (There are in total 2000 sequence "word", so you could create a feature set with 2000 input, and you could train NB for each output function "word"), you could also try CNN, but if you are not familiar with AI, don't be panic, you could still do it with the following steps. Give you one example, to make it simple, let's assume ABC, BCD, DEF are "word" for protein sequences, and HIJK, IJKH, ZZZZ are "word" for protein functions, and here are the data:
ABC BCD | ZZZZ
ABC DEF | HIJK IJKH
BCD DEF BCD | IJKH ZZZZ

so now you could write a script to calculate the probability P(function "word" | sequence "word"), such as P(ZZZZ | ABC) = frequency(ZZZZ and ABC) / frequency(ABC). Check the example data, there is one line (the first line) that ABC and ZZZZ exists together, and there is two lines containing ABC (The first two lines). So P(ZZZZ | ABC) = 1/2 = 0.5. That means if you see ABC in the input protein sequence, there is 50% possiblity that protein has function ZZZZ. Now you could calculate the probability for each protein function "word" given each protein sequence "word". 

For the prediction, you could write a script to load all protein sequence "word" file: New_Balanced_FragDATABASE_34567_top2000.txt, and check if any "word" is in the input protein fasta sequence, if that's the case, get the function "word" based on the probability you calculated, and of course, if several sequence "words" point to the same function "word", you should have higher probability for that function "word". You could load the file F_3_GO_table.DAT to map your final prediction to GO terms. 

This is one method proposed by Dr. Cao, but you may want to develop other method like Naive Bayesian or NN to train a model for prediction, please document your method well in the final report! 

Please contact Dr. Cao for any questions. 


