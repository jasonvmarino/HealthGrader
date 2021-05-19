import csv

class csv_file:

    def __init__(self,inputfile):
        self.input = inputfile
        self.info = {}

    def read(self):
        ids = []
        ans = []
        floats = []
        with open(self.input, newline='',encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile,dialect='excel')
            for row in reader:
                passed_data = []
                for items in row:  # used to remove empty space
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
        self.info = dict(zip(ids[1:],floats[1:]))

    def print(self):
        print(self.info)

    def test(self):
        print(self.input)

