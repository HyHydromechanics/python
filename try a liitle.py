# coding=utf-8

strli = "kaka is li is da is wei !"


def split_li(sep_li, find_li, str_li):
    last = ""
    list_li = []
    strsplit = str_li.split(sep_li)
    for sp in strsplit:
        if last == find_li:
            list_li.append(sp)
        last = sp
    return list_li


sep_li = ' '
find_li = 'is'
str_li = strli
return_list = []

return_list = split_li(sep_li, find_li, str_li)
print(return_list)