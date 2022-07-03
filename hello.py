#has the same default parameter value as javascript 
def main():
  name = input("What's your name? ")
  hello(name)


def hello(to="world"):
  print(f"Hello {to}")


main()
