from sklearn import svm

test_data = [
    [14,40,'불합격'],
    [20,80,'합격'],
    [12,40,'불합격']
]
test_label = []
for row in test_data:
    test_label.append(row[2])



Sdata = [
    [20,100,'합격'],
    [20,80,'합격'],
    [15,10,'불합격'],
    [18,80,'합격'],
    [18,0,'불합격'],
    [20,90,'합격'],
    [17,50,'불합격'],
    [20,100,'합격'],
    [19,90,'합격'],
    [14,40,'불합격'],
    [12,40,'불합격'],

]

data = []
label = []

for i in Sdata:
    d = i[0]
    t = i[1]
    r = i[2]
    data.append([d,t])
    label.append(r)

# print(data)

clf = svm.SVC()
clf.fit(data,label)

pre = clf.predict(data)
# print("예측결과",pre)


ok = 0
total = len(test_label)
for i in range(len(test_label)):
    answer = test_label[i]
    p = pre[i]
    if p == answer:
        ok += 1

print(ok/total)

