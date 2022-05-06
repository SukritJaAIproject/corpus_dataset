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
| :---:| :---: | :--- | 
|  0  |  ClubFridayShow2  |  ['neutral', 'sad']  |
|  1  |  Club_Friday_Show  |  ['angry', 'happy', 'neutral', 'relax', 'sad']  |
|  2  |  Love_in_Depression  |  ['angry', 'happy', 'neutral', 'relax', 'sad']  |
|  3  |  face10_01  |  ['angry', 'happy', 'neutral', 'relax', 'sad']  |
|  4  |  face10_02  |  ['angry', 'happy', 'neutral', 'relax', 'sad']  |
|  5  |  face1_01  |  ['angry', 'happy', 'neutral']  |
|  6  |  face1_02  |  ['angry', 'happy', 'neutral']  |
|  7  |  face1_03  |  ['angry', 'happy', 'neutral', 'relax', 'sad']  |
|  8  |  face1_04  |  ['angry', 'happy', 'neutral', 'relax', 'sad']  |
|  9  |  face1_05  |  ['angry', 'happy', 'neutral', 'relax']  |
|  10  |  face2_01  |  ['angry', 'happy', 'neutral', 'relax', 'sad']  |
|  11  |  face2_02  |  ['angry', 'happy', 'neutral', 'relax']  |
|  12  |  face4  |  ['angry', 'happy', 'neutral', 'relax', 'sad']  |
|  13  |  face5_01  |  ['angry', 'happy', 'neutral', 'relax', 'sad']  |
|  14  |  face5_02  |  ['angry', 'happy', 'neutral', 'relax']  |
|  15  |  face5_03  |  ['angry', 'sad']  |
|  16  |  face6_01  |  ['angry', 'happy', 'neutral', 'relax', 'sad']  |
|  17  |  face6_02  |  ['angry', 'happy', 'neutral', 'relax', 'sad']  |
|  18  |  face7_01  |  ['angry', 'happy', 'neutral', 'relax']  |
|  19  |  face7_02  |  ['neutral', 'relax']  |
|  20  |  face9_1  |  ['happy', 'neutral', 'relax']  |
|  21  |  face9_2  |  ['angry', 'happy', 'neutral', 'relax']  |
|  22  |  face9_3  |  ['angry', 'happy', 'neutral', 'relax']  |
|  23  |  face9_4  |  ['angry', 'happy', 'neutral', 'relax', 'sad']  |
|  24  |  face9_5  |  ['angry', 'happy', 'neutral', 'relax']  |


## Table2
| no.  | Video  | x | y | 
| :---:| :---: | :--- | :--- | 
|  0  |  ClubFridayShow2  	|<sub><sup>https://drive.google.com/file/d/<br>1f_duwyvzOIxnQJsN87nEFWs7YJFY7IxW/view?usp=sharing</sup></sub>   |https://drive.google.com/file/d/1aytbVCulR4CDDsqIasaUH5Get1XafFMB/view?usp=sharing   |
|  1  |  Club_Friday_Show  	|<sub>https://drive.google.com/file/d/<br>175jOX7qPNsGsnaCn-bLvuZjxMNjNiuh-/view?usp=sharing</sub>|https://drive.google.com/file/d/1LsNdhd-3tUj_UbH6laurMd8YBEJAH2TF/view?usp=sharing   |
|  2  |  Love_in_Depression |   |   |
|  3  |  face10_01  		|   |   |
|  4  |  face10_02  		|   |   |
|  5  |  face1_01  			|<sub>https://drive.google.com/file/d/1jvD65mszqoZaSjZLJvlx-Loc3zsQNXCB/view?usp=sharing</sub>|https://drive.google.com/file/d/1Y7vapjuxd9daKjC8PeZtWT5yek8XOnCn/view?usp=sharing   |
|  6  |  face1_02  			|<sub>https://drive.google.com/file/d/1fTbtQ7Y-3lxW9n-tLi5evYoFBYK7rfBH/view?usp=sharing</sub>|https://drive.google.com/file/d/105H0RT9iCVO0uwgy_s8lbWAm7QglMZ0V/view?usp=sharing   |
|  7  |  face1_03  			|<sub>https://drive.google.com/file/d/1O83T6djepqU5wPVwyqvJqeJapbUzjBnN/view?usp=sharing</sub>|https://drive.google.com/file/d/1AI-Cl2V4tmL4GocnrQrbphNT29sT_Ex2/view?usp=sharing   |
|  8  |  face1_04  			|<sub>https://drive.google.com/file/d/1LyzRXdoGthIyW0wNRtUxuJoUakL4YphX/view?usp=sharing</sub>|https://drive.google.com/file/d/1OeV28yGNqvzlJQ7yYiBmP6Q0TnrFMtn6/view?usp=sharing   |
|  9  |  face1_05  			|<sub>https://drive.google.com/file/d/1fYbvNN1AlLbXeXu9kkOUJbvKWR5emr7X/view?usp=sharing</sub>|https://drive.google.com/file/d/1McHmdM1aP5MVxYvLWUuQ6Tr6g6B8LhjN/view?usp=sharing   |
|  10  |  face2_01 			|   |   |
|  11  |  face2_02 			|<sub>https://drive.google.com/file/d/11GAEpU52kmiCpZv-B4DrAYe17g1zI6dh/view?usp=sharing</sub>|https://drive.google.com/file/d/1rUlSbXdQPunmktQaNntFFOmql-6Dboj-/view?usp=sharing   |
|  12  |  face4    			|<sub>https://drive.google.com/file/d/1CF_BGlU6WF6rb71hTexjUsqJtJZ3LiBs/view?usp=sharing</sub>|https://drive.google.com/file/d/1J4GPhgmv4bCgSZlvm22Mx4nEzx9dklBl/view?usp=sharing   |
|  13  |  face5_01 			|   |   |
|  14  |  face5_02 			|<sub>https://drive.google.com/file/d/108Y-6IB8gYJpwgMVRnH--Jn4R1GSxPaF/view?usp=sharing</sub>|https://drive.google.com/file/d/1K3y5cDTyC-8YMtXswrkr1XKiu9Br70ot/view?usp=sharing   |
|  15  |  face5_03 			|<sub>https://drive.google.com/file/d/1V8ZS2PRaKkoG-Uzhe_-WULXBxUkm-BCY/view?usp=sharing</sub>|https://drive.google.com/file/d/109SCnJwb60P6BXBtOMkBmwLzRHG5DDGE/view?usp=sharing   |
|  16  |  face6_01 			|<sub>https://drive.google.com/file/d/1h6h14_XFeJUcYdDggc2dec-Kn15IFdDi/view?usp=sharing</sub>|https://drive.google.com/file/d/10vPQms7PraN3uFefwWZVhXdGUsRqK7o4/view?usp=sharing   |
|  17  |  face6_02 			|<sub>https://drive.google.com/file/d/1OrOwSbkBZBNkG19Cg7tqdJoQqs1lEqX7/view?usp=sharing</sub>|https://drive.google.com/file/d/1xMnhhVNOB9SwwR9LYlsP4htHLkz-X6nr/view?usp=sharing   |
|  18  |  face7_01 			|<sub>https://drive.google.com/file/d/1TDkl5aEM45eqonZ5qp0Q6-XwS3tcDZbt/view?usp=sharing</sub>|https://drive.google.com/file/d/1nfMOiCo00MgUSBN-DsV5mJOE2zDE-Vbt/view?usp=sharing   |
|  19  |  face7_02 			|<sub>https://drive.google.com/file/d/1lIUr2JPD0KB1o1U-AADkHKG07WBToo-a/view?usp=sharing</sub>|https://drive.google.com/file/d/1Lo37MFomk305r8fp9r47kQG2PKyEVnfB/view?usp=sharing   |
|  20  |  face9_1  			|<sub>https://drive.google.com/file/d/1xUAWJq0hgAZivd8uF_JV7NLl51lXfFgI/view?usp=sharing</sub>|https://drive.google.com/file/d/18au3wSwHlsqlG4C2a6Tpq1cSmUtjRnWI/view?usp=sharing   |
|  21  |  face9_2  			|<sub>https://drive.google.com/file/d/1E6rLCglABL7ILUecVXIkr1-M2oa1URv6/view?usp=sharing</sub>|https://drive.google.com/file/d/1Hu8ok1ck33XFBBJl-j2jS4GqFA_vmZDZ/view?usp=sharing   |
|  22  |  face9_3  			|   |   |
|  23  |  face9_4  			|<sub>https://drive.google.com/file/d/1gGSPmnLdYQfYDVJZrsn1nWc7-3KZhLcG/view?usp=sharing</sub>|https://drive.google.com/file/d/1bAaK16B40FhWAtFANHE_mhtI_xAG1f4h/view?usp=sharing   |
|  24  |  face9_5  			|<sub>https://drive.google.com/file/d/19ocEkiNjohI15Lqg2AwXjFfuBM2Ic4mS/view?usp=sharing</sub>|https://drive.google.com/file/d/1s5bAFp2LJVmlrnIznVKB47xffD43JaXs/view?usp=sharing   |











##style
	- https://medium.com/analytics-vidhya/writing-github-readme-e593f278a796