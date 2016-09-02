#!/usr/bin/env python

import sys
import webbrowser

def get_args():
    query=""
    counter=1
    for arg in sys.argv[1:]:
        if counter<(len(sys.argv)-1):
            query+=arg
            query+="+"
            counter+=1
        else:
            query+=arg

    return query

search_link="http://www.uptodate.com.sci-hub.bz/contents/search?search="+get_args()+"&x=0&y=0"
webbrowser.open(search_link)
    
    