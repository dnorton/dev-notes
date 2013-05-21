#!/usr/bin/python2.6

import os
import shutil
import tempfile
import sys

__author__ = 'dnorton'
"""
Utility script that can do a find/replace across a path
"""

search_string = None
replacement_string = None
do_replace = True
ignore_list = None

def _replace(file):
    """replace any instance of search_string with replacement_string in file. Note: file must include the full path"""
    assert os.path.exists(file),\
    'the path %s does not exist' % file

    reduced_ignore_list = [x for x in ignore_list if file.find(x) >= 0] if ignore_list is not None else None

    if reduced_ignore_list is None or len(reduced_ignore_list) == 0:
        preview_text = "PREVIEW - " if not do_replace else ""
        print preview_text + "replacing string [%s] with string [%s] in %s" % (search_string, replacement_string, file)

    if do_replace and \
        (reduced_ignore_list is None or len(reduced_ignore_list) == 0):
        t1 = tempfile.NamedTemporaryFile()
        f1 = open(file, 'r')
        text = f1.read().replace(search_string, replacement_string)
        f1.close()
        t1.write(text)
        t1.flush()
        t1.seek(0)

        # reopen the original file for the copy command
        f1 = open (file, 'wb')
        shutil.copyfileobj(t1, f1)
        t1.close()

def _backup(filepath):
    import datetime
    backup_path = filepath + ".bak"
    if os.path.exists(backup_path):
        now = datetime.date.today()
        shutil.copy(backup_path, backup_path + "." + now.strftime('%Y%m%d%H%M'))

    shutil.copy(filepath, backup_path)

def search(filepath):
    file_obj = open(filepath, 'r')
    lines = file_obj.readlines()
    res = [x for x in lines if x.find(search_string) > -1]

    if len(res) > 0:
        #copy the original file to .bak
        if filepath.find('.bak') < 0:
            _backup(filepath)
            _replace(filepath)

if __name__ == "__main__":

#    options = None
#    args = None

    import optparse
    parser = optparse.OptionParser(usage="usage: %prog [options] 'search_string' 'replace_string' filepath (or dir)")
    parser.add_option('-n', action="store_false", dest="replace", help="preview the replacement")
    parser.add_option('-i', dest="ignore", help="pattern to ignore. Comma separated.")

    (options, args) = parser.parse_args()


    if len(args) >= 3:
        search_string = args[0]
        replacement_string = args[1]
        file = args[2]
    else:
        print parser.get_usage()
        exit(0)

    if options.replace is not None:
        do_replace = options.replace

    if options.ignore is not None:
        ignore_list = options.ignore.split(',')

    if os.path.exists(file):
        if os.path.isdir(file):
            for root, dirs, files in os.walk(file):
                for f in files:
                    search(os.path.join(root, f))
        else:
            search(file)
    else:
        print 'the file specified', file, 'does not exist'
        exit(1)





