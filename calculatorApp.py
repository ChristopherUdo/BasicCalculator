#!/Library/Frameworks/Python.framework/Versions/3.4/bin/python3
# Darian Nwankwo, August 1, 2015, Calculator App using tkinter gui
from tkinter import *
from tkinter import ttk


class BasicCalculator(object):
  """Basic Calculatorfor simple addition, subtraction, multiplication, and division."""
  def __init__(self, master):
    """Creates the calculators GUI for basic actions"""
    self.action = ''
    self.nums_inputed = []
    self.operations = [
        self._divide, self._multiply,
        self._subtract, self._add,
        self._equals, self._decimal
    ]
    # Saves the commands for each number into a list
    self.nums_commands = [
        self._one, self._two, self._three,
        self._four, self._five, self._six,
        self._seven, self._eight, self._nine,
        self._zero
    ]

    self._CreateEntryField(master)
    self._CreateNumberButtons(master)
    self._CreateClearButton(master)
    self._CreateOperators(master)
  
  def _CreateEntryField(self, master):
    """Creates the entry field where user input and results are displayed."""
    self._entry = ttk.Entry(master)
    self._entry.config(width = 39)
    self._entry.grid(row = 0, columnspan = 30)

  def _CreateDecimalButton(self, master):
    self._decimal = ttk.Frame(master)
    self._decimal.grid(row = 5, column = 1)
    ttk.Button(self._decimal, text = '.', command = self.operations[5]).pack()

  def _CreateNumberButtons(self, master):
    """Creates the number buttons for the interface."""
    self._CreateDecimalButton(master)
    try:
      for i in range(10):
        # Creates a new frame for each button
        self._numbers = ttk.Frame(master)
        # Creates button objects 1-3 on third row
        if (i < 3):
          self._numbers.grid(row = 2, column = (i % 3))
          ttk.Button(self._numbers, text = (i + 1), command = self.nums_commands[i]).pack()
        # Creates button objects 4-6 on fourth row
        elif (i >= 3 and i <= 5):
          self._numbers.grid(row = 3, column = (i % 3))
          ttk.Button(self._numbers, text = (i + 1), command = self.nums_commands[i]).pack()
        # Creates button objects 7-9 on fifth row
        elif (i >=5 and i <= 8):
          self._numbers.grid(row = 4, column = (i % 3))
          ttk.Button(self._numbers, text = (i + 1), command = self.nums_commands[i]).pack()
        # Creates button object 0 on sixth row
        elif (i == 9):
          self._numbers.grid(row = 5, column = (i % 3))
          ttk.Button(self._numbers, text = 0, command = self.nums_commands[i]).pack()
    except:
      return "Something went wrong"
        
  def _CreateClearButton(self, master):
    """Creates the button object for clear."""
    self._clear = ttk.Frame(master)
    self._clear.grid(row = 1, column = 0)
    ttk.Button(self._clear, text = 'Clear', command= self.Clear).pack()

  def Clear(self):
    """Clear all characters in the entry field and from storage."""
    self.nums_inputed = []
    self._entry.delete(0, END)
  
  def _CreateOperators(self, master):
    """Creates the operator buttons. (To-Do): Iterate and Create.""" 
    divide, multiply, subtract, add, equals = ttk.Frame(master), ttk.Frame(master), ttk.Frame(master), ttk.Frame(master), ttk.Frame(master)
    divide.grid(row = 1, column = 3)
    div = ttk.Button(divide, text = '/', command = self.operations[0]).pack()
    multiply.grid(row = 2, column = 3)
    mult = ttk.Button(multiply, text = 'x', command = self.operations[1]).pack()
    subtract.grid(row = 3, column = 3)
    sub = ttk.Button(subtract, text = '-', command = self.operations[2]).pack()
    add.grid(row = 4, column = 3)
    addition = ttk.Button(add, text = '+', command = self.operations[3]).pack()
    equals.grid(row = 5, column = 3)
    eq = ttk.Button(equals, text = '=', command = self.operations[4]).pack() 

  def _decimal(self):
    self._entry.insert(len(self._entry.get()), '.')

  def _add(self):
    self.action = '+'
    self.nums_inputed.append(float(self._entry.get()))
    self._entry.delete(0, END)

  def _subtract(self):
    self.action = '-'
    self.nums_inputed.append(float(self._entry.get()))
    self._entry.delete(0, END)

  def _divide(self):
    self.action = '/'
    self.nums_inputed.append(float(self._entry.get()))
    self._entry.delete(0, END)

  def _multiply(self):
    self.action = 'x'
    self.nums_inputed.append(float(self._entry.get()))
    self._entry.delete(0, END)

  def _equals(self):
    self.nums_inputed.append(float(self._entry.get()))
    # If there is only one number inputed, display that number
    if len(self.nums_inputed) == 1:
      self._entry.delete(0, END)
      self._entry.insert(0, self.nums_inputed[0])
    
    if self.action == '/' or self.action == 'x':
      # Math logic behind division
      if self.action == '/':
        total = self.nums_inputed[0]
        for nums in range(len(self.nums_inputed) - 1):
          total /= self.nums_inputed[nums + 1]
        self._entry.delete(0, END)
      # Math logic behind multiplication
      elif self.action == 'x':
        total = self.nums_inputed[0]
        for nums in range(len(self.nums_inputed) - 1):
          total *= self.nums_inputed[nums + 1]
        self._entry.delete(0, END)
    elif self.action == '+' or self.action == '-':
      # Math logic behind addition
      if self.action == '+':
        total = 0
        for nums in range(len(self.nums_inputed)):
          total += self.nums_inputed[nums]
        self._entry.delete(0, END)
      # Math logic behind subtraction
      elif self.action == '-':
        total = self.nums_inputed[0]
        for nums in range(len(self.nums_inputed) - 1):
          total -= self.nums_inputed[nums + 1]
        self._entry.delete(0, END)

    if total == int(total):
      self._entry.insert(0, int(total))
    else:
      self._entry.insert(0, total)
    self.nums_inputed = []


  def _one(self):
    self._entry.insert((len(self._entry.get())), '1')

  def _two(self):
    self._entry.insert((len(self._entry.get())), '2')

  def _three(self):
    self._entry.insert((len(self._entry.get())), '3')

  def _four(self):
    self._entry.insert((len(self._entry.get())), '4')

  def _five(self):
    self._entry.insert((len(self._entry.get())), '5')

  def _six(self):
    self._entry.insert((len(self._entry.get())), '6')

  def _seven(self):
    self._entry.insert((len(self._entry.get())), '7')

  def _eight(self):
    self._entry.insert((len(self._entry.get())), '8')

  def _nine(self):
    self._entry.insert((len(self._entry.get())), '9')

  def _zero(self):
    self._entry.insert((len(self._entry.get())), '0')


def main():
  root = Tk()
  root.title('Calculator')
  root.resizable(False, False)
  calculator = BasicCalculator(root)
  root.mainloop()

if __name__ == '__main__':
  main()
