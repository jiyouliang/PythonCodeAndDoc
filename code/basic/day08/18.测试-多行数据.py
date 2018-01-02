f = open("temp2.txt", "a+", encoding="utf-8")
for i in range(100, 150):
    if i < 10:
        f.write("day0%d\n" % i)
    else:
        f.write("day%d\n" % i)
f.close()
