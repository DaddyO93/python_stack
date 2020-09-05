class Underscore:
    def map(self, iterable, callback):
        count=0
        for num in iterable:
            iterable[count]=callback(num)
            count+=1
        print(iterable)
        return(iterable)
    def find(self, iterable, callback):
        for num in iterable:
            if callback(num):
                print(num)
                return num
            else:
                pass
    def filter(self, iterable, callback):
        for num in range(len(iterable)-1):
            if num<len(iterable):
                if callback(iterable[num]):
                    pass
                else: 
                    iterable.pop(num)
                    num -=1
            else:
                print(iterable)
                return iterable
    def reject(self, iterable, callback):
        for num in range(len(iterable)-1):
            if num<len(iterable):
                if callback(iterable[num]):
                    iterable.pop(num)
                    num -=1
                else:
                    pass
            else:
                print(iterable)
                return(iterable)


_ = Underscore() # yes we are setting our instance to a variable that is an underscore
evens = _.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0) # should return [2, 4, 6]
odds = _.reject([1,2,3,4,5,6], lambda x: x%2==0) # should return [1,3,5]
double = _.map([1,2,3], lambda x: x*2) # should return [2,4,6]
greater_than_4 = _.find([1,2,3,4,5,6], lambda x: x>4) # should return the first value that is greater than 4

