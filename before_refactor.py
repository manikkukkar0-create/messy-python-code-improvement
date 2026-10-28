# Unrefactored / Messy Python Code
# Common student script: poor variable names, monolithic structure, lack of functions, no error handling

d = [
    {"n": "Alice", "s": [85, 90, 78], "a": 20},
    {"n": "Bob", "s": [50, 60, 55], "a": 21},
    {"n": "Charlie", "s": [95, 100, 92], "a": 19},
    {"n": "David", "s": [40, 35, 45], "a": 22}
]

# Calculate averages and grades
res = []
for x in d:
    t = 0
    for y in x["s"]:
        t = t + y
    avg = t / len(x["s"])
    if avg >= 90:
        g = "A"
    elif avg >= 75:
        g = "B"
    elif avg >= 50:
        g = "C"
    else:
        g = "F"
    res.append({"name": x["n"], "average": avg, "grade": g})

print("RESULTS:")
for r in res:
    print(r["name"] + " -> Avg: " + str(r["average"]) + " (" + r["grade"] + ")")

# Find top student
top = res[0]
for r in res:
    if r["average"] > top["average"]:
        top = r

print("Top student: " + top["name"])
