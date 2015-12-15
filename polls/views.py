# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response, RequestContext, get_object_or_404
from django.http import HttpResponseRedirect
from .models import *
import datetime
from .forms import *
import os
# Create your views here.
from collections import Counter
from re import split

myvar = "-" * 35

def my_print(counter, is_reverse=False):
    lst = counter.items()
    lst.sort(key=lambda (a, b): (b, a), reverse=is_reverse)
    print ("[Unique Words: %d]" % len(lst)).center(35, "=")
    print "%-16s | %16s" % ("Word", "Count")
    print myvar
    for word, count in lst:
        print "%-16s | %16d" % (word, count)

def count_words_in_file(filename):
    counter = Counter()
    with open(filename, "rU") as f:
        for line in f:
            line = line.strip().lower()
            if not line:
                continue
            counter.update(x for x in split("[^a-zA-Z']+", line) if x)
    return counter

my_print(count_words_in_file("input.txt"), is_reverse=False)