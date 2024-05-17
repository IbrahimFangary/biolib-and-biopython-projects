from Bio import ExPASy #used to search domain specific details of protein
from Bio.ExPASy import Prosite
from Bio import SeqIO
handle =ExPASy.get_prosite_raw('PS51442') #number assosiated with doamain 
record =Prosite.read(handle)
print(record.description)
print(record.pdb_structs[:10])
from Bio.ExPASy import ScanProsite
prot_record=SeqIO.read('C:/Users/user/Downloads/nuc_seq.fasta',format='fasta')
print(len(prot_record))
handle=ScanProsite.scan(seq=prot_record.seq,mirror='http://prosite.expasy.org/')
result=ScanProsite.read(handle)
print(result.n_match)
