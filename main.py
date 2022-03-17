import funzioni
print("Scegliere l'elemento geometrico di cui si vuole calcolare l'area - 'q' per quadrato, 'r' per rettangolo, 'c' per cerchio, 't' per triangolo rettangolo: ")
fig = input()
if(fig=="q"):
  print("Inserire il lato del quadrato: ")
  l = float(input())
  funzioni.area_quadrato(l)

if(fig=="r"):
  print("Inserire i due lati del rettangolo: ")
  print("lato 1 ->")
  l1 = float(input())
  print("lato 2 ->")
  l2 = float(input())
  funzioni.area_rettangolo(l1,l2)

if(fig=="c"):
  print("Inserire il raggio del cerchio: ")
  r = float(input())
  funzioni.area_cerchio(r)

if(fig=="t"):
  print("Inserire i due lati del triangolo rettangolo: ")
  print("lato 1 ->")
  a = float(input())
  print("lato 2 ->")
  b = float(input())
  funzioni.area_triangolo(a,b)