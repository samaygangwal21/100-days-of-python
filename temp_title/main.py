
import pandas

data = pandas.read_csv("weather_data.csv")
# print(data)
# data_dict = data.to_dict()
# print(data_dict)

temp_list = data["temp"].to_list()
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
data_dict = {"students": ["Amy", "James", "Angela"],
             "scores": [76, 85, 52]}
data2 = pandas.DataFrame(data_dict)
data2.to_csv("data2.csv")