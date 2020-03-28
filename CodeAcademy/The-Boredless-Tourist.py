destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "Sao Paulo, Brazil", "Cairo, Egypt"]
test_traveler = ["Erin Wilkes", "Shanghai, China", "historical site", "art"]

def get_dest_index(destination):
  dest_index = destinations.index(destination)
  return dest_index

print(get_dest_index("Los Angeles, USA"))
print(get_dest_index("Paris, France"))

def get_trav_loc(traveler):
  trav_dest = test_traveler[1]
  trav_dest_index = get_dest_index(trav_dest)
  return trav_dest_index

test_dest_index = get_trav_loc(test_traveler)
print(test_dest_index)

attractions = []
for dest in destinations:
  attractions.append([])
print(attractions)

def add_attrac(dest, attrac):
  try:
    attrac_for_dest = attractions[get_dest_index(dest)]
    attrac_for_dest.append(attrac)
    return
  except ValueError:
    return
add_attrac("Los Angeles, USA", ["Venice Beach", ["beach"]])
add_attrac("Paris, France", ["the Louvre", ["art", "museum"]])
add_attrac("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attrac("Shanghai, China", ["Yu Garden", ["garden", "historcical site"]])
add_attrac("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attrac("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attrac("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attrac("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attrac("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attrac("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attrac("Cairo, Egypt", ["Egyptian Museum", ["museum"]])
print(attractions)

def find_attrac(dest, interests):
  dest_index = get_dest_index(dest)
  attrac_in_city = attractions[dest_index]
  attrac_w_interest = []
  for attrac in attrac_in_city:
    attrac_tag = attrac[1]
    for interest in interests:
      if interest in attrac_tag:
        attrac_w_interest.append(attrac)
  return attrac_w_interest
print(find_attrac("Los Angeles, USA", ['art']))