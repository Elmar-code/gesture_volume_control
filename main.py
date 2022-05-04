pul = 0
def tanlov():
    print("Qanday.Yeguliklarimizdan xarid kimoxchisiz?")
    a = int(input("1 Taom\n"
                  "2 Ichimlik\n"
                  "3 Fast_fud\n"
                  "4 Shirinlik\n"))
    global pul
    if a == 1:
        d = int(input("1_Osh\n"
                      "2_Mastava\n"
                      "3_Lagmon\n"
                      "4_Gril\n"))
        if d == 1:
            pul += 10
        elif d == 2:
            pul += 12
        elif d == 3:
            pul += 13
        elif d == 4:
            pul += 30
        else:
            tanlov()

        a = int(input("Taomlarimizdan yana olmoxchimisiz\n"
                      "1 Xa\n2 Yo'q\n"))
        if a == 1:tanlov()
        else:
            print("Xaridingiz uchun raxmad,mijoz")

    elif a == 2:
        b = int(input("1_Kola\n"
                  "2_Fanta\n"
                  "3_Sprayt\n"
                  "4_Fanta\n"))
        if b == 1:
            pul += 10
        elif b == 2:
            pul += 11
        elif b == 3:
            pul += 9
        elif b == 4:
            pul += 12
        else:
            tanlov()

        a = int(input("Taomlarimizdan yana olmoxchimisiz\n"
                      "1 Xa\n2 Yo'q\n"))
        if a == 1:
            tanlov()
        else:
            print("Xaridingiz uchun raxmad,mijoz")

    elif a ==  3:
        f = int(input("1_Xod dog\n"
                      "2_Lavash\n"
                      "3_Non berger\n"
                      "4_Gamburger\n"))
        if f == 1:
            pul += 14
        elif f == 2:
            pul += 7
        elif f == 3:
            pul += 12
        elif f == 4:
            pul =+ 15
        else:
            tanlov()

        a = int(input("Taomlarimizdan yana olmoxchimisiz\n"
                      "1 Xa\n2 Yo'q\n"))
        if a == 1:
            tanlov()
        else:
            print("Xaridingiz uchun raxmad,mijoz")

    elif a ==4:
        h = int(input("1_Tord\n"
                      "2_Napalion\n"
                      "3_Kexs\n"
                      "4_Medavik\n"))
        if h == 1:
            pul += 70
        elif h == 2:
            pul += 28
        elif h == 3:
            pul += 45
        elif h == 4:
            pul += 38

        a = int(input("Taomlarimizdan yana olmoxchimisiz\n"
                      "1 Xa\n2 Yo'q\n"))
        if a == 1:
            tanlov()
        else:
            print("Xaridingiz uchun raxmad,mijoz")

    else:
        tanlov()

tanlov(),print("Sizning xaridingiz",pul,"som boldi\n")

