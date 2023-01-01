inch=[74,74,72,72,73,69,69,71,76,71]
y=[]
for x in inch:
    t=[x*0.0254]
    y=y+t
print(y)
print(y[0:3],y[7:10])
print(sum(y)/len(y))
print("max",max(y),"min",min(y))
print(sorted(y))
print(sorted(y,reverse=True))