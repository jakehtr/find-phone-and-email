#!/usr/bin/env python3

"""
find_phone_email.py - Finds phone numbers and email addresses from the clipboard.
"""

import pyperclip
import re


def find_matches():
    phone_numbers = set(groups[0].strip() for groups in phone_regex.findall(text))
    emails = set(groups[0].strip() for groups in email_regex.findall(text))
    return phone_numbers.union(emails)


def results_from_clipboard():
    matches = find_matches()
    if matches:
        all_matches = '\n'.join(matches)
        pyperclip.copy(all_matches)
        print('Copied to clipboard:\n{}'.format(all_matches))
    else:
        print('No phone numbers or email addresses found.')

if __name__ == '__main__':
    phone_regex = re.compile(r'''(
        (\+44|0)?                           # UK area code
        (\s\(0\)|\(0\))?                    # (0)
        (\s)?                               # separator
        (\d{2,4})                           # first 2-4 digits
        (\s)                                # separator
        (\d{3,8})                           # mid/last 3-8 digits
        (\s)?                               # separator
        (\d{4})?                            # last 4 digits
        )''', re.VERBOSE)

    email_regex = re.compile(r'''(
        [a-zA-Z0-9._-]+                     # username
        @                                   # @ symbol
        [a-zA-Z0-9-]+                       # domain name
        (\.[a-zA-Z]{2,4})                   # dot-something
        (\.[a-zA-Z]{2,4})?                  # extra dot-something
        )''', re.VERBOSE)

    text = pyperclip.paste()
    results_from_clipboard()
