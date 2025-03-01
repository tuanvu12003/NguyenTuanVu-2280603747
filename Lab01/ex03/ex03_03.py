def tao_tuple_tulist(lst):
    return tuple(lst)
input_list = input("Nhap danh sach cac so cach nhau bang dau phay: ")
nums = list(map(int, input_list.split(', ')))
my_tuple = tao_tuple_tulist(nums)
print("List", nums)
print("Tuple tu List", my_tuple)