class Vector():
  energy_efficiency: float
  water: float
  resilience: float

  def __init__(self, energy_efficiency, water, resilience):
    self.energy_efficiency = energy_efficiency
    self.water = water
    self.resilience = resilience

  def __str__(self):
    return f'(energy efficiency:{self.energy_efficiency},water:{self.water},resilience:{self.resilience})'