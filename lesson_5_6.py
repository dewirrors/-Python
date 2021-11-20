#Не работает...
with open("task_6.txt") as subjs:
    subjs_list = subjs.readlines()
    subjs_dict = {}
    for subj in subjs_list:
        val_list = subjs.split()
        hs = 0

        for el in val_list:
            num = '0'

            for i in el:

                if i.isdigit():
                    num += i
                else:
                    break

            hs += int(num)
        subjs_dict.update({val_list[0] : hs})

print(subjs_dict)
