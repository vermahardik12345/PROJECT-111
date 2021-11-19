import statistics
import pandas as pd
import csv
import plotly.graph_objects as go
import plotly.figure_factory as ff
import random
df=pd.read_csv('data.csv')
listeddata=df['reading_time'].tolist()
mean=statistics.mean(listeddata)
print('Mean of population is:',mean)
def random_set_of_mean(counter):
    dataset=[]
    for i in range(0,counter):
        random_index=random.randint(0,len(listeddata)-1)
        value=listeddata[random_index]
        dataset.append(value)
        mean=statistics.mean(dataset)
        return mean
def show_fig(meanList):
  figData = meanList

  fig = ff.create_distplot([figData],["Reading Time"],show_hist = False)

  samplingMean = statistics.mean(meanList)
  sd = statistics.stdev(meanList)
  
  sd1_str,sd1_end = samplingMean - sd,samplingMean + sd
  sd2_str,sd2_end = samplingMean - (2*sd),samplingMean + (2*sd)
  sd3_str,sd3_end = samplingMean - (3*sd),samplingMean + (3*sd)
  
  print("\nStandard Deviation 1:",sd1_str,",",sd1_end)
  print("Standard Deviation 2:",sd2_str,",",sd2_end)
  print("Standard Deviation 3:",sd3_str,",",sd3_end)

  fig.add_trace(go.Scatter(x = [sd1_str,sd1_str],y = [0,0.8]))
  fig.add_trace(go.Scatter(x = [sd1_end,sd1_end],y = [0,0.8]))
  fig.add_trace(go.Scatter(x = [sd2_str,sd2_str],y = [0,0.8]))
  fig.add_trace(go.Scatter(x = [sd2_end,sd2_end],y = [0,0.8]))
  fig.add_trace(go.Scatter(x = [sd3_str,sd3_str],y = [0,0.8]))
  fig.add_trace(go.Scatter(x = [sd3_end,sd3_end],y = [0,0.8]))


  fig.add_trace(go.Scatter(x = [samplingMean,samplingMean],y = [0,0.8]))
  sampleMean = statistics.mean(listeddata)
  fig.add_trace(go.Scatter(x = [sampleMean,sampleMean],y = [0,0.8]))
  
  zTest = (sampleMean - samplingMean)/sd
  print("\nZ Test:",zTest)

  fig.show()
mean_list = []
for i in range(0,100):
    set_of_means= random_set_of_mean(30)
    mean_list.append(set_of_means)

show_fig(mean_list)
