import os

#Each website crawled is a sperate project
def create_directory(directory):
    if not os.path.exists(directory):
    print('Creating project ' + directory)
    os.makedirs(directory)

create_directory('TESTDIR')
