<?php require ('../template/header.php'); ?>

<section class="content-header">
  <h1>Information on file formats</h1>
</section>
<section class="content">
	<div class="box">
		<div class="box-body">
		  <h4>Reference genome</h4>
		  <pre>
>1
GGATTTTTGGAGGATTCGTCGATCCGACTACGACGAGCAAGCCTGAGGCGCCAATGCAAT
CGCTGAACCAACTCCCTGTGGTTACCGACCTTGCTGATGCGAGATCGGCCTGATCACGAA
>2
GGATTTTTGGAGGATTCGTCGATCCGACTACGACGAGCAAGCCTGAGGCGCCAATGCAAT
CGCTGAACCAACTCCCTGTGGTTACCGACCTTGCTGATGCGAGATCGGCCTGATCACGAA
		  </pre>
  	</div><!-- box-body -->
  </div><!-- box -->
  <div class="box">
		<div class="box-body">
		  <h4>Reference GFF</h4>
		  <pre>
1	gramene	gene	4854	9652	.	-	.	gene_id "Gene_2G059865"; gene_version "1"; gene_source "gramene"; gene_biotype "protein_coding";
1	gramene	transcript	4854	9652	.	-	.	gene_id "Gene_2G059865"; gene_version "1"; transcript_id "Gene_2G059865_T01"; transcript_version "1"; gene_source "gramene"; gene_biotype "protein_coding"; transcript_source "gramene"; transcript_biotype "protein_coding";
1	gramene	exon	9193	9652	.	-	.	gene_id "Gene_2G059865"; gene_version "1"; transcript_id "Gene_2G059865_T01"; transcript_version "1"; exon_number "1"; gene_source "gramene"; gene_biotype "protein_coding"; transcript_source "gramene"; transcript_biotype "protein_coding"; exon_id "Gene_2G059865_T01.exon1"; exon_version "1";
1	gramene	CDS	9193	9519	.	-	0	gene_id "Gene_2G059865"; gene_version "1"; transcript_id "Gene_2G059865_T01"; transcript_version "1"; exon_number "1"; gene_source "gramene"; gene_biotype "protein_coding"; transcript_source "gramene"; transcript_biotype "protein_coding"; protein_id "Gene_2G059865_P01"; protein_version "1";
1	gramene	start_codon	9517	9519	.	-	0	gene_id "Gene_2G059865"; gene_version "1"; transcript_id "Gene_2G059865_T01"; transcript_version "1"; exon_number "1"; gene_source "gramene"; gene_biotype "protein_coding"; transcript_source "gramene"; transcript_biotype "protein_coding";
		  </pre>
  	</div><!-- box-body -->
  </div><!-- box -->
  <div class="box">
		<div class="box-body">
		  <h4>Gene descriptions</h4>
		  <pre>
#gene_id  description
Gene_2G122523	1-aminocyclopropane-1-carboxylate oxidase
Gene_2G122524	Uncharacterized protein
Gene_2G122525	Uncharacterized protein
Gene_2G122526	Uncharacterized protein
Gene_2G122527	Proteasome subunit alpha type
Gene_2G122528	Uncharacterized protein
		  </pre>
  	</div><!-- box-body -->
  </div><!-- box -->
  <div class="box">
		<div class="box-body">
		  <h4>GO file</h4>
		  <pre>
#gene_id  go_term go_description
Gene_2G151616	GO:0046872	metal ion binding
Gene_2G151616	GO:0008270	zinc ion binding
Gene_2G151616	GO:0005515	protein binding
Gene_2G111238	GO:0005622	intracellular
Gene_2G111238	GO:0003676	nucleic acid binding
		  </pre>
  	</div><!-- box-body -->
  </div><!-- box -->
  <div class="box">
		<div class="box-body">
		  <h4>Ortholog file</h4>
		  <pre>
#gene_id	species1	species1_desc	species2	species2_desc	species3	species3_desc	species4	species4_desc	species5	species5_desc	species6	species6_desc
Gene_2G439951			Gene_39503m.g	Uncharacterized protein		Gene_032813	Putative uncharacterized protein	OS10G0376400	Phosphate-induced protein 1 conserved region containing protein; Putative uncharacterized protein Gene_0095C06.7	Gene_005000	Putative uncharacterized protein Gene_005000 
Gene_2G094632			Gene_38090m.g	Uncharacterized protein		Gene_032533	Putative uncharacterized protein	OS10G0148000	Protease inhibitor/seed storage/LTP family protein, expressed	Gene_026220	Putative uncharacterized protein Gene_026220 
Gene_2G095094	Gene_2G01740	Tetratricopeptide repeat (TPR)-like superfamily protein	Gene_025982m.g	Uncharacterized protein			Gene_032530	Putative uncharacterized protein	Gene_0147250	Putative salt-inducible protein	Gene_026260	Putative uncharacterized protein Gene_026260 
		  </pre>
  	</div><!-- box-body -->
  </div><!-- box -->
</section>


<?php require ('../template/footer.php'); ?>

