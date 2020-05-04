dik1 = int(input("1.Dik Kenar: "))
dik2 = int(input("2.Dik Kenar: "))
hipo = int(input("Hipotenüs: "))

aci = int(input("Hangi Uzunluğu Gören Açıyı Seçmek İstersiniz ?: "))

if aci == dik1 :
    print("sin","cos","tan","cot")
    a = input("Hangi İslemi Yapmak İstersiniz? : ")
    if a == "sin":
        b = dik1/hipo
        print(b)
    elif a == "cos":
        b = dik2/hipo
        print(b)
    elif a == "tan":
        b = dik1/dik2
        print(b)
    elif a == "cot":
        b = dik2/dik1
        print(b)
    else:
        print("Sadece sin,cos,tan,cot yazabilirsiniz")


elif aci == dik2 :
    print("sin","cos","tan","cot")
    a = input("Hangi İslemi Yapmak İstersiniz? : ")
    if a == "sin":
        b = dik2/hipo
        print(b)
    elif a == "cos":
        b = dik1/hipo
        print(b)
    elif a == "tan":
        b = dik2/dik1
        print(b)
    elif a == "cot":
        b = dik1/dik2
        print(b)
    else:
        print("Sadece sin,cos,tan,cot yazabilirsiniz")


elif aci == hipo :
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
    else :
        print("Sadece evet veya hayir yazabilirsiniz.")

else:
    print("Böyle Bir Kenar Seçmemiştiniz.")


