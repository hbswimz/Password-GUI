import requests
import hashlib
import tkinter as tk

# Global Vars
count = 0


# Gets data from API
def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}, check the API and try again.')
    return res


# Checks how many times password was hacked
def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0


# Checks how many times password was hacked, continued
def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)
    return get_password_leaks_count(response, tail)


# Prints if password has been hacked and how many times
def main_hacker(password):
    count_hacked = pwned_api_check(password)
    if count_hacked:
        tk.Label(text=f'{password.__len__() * "*"} was hacked {count_hacked} times!').grid(column=0, row=6)
    else:
        tk.Label(text=f'{password.__len__() * "*"} was NOT hacked.').grid(column=0, row=6)
