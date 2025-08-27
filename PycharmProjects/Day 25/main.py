# import csv
#
# with open("./weather_data 1.csv") as file:
#     data = csv.reader(file)
#     temperatures = []
#     for row in data:
#         if row[1]!= "temp":
#
#             temperatures.append(int(row[1]))
#     print(temperatures)
#

import pandas
# data = pandas.read_csv("weather_data 1.csv")
# data_dictionary = data.to_dict()
#
# temp_list = data["temp"].to_list
# mean_temp = data["temp"].mean()
# print(data["temp"].max()
#
# monday = data[data.day=="Monday"]
# monday_temp = monday.temp[0]
#
# pandas.DataFrame(data_dictionary).to_csv("newdata.csv")


## todo 1 Make a data dictionary with panda.readcsv
## todo 2 get a hold of the colours gray red and black squirrel data
## todo 3 make count of the data and make a new file

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
cinnamon_squirrel_count = len(data[data["Primary Fur Color"]=="Cinnamon"])
gray_squirrel_count = len(data[data["Primary Fur Color"]=="Gray"])
black_squirrel_count = len(data[data["Primary Fur Color"]=="Black"])

data_dict = {"Fur Color" :["Cinnamon", "Gray", "Black"],
"Count":[cinnamon_squirrel_count,gray_squirrel_count,black_squirrel_count]}
df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
