from buildHaar import buildplot, haar
from optimizationMethod import search_extremum_point_method
from plotChart import plot_chart
from statistics import init_file_os
from statistics import close_file_os
from statistics import print_statistics_table_in_file_header

data = buildplot(17,1,[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
print(data)

# (point, vec3_for_plot) = search_extremum_point_method(data)
# plot_chart(data, vec3_for_plot)
# plotVec = []
# try:
#     init_file_os()
#     print_statistics_table_in_file_header()
#     pos_in_exel = 2
#     for h in range(2,11,1): # 60
#         # print(pos_in_exel)
#         for i in range(1,63,1):
#             (point, vec3_for_plot) = search_extremum_point_method(pos_in_exel, i, h, data)
#             # plot_chart(data, vec3_for_plot, i, h)
#             # plotVec.append((data, vec3_for_plot, i, h))
#             pos_in_exel += 1
#         # print(pos_in_exel)
#         # print(i)
#         # print(h)
    

#     # print(pos_in_exel)
#     close_file_os(pos_in_exel)
# except FileExistsError:
#     print(FileExistsError)
