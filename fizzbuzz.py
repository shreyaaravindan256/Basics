answer = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
for i in range(1, n+1):
    if(i%3 == 0 and i%5 == 0): 
        answer.append("FizzBuzz")
    elif(i%3 == 0):
        answer.append("Fizz")
    elif(i%5 == 0):
        answer.append("Buzz")
    else:
        answer.append(str(i))

print(answer)
