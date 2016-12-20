## MySQL details
database_host = 'localhost'
database_user = 'root'
database_password =  'loyola'
database_db = 'rnaseqchipseq'

## Reference genome
#reference_genome = 'Zea_mays.AGPv3.21.dna.chromosome.fa'
reference_genome = 'reference_genome.fa'
reference_gtf = 'reference.gtf'

## Additional information
reference_description = 'genedesc.txt'
reference_pathway = 'pathway.txt'
reference_go = 'go.txt'
reference_ortholog = 'ortholog.txt'

## Executables
program_meme = '/home/kreva/meme/bin/meme'
program_blast = '/usr/bin'
program_goatools = '/usr/local/bin/find_enrichment.py'
program_goatools_plot = '/usr/local/bin/plot_go_term.py'
program_jbrowse = 'jbrowse'

## Document_root
document_root = '/var/www/html'

## tar
#tar zcvf genomeexplorer.tar.gz * --exclude=php --exclude=bin/data --exclude=bin/php/data