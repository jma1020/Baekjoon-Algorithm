s = input().upper()
compress_s = list(set(s))
count_list = [s.count(i) for i in compress_s]
 
if count_list.count(max(count_list)) > 1:
    print('?')
else:
    print(compress_s[count_list.index(max(count_list))])
