# import os
# import sys
#
# def list_files():
#     result = []
#     for item in os.listdir():
#         if os.path.isfile(item):
#             result.append(item)
#     return result
#
#
#
# def list_directories():
#     resul = []
#     for i in os.listdir(os.path.join(os.getcwd())):
#         if os.path.isdir(i):
#             resul.append(i)
#     return resul
#
# # resul = []
# # for i in os.listdir(os.path.join(os.getcwd())):
# #     if os.path.isdir(i):
# #         resul.append(i)
# # print(resul)
#
#
# print(list_files())
#
# print(list_directories())
#
# print(sys.platform)
# print(sys.path)

def shopping_history():  # функция печатает историю покупок из двух списков: названий товара и цен
    dict_history = dict(zip(history_item, history_price))
    print('История покупок: ', dict_history)