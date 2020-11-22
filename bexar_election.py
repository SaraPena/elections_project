import pandas as pd

with open('bexar_election_results.txt', 'r') as data:
    lines = data.readlines()

type(lines[0])

len(lines)

a=[0,1,2,3]

for n in a:
    print(a[0:4])


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
filler=[]
district=[]
Filler2=[]


for line in lines:
    racecode.append(line[0:4])
    candidatecode.append(line[4:7])
    precincts.append(line[7:11])
    totals.append(line[11:17])
    election_day.append(line[17:23])
    absentee.append(line[23:29])
    early_voting.append(line[29:35])
    filler.append(line[35:101])
    candidate_party.append(line[101:104])
    district_code.append(line[104:111])
    race_name.append(line[111:167])
    candidate_name.append(line[167:205])
    precinct.append(line[205:209])
    filler.append(line[209:235])
    district.append(line[235:260])

race_name=pd.Series(race_name)
race_name.value_counts()
precincts=pd.Series(precincts)
precincts.nunique()