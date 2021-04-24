import csv


def save_to_file(datas):
    file = open("datas.csv", mode="w", encoding="utf-8-sig")
    writer = csv.writer(file)
    writer.writerow(["company", "report_title", "date"])

    for num in range(0, len(datas)):
        data_list = datas[num]
        for i in range(0, len(data_list)):
            writer.writerow(data_list[i].values())
    print("finished")


