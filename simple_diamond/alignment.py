import blosum as bl
from full_smithwaterman import *
from read_fasta import *
import pandas as pd
import os


def find_best_alignment(DNA_query,protein_database):
    '''
        DNA_query: dictionary of DNA query sequences
        protein_database: dictionary of protein database sequences
        return the name of the best match protein database, and the alignment
    '''
    
    alignments={}
    for query_name,query_protein in DNA_query.items():
        querys=[]
        for data_name,data_protein in protein_database.items():
            max_score = -100000
            max_score_name_protein = ""
            max_score_alignment = []
            query={}
            for i in range(len(query_protein)):
                query_read=query_protein[i]
                alignment = SMalignment(query_read, data_protein,bl.BLOSUM(62))
                score= int(alignment[3])
                if score>max_score:
                    
                    max_score=score
                    max_score_name_protein=data_name
                    max_score_alignment=list(alignment)
                    max_score_alignment.append(i)
                    position=data_protein.find(alignment[2].replace('-',''))
                    frame=i
                    query["data_name"]=data_name
                    query["score"]=score
                    query["alignment"]=alignment
                    query["frame"]=frame
                    query["position"]=position
                    querys=[query]
                elif score==max_score:
                    position=data_protein.find(alignment[2].replace('-',''))
                    frame=i
                    query["data_name"]=data_name
                    query["score"]=score
                    query["alignment"]=alignment
                    query["frame"]=frame
                    query["position"]=position
                    querys.append(query)
        alignments[query_name]=querys

    return alignments
#example usage

if __name__=='__main__':
    CURR_DIR = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(CURR_DIR,'test_DNA_query.fasta')) as protein_database:
        DNA_query = protein_database.readlines()
    with open(os.path.join(CURR_DIR,'test_protein_database.fasta')) as protein_database:
        protein_database = protein_database.readlines()
    DNA_query,_ = read_fasta_for_DNA(DNA_query)
    protein_database,_ = read_fasta_for_proteins(protein_database)
    # print("DNA query:",DNA_query)
    alignments = find_best_alignment(DNA_query,protein_database)
    print("test")
    print(alignments)
    # print("best match protein database name:",protein_name)
    # print("best match query name:",query_name)
    # print(alignment[1])
    # print(alignment[0])
    # print(alignment[2])

    # # print("database alignment:",alignment[0])
    # # print("query alignment:",alignment[2])
    # print("score:",alignment[3])
    # print('frame number:',alignment[4])
    # print('position:',alignment[5])