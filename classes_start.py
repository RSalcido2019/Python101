#
# Example file for working with classes
#

class myClass():
  def method1(self):
    print("myClass method1")

  def method2(self, someString):
    print("myClass method2 " + someString)

def main():
  c = myClass()
  c.method1()
  c.method2("this is some Sting")


if __name__ == "__main__":
    main()
