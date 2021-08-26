
class Tensor():
    def __init__(self,data,shape):
        self.data = data 
        self.shape = shape

        if self.check_shape():
            self.tensor = self.shape_data()
            print(self.tensor)

        """
        Data and shape inputs are given as lists of numbers. 
        Data can be any number (int or float), but shape needs to be a 
        list of positive integers.
        """
    def check_shape(self):
        valid = True
        for x in self.shape:
            if x < 0:
                valid = False
        return valid

    def shape_data(self):
        #Output an empty list if the shape given is also an empty list ([])
        if len(self.shape) is 0:
            return []
        #shape0 = [2, 3, 2] means 
        #[how many elements final list will contain, The number of elements the main list will have, the number of indicies in that sublist]
        #find out what dimmension we need
        #start from end of the shape list
        total_element = 1
        for x in self.shape:
            total_element *= x
        zero_needed = total_element - len(self.data)
        if zero_needed > 0:
            temp = [0 for i in range(zero_needed)]
            self.data = self.data +temp
        else:
            self.data = self.data[0:total_element]

        #get the number and pair the numbers off into sublists
        temp= [self.data[i:i+self.shape[-1]] for i in range(0,len(self.data),self.shape[-1])]
        for x in reversed(self.shape[:-1]):
            temp =[temp[i:i+x] for i in range(0,len(temp),x)]
        try:
            [temp] = temp
        except:
            pass

        return temp       


def main():
    data0 = [0, 1, 2, 3, 4, 5, 0.1, 0.2, -3]
    shape0 = [2, 3, 2]
    shape1 = [5, 2]
    data1 =  [0, 1, 2, 3, 4, 5, 0.1, 0.2, -3, -2, -1, 3, 2, 1]
    tensor0 = Tensor(data1, shape1)
    #tensor0 = Tensor(data0, shape0)

main()
