banyak_bilangan = 15
count = 0
n1 = 0
n2 = 1

while count < banyak_bilangan:
   print(n1)
   bilangan_terakhir = n1 + n2
   n1 = n2
   n2 = bilangan_terakhir
   count += 1

for count in range(11):
  if count > 500:
    break
print ("habis")