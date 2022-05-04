# Youtube_Cut Dataset

## Video
```
- x_path = 'drive/MyDrive/AIHealthcare/AIcare_Phrase1/data/season2/file_v1/videos/' 
- x_path (google drive) = https://drive.google.com/drive/folders/1VuT2s3YTh8Gv5UQtt49_mO5A_y40b2G3?usp=sharing
	[
	'face1_01.mp4', 'face1_02.mp4', 'face1_03.mp4', 'face1_04.mp4', 'face1_05.mp4',
	'face2_01.mp4', 'face2_02.mp4', 'face4.mp4', 'face5_01.mp4', 'face5_02.mp4', 'face5_03.mp4',
	'face6_01.mp4', 'face6_02.mp4', 'face7_01.mp4', 'face7_02.mp4',
	'face9_1.mp4', 'face9_2.mp4', 'face9_3.mp4', 'face9_4.mp4', 'face9_5.mp4','face10_01.mp4', 'face10_02.mp4',
	'ClubFridayShow2.mp4', 'Club_Friday_Show.mp4', 'Love_in_Depression.mp4'
	 ]
```
```
- y_path = 'drive/MyDrive/AIHealthcare/AIcare_Phrase1/data/season2/file_v1/videos/'
- y_path (google drive) = https://drive.google.com/drive/folders/1D37sGYg91EiQ5HY4Nqr8vAQ6XIIb1pY9?usp=sharing		 	 
- y = [
	'face1_01.csv', 'face1_02.csv','face1_03.csv','face1_04.csv','face1_05.csv',
	'face2_01.csv','face2_02.csv','face4.csv','face5_01.csv','face5_02.csv','face5_03.csv',
	'face6_01.csv','face6_02.csv','face7_01.csv','face7_02.csv',
	'face9_1.csv','face9_2.csv','face9_3.csv','face9_4.csv','face9_5.csv','face10_01.csv','face10_02.csv',
	'Club_Friday_Show_dow.csv', 'Club_Friday_Show_pat.csv', 'Love_in_Depression.csv'
	]
```
				
## Code
	- Youtube_cut_corpus.ipynb : https://colab.research.google.com/drive/165qJ-q3Ai2dgxSJWA-pdHvIzlm3MNOtx?usp=sharing
	
<style scoped> table {font-size: 13px;} </style>

## Table1
| no.  | Video  | lebel | shape | frames | FPS | 
| :---:| :---: | :---: | :---: | :---: | :---: |
|  0  |  ClubFridayShow2.mp4  |  Club_Friday_Show_dow.csv  |  (19, 2)  |  7900  |  25  |
|  1  |  Club_Friday_Show.mp4  |  Club_Friday_Show_pat.csv  |  (79, 2)  |  28010  |  25  |
|  2  |  Love_in_Depression.mp4  |  Love_in_Depression.csv  |  (80, 2)  |  57017  |  25  |
|  3  |  face10_01.mp4  |  face10_01.csv  |  (91, 4)  |  27503  |  25  |
|  4  |  face10_02.mp4  |  face10_02.csv  |  (109, 4)  |  24843  |  29  |
|  5  |  face1_01.mp4  |  face1_01.csv  |  (14, 4)  |  14547  |  25  |
|  6  |  face1_02.mp4  |  face1_02.csv  |  (13, 4)  |  22999  |  50  |
|  7  |  face1_03.mp4  |  face1_03.csv  |  (22, 4)  |  17293  |  25  |
|  8  |  face1_04.mp4  |  face1_04.csv  |  (43, 4)  |  9845  |  25  |
|  9  |  face1_05.mp4  |  face1_05.csv  |  (59, 4)  |  10753  |  23  |
|  10  |  face2_01.mp4  |  face2_01.csv  |  (152, 4)  |  93229  |  59  |
|  11  |  face2_02.mp4  |  face2_02.csv  |  (74, 4)  |  40131  |  50  |
|  12  |  face4.mp4  |  face4.csv  |  (204, 4)  |  54752  |  25  |
|  13  |  face5_01.mp4  |  face5_01.csv  |  (154, 4)  |  57856  |  50  |
|  14  |  face5_02.mp4  |  face5_02.csv  |  (72, 4)  |  290084  |  60  |
|  15  |  face5_03.mp4  |  face5_03.csv  |  (5, 4)  |  16831  |  25  |
|  16  |  face6_01.mp4  |  face6_01.csv  |  (108, 4)  |  15216  |  25  |
|  17  |  face6_02.mp4  |  face6_02.csv  |  (228, 4)  |  35480  |  25  |
|  18  |  face7_01.mp4  |  face7_01.csv  |  (211, 4)  |  28211  |  25  |
|  19  |  face7_02.mp4  |  face7_02.csv  |  (10, 4)  |  5781  |  25  |
|  20  |  face9_1.mp4  |  face9_1.csv  |  (29, 4)  |  11288  |  29  |
|  21  |  face9_2.mp4  |  face9_2.csv  |  (21, 4)  |  14162  |  50  |
|  22  |  face9_3.mp4  |  face9_3.csv  |  (27, 4)  |  6414  |  25  |
|  23  |  face9_4.mp4  |  face9_4.csv  |  (81, 4)  |  16307  |  25  |
|  24  |  face9_5.mp4  |  face9_5.csv  |  (22, 4)  |  8864  |  25  |

## Table2
| no.  | Video  | lebel | 
| :---:| :---: | :---: | 
|  0  |  ClubFridayShow2  |  ['neutral' 'sad']  |
|  1  |  Club_Friday_Show  |  ['sad' 'angry' 'neutral' 'relax' 'happy']  |
|  2  |  Love_in_Depression  |  ['neutral' 'angry' 'sad' 'relax' 'happy']  |
|  3  |  face10_01  |  ['sad' 'neutral' 'angry' 'relax' 'happy']  |
|  4  |  face10_02  |  ['happy' 'neutral' 'relax' 'angry' 'sad']  |
|  5  |  face1_01  |  ['neutral' 'happy' 'angry']  |
|  6  |  face1_02  |  ['neutral' 'angry' 'happy']  |
|  7  |  face1_03  |  ['angry' 'sad' 'neutral' 'relax' 'happy']  |
|  8  |  face1_04  |  ['happy' 'relax' 'neutral' 'angry' 'sad']  |
|  9  |  face1_05  |  ['neutral' 'happy' 'angry' 'relax']  |
|  10  |  face2_01  |  ['neutral' 'relax' 'angry' 'happy' 'sad']  |
|  11  |  face2_02  |  ['happy' 'relax' 'neutral' 'angry']  |
|  12  |  face4  |  ['happy' 'relax' 'neutral' 'angry' 'sad']  |
|  13  |  face5_01  |  ['happy' 'relax' 'angry' 'sad' 'neutral']  |
|  14  |  face5_02  |  ['neutral' 'happy' 'angry' 'relax']  |
|  15  |  face5_03  |  ['angry' 'sad']  |
|  16  |  face6_01  |  ['relax' 'happy' 'neutral' 'angry' 'sad']  |
|  17  |  face6_02  |  ['neutral' 'relax' 'happy' 'angry' 'sad']  |
|  18  |  face7_01  |  ['happy' 'angry' 'neutral' 'relax']  |
|  19  |  face7_02  |  ['neutral' 'relax']  |
|  20  |  face9_1  |  ['neutral' 'happy' 'relax']  |
|  21  |  face9_2  |  ['relax' 'neutral' 'angry' 'happy']  |
|  22  |  face9_3  |  ['neutral' 'relax' 'angry' 'happy']  |
|  23  |  face9_4  |  ['neutral' 'happy' 'angry' 'relax' 'sad']  |
|  24  |  face9_5  |  ['neutral' 'angry' 'relax' 'happy']  |