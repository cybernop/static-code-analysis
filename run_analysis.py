from os import listdir, path
import subprocess

entries = listdir(path.join(path.dirname(path.realpath(__file__)), 'modules'))
entries = [path.join('modules', entry) for entry in entries]
command = 'pylint ' + ' '.join(entries)

subprocess.run(command, shell=True)
