immutable_var = 1,2,3,True,'name'
print(immutable_var)
# immutable_var[0] = 4 кортеж нельзя менять т.к. он не поддерживается на Pyton
mutable_list = [1,2,3,'Gregory',False]
print(mutable_list)
mutable_list[1] = 5
print(mutable_list)