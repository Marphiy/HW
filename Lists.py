winners_list_summ = int(input("Введите количество участников! :"))
i = 0
winners_list = []
while i < winners_list_summ:
       new_mem = input("Введите имя следующего участника! : ")
       winners_list.append(new_mem)
       i += 1
print(winners_list)
clr_last = input("Хотите удалить последнего участника? y/n :")
if clr_last == "y":
       winners_list.pop()
       print(winners_list)
clr_all = input("Хотите удалить всех участников? y/n :")
if clr_all == "y":
       winners_list.clear()
       print("Список пуст! {}".format(winners_list))


