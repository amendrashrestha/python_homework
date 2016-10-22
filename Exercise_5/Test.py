__author__ = 'amendrashrestha'

import os

from fasta_parser import FastaParser as module

predicted_genes_file_path = os.getenv('HOME') +"/Desktop/Python_Course/python_ebc_2016/day_05/exercise/predicted_genes.fasta"

all_contigs_file_path = os.getenv('HOME') +"/Desktop/Python_Course/python_ebc_2016/day_05/exercise/all_contigs.fasta"
contigs = module(all_contigs_file_path)
genes = module(predicted_genes_file_path)
#
# # assert contigs.count == 6

# print ()
# print contigs.count

genes.length_dist(os.getenv('HOME') + "/test/genes_lengths.pdf")

# print len(genes.extract_length(30))

# print len(contigs.extract_length(50))

# print contigs[1]

# assert "abc" == "asfsdf"


# keys=['a','b','c','d']
# values=[1,2,3,4]
# # we want to zip these two lists and create a dictionary dict_list
# # another_dict = [' '.join(x) for x in zip(list1, list2)]
# # print another_dict
# # dict_list = zip(list1, list2)
# import collections
#
# dict_list = zip(keys, values)
# # print dict(another_dict)
# print dict(dict_list)

# d = {keys[n]: values[n] for n in range(len(keys))}



# collections.OrderedDict(sorted(d.items(), key=lambda t: t[0]))


# def list_to_dict(li):
#      dct = {}
#      for item in li:
#          if dct.has_key(item):
#              dct[item] = dct[item] + 1
#          else:
#              dct[item] = 1
#      return dct
#
# li = [1, 1, 1, 2, 3, 3, 4, 4, 4, 4, 4, 5, 6, 7, 7]
# print list_to_dict(li)

# mydict = {'a':'1','b':'2'}
# print mydict.values()[1]





