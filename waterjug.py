a=int(input("Enter Jug A Capacity: "))
b=int(input("Enter Jug B Capacity: "))
ai=int(input("Initially water in Jug A: "))
bi=int(input("Initially water in Jug B: "))
af=int(input("Final State of Jug A: "))
bf=int(input("Final State of Jug B: "))
print("List of Operations you can do: ")
print("\n1.Fill Jug A completely \n2.Fill Jug B completely")
print("3.Empty Jug A completely \n4.Empty Jug B completely")
print("5.pour from Jug A till Jug B filled completely or A becomes empty")
print("6.pour from Jug B till Jug A filled completely or B becomes empty")
print("7.Pour all from Jug B to Jug A")
print("8.Pour all from Jug A to Jug B")

while(ai!=af or bi!=bf):
  op=int(input("Enter the operation: "))
  if(op==1):
    ai=a
  elif(op==2):
    bi=b
  elif(op==3):
    ai=0
  elif(op==4):
    bi=0
  elif(op==5):
    if(b-bi>ai):
      bi=ai+bi
      ai=0
    else:
      ai=ai-(b-bi)
      bi=b
  elif(op==6):
    if(a-ai>bi):
      ai=ai+bi
      bi=0
    else:
      bi=bi-(a-ai)
      ai=a
  elif(op==7):
    if(a-ai>=bi):
      ai=ai+bi
      bi=0
    else:
      print("Overflow")
      pass
  elif(op==8):
    if(b-bi>=ai):
      bi=ai+bi
      ai=0
    else:
      print("Overflow")
      pass
  print(ai,bi)
