import re
import sys
import os

from mysql_tables import create_pathway_table, load_table

sys.path.append(os.path.abspath('../'))
from data import *

def genfile(boo):
	b = os.getcwd()
	a = os.path.abspath(os.path.join(os.pardir, 'bin', 'php', 'settings', 'pathway.php'))
	php = "<?php\n$available_pathway = {0};\n?>".format(boo)
	with open(a, "w") as outfile:
		outfile.write(php)

def add_description():
	print('add pathway')
	genfile('TRUE')

def no_description():
	print('no pathway')
	genfile('FALSE')

if __name__ == '__main__':
	print(reference_pathway)
	if reference_pathway:
		create_pathway_table()
		a = os.path.abspath(os.path.join(os.pardir, 'data', reference_pathway))
		load_table('pathway', a)
		add_description()
	else:
		no_description()
