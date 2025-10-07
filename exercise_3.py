a = input('What is your name?')
b = float(input('What is your GPA score?'))
c = int(input('What is your total credit hours?'))
d_l = b >= 3.5 and c >= 12
gpa_needed = max(0, 3.5-b)
hour_needed = max(0, 12-c)

print("\n      Student information    ")
print(f"Name : {a}\n Dean's  List Eligible : {d_l}\n Additional GPA points need: {gpa_needed}\n Additional credit hours need: {hour_needed}")
