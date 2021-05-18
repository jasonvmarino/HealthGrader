import csv


def csv_read(inputfile):
    info = {}
    ids = []
    ans = []
    floats = []
    with open(inputfile) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            stripped = [col.replace('\n', ' ') for col in row]  # sanitizes input data
            passed_data = []
            for items in stripped:  # used to remove empty space
                if items == '':
                    pass
                else:
                    passed_data.append(items)
            id_num = passed_data[1].strip("abcdefghijklmnopqrstuvwxyz.@")  # gets the ID number
            num_ans = len(passed_data[2:])
            ids.append(id_num)
            ans.append(num_ans)
        for values in ans[1:]:
            div = float(values/ans[0])
            #print('The div is ' + str(div))
            floats.append(div)
    info = dict(zip(ids[1:],floats[1:]))
    return inputfile, info

