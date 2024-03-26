import csv


def create():
    with open('pc.csv', 'w', encoding='UTF8', newline='\n') as f:
        writer = csv.writer(f)
        writer.writerow(['pc_name', 'ip'])
        for x in range(1, 101):
            writer.writerow(["P" + str(x), "172.30.2." + str(x)])


create()
