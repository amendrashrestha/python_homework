# 1 Opening/reading/writing files
# This function opens file and add a string and writes in different file again
def read_file_and_append():
    file_path_read = "day_02/exercises/file1.txt"
    file_path_write = "day_02/exercises/file1_new.txt"

    i = 1
    with open(file_path_read, "r") as content:
        line = content.readlines()
        for single_line in line:
            single_line = "Entry " + str(i) + " " + single_line
            file_write = open(file_path_write, 'a')
            file_write.write(single_line)
            i += 1
        file_write.close()


# 2 Filtering by line contents
# This function reads data file and store in a list.
# It takes user's input. It search the user input in the list
# and returns the matched rows
def filter_line_content():
    file_path_read = "day_02/exercises/files/genome.bed"

    data_file = open(file_path_read, 'r').readlines()
    user_input = "chr20"
    entries = 0

    for i in range(len(data_file)):
        if user_input == data_file[i][0:len(user_input)]:
            print data_file[i]
            entries += 1
    print str(entries) + " entries corresponding to " + user_input

# 4. Functions and reusage
# 4.0.1 A
#This function takes two strings and returns true if second string is solely composed of first string 
def is_repetition(s1, s2):
    multi = len(s1) / len(s2)

    if s2 * multi == s1:
        print "true"
    else:
        print "false"

# 5. Combining files
# This functions open 3 different files and store in three different list.
# The lists are merged and written in a bed file
def combine_files():
    file1_path = "day_02/exercises/files/chrom.txt"
    file2_path = "day_02/exercises/files/start_end.txt"
    file3_path = "day_02/exercises/files/gene.txt"

    file_path_to_write = "day_02/exercises/files/bed_file.bed"

    file1 = open(file1_path, 'r').readlines()
    file2 = open(file2_path, 'r').readlines()
    file3 = open(file3_path, 'r').readlines()

    final_list = [file1[i] + file2[i] + file3[i] for i in range(len(file1))]

    for single_line in final_list:
        file_write = open(file_path_to_write, 'a')
        file_write.write(single_line.replace("\n", " "))
        file_write.write("\n")
    file_write.close()