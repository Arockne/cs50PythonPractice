def main():
  x = int(input("what is x? "))
  print(f"{x} squared is", square(x))

def square(num):
  return pow(num, 2)


main()