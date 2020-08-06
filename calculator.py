import re
print("Our Calucalator")
print("Type 'quit' to EXIT")
previous = 0
run = True

def performath():
    global run
    global previous
    equation = input("Enter The Equations")
    if equation == 'quit':
        run = False
    else:
       equation = re.sub('[a-zA-z,.:()" "]', '', equation)
       if previous == 0:
         previous = eval(equation)
       else:
           previous = eval(str(previous) + equation)
       print(previous)
while run:
    performath()