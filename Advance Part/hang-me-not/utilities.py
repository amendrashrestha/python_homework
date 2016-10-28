__author__ = 'amendrashrestha'

def write_into_file(file_path, content):
    file = open(file_path, 'a')
    file.write(content.lower() + "\n")
    file.close()






