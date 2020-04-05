from keras.models import load_model
import numpy as np
from numpy import loadtxt
import csv


model = load_model('hist.h5')


dataset = loadtxt('predict.csv', delimiter=',')
predictions = model.predict_classes(dataset, batch_size=10,verbose=0)

print("predictions",predictions)

model1 = load_model('hist1.h5')
#print(model.predict_classes(m))
#x = dataset[1500:,1:15]
predictions1 = model1.predict_classes(dataset, batch_size=10,verbose=0)


print("predictions1",predictions1)

prd = [[]]
for i in range(3):
    prd.append([predictions[i],predictions1[i]])
#        print(prd[i])

csvFile = open("Results.csv","w+",newline='')

#print(predictions)
try:
    writer = csv.writer(csvFile)
    writer.writerow(('Network_coverage_Trafic_Failure','Data_Consumption_Failure'))
    for i in prd:
        #print(i)
        writer.writerow(i,)

finally:
    csvFile.close()

print(prd)
