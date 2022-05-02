## voting_dataset
	- path_ku : 'drive/MyDrive/tech_vdo/'
	- path_chula : 'drive/MyDrive/tech_own/'
	
## label
	### psy_team
	- psy_team_pathy_v1 = 'drive/MyDrive/tech_vdo/csv_psy/v1/'
	- psy_team_pathy_v1 = 'drive/MyDrive/tech_vdo/csv_psy/v1/numpy/'
		- filenames = ['01.csv', '02.csv', '03.csv', '04.csv', '05.csv', '06.csv', '07.csv', '08.csv', 'pilot01.csv', 'pilot02.csv', 'pilot03.csv', 'pilot04.csv', 'pilot05.csv']
		- filenames =['01.npy', '02.npy', '03.npy', '04.npy', '05.npy', '06.npy', '07.npy', '08.npy', 'pilot01.npy', 'pilot02.npy', 'pilot03.npy', 'pilot04.npy', 'pilot05.npy']
	- psy_team_pathy_v2 = 'drive/MyDrive/tech_vdo/csv_psy/v2/' (filtered dataset)
	- psy_team_pathy_v2 ='drive/MyDrive/tech_vdo/csv_psy/v2/numpy/'
		- filenames = ['01_df.csv', '02_df.csv', '03_df.csv', '04_df.csv', '05_df.csv', '06_df.csv', '07_df.csv', '08_df.csv', 'pilot01_df.csv', 'pilot02_df.csv', 'pilot03_df.csv', 'pilot04_df.csv', 'pilot05_df.csv']
		- filenames =['01.npy', '02.npy', '03.npy', '04.npy', '05.npy', '06.npy', '07.npy', '08.npy', 'pilot01.npy', 'pilot02.npy', 'pilot03.npy', 'pilot04.npy', 'pilot05.npy']
		
## data shape
	- 01.npy, x: (34179, 256, 256, 3) y: (34179,)
	- 02.npy, x: (47202, 224, 224, 3) y: (47202,)
	- 03.npy, x: (12237, 224, 224, 3) y: (12237,)
	- 04.npy, x: (49213, 224, 224, 3) y: (49213,)
	- 05.npy, x: (18933, 126, 94, 3) y: (18933,)
	- 06.npy, x: (31553, 224, 224, 3) y: (31553,)
	- 07.npy, x: (61993, 224, 224, 3) y: (61993,)
	- 08.npy, x: (21672, 134, 98, 3) y: (21672,)
	- pilot01.npy, x: (15707, 224, 224, 3) y: (15707,)
	- pilot02.npy, x: (14731, 150, 150, 3) y: (14731,)
	- pilot03.npy, x: (31451, 150, 150, 3) y: (31451,)
	- pilot04.npy, x: (11870, 150, 150, 3) y: (11870,)
	- pilot05.npy, x: (9100, 150, 150, 3) y: (9100,)

## data class
	- 01 =  ['angry' 'happy' 'neutral' 'relax' 'sad' 'stress']
	- 02 =  ['angry' 'happy' 'neutral' 'relax' 'sad' 'stress']
	- 03 =  ['angry' 'happy' 'neutral' 'relax' 'sad' 'stress']
	- 04 =  ['angry' 'happy' 'neutral' 'relax' 'sad' 'stress']
	- 05 =  ['negative-active' 'negative-deactive' 'neutral' 'positive-active' 'positive-deactive']
	- 06 =  ['angry' 'happy' 'neutral' 'relax' 'sad' 'stress']
	- 07 =  ['angry' 'happy' 'neutral' 'relax' 'sad' 'stress']
	- 08 =  ['negative-active' 'negative-deactive' 'neutral' 'positive-active' 'positive-deactive']
	- pilot01 = ['negative-active' 'negative-deactive' 'neutral' 'positive-active' 'positive-deactive']
	- pilot02 = ['negative-active' 'negative-deactive' 'neutral' 'positive-active' 'positive-deactive']
	- pilot03 = ['negative-active' 'negative-deactive' 'neutral' 'positive-active' 'positive-deactive']
	- pilot04 = ['negative-active' 'negative-deactive' 'neutral' 'positive-active' 'positive-deactive']
	- pilot05 = ['negative-active' 'negative-deactive' 'neutral' 'positive-active' 'positive-deactive']

## Convert
	- {'happy':'positive-active', 'relax':'positive-deactive', 'neutral':'neutral', 'angry':'negative-active', 'stress':'negative-active','sad':'negative-deactive'}
	- {'happy':'pos-act','relax':'pos-deact', 'neutral':'neutral','angry':'neg-act', 'stress':'neg-act','sad':'neg-deact'}
	- convert1 = {'pos-act':0, 'pos-deact':1, 'neutral':2, 'neg-act':3, 'neg-deact':4}
	- convert2 = {'pos-act':1, 'pos-deact':3, 'neutral':2, 'neg-act':0, 'neg-deact':4} #res50
	- convert = {0:'angry', 1:'happy', 2:'neutral', 3:'relax', 4:'sad'}
	- convert = {'happy':0, 'relax':1, 'neutral':2, 'angry':3, 'sad':4}
 
## new class
	- path = 'https://drive.google.com/drive/folders/1cNJ1ktbUMQFe0knqZgxLCfKJkLVO3OJK?usp=sharing
	- path = 'drive/MyDrive/tech_vdo/csv_psy/v2/new_class_name/'
	- 01 = ['neutral' 'pos-deact' 'neg-act' 'pos-act' 'neg-deact']
	- 02 = ['neutral' 'neg-act' 'neg-deact' 'pos-deact' 'pos-act']
	- 03 = ['neg-act' 'neutral' 'pos-deact' 'pos-act' 'neg-deact']
	- 04 = ['neutral' 'pos-deact' 'neg-deact' 'pos-act' 'neg-act']
	- 05 = ['pos-deact' 'neg-deact' 'neutral' 'neg-act' 'pos-act']
	- 06 = ['neg-deact' 'neg-act' 'neutral' 'pos-deact' 'pos-act']
	- 07 = ['neutral' 'pos-act' 'pos-deact' 'neg-deact' 'neg-act']
	- 08 = ['neutral' 'pos-deact' 'pos-act' 'neg-deact' 'neg-act']
	- pilot01 = ['pos-act' 'pos-deact' 'neg-deact' 'neg-act' 'neutral']
	- pilot02 = ['neutral' 'neg-act' 'pos-deact' 'neg-deact' 'pos-act']
	- pilot03 = ['neutral' 'neg-deact' 'pos-deact' 'pos-act' 'neg-act']
	- pilot04 = ['neutral' 'neg-deact' 'pos-act' 'neg-act' 'pos-deact']
	- pilot05 = ['neutral' 'neg-act' 'pos-act' 'neg-deact' 'pos-deact']

## int64 class
	- path = 'drive/MyDrive/tech_vdo/csv_psy/v2/convert2/'
	- 01 = [2 3 0 1 4]
	- 02 = [2 0 4 3 1]
	- 03 = [0 2 3 1 4]
	- 04 = [2 3 4 1 0]
	- 05 = [3 4 2 0 1]
	- 06 = [4 0 2 3 1]
	- 07 = [2 1 3 4 0]
	- 08 = [2 3 1 4 0]
	- pilot01 = [1 3 4 0 2]
	- pilot02 = [2 0 3 4 1]
	- pilot03 = [2 4 3 1 0]
	- pilot04 = [2 4 1 0 3]
	- pilot05 = [2 0 1 4 3]

## implementation
	- x_train = 'drive/MyDrive/tech_vdo/csv_psy/x_train/' 
		- filenames =['01.npy', '02_v1.npy', '03.npy', '04.npy', '05.npy', '06.npy', '07.npy', '08.npy', 'pilot01.npy', 'pilot02.npy', 'pilot03.npy', 'pilot04.npy', 'pilot05.npy']
	- y_train = 'drive/MyDrive/tech_vdo/csv_psy/v2/convert2/'
		- filenames =['01.npy', '02.npy', '03.npy', '04.npy', '05.npy', '06.npy', '07.npy', '08.npy', 'pilot01.npy', 'pilot02.npy', 'pilot03.npy', 'pilot04.npy', 'pilot05.npy']