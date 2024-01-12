
QNO:1
 i in range(1,10):
    print(i)
    
QNO:2

n=(input("enter a number:"))
#we arne using "for loop"to iterate the multiplication 10 times
print("the multiplication table of:",n)
for i in range(1,11):
    print(n,"x",i,"=",n*i)
    

QNO:3

# Taking input from the user
number = int(input("Enter a positive integer: "))

# Initializing variables
sum = 0
i = 1

# Calculating the sum of natural numbers using a while loop
while i <= number:
    sum += i
    i += 1

# Displaying the sum
print(f"The sum of natural numbers up to {number} is: {sum}")





QNO:4

#list names 
lst=["rose","red","yellow","blue","black"]

#iterate through the list names in for loop
for lst in lst:
    print(lst)

QNO:5

def generate_fibonacci(n):
    fib_sequence = []
    a, b = 0, 1

    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b

    return fib_sequence

def main():
    try:
        num_terms = int(input("Enter the number of terms for the Fibonacci series: "))
        if num_terms <= 0:
            print("Please enter a positive integer.")
        else:
            fibonacci_series = generate_fibonacci(num_terms)
            print("Fibonacci Series up to", num_terms, "terms:", fibonacci_series)
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
    
   QNO6
   
   =int(input("enter a number: "))
i=2
while i>=n-1:
    print(i,end=" ")
i+=1n


QNO:7


n=(input("enter a string: "))
 #vowels=["a","e","i","o","u"]
a="vowels"
for a in range(1,5):
    if a in n:
        print(vowels)
        
QNO:8

n=int(input("enter a number: "))
i=1
for i in range(1,5):
    print( i**n,end=" ")