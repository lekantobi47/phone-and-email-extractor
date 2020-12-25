#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 15:51:49 2020

@author: akintilebo
"""

import pyperclip, re

# Regex for finding US number
phoneRegex = re.compile(r"1-\d{3}-\d{3}-\d{4}")

# Regex for finding email
emailRegex = re.compile(r"\w+@\w+.com")
    
# Copy text from clipboard
text = str(pyperclip.paste())


matches = []

# finding phone number matches
for phonenumber in phoneRegex.findall(text):
    matches.append(phonenumber)

# finding email matches
for email in emailRegex.findall(text):
    matches.append(email)
    
# copy result to clipboard
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print("copied")
    print("\n".join(matches))
else:
    print("No phone numbers or email addresses found")