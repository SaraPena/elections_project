# Source Urls - https://www.bexar.org/DocumentCenter/View/28547/Election-by-Precinct-Text-File-Layout
# Source Urls - https://www.bexar.org/DocumentCenter/View/28546/November-3-2020-General-Election-by-Precinct-Text-File
# Source Urls - https://www.bexar.org/2186/Historical-Election-Results

# use pandas to set up a dataframe
import pandas as pd 


# read text file in the folder bexar_election_results.txt
# 'data' is an arbitrary variable name
# create a list of strings that contain each line of the data with .readlines()
# each line in the data contains one race result per precinct

def get_bexar20_data():
    with open('bexar_election_results.txt', 'r') as data:
        lines = data.readlines()


# From precinct layout text file I was able to find the structure of data for each line - https://www.bexar.org/DocumentCenter/View/28547/Election-by-Precinct-Text-File-Layout
# create an empty list for each field/variable label

    racecode=[]
    candidatecode=[]
    precincts=[]
    totals=[]
    election_day=[]
    absentee=[]
    early_voting=[]
    filler=[]
    candidate_party=[]
    district_code=[]
    race_name=[]
    candidate_name=[]
    precinct=[]
    district=[]


    for line in lines:
        racecode.append(line[0:4])
        candidatecode.append(line[4:7])
        precincts.append(line[7:11])
        totals.append(line[11:17])
        election_day.append(line[17:23])
        absentee.append(line[23:29])
        early_voting.append(line[29:35])
        candidate_party.append(line[101:104])
        district_code.append(line[104:111])
        race_name.append(line[111:167])
        candidate_name.append(line[167:205])
        precinct.append(line[205:209])
        district.append(line[235:260])


    # Running through lists to explore data
    # race_name=pd.Series(race_name)
    # race_name.value_counts()
    # precincts=pd.Series(precincts)
    # precincts.nunique()


    # Create the dataframe by combining each list
    df=pd.DataFrame({'racecode':racecode,\
        'candidatecode':candidatecode, \
        'precincts':precincts,\
        'totals':totals,\
        'election_day':election_day,\
        'absentee':absentee,\
        'early_voting':early_voting,\
        'candidate_party':candidate_party,\
        'district_code':district_code,\
        'race_name':race_name,\
        'candidate_name':candidate_name, \
        'precinct':precinct,\
        'district':district})
        
    return df
