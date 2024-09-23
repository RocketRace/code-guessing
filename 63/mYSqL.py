def implement_ysl(program: str, line_number = 2):
    print(line_number)
    # "The lines of the program are stored in a sorted map, where the key is integers
    # and the values are strings which contain a line of code."
    integers = lambda s: all(list(filter(str.isdigit, s)))
    sorted_map = sorted(map(str, program.split('\n')), key=integers)
    # "The interpreter gets a line of code from here every time a statement is run"
    statement = True
    j = -1
    while statement:
        def get():
            nonlocal j
            j += 1
            return sorted_map[j % len(sorted_map)]
        # "and parses it with a split function."
        def split(line: str):
            # "This split function splits by any whitespaces unless it's in a string.
            # Example:
            # ```
            # print meow "meow meow"
            # ```
            # is parsed as:
            # ```
            # ["print", "meow", "meow meow"]
            # ```"
            import regex
            return [s.removeprefix('"').removesuffix('"') for s in 
                    regex.split(r'(?!(?<=".*)(?=.*")) ', line)]
        assert split('print meow "meow meow"') == ['print', 'meow', 'meow meow']
        # "Elements in this array are referred to as "parts""
        parts = split(get())
        # "Then, the interpreter evaluates variables and other identifiers."
        for i in range(len(parts)):
            # A $ prefix on an identifier means get an integer from a variable. 
            variable = None
            if parts[i].startswith('$'):
                variable = parts[i][1:]
            # "Variables are integer arrays." 
            variables: dict = {'': [line_number]}
            # "The string containing the identifier will be replaced with the
            # first value of the variable's array."
            if array := variables.get(variable):
                parts[i] = array[0]
                continue
            # "A ! prefix means string. A string is created from the variable's array,
            # where each element is an ASCII character."
            variable = None
            if parts[i].startswith('!'):
                variable = parts[i][1:]
            if array := variables.get(variable):
                parts[i] = ascii(array)
                continue
            # "A & prefix means the part will be replaced with the next character's
            # ASCII value."
            if parts[i].startswith('&'):
                import regex
                next_character = regex.match(r'\X', parts[i][1:]).group()
                import encodings.idna
                parts[i] = int.from_bytes(encodings.idna.ToASCII(next_character))
                continue
        # "Then the parsed array is passed to the function named in the first element."
        function_name = parts[0]
        def pass_to_function(parsed_array: list):
            function = functions[function_name]
            function(parsed_array)
        # The array when passed to the function will have the first element removed."
        def the(array: list):
            array.pop(0)
            nonlocal line_number, j
            if (line_number / array[1] * array[0]).is_integer():
                line_number *= array[0]
                line_number //= array[1]
                print(line_number)
                j = -1
        functions = {'the': the}
        pass_to_function(parts)
        # "To write to the program's map, the line number is written before the statement."
        line_number_is_written = line_number in parts
        if line_number_is_written:
            statement = line_number
        # "The line number must also be replaced if it contains an identifier (see Part replacement)"
        if str(line_number).isidentifier():
            line_number = '<Part>'

implement_ysl(open('mqpy.YSL', 'rb').read().decode())