import os
import sys
import shutil

from mysql_tables import create_cluster, load_table

sys.path.append(os.path.abspath('../'))
from data import *

def setup_meme():
	meme = os.path.abspath(os.path.join(os.pardir, 'php', 'sequence', 'memeprogram.php'))
	with open(meme, 'w') as fh:
		fh.write("<?php\n$memeprogram='"+ program_meme +"';\n?>")

def setup_blastdb():
	ref_dir = os.path.abspath(os.path.join(os.pardir, 'data'))
	src = os.path.join(ref_dir, reference_genome)
	target = os.path.abspath(os.path.join(os.pardir, 'bin', 'php', 'data', reference_genome))
	print(src)
	print(target)
	shutil.copyfile(src, target)
	cmd = program_blast + '/makeblastdb -in '+ src +' -dbtype nucl -out '+ target
	os.system(cmd)

def setup_blast_program():
	meme = os.path.abspath(os.path.join(os.pardir, 'bin', 'php', 'sequence', 'blastprogram.php'))
	#rint(meme)
	target = os.path.join('data', reference_genome)
	with open(meme, 'w') as fh:
		fh.write("<?php\n$blastprogram='"+ program_blast +"';\n$blastdb='"+ target +"'\n;?>")

def load_cluster():
	ref_dir = os.path.abspath(os.path.join(os.pardir, 'data'))
	cluster = os.path.join(ref_dir, 'cluster.txt')
	create_cluster
	load_table('cluster', cluster)

if __name__ == '__main__':
	setup_meme()
	setup_blastdb()
	setup_blast_program()
	load_cluster()