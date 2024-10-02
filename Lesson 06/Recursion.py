#recursion happens when function call itself again

def recursionadd_one_func(num):
  if (num >=  9):
    return num+1
  
  total = num + 1

  return recursionadd_one_func(total)

final_total = recursionadd_one_func(0)
print(final_total)