from logging import error
from bs4 import BeautifulSoup
from pywinauto import Application
import requests
import sys
import os
import json
import shutil

def main():

    # Get url of current window using pywinauto
    app = Application(backend='uia')
    app.connect(title_re=".*Chrome.*")
    dlg = app.top_window()
    url = dlg.child_window(title="Address and search bar", control_type="Edit").get_value()
    if url.find('https://') == -1:
        url = 'https://' + url
    if url.find('https://codeforces.com') == -1 and url.find('https://codechef.com') == -1:
        print('Please open a problem page and try again')
        exit()
    else:
        try:
            html_text = requests.get(url).text
        except error as e:
            print(e)
            exit()

    # parse the testcases
    soup = BeautifulSoup(html_text, 'lxml')
    sample_tests = soup.select('pre')

    input_string = str(sample_tests[0])[6:-6]
    output_string = str(sample_tests[1])[6:-6]

    write_input = open("input.txt", 'w')
    write_input.write(input_string)

    write_output = open("correct.txt", 'w')
    write_output.write(output_string)
    
if __name__ == '__main__':
    main()