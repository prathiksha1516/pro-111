def random_set_of_mean(counter):
dataset = []
for i in range(0, counter):
random_index= random.randint(0, len(data))
value = data[random_index]
dataset.append(value)
mean = statistics.mean(dataset)
return mean

def setup():
mean_list = []
for i in range(0,100):
set_of_means= random_set_of_mean (30)
mean_list.append(set_of_means)
show_fig(mean_list)

def show_fig(mean_list):
df = mean list
fig ff.create_distplot([df], ["temp"], show_hist=False)
fig.show()

** findig the standard deviation starting and ending values
first_std deviation start, first_std deviation end = mean-std deviation, mean+std deviation
second std deviation start, second std deviation end - mean-(2 std deviation), mean+(2*std deviation)
third std deviation start, third std deviation end - mean-(3std deviation), mean+(3 std deviation)
print("stdi", first_std_deviation_start, first_std_deviation_end)
print("std2", second_std_deviation_start, second_std_deviation_end)
print("std3", third_std_deviation_start, third_std_deviation_end)
## plotting the graph with traces
fig - ff.create_distplot(nean_list], ["student marks"), show_hist=False)
fig. add trace(go.Scatter(x-[mean, mean), y=[0, 0.17), mode="lines", name="MEAN"))
fig.add_trace(go. Scatter(x=[first_std_deviation_start, first_std_deviation_start], y=[0, 0.17), mode="line:
fig.add_trace(go.Scatter(x-[first_std_deviation_end, first_std_deviation_end], y=[e, 8.17), modelines",
fig.add_trace(go.Scatter(x=[second_std_deviation_start, second_std_deviation_start], y=[0, 0.17], mode="lir
fig.add_trace(go.Scatter(x=[second std deviation_end, second_std_deviation_end], y=[0, 0.17], mode="lines"
fig.add_trace(go.Scatter(x-[third_std_deviation_start, third_std_deviation_start], y=[0,0.17), modelines",
fig.add_trace(go.Scatter(x=[third_std_deviation_end, third_std_deviation_end], y=[0,0.17), mode="lines", nan
fig.show()
