p = float(input('กรุณาใส่ค่า Hp >>'))
if p >= 14:
  print('เบสสุดๆ'+" (Super bass)")
if p <= 13 and p >= 8:
  print('เป็นเบส'+" (Basic or Alkali)")
if p == 7:
  print('เป็นกลาง'+" (Neutral)")
if p <= 5 and p >= 0:
  print('เป็นกรด'+" (Acidic)")
