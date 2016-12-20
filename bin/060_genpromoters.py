import re
import sys
import os
#from helpers import get_path, run_system_cmd
from mysql_connection import execute
from mysql_tables import create_promoter_table, load_table

sys.path.append(os.path.abspath('../'))
from data import *

class Promoters:

	def __init__(self, filename):
		self.filename = filename
		#self.chrs = []
		## Only for testing
		#self.chrs = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Mt', 'Pt']
		self.chrs = ['1']

	def save_chromosome(self, chr, seq):
		print(chr)
		self.chrs.append(chr)
		fh = open("data/reference_sequence." + chr + ".fasta", "w")
		fh.write(">"+chr+"\n"+seq+"\n")
		fh.close()

	def split_fasta_file(self):
		fh = open('../data/'+self.filename, "r")
		pre = ''
		seq = ''
		for line in fh:
			line = line.rstrip("\r|\n")
			if ">" in line:
				chr = re.search('>([0-9A-Za-z_]*) ', line).group(1)
				#print(pre, chr, line)
				if seq != '' and pre != chr:
					#print(">", pre, "\n", seq, "\n")
					self.save_chromosome(pre, seq)
					pre = chr
					seq = ''
				else:
					pre = chr
			else:
				seq += line
		#print(">", pre, "\n", seq, "\n")
		self.save_chromosome(pre, seq)

	def get_chrs(self):
		return self.chrs

	def get_header_seq(self, filename):
		fh = open("data/" + filename, "r")
		line = fh.readline()
		seq = fh.readline()
		fh.close
		return line, seq

	def get_stend_pos_genes(self, chr):
		sql = 'select * from gff where chr like "' + chr + '"'
		print(sql)
		out = execute(sql)
		return out

	def mask_genes(self):
		for chr in self.get_chrs():
			#fh = open(get_path("reference_sequence." + chr + ".fasta"), "r")
			#line = fh.readline()
			#seq = fh.readline()
			#fh.close
			#print(chr, line, len(seq))
			line, fseq = self.get_header_seq("reference_sequence." + chr + ".fasta")
			rseq = fseq
			print(chr, line, len(fseq))
			out = self.get_stend_pos_genes(chr)
			#print(fseq[105024300:105025150])
			for row in out:
				#print(row);
				#print(row['start'], row['end']);
				st = int(row['start']) - 1
				en = int(row['end'])
				xing = "X" * (en - st)
				if row['strand'] == '+':
					fseq = fseq[:st] + xing + fseq[en:]
				if row['strand'] == '-':
					rseq = rseq[:st] + xing + rseq[en:]
				#print(fseq[105024300:105025150])
				#break
			fh = open("data/reference_sequence." + chr + ".masked.forward.fasta", "w")
			fh.write(line + fseq)
			fh.close()
			fh = open("data/reference_sequence." + chr + ".masked.reverse.fasta", "w")
			fh.write(line + rseq)
			fh.close()

	def toleft(self, seq, pos, pre):
		st = int(pos) - pre - 1
		en = int(pos) - 1
		if(st < 0):
			st = 0
		pro = seq[st:en]
		pro = re.sub(r".*X", "", pro)
		return str(st), str(en), pro

	def toright(self, seq, pos, pre):
		st = int(pos)
		en = int(pos) + pre
		if(en > len(seq)):
			en = len(seq) - 1
		pro = seq[st:en]
		pro = re.sub(r"X.*", "", pro)
		return str(st), str(en), pro

	def get_promoters(self, num):
		fh = open("data/promoters.sql.{}.txt".format(num), "w")
		for dir in ["forward", "reverse"]:
			for chr in self.get_chrs():
				print(chr)
				line, seq = self.get_header_seq("reference_sequence." + chr + ".masked."+dir+".fasta")
				out = self.get_stend_pos_genes(chr)
				for row in out:
					if row['strand'] == '+' and dir == "forward":
						st, en, pro = self.toleft(seq, row['start'], num)
						fh.write(row['gene_id'] +"\t"+ chr +"\t"+ st +"\t"+ en +"\tupstream\t"+ pro +"\n")
						st, en, pro = self.toright(seq, row['end'], num)
						fh.write(row['gene_id'] +"\t"+ chr +"\t"+ st +"\t"+ en +"\tdownstream\t"+ pro +"\n")
					if row['strand'] == '-' and dir == "reverse":
						st, en, pro = self.toright(seq, row['end'], num)
						fh.write(row['gene_id'] +"\t"+ chr +"\t"+ st +"\t"+ en +"\tdownstream\t"+ pro +"\n")
						st, en, pro = self.toleft(seq, row['start'], num)
						fh.write(row['gene_id'] +"\t"+ chr +"\t"+ st +"\t"+ en +"\tupstream\t"+ pro +"\n")
		fh.close()

	def load_promoters_to_mysql(self):
		ls = ['10000', '5000', '2000', '1000', '500']
		for l in ls:
			filename = 'data/promoters.sql.'+ l +'.txt'
			tname = "promoter_" + l
			print(filename, tname)
			create_promoter_table(tname)
			load_table(tname, filename)

if __name__ == '__main__':
	#filename = 'test.fasta'
	filename = reference_genome
	a = Promoters(filename)
	#a.split_fasta_file()
	#print(a.get_chrs())
	#a.mask_genes()
	#a.get_promoters(500)
	#a.get_promoters(1000)
	#a.get_promoters(2000)
	#a.get_promoters(5000)
	#a.get_promoters(10000)
	a.load_promoters_to_mysql()
