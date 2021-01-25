### PYTHON ###

#HESAP MAKİNESİ#

seçenek1 = "(1) topla"
seçenek2 = "(2) çıkar"
seçenek3 = "(3) çarp"
seçenek4 = "(4) böl"
seçenek5 = "(5) karesini hesapla"
seçenek6 = "(6) karekök hesapla"

print(seçenek1,seçenek2,seçenek3,seçenek4,seçenek5,seçenek6, sep="\n")

soru = input("Yapmak istediğiniz işlemin numarasını giriniz: ")

if soru == "1":
    sayı1 = int(input("Toplama işlemi için ilk sayıyı giriniz:"))
    sayı2 = int(input("Toplama işlemi için ikinci sayıyı giriniz:"))
    print(sayı1,"+",sayı2,"=",sayı1+sayı2)
elif soru == "2":
     sayı3 = int(input("Çıkarma işlemi için ilk sayıyı giriniz:"))
     sayı4 = int(input("Çıkarma işlemi için ikinci sayıyı giriniz:"))
     print(sayı3,"-",sayı4,"=",sayı3+sayı4)
elif soru == "3":
    sayı5 = int(input("Çarpma işlemi için ilk sayıyı giriniz:"))
    sayı6 = int(input("Çarpma işlemi için ikinci sayıyı giriniz:"))
    print(sayı5,"*",sayı6,"=",sayı5*sayı6)
elif soru == "4":
    sayı7 = int(input("Bölme işlemi için ilk sayıyı giriniz:"))
    sayı8 = int(input("Bölme işlemi için ikinci sayıyı giriniz:"))
    print(sayı7,"/",sayı8,"=",sayı7/sayı8)
elif soru == "5":
     sayı9 = int(input("Karesini hesaplamak için sayıyı giriniz:"))
     print(sayı9,"sayını karesi =",sayı9**2)
    
elif soru == "6":
    sayı10 = int(input("Karekökünü hesaplamak için sayıyı giriniz:"))
    print(sayı10,"sayının karekökü =",sayı10**0.5)
else :
 print("YANLIŞ GİRİŞ.")
 print("Aşağıdaki seçeneklerden birini giriniz:",seçenek1,seçenek2,seçenek3,seçenek4,seçenek5,seçenek6, sep="\n")
