# zlang_interpreter.py

import pyparsing as pp
import re

class ZLangInterpreter:
    def __init__(self):
        self.variables = {}

    def tokenize(self, zlang_code):
        # Define regular expressions for Z-Lang tokens
        token_patterns = {
            'IDENTIFIER': r'[a-zA-Z_][a-zA-Z_0-9]*',
            'STRING_LITERAL': r"'[^']*'",
            'NUMBER_LITERAL': r'\d+',
            'KEYWORD': r'(spill|store|if|while|func)',
            'OPERATOR': r'[=<>+\-*/%()]',
            'WHITESPACE': r'\s+',
            'COMMENT': r'#.*'
        }

        # Tokenize the Z-Lang code
        tokens = []
        for pattern, regex in token_patterns.items():
            for match in re.finditer(regex, zlang_code):
                token = (pattern, match.group())
                tokens.append(token)

        return tokens

    def parse_tokens(self, tokens):
        # Recursive descent parser
        def parse_expression(tokens):
            if tokens[0][0] == 'IDENTIFIER':
                return Identifier(tokens[0][1])
            elif tokens[0][0] == 'STRING_LITERAL':
                return StringLiteral(tokens[0][1])
            elif tokens[0][0] == 'NUMBER_LITERAL':
                return NumberLiteral(int(tokens[0][1]))
            elif tokens[0][0] == 'OPERATOR':
                if tokens[0][1] == '(':
                    return parse_expression(tokens[1:])
                elif tokens[0][1] == ')':
                    return None
                else:
                    raise SyntaxError("Invalid operator")
            else:
                raise SyntaxError("Invalid token")

        def parse_statement(tokens):
            if tokens[0][0] == 'KEYWORD':
                if tokens[0][1] == 'spill':
                    return SpillStatement(parse_expression(tokens[1:]))
                elif tokens[0][1] == 'store':
                    return StoreStatement(tokens[1][1], parse_expression(tokens[2:]))
                elif tokens[0][1] == 'if':
                    return IfStatement(parse_expression(tokens[1:]), parse_statement(tokens[2:]))
                elif tokens[0][1] == 'while':
                    return WhileStatement(parse_expression(tokens[1:]), parse_statement(tokens[2:]))
                elif tokens[0][1] == 'func':
                    return FuncStatement(tokens[1][1], parse_statement(tokens[2:]))
            else:
                raise SyntaxError("Invalid keyword")

        ast = []
        while tokens:
            statement = parse_statement(tokens)
            ast.append(statement)
            tokens = tokens[statement.end:]

        return ast

    def generate_python_code(self, ast):
        python_code = ''
        for statement in ast:
            python_code += statement.generate_python_code() + '\n'
        return python_code

    def execute_python_code(self, python_code):
        exec(python_code)

    def interpret(self, zlang_code):
        tokens = self.tokenize(zlang_code)
        ast = self.parse_tokens(tokens)
        python_code = self.generate_python_code(ast)
        self.execute_python_code(python_code)

class Identifier:
    def __init__(self, name):
        self.name = name
        self.end = 1

    def generate_python_code(self):
        return self.name

class StringLiteral:
    def __init__(self, value):
        self.value = value
        self.end = 1

    def generate_python_code(self):
        return f"'{self.value}'"

class NumberLiteral:
    def __init__(self, value):
        self.value = value
        self.end = 1

    def generate_python_code(self):
        return str(self.value)

class SpillStatement:
    def __init__(self, expression):
        self.expression = expression
        self.end = expression.end + 1

    def generate_python_code(self):
        return f"print({self.expression.generate_python_code()})"

class StoreStatement:
    def __init__(self, name, expression):
        self.name = name
        self.expression = expression
        self.end = expression.end + 1

    def generate_python_code(self):
        return f"{self.name} = {self.expression.generate_python_code()}"

class IfStatement:
    def __init__(self, condition, statement):
        self.condition = condition
        self.statement = statement
        self.end = statement.end + 1

    def generate_python_code(self):
        return f"if {self.condition.generate_python_code()}:\n    {self.statement.generate_python_code()}"

class WhileStatement:
    def __init__(self, condition, statement):
       self.condition = condition
        self.statement = statement
        self.end = statement.end + 1

    def generate_python_code(self):
        return f"while {self.condition.generate_python_code()}:\n    {self.statement.generate_python_code()}"

class FuncStatement:
    def __init__(self, name, statement):
        self.name = name
        self.statement = statement
        self.end = statement.end + 1

    def generate_python_code(self):
        return f"def {self.name}():\n    {self.statement.generate_python_code()}"

interpreter = ZLangInterpreter()
zlang_code = "spill('Hello, World!')"
interpreter.interpret(zlang_code)


class ZLangInterpreter:
    # ... (rest of the class remains the same)

    def parse_zlang(self, zlang_code):
        # Define the Z-lang grammar using pyparsing
        zlang_keyword = pp.oneOf(self.zlang_to_python.keys())
        zlang_identifier = pp.Word(pp.alphas + '_', pp.alphanums + '_')
        zlang_literal = pp.pyparsing_common.number | pp.quotedString
        zlang_expression = pp.Forward()
        zlang_expression << (zlang_literal | zlang_identifier | pp.nestedExpr(content=zlang_expression))
        zlang_assignment = zlang_identifier + '=' + zlang_expression
        zlang_function_call = zlang_identifier + pp.nestedExpr(content=zlang_expression)
        zlang_if_statement = pp.Keyword('chk') + zlang_expression + pp.Keyword('then') + zlang_expression
        zlang_for_loop = pp.Keyword('4each') + zlang_identifier + pp.Keyword('in') + zlang_expression + pp.Keyword('do') + zlang_expression
        zlang_while_loop = pp.Keyword('loop') + zlang_expression + pp.Keyword('do') + zlang_expression
        zlang_statement = pp.Forward()
        zlang_statement << (zlang_keyword | zlang_assignment | zlang_function_call | zlang_if_statement | zlang_for_loop | zlang_while_loop)

        # Parse the Z-lang code
        parse_tree = zlang_statement.parseString(zlang_code, parseAll=True)

        # Translate the parse tree to Python code
        python_code = ''
        for node in parse_tree:
            if node in self.zlang_to_python:
                python_code += self.zlang_to_python[node] + ' '
            elif node in self.zlang_data_types:
                python_code += self.zlang_data_types[node] + ' '
            elif node in self.zlang_control_flow:
                python_code += self.zlang_control_flow[node] + ' '
            elif isinstance(node, pp.ParseResults):
                if node[0] == 'chk':
                    python_code += 'if ' + str(node[1]) + ': ' + str(node[2]) + '\n'
                elif node[0] == '4each':
                    python_code += 'for ' + str(node[1]) + ' in ' + str(node[2]) + ': ' + str(node[3]) + '\n'
                elif node[0] == 'loop':
                    python_code += 'while ' + str(node[1]) + ': ' + str(node[2]) + '\n'
                else:
                    python_code += str(node) + ' '
            else:
                python_code += str(node) + ' '
        return python_code