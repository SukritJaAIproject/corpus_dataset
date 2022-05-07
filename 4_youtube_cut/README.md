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
	
<style>
  .markdown-body table td {
    font-size: 12px !important;
  }
</style>

## Table1
|```no.```|```Video```|```lebel```|```shape```|```frames```|```FPS```| 
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
|```no.```|```Video```|```lebel```| 
| :---:| :---: | :---: | 
|<sub>0</sup>|<sub>ClubFridayShow2</sup>|<sub><sup>['neutral', 'sad']</sup></sub>|
|<sub>1</sup>|<sub>Club_Friday_Show</sup>|<sub><sup>['angry', 'happy', 'neutral', 'relax', 'sad']</sup></sub>|
|<sub>2</sup>|<sub>Love_in_Depression</sup>|<sub><sup>['angry', 'happy', 'neutral', 'relax', 'sad']</sup></sub>|
|<sub>3</sup>|<sub>face10_01</sup>|<sub><sup>['angry', 'happy', 'neutral', 'relax', 'sad']</sup></sub>|
|<sub>4</sup>|<sub>face10_02</sup>|<sub><sup>['angry', 'happy', 'neutral', 'relax', 'sad']</sup></sub>|
|<sub>5</sup>|<sub>face1_01</sup>|<sub><sup>['angry', 'happy', 'neutral']</sup></sub>|
|<sub>6</sup>|<sub>face1_02</sup>|<sub><sup>['angry', 'happy', 'neutral']</sup></sub>|
|<sub>7</sup>|<sub>face1_03</sup>|<sub><sup>['angry', 'happy', 'neutral', 'relax', 'sad']</sup></sub>|
|<sub>8</sup>|<sub>face1_04</sup>|<sub><sup>['angry', 'happy', 'neutral', 'relax', 'sad']</sup></sub>|
|<sub>9</sup>|<sub>face1_05</sup>|<sub><sup>['angry', 'happy', 'neutral', 'relax']</sup></sub>|
|<sub>10</sup>|<sub>face2_01</sup>|<sub><sup>['angry', 'happy', 'neutral', 'relax', 'sad']</sup></sub>|
|<sub>11</sup>|<sub>face2_02</sup>|<sub><sup>['angry', 'happy', 'neutral', 'relax']</sup></sub>|
|<sub>12</sup>|<sub>face4</sup>|<sub><sup>['angry', 'happy', 'neutral', 'relax', 'sad']</sup></sub>|
|<sub>13</sup>|<sub>face5_01</sup>|<sub><sup>['angry', 'happy', 'neutral', 'relax', 'sad']</sup></sub>|
|<sub>14</sup>|<sub>face5_02</sup>|<sub><sup>['angry', 'happy', 'neutral', 'relax']</sup></sub>|
|<sub>15</sup>|<sub>face5_03</sup>|<sub><sup>['angry', 'sad']</sup></sub>|
|<sub>16</sup>|<sub>face6_01</sup>|<sub><sup>['angry', 'happy', 'neutral', 'relax', 'sad']</sup></sub>|
|<sub>17</sup>|<sub>face6_02</sup>|<sub><sup>['angry', 'happy', 'neutral', 'relax', 'sad']</sup></sub>|
|<sub>18</sup>|<sub>face7_01</sup>|<sub><sup>['angry', 'happy', 'neutral', 'relax']</sup></sub>|
|<sub>19</sup>|<sub>face7_02</sup>|<sub><sup>['neutral', 'relax']</sup></sub>|
|<sub>20</sup>|<sub>face9_1</sup>|<sub><sup>['happy', 'neutral', 'relax']</sup></sub>|
|<sub>21</sup>|<sub>face9_2</sup>|<sub><sup>['angry', 'happy', 'neutral', 'relax']</sup></sub>|
|<sub>22</sup>|<sub>face9_3</sup>|<sub><sup>['angry', 'happy', 'neutral', 'relax']</sup></sub>|
|<sub>23</sup>|<sub>face9_4</sup>|<sub><sup>['angry', 'happy', 'neutral', 'relax', 'sad']</sup></sub>|
|<sub>24</sup>|<sub>face9_5</sup>|<sub><sup>['angry', 'happy', 'neutral', 'relax']</sup></sub>|

	## Table2
|```no.```|```Video```|```x```|```y```| 
| :---:| :---: | :---: | :---: | 
|<sub>0</sub>|<sub>ClubFriday<br>Show2</sub>|<sub><https://drive.google.com/file/d/<br>1f_duwyvzOIxnQJsN87nEFWs7YJFY7IxW/view?usp=sharing</sub>|<sub>https://drive.google.com/file/d/<br>1aytbVCulR4CDDsqIasaUH5Get1XafFMB/view?usp=sharing</sub>|
|<sub>1</sub>|<sub>Club_Friday<br>Show</sub>|<sub>https://drive.google.com/file/d/<br>175jOX7qPNsGsnaCn-bLvuZjxMNjNiuh-/view?usp=sharing</sub>|<sub>https://drive.google.com/file/d/<br>1LsNdhd-3tUj_UbH6laurMd8YBEJAH2TF/view?usp=sharing</sub>|
|<sub>2</sub>|<sub>Love in<br>Depression</sub>|<sub>https://drive.google.com/file/d/<br>1hEf0CzXUnL6Bil0zv-CC6xo2Ob8HvqPD/view?usp=sharing</sub>|<sub>https://drive.google.com/file/d/<br>19cUhX3QHm9vYSF6IxVpet-Sw1uaK7CkB/view?usp=sharing</sub>|
|<sub>3</sub>|<sub>face10_01</sub>|<sub>https://drive.google.com/file/d/<br>1Eo5Toq_wT5KJnlKj0JTGX1qnh5iFBbA_/view?usp=sharing</sup>|<sub>https://drive.google.com/file/d/<br>1eUtcFQ-VQ5-Ohv2WfUo5jNUxe34_3eEw/view?usp=sharing</sup>|
|<sub>4</sub>|<sub>face10_02</sub>|<sub>https://drive.google.com/file/d/<br>14DY5MoyQmkzCiB1GFHuwn2ex7qSfIjCL/view?usp=sharing</sub>|<sub>https://drive.google.com/file/d/<br>1S2mZi1l1_vxAL176mr3LeMA_lrCfZfhY/view?usp=sharing</sub>|
|<sub>5</sub>|<sub>face1_01</sub>|<sub>https://drive.google.com/file/d/<br>1jvD65mszqoZaSjZLJvlx-Loc3zsQNXCB/view?usp=sharing</sub>|<sub>https://drive.google.com/file/d/<br>1Y7vapjuxd9daKjC8PeZtWT5yek8XOnCn/view?usp=sharing</sub>|
|<sub>6</sub>|<sub>face1_02</sub>|<sub>https://drive.google.com/file/d/<br>1fTbtQ7Y-3lxW9n-tLi5evYoFBYK7rfBH/view?usp=sharing</sub>|<sub>https://drive.google.com/file/d/<br>105H0RT9iCVO0uwgy_s8lbWAm7QglMZ0V/view?usp=sharing</sub>|
|<sub>7</sub>|<sub>face1_03</sub>|<sub>https://drive.google.com/file/d/<br>1O83T6djepqU5wPVwyqvJqeJapbUzjBnN/view?usp=sharing</sub>|<sub>https://drive.google.com/file/d/<br>1AI-Cl2V4tmL4GocnrQrbphNT29sT_Ex2/view?usp=sharing</sub>|
|<sub>8</sub>|<sub>face1_04</sub>|<sub>https://drive.google.com/file/d/<br>1LyzRXdoGthIyW0wNRtUxuJoUakL4YphX/view?usp=sharing</sub>|<sub>https://drive.google.com/file/d/<br>1OeV28yGNqvzlJQ7yYiBmP6Q0TnrFMtn6/view?usp=sharing</sub>|
|<sub>9</sub>|<sub>face1_05</sub>|<sub>https://drive.google.com/file/d/<br>1fYbvNN1AlLbXeXu9kkOUJbvKWR5emr7X/view?usp=sharing</sub>|<sub>https://drive.google.com/file/d/<br>1McHmdM1aP5MVxYvLWUuQ6Tr6g6B8LhjN/view?usp=sharing</sub>|
|<sub>10</sub>|<sub>face2_01</sub>|   |   |
|<sub>11</sub>|<sub>face2_02</sub>|<sub>https://drive.google.com/file/d/<br>11GAEpU52kmiCpZv-B4DrAYe17g1zI6dh/view?usp=sharing</sub>|<sub>https://drive.google.com/file/d/<br>1rUlSbXdQPunmktQaNntFFOmql-6Dboj-/view?usp=sharing</sub>|
|<sub>12</sub>|<sub>face4</sub>|<sub>https://drive.google.com/file/d/<br>1CF_BGlU6WF6rb71hTexjUsqJtJZ3LiBs/view?usp=sharing</sub>|<sub>https://drive.google.com/file/d/<br>1J4GPhgmv4bCgSZlvm22Mx4nEzx9dklBl/view?usp=sharing</sub>|
|<sub>13</sub>|<sub>face5_01</sub>|   |   |
|<sub>14</sub>|<sub>face5_02</sub>|<sub>https://drive.google.com/file/d/<br>108Y-6IB8gYJpwgMVRnH--Jn4R1GSxPaF/view?usp=sharing</sub>|<sub>https://drive.google.com/file/d/<br>1K3y5cDTyC-8YMtXswrkr1XKiu9Br70ot/view?usp=sharing</sub>|
|<sub>15</sub>|<sub>face5_03</sub>|<sub>https://drive.google.com/file/d/<br>1V8ZS2PRaKkoG-Uzhe_-WULXBxUkm-BCY/view?usp=sharing</sub>|<sub>https://drive.google.com/file/d/<br>109SCnJwb60P6BXBtOMkBmwLzRHG5DDGE/view?usp=sharing</sub>|
|<sub>16</sub>|<sub>face6_01</sub>|<sub>https://drive.google.com/file/d/<br>1h6h14_XFeJUcYdDggc2dec-Kn15IFdDi/view?usp=sharing</sub>|<sub>https://drive.google.com/file/d/<br>10vPQms7PraN3uFefwWZVhXdGUsRqK7o4/view?usp=sharing</sub>|
|<sub>17</sub>|<sub>face6_02</sub>|<sub>https://drive.google.com/file/d/<br>1OrOwSbkBZBNkG19Cg7tqdJoQqs1lEqX7/view?usp=sharing</sub>|<sub>https://drive.google.com/file/d/<br>1xMnhhVNOB9SwwR9LYlsP4htHLkz-X6nr/view?usp=sharing</sub>|
|<sub>18</sub>|<sub>face7_01</sub>|<sub>https://drive.google.com/file/d/<br>1TDkl5aEM45eqonZ5qp0Q6-XwS3tcDZbt/view?usp=sharing</sub>|<sub>https://drive.google.com/file/d/<br>1nfMOiCo00MgUSBN-DsV5mJOE2zDE-Vbt/view?usp=sharing</sub>|
|<sub>19</sub>|<sub>face7_02</sub>|<sub>https://drive.google.com/file/d/<br>1lIUr2JPD0KB1o1U-AADkHKG07WBToo-a/view?usp=sharing</sub>|<sub>https://drive.google.com/file/d/<br>1Lo37MFomk305r8fp9r47kQG2PKyEVnfB/view?usp=sharing</sub>|
|<sub>20</sub>|<sub>face9_1</sub>|<sub>https://drive.google.com/file/d/<br>1xUAWJq0hgAZivd8uF_JV7NLl51lXfFgI/view?usp=sharing</sub>|<sub>https://drive.google.com/file/d/<br>18au3wSwHlsqlG4C2a6Tpq1cSmUtjRnWI/view?usp=sharing</sub>|
|<sub>21</sub>|<sub>face9_2</sub>|<sub>https://drive.google.com/file/d/<br>1E6rLCglABL7ILUecVXIkr1-M2oa1URv6/view?usp=sharing</sub>|<sub>https://drive.google.com/file/d/<br>1Hu8ok1ck33XFBBJl-j2jS4GqFA_vmZDZ/view?usp=sharing</sub>|
|<sub>22</sub>|<sub>face9_3</sub>|   |   |
|<sub>23</sub>|<sub>face9_4</sub>|<sub>https://drive.google.com/file/d/<br>1gGSPmnLdYQfYDVJZrsn1nWc7-3KZhLcG/view?usp=sharing</sub>|<sub>https://drive.google.com/file/d/<br>1bAaK16B40FhWAtFANHE_mhtI_xAG1f4h/view?usp=sharing</sub>|
|<sub>24</sub>|<sub>face9_5</sub>|<sub>https://drive.google.com/file/d/<br>19ocEkiNjohI15Lqg2AwXjFfuBM2Ic4mS/view?usp=sharing</sub>|<sub>https://drive.google.com/file/d/<br>1s5bAFp2LJVmlrnIznVKB47xffD43JaXs/view?usp=sharing</sub>|



	## Styless
	- https://medium.com/analytics-vidhya/writing-github-readme-e593f278a796
	- https://www.pluralsight.com/guides/working-tables-github-markdown
	