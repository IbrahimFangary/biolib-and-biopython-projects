from Bio.PDB import PDBParser, PDBList

pdbl=PDBList()
print(pdbl.retrieve_pdb_file('pdb from the 3d structure',file_format='pdb',pdir='dir'))
parser=PDBParser()
structure=parser.get_structure('pdb from the 3d structure','paste here the pdb file')
for chain in structure[0]: #printing chains of protein
    print(f'chainid:{chain.id}')
resolutions=structure.header['resolution'] #the header is for the protein information header 
print(resolutions) #printing resoluition of protein which is the certainity of positions of every atom
keywords=structure.header['keywords']
print(keywords) #printing all kewwords of the protein 
