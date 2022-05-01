## merge classes
# convert = { 'happy':'positive-active', 'relax':'positive-deactive', 'neutral':'neutral', 'angry':'negative-active', 'stress':'negative-active', 'sad':'negative-deactive',}
class1 = ['happy', 'relax', 'neutral', 'angry', 'stress', 'sad']
class2 = ['positive-active', 'positive-deactive', 'neutral', 'negative-active', 'negative-active', 'negative-deactive'] #full word
class3 = ['pos-act', 'pos-deact', 'neutral', 'neg-act', 'neg-act', 'neg-deact'] #short word

for i in range(len(x_name)):
  # y_test = np.load(path_y+y_name[i])
  y_test = np.load(path_y+y_name[i]).astype('<U32')
  print(y_name[i][:-4]+'=', pd.unique(y_test))

  for j in range(len(class1)):
    y_test[y_test == class1[j]] = class3[j]
    y_test[y_test == class2[j]] = class3[j]
    # np.place(y_test, y_test==class1[j], class2[j])
  np.save(path_y+y_name[i][:-4]+'_pn.npy', y_test)
  print(y_name[i][:-4]+'=', pd.unique(y_test))
  print(" ")
  
  
  
## convert from str to numerical

# !ls 'drive/MyDrive/tech_vdo/csv/numpy/new_class_name/'
path = 'drive/MyDrive/tech_vdo/csv/numpy/new_class_name/'
filenames =['face001.npy', 'face002.npy', 'face003.npy', 'face004.npy', 'face005.npy', 'face006.npy', 'face007.npy', 'face008.npy', 'pilot01.npy', 'pilot02.npy', 'pilot03.npy', 'pilot04.npy', 'pilot05.npy']

convert = {'pos-act':0, 'pos-deact':1, 'neutral':2, 'neg-act':3, 'neg-deact':4}
for filename in filenames:
  y = np.load(path+filename)
  for key, value in convert.items():
    # np.place(y, y==key, value)
    y[y == key] = value
  y = y.astype(int)
  print(filename[:-4]+'=', pd.unique(y))
  np.save(path+filename[:-4]+'_int.npy', y)
  
  
 
# y_test[y_test == 'happy'] = 'positive-active'
# y_test[y_test == 'relax'] = 'positive-deactive'
# y_test[y_test == 'neutral'] = 'neutral'
# y_test[y_test == 'angry'] = 'negative-active'
# y_test[y_test == 'stress'] = 'negative-active'
# y_test[y_test == 'sad'] = 'negative-deactive'

# face001 = ['neutral', 'happy', 'sad', 'angry', 'stress', 'relax']
# face002 = ['neutral', 'stress','happy','sad','relax','angry']
# face003 = ['stress','sad','neutral','happy','relax','angry']
# face004 = ['neutral','happy','relax','stress','sad','angry']
# face005 = ['negative-deactive','positive-deactive','positive-active','neutral','negative-active']
# face006 = ['neutral','stress','sad','relax','happy','angry']
# face007 = ['neutral','stress','happy','relax','sad','angry']
# face008 = ['neutral','positive-deactive','positive-active','negative-active','negative-deactive']
# pilot01 = ['positive-active','positive-deactive','negative-deactive','neutral','negative-active']
# pilot02 = ['positive-deactive','neutral','negative-deactive','positive-active','negative-active']
# pilot03 = ['negative-deactive','positive-deactive','negative-active','positive-active','neutral']
# pilot04 = ['negative-deactive','positive-deactive','positive-active','negative-active']
# pilot05 = ['negative-deactive','neutral','positive-deactive','positive-active','negative-active']

#dic_con = {'happy':'positive-active', 'relax':'positive-deactive', 'neutral':'neutral','angry':'negative-active', 'stress':'negative-active','sad':'negative-deactive',}

## print show int classes
# # !ls 'drive/MyDrive/tech_vdo/csv/numpy/new_class_name/int_class/'
# path = 'drive/MyDrive/tech_vdo/csv/numpy/new_class_name/int_class/'
# y_name =['face001.npy', 'face002.npy', 'face003.npy', 'face004.npy', 'face005.npy', 'face006.npy', 'face007.npy', 'face008.npy', 'pilot01.npy', 'pilot02.npy', 'pilot03.npy', 'pilot04.npy', 'pilot05.npy']

# for i in range(len(y_name)):
#   y = np.load(path+y_name[i])
#   print(y_name[i][:-4]+'=', pd.unique(y))

### backup 1
# path_x, path_y = 'drive/MyDrive/tech_own/x_data_team/', 'drive/MyDrive/tech_vdo/csv/numpy/'
# x_name = ['face001.npy', 'face002.npy', 'face003.npy', 'face004.npy', 'face005.npy', 'face006.npy', 'face007.npy', 'face008.npy', 'pilot01.npy', 'pilot02.npy', 'pilot03.npy', 'pilot04.npy', 'pilot05.npy']
# y_name = x_name
# ### print show shape 
# # for i in range(len(x_name)):
# #   x_test, y_test = np.load(path_x+x_name[i]), np.load(path_y+y_name[i])
# #   print('x_test: ', x_test.shape, '| y_test: ', y_test.shape)

### backup 2
# # !ls 'drive/MyDrive/tech_vdo/csv/numpy/'
# # filenames =['face001.npy', 'face002.npy', 'face003.npy', 'face004.npy', 'face005.npy', 'face006.npy', 'face007.npy', 'face008.npy', 'pilot01.npy', 'pilot02.npy', 'pilot03.npy', 'pilot04.npy', 'pilot05.npy']
# !ls 'drive/MyDrive/tech_own/x_data_team/'
# filenames =['face001.npy', 'face002.npy', 'face003.npy', 'face004.npy', 'face005.npy', 'face006.npy', 'face007.npy', 'face008.npy', 'pilot01.npy', 'pilot02.npy', 'pilot03.npy', 'pilot04.npy', 'pilot05.npy']

### backup 3
# # psy_team_pathy_v1 = 'drive/MyDrive/tech_vdo/csv_psy/v1/numpy/' 
# # psy_team_pathy_v2 ='drive/MyDrive/tech_vdo/csv_psy/v2/numpy/'

# # data_team_pathy_v1 = 'drive/MyDrive/tech_own/data_dict/med/v3/numpy/'
# data_team_pathy_v2 = 'drive/MyDrive/tech_vdo/csv/numpy/' 
#   # filenames =['face001.npy', 'face002.npy', 'face003.npy', 'face004.npy', 'face005.npy', 'face006.npy', 'face007.npy', 'face008.npy', 'pilot01.npy', 'pilot02.npy', 'pilot03.npy', 'pilot04.npy', 'pilot05.npy']