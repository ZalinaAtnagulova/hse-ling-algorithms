#Задача 5 Valid Parentheses 
class Stack:
      def __init__(self): 
          self.input = []

      def push(self, item):
          self.input.append(item)

      def pop(self, item):
          brackets = {}
          brackets[']'] = '['
          brackets[')'] = '('
          brackets['}'] = '{'
          if brackets[item] in self.input:
              self.input.remove(brackets[item])
          else:
              self.push(item)

fun = Stack()
string = '{}'
string2 = '[{('
for item in string:
    if item in string2:
        fun.push(item)
    else:
        fun.pop(item)
if len(fun.input) != 0:
    print('Not balanced parantheses')
else:
    print('Balanced parantheses')