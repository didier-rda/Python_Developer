#Given the below class:
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
cat1 = Cat('miau', 17)
cat2 = Cat('crau', 28)
cat3 = Cat('tal', 14)


# 2 Create a function that finds the oldest cat
def oldest_cat(c1, c2, c3):
  lista = []
  lista.append(c1.age)
  lista.append(c2.age)
  lista.append(c3.age)
  return max(lista)

  # 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
print(f'The oldest cat is {oldest_cat(cat1, cat2, cat3)} years old.')
