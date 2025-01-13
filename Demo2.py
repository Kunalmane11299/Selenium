values = [1, 2, 5, "Kunal", 4, 5]
print(values[0])
print(values[-1])
print(values[1:4]) # 2 5 Kunal

values.insert(4, "Mane")
print(values)

values.append("End")
print(values)

values[3] = "KUNAL"
del values[0]
print(values)