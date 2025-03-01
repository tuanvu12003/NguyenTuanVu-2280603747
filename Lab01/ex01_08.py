def chiahetcho_5(sonhiphan):
    sothapphan = int(sonhiphan, 2)
    if sothapphan % 5 ==0:
        return True
    else:
        return False
chuoisonhiphan = input("Nhap chuoi so nhi phan (phan tach boi dau phay): ")
sonhiphanList = chuoisonhiphan.split(', ')
sochiahetcho_5 = [so for so in sonhiphanList if chiahetcho_5(so)]
if len(sochiahetcho_5) > 0:
    ketqua = ', '.join(sochiahetcho_5)
    print("Cac so nhi phan chia het cho 5 la: ", ketqua)
else:
    print("Khong co so nhi phan nao chia het cho 5 trong chuoi da nhap!!!")