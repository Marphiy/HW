winners_list_summ = int(input("Введите количество участников! :"))
i = 0
winners_list = []
while i < winners_list_summ:
       new_mem = input("Введите имя следующего участника! : ")
       winners_list.append(new_mem)
       i += 1
print(winners_list)


