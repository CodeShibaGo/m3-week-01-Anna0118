def abbrev_name(name):
  first_name, second_name= name.split()
  return f"{first_name[0].upper()}.{second_name[0].upper()}"
