#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright (c) 2018 games195. Under MIT License.

import re, requests

def RemoveSpecialCharacter(string):
    return re.sub(r'[\/:*?"<>|]', '', string)

def OpenloadStreamangoCheck(url):
    page = requests.get(url).text
    invalid = re.search(r'<title>File not found \;\(<\/title>', str(page), re.IGNORECASE)
    if invalid:
        return False
    else:
        return True

__all__ = ['RemoveSpecialCharacter', 'OpenloadStreamangoCheck']
