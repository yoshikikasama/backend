import tarfile

with tarfile.open('teest.tar.gz', 'w:gz') as tr:
    tr.add('lesson_package')