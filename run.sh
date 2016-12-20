#!/usr/bin/env bash

## Run the scripts in bin folder 
cd bin
python3 010_genome.py
python3 020_gtf.py
python3 021_descriptions.py
python3 022_pathway.py
python3 023_goterms.py
python3 024_ortholog.py
python3 030_user.py
python3 040_rnaseq.py
python3 050_chipseq.py
python3 060_genpromoters.py
python3 070_programs.py
python3 080_genmotifs.py

## Copy the PHP folder to DOCUMENT_ROOT
#cp -r php/* /var/www/html/.

## Leave folder
cd ..

