# identity operator
a = 100
b = a  

print(f"a = {a} -> {id(a)}, b= {b} -> {id(b)}")
if(a is b) : 
    print("a is b")
else : 
    print("a is not b")


b += 1
print(f"\na = {a} -> {id(a)}, b= {b} -> {id(b)}")
if(a == b) : 
  print("The value of 'a' is equal to 'b'")
else : 
  print("The value of 'a' is not equal to 'b'")


m = 5
n = 5.0
print(f"\nm = {m} -> id = {id(m)}, n = {n} -> id = {id(n)}")
if(m == n) : 
  print("m == n")
else :
  print("m != n")