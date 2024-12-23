# 1-savol

# def counter():
#     count = 0
#     def ichki():
#         nonlocal count
#         count += 1
#         return count
#     return ichki
# counter1 = counter()
# print(counter1())
# print(counter1())


# 2-savol

# def son(a):
#     def royxat(b):
#         return [i for i in b if i > a]
#     return royxat
# son1 = son(5)
# print(son1([2,4,6,1,8]))
# print(son1([1,0,8]))


# 3-savol

# def math_operation(a,b):
#     def son(c):
#         if b == 'add':
#             return a+c
#         elif b == 'subtract':
#             return a-c
#         elif b == 'multiply':
#             return a*c
#         elif b == 'divide':
#             return a/c
#         else:
#             return f"Bunaqa amal mavjud emas!!!"
#     return son
# math = math_operation(10, 'add')
# math1 = math_operation(20, 'subtract')
# math2 = math_operation(30, 'multiply')
# math3 = math_operation(40, 'divide')
# math4 = math_operation(50, 'ayirish')
# print(math(1))
# print(math1(2))
# print(math2(3))
# print(math3(4))
# print(math4(5))


# 4-savol


# def toplamni_filtrlash(turi):
#     def filter_func(sonlar):
#         if turi == 'juft':
#             return [i for i in sonlar if i % 2 == 0]
#         elif turi == 'toq':
#             return [i for i in sonlar if i % 2 != 0]
#         else:
#             return []
#     return filter_func
# juft = toplamni_filtrlash('juft')
# toq = toplamni_filtrlash('toq')
# print(juft([2, 3, 8]))
# print(toq([2, 3, 8]))


# 5-savol


# def tekshirish(turi):
#     def filter_func(sonlar):
#         if turi == 'polindrom':
#             return [i for i in sonlar if i % 10 == i // 100]
#         elif turi == 'polindrom_bolmagan':
#             return [i for i in sonlar if i % 10 != i // 100]
#         else:
#             return []
#     return filter_func
#
# polindrom = tekshirish('polindrom')
# polindrom_bolmagan = tekshirish('polindrom_bolmagan')
#
# print(polindrom([121, 3, 282]))
# print(polindrom_bolmagan([121, 3, 8]))


# 6-savol


# def tekshirish(turi):
#     def tub_tekshir(son):
#         if son <= 1:
#             return False
#         for d in range(2, int(son ** 0.5) + 1):
#             if son % d == 0:
#                 return False
#         return True
#     def filter_func(sonlar):
#         if turi == 'tub':
#             return [i for i in sonlar if tub_tekshir(i)]
#         elif turi == 'murakkab_bolmagan':
#             return [i for i in sonlar if not tub_tekshir(i)]
#         else:
#             return []
#     return filter_func
#
# tub = tekshirish('tub')
# murakkab_bolmagan = tekshirish('murakkab_bolmagan')
# print(tub([2, 3, 4, 5, 9, 11, 15]))
# print(murakkab_bolmagan([2, 3, 4, 5, 9, 11, 15]))





# def daraja(x):
#     def sonlar(y):
#         return y ** x
#     return sonlar
#
# a = daraja(2)
# print(a(5))



# def til(a):
#     def ism(b):
#         if a == 'en':
#             return f"Hello {b}"
#         elif a == 'uz':
#             return f"Salom {b}"
#         else:
#             return f"Tilni uz yoki en yozing!!!"
#     return ism
#
# uz = til('uz')
# en = til('en')
# boshqa = til('boshqa')
#
# print(uz("Feruzjon"))
# print(en("Feruzjon"))
# print(boshqa("Feruzjon"))


