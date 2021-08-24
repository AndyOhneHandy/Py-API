AfDKw = ["afd", "höcke", "weidel", "meuthen", "von Storch", "chrupalla"]
FDPKw = ["fdp", "die liberalen", "freie demokraten", "freien demokraten", "lindner", "kubicki"]
CDUKw = ["cdu", "csu", "Die Union", "christdemokraten", "laschet", "merkel", "söder", "merz", "röttgen", "leyen", "karrenbauer", "akk", "seehofer", "scheuer"]
SPDKw = ["spd", "sozialdemokrat", "scholz", "esken", "borjans", "maas", "klingbeil", "kühnert"]
B90Kw = ["die grünen", "bündnis 90", "baerbock", "bärbock", "habeck", "kretschmann"]
LinKw = ["die linke", "linkspartei", "wissler", "wellsow"]

triggerwords = AfDKw + FDPKw + CDUKw + SPDKw + B90Kw + LinKw
# print(triggerwords)
posKw = ["gut", "toll", "wunderbar", ]
negKw = ["schlecht", "blöd", "nervig", ]
unklarKw = ["nicht ", "keinesfalls"]

def konnotationcheck(testinput):
    poscount = 0
    negcount = 0
    wordcount = 0
    unklar = 0
    for pos in posKw:
        if pos in testinput:
            poscount += 1
            wordcount += 1
    for neg in negKw:
        if neg in testinput:
            negcount -= 1
            wordcount += 1

    pncount = poscount + negcount

    for unk in unklarKw:
        if unk in testinput:
            pncount  = pncount*(-1)
            unklar = 1
    
    if wordcount == 0:
        konnotationvalue = 0
    else:
        konnotationvalue = round(pncount/wordcount, 2)

    return [konnotationvalue, unklar]

def partycheck(testinput):
    afdDummy = 0
    aAbs = 0
    fdpDummy = 0
    fAbs = 0
    cduDummy = 0
    cAbs = 0
    spdDummy = 0
    sAbs = 0
    b90Dummy = 0
    gAbs = 0
    linDummy = 0
    lAbs = 0
    multipdummy = 0
    triggerwordlist = ""
    triggerwordcount = 0
    
    for afdk in AfDKw:
        if afdk in testinput:    
            afdDummy = 1
            aAbs += 1
            triggerwordlist += afdk + ";"


    for fdpk in FDPKw:
        if fdpk in testinput:    
            fdpDummy = 1
            fAbs += 1
            triggerwordlist += fdpk + ";"


    for cduk in CDUKw:
        if cduk in testinput:    
            cduDummy = 1
            cAbs += 1
            triggerwordlist += cduk + ";"


    for spdk in SPDKw:
        if spdk in testinput:    
            spdDummy = 1
            sAbs += 1
            triggerwordlist += spdk + ";"


    for b90k in B90Kw:
        if b90k in testinput:    
            b90Dummy = 1
            gAbs += 1
            triggerwordlist += b90k + ";"


    for link in LinKw:
        if link in testinput:    
            linDummy = 1
            lAbs += 1
            triggerwordlist += link + ";"


    triggerwordcount = aAbs + fAbs + cAbs + sAbs + gAbs + lAbs

    if afdDummy + fdpDummy + cduDummy + spdDummy + b90Dummy + linDummy > 1:
        multipdummy = 1

    return [afdDummy, fdpDummy, cduDummy, spdDummy, b90Dummy, linDummy, multipdummy, triggerwordlist, aAbs, fAbs, cAbs, sAbs, gAbs, lAbs, triggerwordcount]

# def countoutput(com):
#     return com

def mainF(testinput):   
    return partycheck(testinput) + konnotationcheck(testinput)