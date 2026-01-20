print("IMMUTABLE DATA TYPES IN PYTHON\n")

# int 
print("int datatype")
a = 10
print("a = ", a, "id:", id(a))

a += 5   # rebinding
print("a =", a, "id:", id(a))
print("-" * 80)


# float
print("float datatype")
x = 2.5
print("x =", x, "id:", id(x))

x = x + 1.5   # rebinding
print("x =", x, "id:", id(x))
print("-" * 80)


# complex
print("complex datatype")
z = 3 + 4j
print("z =", z, "id:", id(z))

z += 1   # rebinding
print("z =", z, "id:", id(z))
print("-" * 80)


# bool
print("bool datatype")
flag = True
print("flag =", flag, "id:", id(flag))

flag = False   # rebinding
print("flag =", flag, "id:", id(flag))
print("-" * 80)


# str 
print("str datatype")
s = "python"
print("s =", s, "id:", id(s))

# s[0] = "P"  
# ERROR: strings are immutable

s = "P" + s[1:]   # rebinding
print("s =", s, "id:", id(s))
print("-" * 80)


# tuple
print("tuple datatype")
t = (1, 2, 3)
print("t =", t, "id:", id(t))

# t[0] = 10  
# ERROR: tuple is immutable

# Tuple containing mutable object
print("my_tuple contains a mutable object which is mutable")
my_tuple = (1, [2, 3])
print("my_tuple before:", my_tuple, "id:", id(my_tuple))

my_tuple[1].append(4)   # list inside tuple is mutable
print("my_tuple after :", my_tuple, "id:", id(my_tuple))
print("-" * 80)


# frozenset
print("frozenset datatype")
fs = frozenset({1, 2, 3})
print("fs =", fs, "id:", id(fs))

# fs.add(4)  
# ERROR: frozenset is immutable
print("-" * 80)


# bytes
print("bytes datatype")
b = b"hello"
print("b =", b, "id:", id(b))

# b[0] = 72 
# ERROR: bytes are immutable

# Mutable alternative
print("\nbytearray are mutable")
my_bytearray = bytearray(b)
print("bytearray =", my_bytearray ,"id = ", id(my_bytearray))
my_bytearray[0] = 72   # modifies same object
print("bytearray =", my_bytearray ,"id = ", id(my_bytearray))
print("-" * 80)


# NoneType
print("NoneType datatype")
n = None
print("n =", n, "id:", id(n))

m = None
print("m =", m, "id:", id(m))  # same id → only one None object
print("-" * 80)


# What happens when you 'change' immutable data?
print("Rebinding a string")
x = "hi"
print("x =", x, "id:", id(x))

x += "!"   # x = x.__add__("!")
print("x =", x, "id:", id(x))
print("-" * 80)
