from Bio.KEGG import REST, Enzyme
request =REST.kegg_get('ec:5.4.2.2') #ec stands for enzyme commission number
open('C:/Users/user/Downloads/a7a.txt','w').write(request.read())

records= Enzyme.parse(open('C:/Users/user/Downloads/a7a.txt','r'))
record=list(records)[0]
print(record.classname)
print(record.pathway)
print(record.genes[:10])
list_genes=[]
for x,y in record.genes:
    list_genes+= x.split("\n")
print(list_genes)