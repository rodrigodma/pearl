from entities.home_buyer import Home_Buyers
from entities.neighborhood import Neighborhood
from entities.vector import Vector

class Challenge:
  neighborhoods = {}
  home_buyers = {}
  table_fits = {}

  def add_neighborhood(self, name, energy_efficiency, water, resilience):
    self.neighborhoods[name] = Neighborhood(name, Vector(energy_efficiency, water, resilience))
    self.table_fits[name] = {}

  def add_home_buyer(self, name, energy_efficiency, water, resilience, preferences):
    self.home_buyers[name] = Home_Buyers(name, Vector(energy_efficiency, water, resilience), preferences)

  def resolve(self):
    resolved_fits = {}
    for neighborhood_key in self.neighborhoods.keys():
      resolved_fits[neighborhood_key] = {}

    total_neighborhoods = len(self.home_buyers) / len(self.neighborhoods)
  
    for neighborhood in self.neighborhoods:
      self.table_fits[neighborhood] = {}

      for home_buyer in self.home_buyers:
        fit = int(self.home_buyers[home_buyer].fit(self.neighborhoods[neighborhood].scores))
        self.table_fits[neighborhood][home_buyer] = fit

      self.table_fits[neighborhood] = dict(sorted(self.table_fits[neighborhood].items(), key=lambda item: item[1], reverse=True))

    for i in range(len(self.home_buyers)):
      for neighborhood in self.neighborhoods:
        home_buyer = list(self.table_fits[neighborhood].keys())[i]

        if self.home_buyers[home_buyer].setted == False and len(resolved_fits[neighborhood]) < total_neighborhoods:
          for preference in self.home_buyers[home_buyer].preferences:
            if preference == neighborhood:
              resolved_fits[neighborhood][home_buyer] = self.table_fits[neighborhood][home_buyer]
              self.home_buyers[home_buyer].setted == True
            elif len(resolved_fits[preference]) < total_neighborhoods:
              break
    return resolved_fits

def challenge_from_file(input_file_name: str, challenge: Challenge):
    input_file = open(input_file_name, "r")

    for line in input_file:
        tokens = line.split(" ")
        if tokens[0] == "N":
            challenge.add_neighborhood(tokens[1], 
                                       float(tokens[2].split(":")[1]), 
                                       float(tokens[3].split(":")[1]), 
                                       float(tokens[4].split(":")[1]))
        elif tokens[0] == "H":
            challenge.add_home_buyer(tokens[1], 
                                     float(tokens[2].split(":")[1]), 
                                     float(tokens[3].split(":")[1]), 
                                     float(tokens[4].split(":")[1]), 
                                     tokens[5].split("\n")[0].split(">"))
    return challenge

if __name__ == "__main__":
    INPUT_FILE_PATH = "input.txt"
    challenge = challenge_from_file(INPUT_FILE_PATH, Challenge())
    result = challenge.resolve()
    print(result)