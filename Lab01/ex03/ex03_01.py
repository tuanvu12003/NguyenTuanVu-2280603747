def tinhtongsochan(lst):
    tong = 0
    for item in lst:
        if item % 2 == 0:
            tong += item
        return tong
input_list = input("Nhap danh sach cac so cach nhau bang dau phay: ")
nums = list(map(int, input_list.split(', ')))
tongchan = tinhtongsochan(nums)
print("tong cac so chan trong list la: ", tongchan)
            