import pathlib
import test
def CodeTesting():
    # "prob3_bronze_jan21/" + "1.in"
    path = "prob3_bronze_jan21/"
    for i in range(1,13):
        current_file = open(path+str(i)+".in", "r")
        input = current_file.read()
        input = input.split("\n")
        current_file = open(path+str(i)+".out", "r")
        out = current_file.read().strip()
        if test.demo1(input) == out:
            print("Yay!")
        else:
            print(test.demo1(input))
            print(out)
            print("")
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    CodeTesting()
