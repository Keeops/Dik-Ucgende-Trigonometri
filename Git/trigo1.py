dik1 = int(input("1.Dik Kenar: "))
dik2 = int(input("2.Dik Kenar: "))
hipo = int(input("Hipotenüs: "))

aci = int(input("Hangi Uzunluğu Gören Açıyı Seçmek İstersiniz ?: "))

def sin(karsi,hipot):
    print(karsi/hipot)
def cos(komsu,hipot):
    print(komsu/hipot)
def tan(karsi,komsu):
    print(karsi/komsu)
def cot(komsu,karsi):
    print(komsu/karsi)


if aci == dik1:

    karsi = dik1
    komsu = dik2
    hipot = hipo

    print("sin", "cos", "tan", "cot")
    a = input("Hangi İslemi Yapmak İstersiniz? : ")

    if a == "sin":
        sin(karsi,hipot)
    elif a == "cos":
        cos(komsu,hipot)
    elif a == "tan":
        tan(karsi,komsu)
    elif a == "cot":
        cot(komsu,karsi)
    else:
        print("Sadece sin,cos,tan,cot yazabilirsiniz")


elif aci == dik2:
    karsi = dik2
    komsu = dik1
    hipot = hipo

    print("sin", "cos", "tan", "cot")
    a = input("Hangi İslemi Yapmak İstersiniz? : ")

    if a == "sin":
        sin(karsi,hipot)
    elif a == "cos":
        cos(komsu,hipot)
    elif a == "tan":
        tan(karsi,komsu)
    elif a == "cot":
        cot(komsu,karsi)
    else:
        print("Sadece sin,cos,tan,cot yazabilirsiniz")

elif aci == hipo:
    a = input("Hipotenüsü Seçtiniz Devam Etmek İster Misiniz? (evet/hayir) : ")
    if a == "evet":
        print("sin", "cos", "tan", "cot")
        b = input("Hangi İslemi Yapmak İstersiniz? : ")
        if b == "sin":
            print("Sin(90) = 1")
        elif b == "cos":
            print("Cos(90) = 0")
        elif b == "tan":
            print("Tan(90) = Tanımsız")
        elif b == "cot":
            print("Cot(90) = Tanımsız")
        else:
            print("Sadece sin,cos,tan,cot yazabilirsiniz")
    elif a == "hayir":
        print("Tekrar Deneyin")
    else:
        print("Sadece evet veya hayir yazabilirsiniz.")

else:
    print("Böyle Bir Kenar Seçmemiştiniz.")
