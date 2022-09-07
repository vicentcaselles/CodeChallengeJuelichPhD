wget https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/001/298/445/GCF_001298445.1_ASM129844v1/GCF_001298445.1_ASM129844v1_protein.faa.gz -O N_piscinale.faa.gz
gzip -d N_piscinale.faa.gz
wget https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/000/020/025/GCF_000020025.1_ASM2002v1/GCF_000020025.1_ASM2002v1_genomic.fna.gz -O N_punctiforme.faa.gz
gzip -d N_punctiforme.faa.gz
makeblastdb -dbtype prot -in N_punctiforme.faa
makeblastdb -dbtype prot -in N_piscinale.faa 
blastp -query N_piscinale.faa -db N_punctiforme.faa -outfmt 6 -out N_piscinale_N_punctiforme.txt -evalue 1e-6
blastp -query N_punctiforme.faa -db N_piscinale.faa -outfmt 6 -out N_punctiforme_N_piscinale.txt -evalue 1e-6
python3 RBH_v1.py N_piscinale_N_punctiforme.txt N_punctiforme_N_piscinale.txt output_RBH.txt