
#SORU1 :

# o="04.05.2020"
# print("KULLANICI TARAFINDAN GİRİLEN TARİH")
# dict_1={1:" 1 ocak 2020",2:" 2 ocak 2020",3:"3 mart 2020",4:" 4 nisan 2020",5:" 4 mayıs 2020",6:" 5 haziran 2020",7:" 6 temmuz 2020",8:" 7 ağustos 2020",9:" 8 eylül 2020"
#      ,10:" 9 ekim 2020",11:"10  kasım 2020" ,12:" 11 aralık 2020"}
# print(o)
# print(" kullanıcı tarafından girilen   tarihin ay kısmının yazıya döndürülmüş hali =", dict_1[5])


#SORU2 :
# o=int(input("lütfen bir sayı giriniz"))
#
# if (9<=o<16):
#     m = 0
#     e = 0
#     while ( m <o*2 ):
#         m = m + 2
#         e = e + m
#     print("1- girdiğiniz sayı ikiyle çarpıldı\n2- 2' den başlayıp girdiiğiniz sayının iki katına kadar   çift sayıların toplamı = ",e)
#
# if (o>=16) :
#     print("üzgünüz 16'dan büyük  bir sayı girdiniz")
# if (o<0):
#         print("üzgünüz 0'dan  küçük  bir sayı girdiniz")
#
# if (9>o>=0):
#     carpim = 1
#     for i in range(o):
#         if (9 > o >= 0):
#             carpim *= i + 1
#     r=carpim*3
#     print("girdiğiniz değerin faktöriyeli alınıp 3 ile çarpılmıştır =    " ,r)
#




# #SORU3 :
# sifreli_metin={"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8,
# "i":9,"j":10,"k":11,"l":12,"m":13,"n":14,"o":15,"p":16,"q":17,
# "r":18,"s":19,"t":20,"u":21,
#       "v":22,"w":23,"x":24,"y":25,"z":26}
# sifre=[[1,2,-1],
#     [2,5,2],
#     [-1,-2,2]]
#
# s=[[15,13,5],    #ömerba gündüz , metin şifrelemesi üçer üçer ayrılarak yapıldı.
#     [18,2,1],
#     [7,21,14],
#     ]
# e=[[4,21,26]]
#
# m=[[0,0,0],
#     [0,0,0],
#     [0,0,0],
#    [0,0,0]]
# for i in range (3):
#     for j in range(3):
#         m[i][j]=sifre[i][j]*s[i][j]
# for i in range(3):
#
#     print(m[i])
#     for i in range(1):
#         for j in range(1):
#             m[i][j]=sifre[i][j]*e[i][j]
#             for i in range(1):
#                 print(m[i])


#SORU 4 :

# dizi=[]
# print(type(dizi))
# for j in range(1,35):  #ÖĞRENCİ NUMARAMIN SON İKİ HANESİ 35 OLDUĞU İÇİN DÖNGÜ 35'E KADAR İLERLİYOR.
#     if j > 1:
#         for i in range(2,j):
#             if (j % i == 0):
#
#                 break
#
#         else:
#             dizi.append(j)
#
#             print(dizi)
# print("1 ile öğrenci numaram olan 35 sayısı arasında olan tüm asal sayılar list biçiminde diziye eklenmiştir.")
