#Challenge 1
def map_score(grades):
    l = list(map(lambda record: [record[0], 20*record[1]/10.0 + 80*record[2]/100.0], grades))
    for i in range(len(l)):
        if l[i][1] < 40:
            l[i][1] = 'D'
        elif 40 <= l[i][1] < 60:
            l[i][1] = 'C'
        elif 60 <= l[i][1] < 80:
            l[i][1] = 'B'
        elif 80 <= l[i][1] <= 100:
            l[i][1] = 'A'
        else:
            l[i][1] = "NA"
    return l
