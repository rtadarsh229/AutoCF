import sys
import os
import sublime_plugin
import _thread
import threading
import subprocess

class TestCaseParser:
    def runCommand(file_name):
        script_filename = "ip.py"
        path = file_name.split("\\")
        current_driver = path[0]
        path.pop()
        current_directory = "\\".join(path)
        command = "cd " + current_directory + " & "+current_driver + " & python " + script_filename

        subprocess.call(command, shell=True)


class CmdCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        try:
            _thread.start_new_thread(TestCaseParser.runCommand, (self.view.file_name(),))
        except Exception as e:
            print("Error: unable to start thread - " + str(e))