import matplotlib.pyplot as plt
import numpy as np

dict_races = {}
dict_race_count_mr_sr = {}#list for each race - 0idx - count of SR, 1 idx - count of MR

count_mr = 0
# with open('pat_don_mr_high_geno_races.csv') as in_f:
with open('new_data_geno.txt') as in_f:
    for line in in_f:
        line = line.strip().split(',')
        race1 = line[2]
        race2 = line[3]

        races = [race1, race2]
        if race1 != race2:
            if race1 in dict_race_count_mr_sr:
                dict_race_count_mr_sr[race1][1] +=1
            else:
                dict_race_count_mr_sr[race1] = [0,1]

            if race2 in dict_race_count_mr_sr:
                dict_race_count_mr_sr[race2][1] += 1
            else:
                dict_race_count_mr_sr[race2] = [0, 1]

            count_mr +=1
        else:
            if race1 in dict_race_count_mr_sr:
                dict_race_count_mr_sr[race1][0] += 1
                #dict_race_count_mr_sr[race1] += 1
            else:
                dict_race_count_mr_sr[race1] = [1, 0]
                #dict_race_count_mr_sr[race1] = 1
        races = ('_').join(sorted(races))

        dict_races[races] = dict_races.get(races, 0) + 1



print(count_mr)
print(len(dict_races))

sorted_dict_races = sorted(dict_races.items(), key=lambda kv: kv[1], reverse=True)
sorted_dict = sorted(dict_race_count_mr_sr.items(), key=lambda kv: kv[1], reverse=True)
sum = 0

x, y = [], []
v1, v2 = [],[]

for key, val in sorted_dict:
    value = val[0]+val[1]
    x.append(key)
    y.append(value)
    v1.append(val[0])
    v2.append(val[1])

    print(key + '-  ' + str(val))
    sum += val[0]

# #mr_sr_plot
# plt.figure()
# plt.bar(x, v1, color='royalblue', label='sr')
# plt.bar(x, v2, color='silver',  label='mr', bottom=v1)
# plt.xticks(np.arange(len(sorted_dict)), x, rotation='vertical',fontsize=7)
# plt.yticks(fontsize=7)
# plt.ylabel('Number in category')
# plt.xlabel('Races')
# plt.title('Number of individuals per race')
# plt.legend()
# plt.tight_layout()
# plt.show()
# print(sum)


plt.figure()
plt.bar(x, y,color='royalblue', label='sr')
plt.xticks(np.arange(len(sorted_dict)), x, rotation='vertical',fontsize=7)
plt.yticks(fontsize=7)
plt.ylabel('Number in category')
plt.xlabel('Races')
plt.title('Number of individuals per race')
plt.legend()
plt.tight_layout()
plt.show()
print(sum)
