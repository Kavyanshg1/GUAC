class ZLangInterpreter:
  def __init__(self):
      self.zlang_to_python = {
          'spill': 'print',
          'ask': 'input',
          'size': 'len',
          'kind': 'type',
          'num': 'int',
          'drip': 'float',
          'chatter': 'str',
          'squad': 'list',
          'stash': 'dict',
          'clique': 'set',
          'pair': 'tuple',
          'span': 'range',
          'addem': 'sum',
          'top': 'max',
          'low': 'min',
          'fabs': 'abs',
          'curve': 'round',
          'pop': 'open',
          'shut': 'close',
          'addon': 'append',
          'toss': 'remove',
          'flip': 'reverse',
          'like': 'isinstance',
          'snap': 'map',
          'sift': 'filter',
          'crunch': 'reduce',
          'link': 'zip',
          'index': 'enumerate',
          'bet': 'all',
          'sus': 'any',
          'look': 'dir',
          'assist': 'help',
          'tag': 'id',
          'judge': 'eval',
          'make': 'compile',
          'ringable': 'callable',
          'mark': 'hash',
          'icyclique': 'frozenset',
          'fresh': 'sort',
          'runit': 'exec',
          'sortedvibes': 'sorted',
          'vibecheck': 'bool',
          '4each': 'for',
          'loop': 'while',
          'chk': 'if',
          'otherwize': 'else',
          'or_else': 'elif',
          'stop': 'break',
          'carryon': 'continue',
          'd-fine': 'def',
          'brb': 'return',
          'give_it_a_shot': 'try',
          'uh_oh': 'except',
          'last_call': 'finally',
          'rollin_with': 'with',
          'chill': 'pass',
          'fn': 'lambda',
          'ghost': 'None',
          'fr': 'True',
          'cap': 'False',
          '&&': 'and',
          '||': 'or',
          '!': 'not',
          'isnot': 'is not',
          'notin': 'not in'
      }

      self.zlang_data_types = {
          'digit': 'int',
          'drip': 'float',
          'chatter': 'str',
          'squad': 'list',
          'pair': 'tuple',
          'stash': 'dict',
          'clique': 'set',
          'check': 'bool'
      }

      self.zlang_boolean_values = {
          'fr': 'True',
          'cap': 'False'
      }

      self.zlang_control_flow = {
          '4each': 'for',
          'loop': 'while',
          'chk': 'if',
          'otherwize': 'else',
          'or_else': 'elif',
          'stop': 'break',
          'carryon': 'continue',
          'd-fine': 'def',
          'brb': 'return',
          'give_it_a_shot': 'try',
          'uh_oh': 'except',
          'last_call': 'finally',
          'rollin_with': 'with',
          'chill': 'pass'
      }

      self.zlang_operators = {
          '+': '+',
          '-': '-',
          '*': '*',
          '/': '/',
          '%': '%',
          '**': '**',
          '//': '//',
          '=': '=',
          '==': '==',
          '!=': '!=',
          '<': '<',
          '<=': '<=',
          '>': '>',
          '>=': '>=',
          '&&': 'and',
          '||': 'or',
          '!': 'not',
          'is': 'is',
          'in': 'in',
          'notin': 'not in',
          'isnot': 'is not',
          'fn': 'lambda'
      }

      self.zlang_constants = {
          'ghost': 'None'
      }

  def parse_zlang(self, zlang_code):
      python_code = ''
      for line in zlang_code.split('\n'):
          words = line.split()
          for i, word in enumerate(words):
              if word in self.zlang_to_python:
                  words[i] = self.zlang_to_python[word]
              elif word in self.zlang_data_types.values():
                  words[i] = list(self.zlang_data_types.keys())[list(self.zlang_data