# AutoCF
An automatic test case parser that grabs test cases from Codeforces and feeds it to CppFastOlympicCoding or "input.txt" file

# How to Setup:
- Install the required dependencies
- Clone the [repo](https://github.com/rtadarsh/AutoCF)
- If you use CppFastOlympicCoding
    - Open Sublime Text -> Preferences -> Browse Packages. Copy the CMD folder here.
    - Open cmd.py in CMD folder. In line 10, set script_filename as "olympic.py"
    - In CppFastOlympicCoding settings, add this line: "tests_file_suffix": "__tests"
    - Copy olympic.py in your desired folder where you solve questions
- If you use "input.txt" and "output.txt"
    - Open Sublime Text -> Preferences -> Browse Packages. Copy the CMD folder here.
    - Copy ip.py in your desired folder where you solve questions
- Open Preferences -> Settings and add this line: "always_prompt_for_file_reload": false
- Open the Codeforces problem page on Google Chrome (Don't minimize the browser)
- Open your solution file. Right click and select 'Load Test Cases'
- Continue writing your solution

# TLDR: YOU ONLY NEED TO SET ONE FILE OUT OF OLYMPIC.PY AND IP.PY

# Dependencies
- install Python3
- pip install bs4
- pip install lxml
- pip install pywinauto
- pip install requests

- If you find any other missing dependency, install it by using command 'pip install {Dependency name}'

# Some more stuff
 This script can only grab testcases from Codeforces open on Google Chrome. Support for other sites and browsers may be added later (or maybe you can help me do it)
 
 If you find anything broken, feel free to contribute ❤️