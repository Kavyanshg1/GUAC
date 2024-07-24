interpreter = ZLangInterpreter()

# spill
zlang_code = "spill('Hello, World!')"
python_code = interpreter.parse_zlang(zlang_code)
print(python_code)  # Output: print('Hello, World!')
exec(python_code)  # Output: Hello, World!

# ask
zlang_code = "name = ask('What is your name? ')"
python_code = interpreter.parse_zlang(zlang_code)
print(python_code)  # Output: name = input('What is your name? ')
exec(python_code)  # Prompt: What is your name? 

# size
zlang_code = "my_list = [1, 2, 3, 4, 5]; print(size(my_list))"
python_code = interpreter.parse_zlang(zlang_code)
print(python_code)  # Output: my_list = [1, 2, 3, 4, 5]; print(len(my_list))
exec(python_code)  # Output: 5

# kind
zlang_code = "my_var = 10; print(kind(my_var))"
python_code = interpreter.parse_zlang(zlang_code)
print(python_code)  # Output: my_var = 10; print(type(my_var))
exec(python_code)  # Output: <class 'int'>

# num
zlang_code = "my_num = num(10.5)"
python_code = interpreter.parse_zlang(zlang_code)
print(python_code)  # Output: my_num = int(10.5)
exec(python_code)  # Output: 10

# drip
zlang_code = "my_drip = drip(10.5)"
python_code = interpreter.parse_zlang(zlang_code)
print(python_code)  # Output: my_drip = float(10.5)
exec(python_code)  # Output: 10.5

# chatter
zlang_code = "my_chatter = chatter('Hello, World!')"
python_code = interpreter.parse_zlang(zlang_code)
print(python_code)  # Output: my_chatter = str('Hello, World!')
exec(python_code)  # Output: Hello, World!

# squad
zlang_code = "my_squad = squad([1, 2, 3, 4, 5])"
python_code = interpreter.parse_zlang(zlang_code)
print(python_code)  # Output: my_squad = list([1, 2, 3, 4, 5])
exec(python_code)  # Output: [1, 2, 3, 4, 5]

# stash
zlang_code = "my_stash = stash({'a': 1, 'b': 2, 'c': 3})"
python_code = interpreter.parse_zlang(zlang_code)
print(python_code)  # Output: my_stash = dict({'a': 1, 'b': 2, 'c': 3})
exec(python_code)  # Output: {'a': 1, 'b': 2, 'c': 3}

# clique
zlang_code = "my_clique = clique([1, 2, 3, 4, 5])"
python_code = interpreter.parse_zlang(zlang_code)
print(python_code)  # Output: my_clique = set([1, 2, 3, 4, 5])
exec(python_code)  # Output: {1, 2, 3, 4, 5}

# pair
zlang_code = "my_pair = pair((1, 2))"
python_code = interpreter.parse_zlang(zlang_code)
print(python_code)  # Output: my_pair = tuple((1, 2))
exec(python_code)  # Output: (1, 2)

# span
zlang_code = "my_span = span(5)"
python_code = interpreter.parse