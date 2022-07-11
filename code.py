import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics as stat
import random as rand
import csv 

df = pd.read_csv("data.csv")
data = df["Math_score"].tolist()
# fig1 = ff.create_distplot([data], ["Math_score"], show_hist = False)
# fig1.show()
mean = stat.mean(data)
std = stat.stdev(data)

print("Mean of population = ", mean)
print("Standard deviation of population = ", std)

def random_set_of_mean(counter):
    dataset = []
    for i in range(0,counter) :
        random_index = rand.randint(0, len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = stat.mean(dataset)
    return mean

mean_list = []
for i in range(0,1000):
    set_of_means = random_set_of_mean(100)
    mean_list.append(set_of_means)

std_deviation = stat.stdev(mean_list)
mean = stat.mean(mean_list)

print("Mean of sampling distribution = ", mean)

# fig = ff.create_distplot([mean_list], ["Math_score"], show_hist = False)
# fig.add_trace(go.Scatter(x = [mean, mean], y = [0,0.20], mode = "lines", name = "Mean"))
# fig.show()

first_std_deviation_start, first_std_deviation_end = mean - std_deviation, mean + std_deviation
second_std_deviation_start, second_std_deviation_end = mean-(2*std_deviation), mean+(2*std_deviation)
third_std_deviation_start, third_std_deviation_end = mean-(3*std_deviation), mean+(3*std_deviation)
print("Standard Deviation 1 = ",first_std_deviation_start, first_std_deviation_end)
print("Standard Deviation 2 = ",second_std_deviation_start, second_std_deviation_end)
print("Standard Deviation 3 = ",third_std_deviation_start,third_std_deviation_end)

# fig = ff.create_distplot([mean_list], ["student marks"], show_hist = False)
# fig.add_trace(go.Scatter(x = [mean, mean], y=[0, 0.17], mode = "lines", name = "Mean"))
# fig.add_trace(go.Scatter(x = [first_std_deviation_start, first_std_deviation_start], y = [0, 0.17], mode = "lines", name = "Standard Deviation 1 start"))
# fig.add_trace(go.Scatter(x = [first_std_deviation_end, first_std_deviation_end], y = [0, 0.17], mode = "lines", name = "Standard Deviation 1 end"))
# fig.add_trace(go.Scatter(x = [second_std_deviation_start, second_std_deviation_start], y = [0,0.17], mode = "lines", name = "Standard Deviation 2 start"))
# fig.add_trace(go.Scatter(x = [second_std_deviation_end, second_std_deviation_end], y = [0,0.17], mode = "lines", name = "Standard Deviation 2 end"))
# fig.add_trace(go.Scatter(x = [third_std_deviation_start, third_std_deviation_start], y = [0,0.17], mode = "lines", name = "Standard Deviation 3 start"))
# fig.add_trace(go.Scatter(x = [third_std_deviation_end, third_std_deviation_end], y = [0,0.17], mode = "lines", name = "Standard Deviation 3 end"))
# fig.show()

# df1 = pd.read_csv("data1.csv")
# data = df1["Math_score"].tolist()
# mean_of_df1 = stat.mean(data)
# print("Mean of sample 1 = ", mean_of_df1)
# graph = ff.create_distplot([mean_list], ["students marks"], show_hist = False)
# graph.add_trace(go.Scatter(x = [mean, mean], y = [0, 0.17], mode = "lines", name = "Mean"))
# graph.add_trace(go.Scatter(x = [mean_of_df1, mean_of_df1], y = [0, 0.17], mode = "lines", name = "Mean of intervention 1"))
# graph.add_trace(go.Scatter(x = [first_std_deviation_end, first_std_deviation_end], y = [0, 0.17], mode = "lines", name = "Standard Deviation 1 end"))
# graph.show()

# z_score = (mean - mean_of_df1)/std_deviation
# print("The z score is = ",z_score)
# # -0.49886841449172525

df2 = pd.read_csv("data2.csv")
data2 = df2["Math_score"].tolist()
mean_of_df2 = stat.mean(data2)
print("Mean of sample 2 = ", mean_of_df2)
graph2 = ff.create_distplot([mean_list], ["students marks"], show_hist = False)
graph2.add_trace(go.Scatter(x = [mean, mean], y = [0, 0.17], mode = "lines", name = "Mean"))
graph2.add_trace(go.Scatter(x = [mean_of_df2, mean_of_df2], y = [0, 0.17], mode = "lines", name = "Mean of intervention 2"))
graph2.add_trace(go.Scatter(x = [first_std_deviation_end, first_std_deviation_end], y = [0, 0.17], mode = "lines", name = "Standard Deviation 1 end"))
graph2.add_trace(go.Scatter(x = [second_std_deviation_end, second_std_deviation_end], y = [0,0.17], mode = "lines", name = "Standard Deviation 2 end"))
graph2.show()
z_score = (mean - mean_of_df2)/std_deviation
print("The z score is = ",z_score)





# df3 = pd.read_csv("data2.csv")
# data3 = df3["Math_score"].tolist()
# mean_of_df3 = stat.mean(data3)
# print("Mean of sample 3 = ", mean_of_df3)
# graph3 = ff.create_distplot([mean_list], ["students marks"], show_hist = False)
# graph3.add_trace(go.Scatter(x = [mean, mean], y = [0, 0.17], mode = "lines", name = "Mean"))
# graph3.add_trace(go.Scatter(x = [mean_of_df3, mean_of_df3], y = [0, 0.17], mode = "lines", name = "Mean of intervention 3"))
# graph3.add_trace(go.Scatter(x = [first_std_deviation_end, first_std_deviation_end], y = [0, 0.17], mode = "lines", name = "Standard Deviation 1 end"))
# graph3.add_trace(go.Scatter(x = [second_std_deviation_end, second_std_deviation_end], y = [0,0.17], mode = "lines", name = "Standard Deviation 2 end"))
# graph3.add_trace(go.Scatter(x = [third_std_deviation_end, third_std_deviation_end], y = [0,0.17], mode = "lines", name = "Standard Deviation 3 end"))
# graph3.show()
# z_score = (mean - mean_of_df3)/std_deviation
# print("The z score is = ",z_score)
# # -1.4985782656862667