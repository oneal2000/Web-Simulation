resultID = 8.01
results = []
op = []
for i in range(0,40):
    results.append(resultID)
    op.append(    int((resultID+0.24-8)/0.72)     )  
    print(results[i],op[i])
    resultID += 0.24
