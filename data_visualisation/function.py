def read_points(scv_file: str) -> dict:

    import csv

    file = open(scv_file)
    csvreader = csv.reader(file)
    header = []
    header = next(csvreader)
    rows = []
    for row in csvreader:
            rows.append(row)
    file.close()

    for j in range(len(rows)):
        rows[j][0]=float(rows[j][0])
        rows[j][2]=float(rows[j][2])

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
        'data_measured': data_measured
    }

    return data