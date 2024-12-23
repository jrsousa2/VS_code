# IF THE DRIVE OF D:\MP3 FOLDER CHANGES
# THIS CODE CAN UPDATE THE ITUNES LIBRARY

from os.path import exists
#from os import listdir 
import Read_PL
import Tags
from Files import get_Win_files


# COMPARES TWO SETS CASE-INSENTITIVE
def Set_diff(orig_set, comp_set):
    # CREATES SETS
    orig_set_lower = {item.lower() for item in orig_set}
    comp_set_lower = {item.lower() for item in comp_set}

    # TAKES THE DIFFERENCE OF THE 2 SETS    
    diff_lower = orig_set_lower.difference(comp_set_lower)
    
    # FOR EACH ELEMENT IN THE DIFFERENT OF THE 2 SETS, FINDS ORIGINAL VALUE (NON LOWERCASE)
    diff = [item for item in orig_set if item.lower() in diff_lower]
    # TURNS LIST TO SET
    diff = set(diff)
    
    return diff


def Call_Add_miss(PL_name=None,PL_nbr=None,Do_lib=False,rows=None):
    # CALLS FUNCTION
    col_names =  ["Arq"] 
    dict = Read_PL.Read_PL(col_names,PL_name=PL_name,PL_nbr=PL_nbr,Do_lib=Do_lib,rows=rows) 
    # App = dict['App']
    PLs = dict['PLs']
    df = dict['DF']

    # TEST LIST CREATION (list comprehension) 
    Arq = [x.lower() for x in df["Arq"]]
    Arq_set = set(Arq)
    #Arq_set_lower = {x.lower for x in Arq_set}
    nbr_files = len(Arq)
    #print()
    print("\nPlaylist has",nbr_files,"files (",len(Arq_set),"distinct)\n")

    # LIST OF ALL MP3 FILES
    dir_path = "D:\\MP3"
    print("Building list of mp3 files in",dir_path)
    Dir_set_tuple = get_Win_files(dir_path, ".mp3")
    Dir_set = [x for (x,y) in Dir_set_tuple]
    nbr_dir_files = len(Dir_set)
    print("\nDirectory has",nbr_dir_files,"files\n")

    
    #file_list = [file for file in listdir(dir) if file.endswith(".mp3")]
    print("Searching missing files\n")
    # BELOW COMPARISON IS CASE INSENSITIVE
    miss_files = Set_diff(Dir_set, Arq_set)
    miss_files = list(miss_files)
    nbr_miss_files = len(miss_files)

    # STATS
    print("Files in the directory:",nbr_dir_files)
    print("Files in the playlist:",nbr_files,"(",len(Arq_set),"distinct)")
    print("Missing files to add:",nbr_miss_files,"\n")

    # CHAMA A FUNCAO QUE CRIA A PL
    # CRIA PLAYLIST APENAS SE HOUVER ARQUIVOS 
    Created_PL_name = "Newly_added"
    if nbr_miss_files>0:
       Move_PL =Read_PL.Cria_PL(Created_PL_name,recria="y")

    # READS PLAYLISTS
    for j in range(nbr_miss_files):
        miss_file = miss_files[j]
        print("Adding file",j+1,"of",nbr_miss_files,"missing:",miss_file)
        Read_PL.Add_file_to_PL(PLs,Created_PL_name,miss_file)

# CALLS FUNC ,rows=500
Call_Add_miss(PL_name="ALL",Do_lib=True, rows=None)