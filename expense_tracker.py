import json
class Tracker:
  def __init__(self):
    self.expense = []
  def add_expense(self,a,b,c):
    new = {'name': a,"amount" : b,"category":c}
    self.expense.append(new)
    return self.expense
  def spent(self):
     count = 0
     for i in self.expense:
            count+= i["amount"]
     return count
  def delete(self,idx):
     self.expense.pop(idx)
     return self.expense
  def save_to_file(self,filename):
    with open(filename,"w")as f:
      json.dump(self.expense,f)
  def load_from_file(self,filename):
    with open(filename,"r")as f:
      self.expense = json.load(f)
      return self.expense
def Menu():
    c1 = Tracker()
    while True:
     i =  int(input("enter a choice: "))
     match i :
            case 1:
                 a = input(("item is "))
                 b = int(input(("amount is ")))
                 c = input(("category is "))
                 print(c1.add_expense(a,b,c))
            case 2:
                print(c1.spent())
            case 3:
                idx = int(input("idx is : "))
                c1.delete(idx)
                print(c1.expense)
            case 4:
                filename = "him.txt"
                print(c1.save_to_file(filename))
            case 5:
                filename = "him.txt"
                print(c1.load_from_file(filename))
            case 6:
                break
print(Menu())
