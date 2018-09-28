def standaardprijs(afstandKM):

    if afstandKM <= int(0):
        afstandKM = 0
        return afstandKM
    if afstandKM <= int(50) and afstandKM > int(0):
        afstandKM = afstandKM * float(0.80)
        return afstandKM
    elif afstandKM >= int(51):
        afstandKM = ( afstandKM * float(0.60) ) + int(15)
        return afstandKM


def ritprijs(leeftijd, weekendrit, afstandKM):

    reiskosten = standaardprijs(afstandKM)

    if weekendrit:
        if 11 <= leeftijd <= 64:
            output = reiskosten / 100 * 60
            print(output)
        else:
            output = round(reiskosten, 2)
            print(output)
    else:
        if weekendrit:
            if 12 >= leeftijd >= 65:
                output = reiskosten / 100 * 70
                print(output)
        else:
            output = reiskosten / 100 * 65
            print(output)



ritprijs(11, True, 57)
ritprijs(11, False, 57)
ritprijs(11, True, 43)
ritprijs(11, False, 43)
ritprijs(11, False, -5)
ritprijs(11, True, -5)

ritprijs(12, True, 57)
ritprijs(12, False, 57)
ritprijs(12, True, 43)
ritprijs(12, False, 43)
ritprijs(12, False, -5)
ritprijs(12, True, -5)

ritprijs(64, True, 57)
ritprijs(64, False, 57)
ritprijs(64, True, 43)
ritprijs(64, False, 43)
ritprijs(64, True, -5)
ritprijs(64, False, -5)

ritprijs(65, True, 57)
ritprijs(65, False, 57)
ritprijs(65, True, 43)
ritprijs(65, False, 43)
ritprijs(65, True, -5)
ritprijs(65, False, -5)
