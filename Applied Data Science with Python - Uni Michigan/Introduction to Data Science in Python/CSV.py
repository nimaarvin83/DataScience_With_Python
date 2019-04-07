import csv
# % precision 2
with open('mpg.csv') as csvfile:
    mpg=list(csv.DictReader(csvfile))
print(mpg[:3])
print(len(mpg))
print(mpg[0].keys())
print(sum(float(d['cty']) for d in mpg)/len(mpg))
print(sum(float(d['hwy']) for d in mpg)/len(mpg))