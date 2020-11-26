

# CREATING DATA_SET*********************************************************
data_set = {
    "set_one":[
        {
            "gender": "female",
            "height": 1.6,
            "class": "short"
        },
        {
            "gender": "female",
            "height": 1.9,
            "class": "medium",
        },
        {
            "gender": "female",
            "height": 1.85,
            "class": "medium",
        },
        {
            "gender": "female",
            "height": 1.6,
            "class": "short",
        },
        {
            "gender": "female",
            "height": 1.65,
            "class": "short",
        }
    ],
    "set_two":[

        {
            "gender": "male",
            "height": 2.0,
            "class": "tall",

        },
        {
            "gender": "male",
            "height": 2.8,
            "class": "tall",
        },
        {
            "gender": "male",
            "height": 1.7,
            "class": "short",
        },
        {
            "gender": "male",
            "height": 1.8,
            "class": "medium",
        }
    ]

}
# DATA_SET created ******************************************************

#*******************probability******************************************
TotalNumOfData = len(data_set["set_one"]) + len(data_set["set_two"])

val_S,val_M,val_T = 0,0,0
male_S,male_M,male_T = 0,0,0
female_S,female_M,female_T = 0,0,0
for x in data_set['set_one']:
    if x.get("class") == "short" :
        val_S += 1
        female_S += 1
    elif x.get("class") == "medium":
        val_M += 1
        female_M += 1
    elif x.get("class") == "tall":
        val_T += 1
        female_T += 1
for x in data_set['set_two']:
    if x.get("class") == "short" :
        val_S += 1
        male_S += 1
    elif x.get("class") == "medium":
        val_M += 1
        male_M += 1
    elif x.get("class") == "tall":
        val_T += 1
        male_T += 1

NumOfFemaleShort = female_S
NumOfFemaleMedium = female_M
NumOfFemaleTall = female_T
NumOfMaleShort = male_S
NumOfMaleMedium = male_M
NumOfMaleTall = male_T

TotalNumOfShort = val_S
TotalNumOfMedium = val_M
TotalNumOfTall = val_T

ProbOfShort = TotalNumOfShort/TotalNumOfData
ProbOFMedium = TotalNumOfMedium/TotalNumOfData
ProbOfTall = TotalNumOfTall/TotalNumOfData

print("Probability of short : ",end="")
print(round(ProbOfShort,2))
print("Probability of medium : ",end="")
print(round(ProbOFMedium,2))
print("Probability of tall : ",end="")
print(round(ProbOfTall,2))


# CREATING Probability chart *****************************************************
Prob_shortMale = NumOfMaleShort/TotalNumOfShort
Prob_mediumMale = NumOfMaleMedium/TotalNumOfMedium
prob_tallMale = NumOfMaleTall/TotalNumOfTall
Prob_shortFemale = NumOfFemaleShort /TotalNumOfShort
Prob_mediumFemale = NumOfFemaleMedium/TotalNumOfMedium
Prob_tallFemale = NumOfFemaleTall/TotalNumOfTall

print(NumOfMaleShort,NumOfMaleMedium,NumOfMaleTall)
print(NumOfFemaleShort,NumOfFemaleMedium,NumOfFemaleTall)

print(round(Prob_shortMale,2),round(Prob_mediumMale,2),round(prob_tallMale,2))
print(round(Prob_shortFemale,2),round(Prob_mediumFemale,2),round(Prob_tallFemale,2))


val_S,val_M,val_T = 0,0,0

for x in data_set['set_one']:
    if x.get("height") >= 0 and x.get("height") <= 1.60:
        if x.get("class") == "short":
            val_S += 1
        elif x.get("class") == "medium":
            val_M += 1
        elif x.get("class") == "tall":
            val_T += 1

for x in data_set['set_two']:
    if x.get("height") >= 0 and x.get("height") <= 1.60:
        if x.get("class") == "short":
            val_S += 1
        elif x.get("class") == "medium":
            val_M += 1
        elif x.get("class") == "tall":
            val_T += 1

FirstRangeOfShort = val_S
FirstRangeOfMedium = val_M
FirstRangeOfTall = val_T



val_S,val_M,val_T = 0,0,0

for x in data_set['set_one']:
    if x.get("height") >= 1.61 and x.get("height") <= 1.70:
        if x.get("class") == "short":
            val_S += 1
        elif x.get("class") == "medium":
            val_M += 1
        elif x.get("class") == "tall":
            val_T += 1


for x in data_set['set_two']:
    if x.get("height") >= 1.61 and x.get("height") <= 1.70:
        if x.get("class") == "short":
            val_S += 1
        elif x.get("class") == "medium":
            val_M += 1
        elif x.get("class") == "tall":
            val_T += 1

SecondRangeOfShort = val_S
SecondRangeOfMedium = val_M
SecondRangeOfTall = val_T

val_S,val_M,val_T = 0,0,0

for x in data_set['set_one']:
    if x.get("height") >= 1.71 and x.get("height") <= 1.80:
        if x.get("class") == "short":
            val_S += 1
        elif x.get("class") == "medium":
            val_M += 1
        elif x.get("class") == "tall":
            val_T += 1


for x in data_set['set_two']:
    if x.get("height") >= 1.71 and x.get("height") <= 1.80:
        if x.get("class") == "short":
            val_S += 1
        elif x.get("class") == "medium":
            val_M += 1
        elif x.get("class") == "tall":
            val_T += 1

ThirdRangeOfShort = val_S
ThirdRangeOfMedium = val_M
ThirdRangeOfTall = val_T

val_S,val_M,val_T = 0,0,0

for x in data_set['set_one']:
    if x.get("height") >= 1.81 and x.get("height") <= 1.90:
        if x.get("class") == "short":
            val_S += 1
        elif x.get("class") == "medium":
            val_M += 1
        elif x.get("class") == "tall":
            val_T += 1


for x in data_set['set_two']:
    if x.get("height") >= 1.81 and x.get("height") <= 1.90:
        if x.get("class") == "short":
            val_S += 1
        elif x.get("class") == "medium":
            val_M += 1
        elif x.get("class") == "tall":
            val_T += 1

FourthRangeOfShort = val_S
FourthRangeOfMedium = val_M
FourthRangeOfTall = val_T

val_S,val_M,val_T = 0,0,0

for x in data_set['set_one']:
    if x.get("height") >= 1.91 and x.get("height") <= 2.0:
        if x.get("class") == "short":
            val_S += 1
        elif x.get("class") == "medium":
            val_M += 1
        elif x.get("class") == "tall":
            val_T += 1


for x in data_set['set_two']:
    if x.get("height") >= 1.91 and x.get("height") <= 2.0:
        if x.get("class") == "short":
            val_S += 1
        elif x.get("class") == "medium":
            val_M += 1
        elif x.get("class") == "tall":
            val_T += 1

FifthRangeOfShort = val_S
FifthRangeOfMedium = val_M
FifthRangeOfTall = val_T

val_S,val_M,val_T = 0,0,0

for x in data_set['set_one']:
    if x.get("height") >= 2.1 and x.get("height") <= 10:
        if x.get("class") == "short":
            val_S += 1
        elif x.get("class") == "medium":
            val_M += 1
        elif x.get("class") == "tall":
            val_T += 1


for x in data_set['set_two']:
    if x.get("height") >= 2.1 and x.get("height") <= 10:
        if x.get("class") == "short":
            val_S += 1
        elif x.get("class") == "medium":
            val_M += 1
        elif x.get("class") == "tall":
            val_T += 1

SixthRangeOfShort = val_S
SixthRangeOfMedium = val_M
SixthRangeOfTall = val_T


print(FirstRangeOfShort,FirstRangeOfMedium,FirstRangeOfTall)

print(SecondRangeOfShort,SecondRangeOfMedium,SecondRangeOfTall)

print(ThirdRangeOfShort,ThirdRangeOfMedium,ThirdRangeOfTall)

print(FourthRangeOfShort,FourthRangeOfMedium,FourthRangeOfTall)

print(FifthRangeOfShort,FifthRangeOfMedium,FifthRangeOfTall)

print(SixthRangeOfShort,SixthRangeOfMedium,SixthRangeOfTall)

print("probability of range : ")


Prob_FirstRangeOfShort = FirstRangeOfShort/TotalNumOfShort
Prob_FirstRangeOfMedium = FirstRangeOfMedium/TotalNumOfMedium
Prob_FirstRangeOfTall = FirstRangeOfMedium/TotalNumOfTall

print(round(Prob_FirstRangeOfShort,2),round(Prob_FirstRangeOfMedium,2),round(Prob_FirstRangeOfTall,2))

Prob_SecondRangeOfShort = SecondRangeOfShort/TotalNumOfShort
Prob_SecondRangeOfMedium = SecondRangeOfMedium/TotalNumOfMedium
Prob_SecondRangeOfTall = SecondRangeOfTall/TotalNumOfTall

print(round(Prob_SecondRangeOfShort,2),round(Prob_SecondRangeOfMedium,2),round(Prob_SecondRangeOfTall,2))

Prob_ThirdRangeOfShort = ThirdRangeOfShort/TotalNumOfShort
Prob_ThirdRangeOfMedium = ThirdRangeOfMedium/TotalNumOfMedium
Prob_ThirdRangeOfTall = ThirdRangeOfTall/TotalNumOfTall

print(round(Prob_ThirdRangeOfShort,2),round(Prob_ThirdRangeOfMedium,2),round(Prob_ThirdRangeOfTall,2))

Prob_FourthRangeOfShort = FourthRangeOfShort/TotalNumOfShort
Prob_FourthRangeOfMedium = FourthRangeOfMedium/TotalNumOfMedium
Prob_FourthRangeOfTall = FourthRangeOfTall/TotalNumOfTall

print(round(Prob_FourthRangeOfShort,2),round(Prob_FourthRangeOfMedium,2),round(Prob_FourthRangeOfTall,2))

Prob_FifthRangeOfShort = FifthRangeOfShort/TotalNumOfShort
Prob_FifthRangeOfMedium = FifthRangeOfMedium/TotalNumOfMedium
Prob_FifthRangeOfTall = FifthRangeOfTall/TotalNumOfTall

print(round(Prob_FifthRangeOfShort,2),round(Prob_FifthRangeOfMedium,2),round(Prob_FifthRangeOfTall,2))

Prob_SixthRangeOfShort = SixthRangeOfShort/TotalNumOfShort
Prob_SixthRangeOfMedium = SixthRangeOfMedium/TotalNumOfMedium
Prob_SixthRangeOfTall = SixthRangeOfTall/TotalNumOfTall

print(round(Prob_SixthRangeOfShort,2),round(Prob_SixthRangeOfMedium,2),round(Prob_SixthRangeOfTall,2))

g = input("Enter gender: m or f : ")
h = float(input("Enter height : "))

if g == 'm':
    if h >= 0 and h <= 1.6:
        Prob_TDShort = Prob_shortMale * Prob_FirstRangeOfShort
        Prob_TDMedium = Prob_mediumMale * Prob_FirstRangeOfMedium
        Prob_TDTall = prob_tallMale * Prob_FirstRangeOfTall

    elif h >= 1.61 and h <= 1.7:
        Prob_TDShort = Prob_shortMale * Prob_SecondRangeOfShort
        Prob_TDMedium = Prob_mediumMale * Prob_SecondRangeOfMedium
        Prob_TDTall = prob_tallMale * Prob_SecondRangeOfTall

    elif h >= 1.71 and h <= 1.8:
        Prob_TDShort = Prob_shortMale * Prob_ThirdRangeOfShort
        Prob_TDMedium = Prob_mediumMale * Prob_ThirdRangeOfMedium
        Prob_TDTall = prob_tallMale * Prob_ThirdRangeOfTall

    elif h >= 1.81 and h <= 1.9:
        Prob_TDShort = Prob_shortMale * Prob_FourthRangeOfShort
        Prob_TDMedium = Prob_mediumMale * Prob_FourthRangeOfMedium
        Prob_TDTall = prob_tallMale * Prob_FourthRangeOfTall

    elif h >= 1.91 and h <= 2.0:
        Prob_TDShort = Prob_shortMale * Prob_FifthRangeOfShort
        Prob_TDMedium = Prob_mediumMale * Prob_FifthRangeOfMedium
        Prob_TDTall = prob_tallMale * Prob_FifthRangeOfTall

    elif h >= 2.1 and h <= 10:
        Prob_TDShort = Prob_shortMale * Prob_SixthRangeOfShort
        Prob_TDMedium = Prob_mediumMale * Prob_SixthRangeOfMedium
        Prob_TDTall = prob_tallMale * Prob_SixthRangeOfTall

elif g == 'f':
    if h >= 0 and h <= 1.6:
        Prob_TDShort = Prob_shortFemale * Prob_FirstRangeOfShort
        Prob_TDMedium = Prob_mediumFemale * Prob_FirstRangeOfMedium
        Prob_TDTall = Prob_tallFemale * Prob_FirstRangeOfTall

    elif h >= 1.61 and h <= 1.7:
        Prob_TDShort = Prob_shortFemale * Prob_SecondRangeOfShort
        Prob_TDMedium = Prob_mediumFemale * Prob_SecondRangeOfMedium
        Prob_TDTall = Prob_tallFemale * Prob_SecondRangeOfTall

    elif h >= 1.71 and h <= 1.8:
        Prob_TDShort = Prob_shortFemale * Prob_ThirdRangeOfShort
        Prob_TDMedium = Prob_mediumFemale * Prob_ThirdRangeOfMedium
        Prob_TDTall = Prob_tallFemale * Prob_ThirdRangeOfTall

    elif h >= 1.81 and h <= 1.9:
        Prob_TDShort = Prob_shortFemale * Prob_FourthRangeOfShort
        Prob_TDMedium = Prob_mediumFemale * Prob_FourthRangeOfMedium
        Prob_TDTall = Prob_tallFemale * Prob_FourthRangeOfTall

    elif h >= 1.91 and h <= 2.0:
        Prob_TDShort = Prob_shortFemale * Prob_FifthRangeOfShort
        Prob_TDMedium = Prob_mediumFemale * Prob_FifthRangeOfMedium
        Prob_TDTall = Prob_tallFemale * Prob_FifthRangeOfTall

    elif h >= 2.1 and h <= 10:
        Prob_TDShort = Prob_shortFemale * Prob_SixthRangeOfShort
        Prob_TDMedium = Prob_mediumFemale * Prob_SixthRangeOfMedium
        Prob_TDTall = Prob_tallFemale * Prob_SixthRangeOfTall

#SECOND STEP**************************************************************
"""ProbOfShort = TotalNumOfShort/TotalNumOfData
ProbOFMedium = TotalNumOfMedium/TotalNumOfData
ProbOfTall = TotalNumOfTall/TotalNumOfData"""

Likelihood_Short = Prob_TDShort * ProbOfShort

Likelihood_Medium = Prob_TDMedium * ProbOFMedium

Likelihood_Tall = Prob_TDTall * ProbOfTall

prob_T = Likelihood_Short + Likelihood_Medium + Likelihood_Tall

#Third STEP***************************************************************

Actual_ShortDT = (Prob_TDShort * ProbOfShort)/prob_T

Actual_MediumDT = (Prob_TDMedium * ProbOFMedium)/prob_T

Actual_TallDT = (Prob_TDTall * ProbOfTall)/prob_T

print("Actual prob(short/t) = ",end="")
print(Actual_ShortDT)
print("Actual prob(medium/t) = ",end="")
print(Actual_MediumDT)
print("Actual prob(tall/t) = ",end="")
print(Actual_TallDT)

