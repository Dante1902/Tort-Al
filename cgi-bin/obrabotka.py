#!/usr/bin/env python3

import cgi

our_form = cgi.FieldStorage()

in_name = our_form.getfirst("in_name","не найдено")
in_famile = our_form.getfirst("in_famile","не найдено")

print("Content-type: text/html")
print()
print(in_name)
print(in_famile)
