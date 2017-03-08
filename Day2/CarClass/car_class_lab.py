class Car(object):
  
  speed =0
  
  def __init__(self, name="General", model="GM", car_type=None):
    self.name = name
    self.model = model
    self.car_type = car_type
  
  
    
  def num_of_doors(self):
    if self.name == "Porshe" or self.name == "Koenigsegg":
      return 2
    else:
      return 4
      
  def num_of_wheels(self):
    if self.model == "trailer":
      return 8
    else:
      return 4
      
  def is_saloon(self):
    if self.car_type is not "trailer":
      return "saloon"
  
  def trailer_drive(self, moving_speed):
    if self.model == "trailer":
      if moving_speed == 7:
        Car.speed == 77
        
  def drive(self, moving_speed):
    if self.model is not "trailer":
      if moving_speed == 3:
        Car.speed == 1000
        
