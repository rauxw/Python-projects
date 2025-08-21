# normal args
def add(*args):
  sum = 0
  for n in args:
    sum += n
  print(sum)

# keyword args
def calculate(val, **kwargs):
  val += kwargs["add"]
  val *= kwargs["multiply"]
  print(val)

class Player:

  def __init__(self, **kwargs):
    self.model = kwargs["model"]
    self.name = kwargs["name"]
    self.speed = kwargs["speed"]

  def display(self):
    print(f"Model: {self.model}")
    print(f"Name : {self.name}")
    print(f"Speed : {self.speed} km/h")

jack = Player(model="XVC", name="Feist", speed=23)
jack.display()