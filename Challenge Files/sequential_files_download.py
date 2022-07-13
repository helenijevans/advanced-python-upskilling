import requests
from bs4 import BeautifulSoup
import re
import wget
import os

"""
FIRST SOLUTION
"""

# def download_seq(url, output_path):
#     soup = BeautifulSoup(requests.get(url).text, features="html.parser")
#
#     for link in soup.find_all('a'):
#         link_url = link.get('href')
#         if re.match(".*\.jpg$", link_url):
#             if not os.path.isdir("./Sequential Files"):
#                 os.mkdir("./Sequential Files")
#             wget.download(url+link_url, out=output_path)
#             print(f"Downloaded file {link_url}")
#
#
# download_seq(url='http://699340.youcanlearnit.net/', output_path="./Sequential Files")
"""
Analysis
"""
# Implemented a function that gets how many items there are and downloads that
# However went further ahead to the example given and we're not meant to work out how many items
# Meant to increment until a file no longer exists
# SO...REWRITING

"""
SECOND SOLUTION
"""


def download_seq(url, output_path):
    if not os.path.isdir(output_path):
        os.mkdir(output_path)
    successful = True
    while successful == True:
        try:
            wget.download(url, out=output_path)
            print(f"Successfully downloaded\n{url}")

            digit = int((re.findall(".*(\d{3}).jpg$", url))[0])
            increment_digit = f"{digit + 1:03}" + '.jpg'
            url = re.sub("\d{3}.jpg", increment_digit, url)
        except:
            print(f"Could not retrieve\n{url}\n-- Stopping Iterative Search --")
            successful = False


download_seq(url='http://699340.youcanlearnit.net/image001.jpg', output_path="./Sequential Files")

"""
Analysis
"""
# Making a couple of assumptions in this solution
# That the files are .jpgs, and that the incremental value is a 3 digit number at the end of the url

"""
GIVEN SOLUTION
"""
# import os
# import re
# import urllib.parse
# import urllib.request
#
#
# def download_files(first_url, output_dir):
#     if not os.path.isdir(output_dir):
#         os.mkdir(output_dir)
#     url_head, url_tail = os.path.split(first_url)
#     first_index = re.findall(r'[0-9]+', url_tail)[-1]
#     index_count, error_count = 0, 0
#     while (error_count < 5):
#         next_index = str(int(first_index) + index_count)
#         if first_index[0] == '0':  # zero padded
#             next_index = '0' * (len(first_index) - len(next_index)) + next_index
#         next_url = urllib.parse.urljoin(url_head, re.sub(first_index, next_index, url_tail))
#         try:
#             output_file = os.path.join(output_dir, os.path.basename(next_url))
#             urllib.request.urlretrieve(next_url, output_file)
#             print('Successfully downloaded {}'.format(os.path.basename(next_url)))
#         except IOError:
#             print('Could not retrieve {}'.format(next_url))
#             error_count += 1
#         index_count += 1

# REFLECTION
# Believe my solution to be more readable and concise but the given solution is able to pad numbers so is
# compatible with a wider range of URL variations. Also specified the type of exception caught which is better practice.
