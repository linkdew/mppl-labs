def main(x):
   '''
   Return maximum integer given list of integers.
   Args:
       x - List[Int] - list of incoming integers from which maximum is selected.
   Returns:
       Int - maximum element of x.
   '''
   
   result = x[0]
   
   for i in range(len(x)):
   	if(result < x[i]):
   		result = x[i]
   return result


def test():
    assert main([1,2,3]) == 3, "Check your implementation!"
    assert main([-1,5,3]) == 5, "Check your implementation!"
    print("Local tests for func passed!")


if __name__ == "__main__":
    test()

