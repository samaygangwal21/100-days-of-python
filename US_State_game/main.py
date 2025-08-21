# import pandas
# data = pandas.read_csv("weather_data.csv")
# print(data)
# data_dict = data.to_dict()
# print(data_dict)
# temp_list = data["temp"].to_list()
# print(len(temp_list))
# print(round(sum(temp_list)/len(temp_list),2))
# print(data["temp"].mean())
# print(data["temp"].max())
#
# print(data.temp)

#Get Data in row
# monday = (data[data.day == "Monday"])
# print(data[data.temp == data["temp"].max()])
# print((monday.temp * 9/5) + 32)

#Create a dataframe from scratch
# data_dict = {"students": ["Amy", "James", "Angela"],
#              "scores": [76, 85, 52]}
# data2 = pandas.DataFrame(data_dict)
# data2.to_csv("data2.csv")

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrels = data[data["Primary Fur Color"] == "Gray"]
red_squirrels = data[data["Primary Fur Color"] == "Cinnamon"]
black_squirrels = data[data["Primary Fur Color"] == "Black"]
print(len(grey_squirrels))
print(len(red_squirrels))
print(len(black_squirrels))

data_dict = {"Fur Color": ["Gray", "Cinnamon", "Black"],"Count": [len(grey_squirrels),len(red_squirrels),len(black_squirrels)]}
df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")