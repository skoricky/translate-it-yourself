import os

d = os.path.abspath(os.path.dirname(__file__))

a = 'exit_ico.png'

print(os.path.join(d, a))