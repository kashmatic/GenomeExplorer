import pymysql
conn = pymysql.connect(host='localhost', user='root', passwd='loyola', db='rnaseqchipseq')
cur = conn.cursor()

peaks = {}

cur.execute("SELECT * FROM chipseq")
for r in cur:
	peaks[r[9]] = {}
	peaks[r[9]]['chr'] = r[0]
	peaks[r[9]]['start'] = r[1]
	peaks[r[9]]['end'] = r[2]
	peaks[r[9]]['summit'] = r[4]
cur.close()

pro = conn.cursor()

print(peaks)

for key in peaks.keys():
	pro.execute("SELECT * FROM promoter_500 where start <= " + str(peaks[key]['start']) + " and end > "+ str(peaks[key]['end']))
	for r in pro:
		motifstart = int(peaks[key]['start']) - int(r[1])
		motifend = int(peaks[key]['end']) - int(r[1])
		print(key +
			"\t" + peaks[key]['chr'] +
			"\t" + str(peaks[key]['start']) +
			"\t" + str(peaks[key]['end']) +
			"\t" + str(peaks[key]['summit']) +
			"\t" + r[5][motifstart:motifend])
pro.close()

conn.close()