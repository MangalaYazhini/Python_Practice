'''
  Python Datatypes

  Text Type       :	str
  Numeric Types   :	int, float, complex
  Sequence Types  :	list, tuple, range
  Mapping Type    :	dict
  Set Types       :	set, frozenset
  Boolean Type    :	bool
  Binary Types    :	bytes, bytearray, memoryview
  None Type       :	NoneType

'''
# string
# Used to store text / characters.
# Strings are immutable
my_str = "Hello World"	
print(f"\nmy_str = {my_str}  -> type : {type(my_str)}")

# int	 
# Whole numbers (positive, negative, zero).
my_int = 20	
print(f"\nmy_int = {my_int}  -> type : {type(my_int)}")

# float	
# Numbers with decimals.
my_float = 20.5	
print(f"\nmy_float = {my_float}  -> type : {type(my_float)}")

# complex	
# Numbers with real and imaginary parts.
my_complex = 5+1j	
print(f"\nmy_complex = {my_complex}  -> type : {type(my_complex)}")

# list	
# A list is sequence datatype that is Ordered, mutable, allows duplicates.
my_list = ["apple", "banana", "cherry"]
print(f"\nmy_list = {my_list}  -> type : {type(my_list)}")

# tuple	
# A tuple is Ordered, immutable, allows duplicates.
my_tuple = ("Python", "C", "Java")	
print(f"\nmy_tuple = {my_tuple}  -> type : {type(my_tuple)}")

# range	
# This generates a sequence of numbers.
my_range = range(10)	
print(f"\nmy_range = {my_range}  -> type : {type(my_range)}")

#	dict	
# Stores data as key–value pairs.
my_dict = {"name" : "Elanchezhian", "age" : 50} 
print(f"\nmy_dict = {my_dict}  -> type : {type(my_dict)}")

# set	
# sets are Unordered, mutable, no duplicates.
my_set = {"pen", "pencil", "ink bottle"}	
print(f"\nmy_set = {my_set}  -> type : {type(my_set)}")

# frozenset	
# Immutable version of set.
my_frozenset = frozenset({"TV", "fridge", "washing machine"})	
print(f"\nmy_frozenset = {my_frozenset}  -> type : {type(my_frozenset)}")

# bool	
# Stores True or False.
# Internally 
  # True  -> 1
  # False -> 0

my_bool = True
print(f"\nmy_bool = {my_bool}  -> type : {type(my_bool)}")	

# bytes	
# Immutable sequence of bytes.
my_bytes = b"hello"	
print(f"\nmy_bytes = {my_bytes}  -> type : {type(my_bytes)}")
print("binary :",end ="")
for byte in my_bytes : 
  print(f" {byte} ",end = "")
print()

# bytearray	
# Mutable version of bytes.
my_bytearray = bytearray(b"hello")	
my_bytearray[0] = 72 
print(f"\nmy_bytearray = {my_bytearray}  -> type : {type(my_bytearray)}")

# memoryview	
# This creates a memoryview object that views (points to) the memory of that bytes object without copying it.
data = b"hello world"
chunk = data[0:5]   # copy created

my_memoryview = memoryview(data)
my_chunk = my_memoryview[0:5]
print(f"\nmy_memoryview = {my_memoryview}  -> type : {type(my_memoryview)}")
print(f"\ndata = {data}  -> type : {type(data)}")
print(f"\nmy_chunk = {my_chunk}  -> type : {type(my_chunk)}")
print(f"\nchunk = {chunk}  -> type : {type(chunk)}")


# None
# None represents no value.	
# Variable exists but has no value yet
my_none = None
print(f"\nmy_none = {my_none}  -> type : {type(my_none)}")