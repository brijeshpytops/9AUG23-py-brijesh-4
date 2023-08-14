# PEP 8 – Style Guide for Python Code
# https://peps.python.org/pep-0008/

"""
Tokens: 
    1] identifiers
    identifers : variable, function, class, array
    - Identifier names are unique. x = 10, def add:, class car:
    - Cannot use a keyword as identifiers. for = 1-False
    - Identifier has to begin with a letter or underscore (_)., 1level-False, level_1, level1
    - It should not contain white space. ex: first name-False, first_name, FristName
    - Special characters are not allowed. ex :$,~,!,@.#, $INR, INR$-False
    - Identifiers can consist of only letters, digits, or underscore.
    - Only 31 characters are significant.
    - They are case sensitive. ex : Name, NAME, name

    2] variables
    Variables are used to store information to be referenced and manipulated in a computer program.
    syntax of variable 

    var_name = value_of_variable
    name = "python"
    x = 10, y = 20
    price = 30.5

    get single input from the user
    name = input("Enter your name: ")

    get multiple input from the user
    name, age = input("Enter your name and age sep by comma: ").split(",")
    print(name, age)

    3] keywords
    Python Keywords are some predefined and reserved words in python that have special meanings. 
    S-1] goto idle
    S-2] type help() and press enter
    S-3] type "keywords" and hit on enter
    Here is a list of the Python keywords.  Enter any keyword to get more help.

    False               class               from                or
    None                continue            global              pass
    True                def                 if                  raise
    and                 del                 import              return
    as                  elif                in                  try
    assert              else                is                  while
    async               except              lambda              with
    await               finally             nonlocal            yield
    break               for                 not                 
    
    4] datatypes
    t-1] int
    - An integer is a numerical value in a number system that is not fractional.
    ex : x = 10, y = -45 

    x = 10
    y = -45 
    print(type(x), type(y)) # <class 'int'> <class 'int'>

    t-2] float
    - A floating point number, is a positive or negative whole number with a decimal point.
    ex : x = 2.5, y = -3.66767767
    print(type(x), type(y))
    <class 'float'> <class 'float'>

    t-3] string
    - A string value is just a sequence of characters, like "abc" . A string value is always enclosed in quotes. 
    ex: "python code", 'python code', \"\"\"python code\"\"\", '''python code'''
    
    print(type(x), type(y), type(z), type(a))
    <class 'str'> <class 'str'> <class 'str'> <class 'str'>

    t-4] complex
    - The complex data type in python consists of two values, the first one is the real part of the complex number, and the second one is the imaginary part of the complex number.
    ex : 3 + 7j , 3i + 7j

    x = 3 + 7j
    print(type(x)) # <class 'complex'>

"""
x = 10
y = 20.6
z = "bdgvcfhgdv"
a = 20 + 27j
print(type(a))