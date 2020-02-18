#!/usr/bin/python
#coding:utf-8

import os
import sys

#word_dict = ["i", "like", "sam", "sung", "samsung", "mobile", "ice", "cream", "man", "go"]
#input = "ilikesamsungmobile"

def builddict(word_dict):
    res = {}
    for w in word_dict:
        first = w[0]
        if first not in res:
            res[first] = []

        res[first].append(w)

    return res

def breaksentence(input, res, hash_dict):
    if not input:
        print res
        return

    w = input[0]
    if w not in hash_dict:
        return

    slot_list = hash_dict[w]
    for k in slot_list:
        if not input.startswith(k):
            continue

        replica = res + [k,]
        breaksentence(input[len(k):], replica, hash_dict) 
        

def usage():
    print "usage: python %s [input file]" % sys.argv[0]
    print "input file has two line, fisrt line specify input string, and second specify input list"
    print "input file example:"
    print "ilikesamsungmobile"
    print '["i", "like", "sam", "sung", "mobile", "ice", "cream", "man", "go"]'
 
def main():
    if len(sys.argv) < 2:
        usage()
        return

    file_name = sys.argv[1]
    fp = open(file_name)
    lines = fp.readlines()
    if len(lines) < 2:
        usage()
        return

    input_string = lines[0]
    input_list = lines[1]
    input_string = input_string[:-1]
    input_list = input_list[:-1]
    try:
        input_list = eval(input_list)
        if not isinstance(input_list, list):
            print "customized input_list must be a list"
            return
    except:
        print "customied input_list must be a list"
        return
    
    print "************"
    print "input string is:", input_string
    print "input list is:", input_list
    print "\n\n"
    print "******result******"
    breaksentence(input_string, [], builddict(input_list)) 


if __name__ == "__main__":
    main()
