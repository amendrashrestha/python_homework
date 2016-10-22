__author__ = 'amendrashrestha'
import os
from itertools import groupby
import matplotlib.pyplot as plt

"""Fasta Parser class"""
class FastaParser(object):

# Checks if the festa file exists if not raise IO Error.
# initialize the festa file path
# initialize the parsed festa parse dictionary
    def __init__(self, path):
        self.dict_genes = {}

        if path:
            if not os.path.exists(path):
                raise IOError
        self.path = path
        self.genes_list = self.festa_parser()
        # print type(self.genes_list)

    @property
    def count(self):
        count_gene = len(self.dict_genes)
        return count_gene

    def __len__(self):
        return self.count

#If the key is interger the function returns the
    def __getitem__(self, key):
        if isinstance(key, str):
            if key in self.dict_genes.iterkeys():
                return self.dict_genes[key]
            else:
                raise KeyError
                # print "Key Error"
        else:
            if key > len(self.dict_genes):
                raise IndexError
                # print "Index Error"
            else:
                return self.dict_genes.values()[key]

# Reads festa file and parse it and store in dictionary
# Returns dictionary of genes
    def festa_parser(self):
        f = open(self.path)
        list_festa_desc = []
        list_festa_sequence = []

        content = (x[1] for x in groupby(f, lambda line: line[0] == ">"))

        for gene in content:
            single_gene = gene.next()[1:].strip()
            list_festa_desc.append(single_gene)
            seq = "".join(s.strip() for s in content.next())
            list_festa_sequence.append(seq)

        dict_genes_temp = dict(zip(list_festa_desc, list_festa_sequence))

        for key in sorted(dict_genes_temp.iterkeys()):
            # print key
            # print dict_genes_temp[key]
            self.dict_genes[key] = dict_genes_temp[key]
        return self.dict_genes

#This function takes integer as input.
# It compares the input integer with the length of genes sequence
# and returns list of valid sequences
    def extract_length(self, length):
        list_valid_seq = []

        for key in sorted(self.dict_genes.iterkeys()):
            sequence = self.dict_genes[key]
            # print len(sequence)
            if length > len(sequence):
                list_valid_seq.append(key)
        return list_valid_seq

#Function takes one argument path. It creates a graph of the length
#distribution of the sequences
    def length_dist(self, graph_file_path):
        list_seq = []
        f = plt.figure()
        width = 1/1.5

        for key in sorted(self.dict_genes.iterkeys()):
            sequence = len(self.dict_genes[key])
            list_seq.append(sequence)
        x = range(len(list_seq))

        plt.bar(x, list_seq, width, color="blue")
        plt.show()
        f.savefig(graph_file_path)










