from Bio.Blast import NCBIWWW
from Bio import SeqIO, SearchIO
#nucleotide BLAST
nuc_record =SeqIO.read('C:/Users/user/Downloads/nuc_seq.fasta', format='fasta')
# print(len(nuc_record))
# print(nuc_record.description)
# print(nuc_record.seq)
result_handle=NCBIWWW.qblast('blastn','nt',nuc_record.seq)
blast_handle=SearchIO.read(result_handle,'blast-xnl')
print(blast_handle[0:2])
seq=blast_handle[0]
details=seq[0]
print('evalue:',details.evalue)
print(f'alignment:\n{details.aln}')
#protein blast
prot_record =SeqIO.read('C:/Users/user/Downloads/prot_seq.fasta', format='fasta')
# print(len(prot_record))
# print(prot_record.description)
# print(prot_record.seq)
result_handle=NCBIWWW.qblast('blastp','pdb',prot_record.seq)
blast_handle=SearchIO.read(result_handle,'blast-xnl')
print(blast_handle[0:2])
seq=blast_handle[0]
details=seq[0]
print('evalue:',details.evalue)
print(f'alignment:\n{details.aln}')