import os

def create_project(directory):
    if not os.path.exists(directory):
        print ('Creating project: ' + directory)
        os.makedirs(directory)

def create_files(project_name, starter_url):
    not_crawled = project_name + '/uncrawled.txt'
    crawled = project name + '/crawled.txt'
    if not os.path.isfile(not_crawled):
        write_file(not_crawled, starter_url)
    if not os.path.isfile(crawled):
        write_file(crawled, '')

def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()

def append_file(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')

def delete_file(path):
    with open(path, 'w'):
        pass

def file_to_set(file_name):
    results = set()
    with open (file_name, 'rt') as f:
        for line in f:
            results.add(line.replace('\n', ''))
    return results

def set_to_file(links, file):
    delete_file(file)
    for link in sorted(links):
        append_file(file, link)