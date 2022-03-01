def sign(p1: list,p2: list,p3: list) -> float:
    return (p1[0] - p3[0]) * (p2[1] - p3[1]) - (p2[0] - p3[0]) * (p1[1] - p3[1])

def to_decimal(deg: int,min: int,sec: int) -> float:
    return deg + (1/60)*min + (1/3600)*sec 

def PointInTriangle(pt: list,v1: list,v2: list,v3: list) -> bool:
    '''
    Function for checking if giving point pt
    is in triangle with vertices v1, v2, v3
    '''
    d1 = sign(pt, v1, v2)
    d2 = sign(pt, v2, v3)
    d3 = sign(pt, v3, v1)
    has_neg = (d1 < 0) or (d2 < 0) or (d3 < 0)
    has_pos = (d1 > 0) or (d2 > 0) or (d3 > 0)

    return not(has_neg and has_pos)


def readPoints(scv_file: str) -> dict:
    '''
    Function for converting csv data file from database into
    two separate list, one contains info about measured points
    (data_measured) and other info about all points in database 
    (data_all).
    '''
    import csv

    with open(scv_file) as file:
        csvreader = csv.reader(file)   
        header = []
        header = next(csvreader)
        rows = []
        for row in csvreader:
                rows.append(row)

    for j in range(len(rows)):
        rows[j][0]=float(rows[j][0])
        rows[j][2]=float(rows[j][2])
        rows[j][3]=int(rows[j][3])
        rows[j][4]=float(rows[j][4])
        rows[j][5]=float(rows[j][5])
        rows[j][8]=float(rows[j][8])
        rows[j][10]=float(rows[j][10])


    data_all = []
    for i in range(len(header)):
        data_all.append([])

    data_measured = []
    for i in range(len(header)):
        data_measured.append([])


    for i in range(len(rows)):
        for j in range(len(header)):
            data_all[j].append(rows[i][j])
            if rows[i][2]==-2:
                data_measured[j].append(rows[i][j])

    data = {
        'data_all': data_all,
        'data_measured': data_measured,
        'header': header
    }

    return data


def deFence(side: list) -> None:
    '''
    deleting frame around figure
    '''
    position = []
    position_all = ['right', 'top', 'bottom', 'left']
    for i in range(4):
        if side[i]==1:
            position.append(position_all[i])
    from matplotlib import pyplot as plt
    for pos in position:
        plt.gca().spines[pos].set_visible(False)


def humanTime(epoch: int) -> list:
    '''
    covert epoch time to hour [h]
    '''
    import time
    hour_from_zero = []
    ten_min = 1/6
    min = 1/60
    ten_sec = 1/360
    sec = 1/3600
    human = [time.strftime("%H%M%S", time.localtime(i)) for i in epoch]
    for hour in human:
        temp = int(hour[0])*10 + int(hour[1]) + int(hour[2])*ten_min + int(hour[3])*min + int(hour[4])*ten_sec + int(hour[5])*sec
        hour_from_zero.append(temp)
    return hour_from_zero