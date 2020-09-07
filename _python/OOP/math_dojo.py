class MathDojo:
    def __init__(self):
    	self.result = 0
    def add(self, num, *nums):
        for i in nums:
            self.result += i
        self.result += num
        return self
    def subtract(self, num, *nums):
        for i in nums:
            self.result -= i
        self.result -= num
        return self

# create an instance:
md = MathDojo()
# to test:
x = md.add(2).add(2,5,1).subtract(3,2).result
print(x)	# should print 5
# run each of the methods a few more times and check the result!
x = md.add(1).add(3,67,234,345324513245123).add(4151451,12541,533).result
print(x)

x=md.subtract(1234,1234,234,678,4,234).add(134513,1256246,147,8133).add(5123).result
print(x)