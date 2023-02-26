#!/usr/bin/env python

# assuming a csv file with a name in column 0 and the image url in column 1

import urllib
import ntpath
import urllib.request

opener = urllib.request.build_opener()
opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
urllib.request.install_opener(opener)

def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)

filename = "images"

# open file to read
with open("{0}.csv".format(filename), 'r') as csvfile:
    # iterate on all lines
    i = 0
    for line in csvfile:
        splitted_line = line.split(',')
        img_filename = path_leaf(splitted_line[1])
        # check if we have an image URL
        if splitted_line[1] != '' and splitted_line[1] != "\n":
            urllib.request.urlretrieve(splitted_line[1], "images/" + '{0}'.format(img_filename.rstrip("\r\n")))
            print("Image saved for {0}".format(splitted_line[0]))
            print("Filename: " + img_filename)
            i += 1
        else:
            print("No result for {0}".format(splitted_line[0]))