num1 = int(input("Birinci Sayıyı Giriniz: "))
num2 = int(input("İkinci Sayıyı Girinz: "))

op = input("Bir İşlem Seçiniz (+,-, x, /): ")

if op == "+":
    print (num1, "+", num2, "-", num1 + num2)
elif op == "-":
    print (num1, "-", num2, "-", num1 - num2)
elif op == "x":
    print (num1, "x", num2, "-", num1 * num2)
elif op == "/":
    print(num1, "/", num2, "-", num1 / num2)
else:
    print("Programimmızda Böyle Bir İşlem Geçerli Değildir.")