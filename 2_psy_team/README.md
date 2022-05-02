## voting_dataset
	- path_ku : 'drive/MyDrive/tech_vdo/'
	- path_chula : 'drive/MyDrive/tech_own/'
	
## label
	### psy_team
	~~psy_team_pathy_v1 = 'drive/MyDrive/tech_vdo/csv_psy/v1/'~~
	- psy_team_pathy_v1 = 'drive/MyDrive/tech_vdo/csv_psy/v1/numpy/'
		- filenames = ['01.csv', '02.csv', '03.csv', '04.csv', '05.csv', '06.csv', '07.csv', '08.csv', 'pilot01.csv', 'pilot02.csv', 'pilot03.csv', 'pilot04.csv', 'pilot05.csv']
		- filenames =['01.npy', '02.npy', '03.npy', '04.npy', '05.npy', '06.npy', '07.npy', '08.npy', 'pilot01.npy', 'pilot02.npy', 'pilot03.npy', 'pilot04.npy', 'pilot05.npy']
	- psy_team_pathy_v2 = 'drive/MyDrive/tech_vdo/csv_psy/v2/' (filtered dataset)
	- psy_team_pathy_v2 ='drive/MyDrive/tech_vdo/csv_psy/v2/numpy/'
		- filenames = ['01_df.csv', '02_df.csv', '03_df.csv', '04_df.csv', '05_df.csv', '06_df.csv', '07_df.csv', '08_df.csv', 'pilot01_df.csv', 'pilot02_df.csv', 'pilot03_df.csv', 'pilot04_df.csv', 'pilot05_df.csv']
		- filenames =['01.npy', '02.npy', '03.npy', '04.npy', '05.npy', '06.npy', '07.npy', '08.npy', 'pilot01.npy', 'pilot02.npy', 'pilot03.npy', 'pilot04.npy', 'pilot05.npy']
## data shape
	- face001.npy, x:  (35442, 256, 256, 3),  y:  (35442,)
	- face002.npy, x:  (40428, 256, 256, 3),  y:  (40428,)
	- face003.npy, x:  (13245, 256, 256, 3),  y:  (13245,)
	- face004.npy, x:  (47732, 224, 224, 3),  y:  (47732,)
	- face005.npy, x:  (14991, 126, 94, 3),    y:  (14991,)
	- face006.npy, x:  (32621, 224, 224, 3),  y:  (32621,)
	- face007.npy, x:  (47334, 224, 224, 3),  y:  (47334,)
	- face008.npy, x:  (23840, 134, 98, 3),   y:  (23840,)
	- pilot01.npy, x:  (13089, 224, 224, 3),   y:  (13089,)
	- pilot02.npy, x:  (14831, 150, 150, 3),   y:  (14831,)
	- pilot03.npy, x:  (40041, 150, 150, 3),   y:  (40041,)
	- pilot04.npy, x:  (12491, 150, 150, 3),   y:  (12491,)
	- pilot05.npy, x:  (16156, 150, 150, 3),   y:  (16156,)

## data class
	- face001 = ['neutral', 'happy', 'sad', 'angry', 'stress', 'relax']
	- face002 = ['neutral', 'stress','happy','sad','relax','angry']
	- face003 = ['stress','sad','neutral','happy','relax','angry']
	- face004 = ['neutral','happy','relax','stress','sad','angry']
	- face005 = ['negative-deactive','positive-deactive','positive-active','neutral','negative-active']
	- face006 = ['neutral','stress','sad','relax','happy','angry']
	- face007 = ['neutral','stress','happy','relax','sad','angry']
	- face008 = ['neutral','positive-deactive','positive-active','negative-active','negative-deactive']
	- pilot01 = ['positive-active','positive-deactive','negative-deactive','neutral','negative-active']
	- pilot02 = ['positive-deactive','neutral','negative-deactive','positive-active','negative-active']
	- pilot03 = ['negative-deactive','positive-deactive','negative-active','positive-active','neutral']
	- pilot04 = ['negative-deactive','positive-deactive','positive-active','negative-active']
	- pilot05 = ['negative-deactive','neutral','positive-deactive','positive-active','negative-active']

## Convert
	- {'happy':'positive-active', 'relax':'positive-deactive', 'neutral':'neutral', 'angry':'negative-active', 'stress':'negative-active','sad':'negative-deactive'}
	- {'happy':'pos-act','relax':'pos-deact', 'neutral':'neutral','angry':'neg-act', 'stress':'neg-act','sad':'neg-deact'}
	- convert1 = {'pos-act':0, 'pos-deact':1, 'neutral':2, 'neg-act':3, 'neg-deact':4}
	- convert2 = {'pos-act':1, 'pos-deact':3, 'neutral':2, 'neg-act':0, 'neg-deact':4} #res50
	- convert = {0:'angry', 1:'happy', 2:'neutral', 3:'relax', 4:'sad'}
	- convert = {'happy':0, 'relax':1, 'neutral':2, 'angry':3, 'sad':4}
 
## new class
	- path = 'drive/MyDrive/tech_vdo/csv/numpy/new_class_name/'
	- face001= ['neutral' 'pos-act' 'neg-deact' 'neg-act' 'pos-deact']
	- face002= ['neutral' 'neg-act' 'pos-act' 'neg-deact' 'pos-deact']
	- face003= ['neg-act' 'neg-deact' 'neutral' 'pos-act' 'pos-deact']
	- face004= ['neutral' 'pos-act' 'pos-deact' 'neg-act' 'neg-deact']
	- face005= ['neg-deact' 'pos-deact' 'pos-act' 'neutral' 'neg-act']
	- face006= ['neutral' 'neg-act' 'neg-deact' 'pos-deact' 'pos-act']
	- face007= ['neutral' 'neg-act' 'pos-act' 'pos-deact' 'neg-deact']
	- face008= ['neutral' 'pos-deact' 'pos-act' 'neg-act' 'neg-deact']
	- pilot01= ['pos-act' 'pos-deact' 'neg-deact' 'neutral' 'neg-act']
	- pilot02= ['pos-deact' 'neutral' 'neg-deact' 'pos-act' 'neg-act']
	- pilot03= ['neg-deact' 'pos-deact' 'neg-act' 'pos-act' 'neutral']
	- pilot04= ['neg-deact' 'pos-deact' 'pos-act' 'neg-act']
	- pilot05= ['neg-deact' 'neutral' 'pos-deact' 'pos-act' 'neg-act']

## int class
	- path = 'drive/MyDrive/tech_vdo/csv/numpy/new_class_name/int_class/convert1/'
	- path = 'drive/MyDrive/tech_vdo/csv/numpy/new_class_name/int_class/convert2/'
	- ![alt text](https://github.com/[username]/[reponame]/blob/[branch]/image.jpg?raw=true)
	- face001= [2 0 4 3 1]
	- face002= [2 3 0 4 1]
	- face003= [3 4 2 0 1]
	- face004= [2 0 1 3 4]
	- face005= [4 1 0 2 3]
	- face006= [2 3 4 1 0]
	- face007= [2 3 0 1 4]
	- face008= [2 1 0 3 4]
	- pilot01= [0 1 4 2 3]
	- pilot02= [1 2 4 0 3]
	- pilot03= [4 1 3 0 2]
	- pilot04= [4 1 0 3]
	- pilot05= [4 2 1 0 3]

## implementation
	- x_train = 'drive/MyDrive/tech_own/x_data_team/' 
		- filenames =['face001.npy', 'face002.npy', 'face003.npy', 'face004.npy', 'face005.npy', 'face006.npy', 'face007.npy', 'face008.npy', 'pilot01.npy', 'pilot02.npy', 'pilot03.npy', 'pilot04.npy', 'pilot05.npy']
	- y_train = 'drive/MyDrive/tech_vdo/csv/numpy/new_class_name/int_class/convert2/'
		- filenames =['face001.npy', 'face002.npy', 'face003.npy', 'face004.npy', 'face005.npy', 'face006.npy', 'face007.npy', 'face008.npy', 'pilot01.npy', 'pilot02.npy', 'pilot03.npy', 'pilot04.npy', 'pilot05.npy']
		
	