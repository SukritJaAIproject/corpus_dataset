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
  