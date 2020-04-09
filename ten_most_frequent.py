#!/usr/bin/python

############################################################################
#Reads a fasta file with DNA sequences, finds the 10 most frequent sequences 
#and returns the sequence and their counts in the file ten_most_frequent.txt
#############################################################################

def open_fasta(path):
    """
    opens file with a given path
    reads that file and splits by newline
    """
    fasta = open(path,"r")
    fasta = fasta.read().split("\n")
    return fasta

seq_counter = {}
def count_sequences(fasta):
    """
    loops through contents of a fasta
    adds new sequences and their counts to dictionary
    if sequence is already in dictionary the count is increased by 1
    """
    for seq in fasta:
        if seq in seq_counter:
            seq_counter[seq] += 1
        else:
            seq_counter[seq] = 1
    return seq_counter

def sort_dictionary(dictionary):
    """
    sorts items in dictionary by value
    returns the top ten most frequent sequences
    """
    sorted_seq_counts = sorted(seq_counter.items(), key=lambda x: x[1])
    top_10 = sorted_seq_counts[-10:]
    return top_10

def report_top_10(lst):
    """
    opens the file ten_most_frequent.txt in the working directory
    adds a title to file
    writes each sequence along with its count to the file
    """
    report = open(r"ten_most_frequent.txt","w")
    report.write("Top Ten Sequences:" + "\n\n")
    for pair in lst:
        report.write("Sequence: " + str(pair[0]) + "\n")
        report.write("Count: " + str(pair[1]) + "\n\n")
    report.close()

#calls the functions with the necessary input
fasta = open_fasta(r"./*.fasta")
count_sequences(fasta)
sorted_dictionary = sort_dictionary(seq_counter)
report_top_10(sorted_dictionary)