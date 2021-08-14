testinput = input("Testkommentar eingeben:  ").lower()
print(testinput)

AfDKw = ["afd", ]
FDPKw = ["fdp", ]
CDUKw = ["cdu", ]
SPDKw = ["spd", ]
B90Kw = ["grüne", ]
LinKw = ["linke", ]

triggerwords = AfDKw + FDPKw + CDUKw + SPDKw + B90Kw + LinKw
print(triggerwords)
posKw = ["gut", "toll", "wunderbar", ]
negKw = ["schlecht", "blöd", "nervig", ]
unklarKw = ["nicht", "keinesfalls"]

for trigger in triggerwords:
    if trigger in testinput:
        print("Es klappt!")

def konnotationcheck(testinput):
    poscount = 0
    negcount = 0
    unklar = 0
    for pos in posKw:
        if pos in testinput:
            poscount += 1
    for neg in negKw:
        if neg in testinput:
            negcount -= 1
    pncount = poscount + negcount
    for unk in unklarKw:
        if unk in testinput:
            pncount  = pncount*(-1)
            unklar = 1
    if pncount > 0:
        # posDummy, negDummy, unklar 
        return 1, 0, unklar
    if pncount < 0:
        # posDummy, negDummy, unklar 
        return 0, 1, unklar
    else: 
        return 0, 0, 0
    
print(konnotationcheck(testinput))
