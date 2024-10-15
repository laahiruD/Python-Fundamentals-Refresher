#Classes are blueprints for objects.

class Vehicle:
  #properties of the class
  def __init__(self, make, model):
    self.make = make
    self.model =  model

  
  def moves(self):
    print('Moving along...')

  def get_make_model(self):
    print(f'I am a {self.make} {self.model}.')


#creating an object from vehicle class
my_car = Vehicle('Tesla', 'model-3')
my_car.moves()
print(my_car.model)
my_car.get_make_model()

your_car = Vehicle('Cadillac', 'Escalade')
your_car.get_make_model()



#Inheritance
class Airplane(Vehicle):
  def __init__(self, make, model,faa_id):
    super().__init__(make,model)
    self.faa_id = faa_id

  def moves(self):
    print('Flies Along...')


class Truck(Vehicle):
  def moves(self):
    print('Rumbles along..')


class GolfCart(Vehicle):
  pass 


cessna = Airplane('Cessna', 'Skyhawk','N14J45')
mack = Truck('Mack','Pinnacle')
golfwagon = GolfCart('Yamaha', 'GC 125')

cessna.get_make_model()
cessna.moves()
mack.get_make_model()
mack.moves()
golfwagon.get_make_model()
golfwagon.moves()


###############################
#polymorphism :is ability to behave differently for same input
for v in (my_car, your_car, cessna,mack,golfwagon):
  v.get_make_model()
  v.moves()