
def median(input):
  ind=len(input)

  if ind % 2==0:
     index1=ind//2
     med=(input[index1]+input[(index1-1)])/2
     return med
  else:
    index1=ind//2
    med=input[index1]
    return med