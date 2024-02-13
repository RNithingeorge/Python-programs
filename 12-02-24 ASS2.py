class ArmstrongChecker:
    def __init__(self, number):
        self.num = number

    def is_armstrong(self):
        temp = self.num
        res = 0

        while temp != 0:
            digit = temp % 10
            res += digit ** 3
            temp //= 10

        if self.num == res:
            print("is an Armstrong number")
        else:
            print("  not an Armstrong number")

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    checker = ArmstrongChecker(num)
    checker.is_armstrong()
