#this code opens a list of fasta files for further analysis
import biolib
###IMPORTANT NOTE  #######  dont forget to add the alphaford2 license and the license information  ########
directory = 'C:/Users/user/Downloads/New folder' #direction of your files
# name the files with a numbers from 1 to N and change the N as you like
N= 150 #number of files 
list_of_files_not_found=[]
for i in range(1, N+1):
    filename = f"{i}.fasta"  # Assuming fasta files are named like '1.fasta', '2.fasta', etc.
    
    try:
        alphafold = biolib.load('AlphaFold/alphafold')
        alphafold_results = alphafold.cli(args=filename)
        alphafold_results.save_files("C:/Users/user/Downloads/dir")
        print(f'mabrook ya m3alem, your pdb file of {i}.fasta is ready')
    except FileNotFoundError:
        list_of_files_not_found.append(filename)  
    except IOError:
        print(f"Error reading file '{filename}'.")
        
print('list of files that are not found:',list_of_files_not_found)
# Additional processing or analysis of file contents can be performed here
#if you want to visualize the result, there is a code to do so in biolib documenation website
