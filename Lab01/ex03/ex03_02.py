def daonguoc (lst):
    return lst[::-1]
input_list = input("Nhap danh sach cac so cach nhau bang dau phay: ")
nums = list(map(int, input_list.split(', ')))
list_daonguoc = daonguoc(nums)
print("List dao nguoc la: ", list_daonguoc)