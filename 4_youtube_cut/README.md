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
|```no.```|```Video```|```lebel```|```shape```|```frames```|```FPS```|```dist```| 
| :---:| :---: | :---: | :---: | :---: | :---: | :---: |
|<sub>0</sup>		|<sub>ClubFridayShow2.mp4</sup>					|<sub>Club_Friday_Show_dow.csv</sup>				|<sub>(19, 2)</sup>				|<sub>(1330,)</sup>				|<sub>7900</sup>|<sub>25</sup>				|<img src="https://github.com/SukritJaAIproject/corpus_dataset/blob/main/4_youtube_cut/pic/ClubFridayShow2.png" width="72">|
|<sub>1</sup>		|<sub>Club_Friday_Show.mp4</sup>				|<sub>Club_Friday_Show_pat.csv</sup>				|<sub>(79, 2)</sup>				|<sub>(13329,)</sup>			|<sub>28010</sup>|<sub>25</sup>				|<img src="https://github.com/SukritJaAIproject/corpus_dataset/blob/main/4_youtube_cut/pic/Club_Friday_Show.png" width="72">|
|<sub>2</sup>		|<sub>Love_in_Depression.mp4</sup>				|<sub>Love_in_Depression.csv</sup>					|<sub>(80, 2)</sup>				|<sub>(10445,)</sup>			|<sub>57017</sup>|<sub>25</sup>				|<img src="https://github.com/SukritJaAIproject/corpus_dataset/blob/main/4_youtube_cut/pic/Love_in_Depression.png" width="72">|
|<sub>3</sup>		|<sub>face10_01.mp4</sup>						|<sub>face10_01.csv</sup>							|<sub>(91, 4)</sup>				|<sub>(15614,)</sup>			|<sub>27503</sup>|<sub>25</sup>				|<img src="https://github.com/SukritJaAIproject/corpus_dataset/blob/main/4_youtube_cut/pic/face10_01.png" width="72">|
|<sub>4</sup>		|<sub>face10_02.mp4</sup>						|<sub>face10_02.csv</sup>							|<sub>(109, 4)</sup>			|<sub>(21264,)</sup>			|<sub>24843</sup>|<sub>29</sup>				|<img src="https://github.com/SukritJaAIproject/corpus_dataset/blob/main/4_youtube_cut/pic/face10_02.png" width="72">|
|<sub>5</sup>		|<sub>face1_01.mp4</sup>						|<sub>face1_01.csv</sup>							|<sub>(14, 4)</sup>				|<sub>(741,)</sup>				|<sub>14547</sup>|<sub>25</sup>				|<img src="https://github.com/SukritJaAIproject/corpus_dataset/blob/main/4_youtube_cut/pic/face1_01.png" width="72">|
|<sub>6</sup>		|<sub>face1_02.mp4</sup>						|<sub>face1_02.csv</sup>							|<sub>(13, 4)</sup>				|<sub>(5244,)</sup>				|<sub>22999</sup>|<sub>50</sup>				|<img src="https://github.com/SukritJaAIproject/corpus_dataset/blob/main/4_youtube_cut/pic/face1_02.png" width="72">|
|<sub>7</sup>		|<sub>face1_03.mp4</sup>						|<sub>face1_03.csv</sup>							|<sub>(22, 4)</sup>				|<sub>(4338,)</sup>				|<sub>17293</sup>|<sub>25</sup>				|<img src="https://github.com/SukritJaAIproject/corpus_dataset/blob/main/4_youtube_cut/pic/face1_03.png" width="72">|
|<sub>8</sup>		|<sub>face1_04.mp4</sup>						|<sub>face1_04.csv</sup>							|<sub>(43, 4)</sup>				|<sub>(12786,)</sup>			|<sub>9845</sup>|<sub>25</sup>				|<img src="https://github.com/SukritJaAIproject/corpus_dataset/blob/main/4_youtube_cut/pic/face1_04.png" width="72">|
|<sub>9</sup>		|<sub>face1_05.mp4</sup>						|<sub>face1_05.csv</sup>							|<sub>(59, 4)</sup>				|<sub>(9319,)</sup>				|<sub>10753</sup>|<sub>23</sup>				|<img src="https://github.com/SukritJaAIproject/corpus_dataset/blob/main/4_youtube_cut/pic/face1_05.png" width="72">|
|<sub>10</sup>		|<sub>face2_01.mp4</sup>						|<sub>face2_01.csv</sup>							|<sub>(152, 4)</sup>			|<sub>(76952,)</sup>			|<sub>93229</sup>|<sub>59</sup>				|<img src="https://github.com/SukritJaAIproject/corpus_dataset/blob/main/4_youtube_cut/pic/face2_01.png" width="72">|
|<sub>11</sup>		|<sub>face2_02.mp4</sup>						|<sub>face2_02.csv</sup>							|<sub>(74, 4)</sup>				|<sub>(30741,)</sup>			|<sub>40131</sup>|<sub>50</sup>				|<img src="https://github.com/SukritJaAIproject/corpus_dataset/blob/main/4_youtube_cut/pic/face2_02.png" width="72">|
|<sub>12</sup>		|<sub>face4.mp4</sup>							|<sub>face4.csv</sup>								|<sub>(204, 4)</sup>			|<sub>(26915,)</sup>			|<sub>54752</sup>|<sub>25</sup>				|<img src="https://github.com/SukritJaAIproject/corpus_dataset/blob/main/4_youtube_cut/pic/face4.png" width="72">|
|<sub>13</sup>		|<sub>face5_01.mp4</sup>						|<sub>face5_01.csv</sup>							|<sub>(154, 4)</sup>			|<sub>(59824,)</sup>			|<sub>57856</sup>|<sub>50</sup>				|<img src="https://github.com/SukritJaAIproject/corpus_dataset/blob/main/4_youtube_cut/pic/face5_01.png" width="72">|
|<sub>14</sup>		|<sub>face5_02.mp4</sup>						|<sub>face5_02.csv</sup>							|<sub>(72, 4)</sup>				|<sub>(32087,)</sup>			|<sub>290084</sup>|<sub>60</sup>			|<img src="https://github.com/SukritJaAIproject/corpus_dataset/blob/main/4_youtube_cut/pic/face5_02.png" width="72">|
|<sub>15</sup>		|<sub>face5_03.mp4</sup>						|<sub>face5_03.csv</sup>							|<sub>(5, 4)</sup>				|<sub>(1158,)</sup>				|<sub>16831</sup>|<sub>25</sup>				|<img src="https://github.com/SukritJaAIproject/corpus_dataset/blob/main/4_youtube_cut/pic/face5_03.png" width="72">|
|<sub>16</sup>		|<sub>face6_01.mp4</sup>						|<sub>face6_01.csv</sup>							|<sub>(108, 4)</sup>			|<sub>(13708,)</sup>			|<sub>15216</sup>|<sub>25</sup>				|<img src="https://github.com/SukritJaAIproject/corpus_dataset/blob/main/4_youtube_cut/pic/face6_01.png" width="72">|
|<sub>17</sup>		|<sub>face6_02.mp4</sup>						|<sub>face6_02.csv</sup>							|<sub>(228, 4)</sup>			|<sub>(39794,)</sup>			|<sub>35480</sup>|<sub>25</sup>				|<img src="https://github.com/SukritJaAIproject/corpus_dataset/blob/main/4_youtube_cut/pic/face6_02.png" width="72">|
|<sub>18</sup>		|<sub>face7_01.mp4</sup>						|<sub>face7_01.csv</sup>							|<sub>(211, 4)</sup>			|<sub>(38519,)</sup>			|<sub>28211</sup>|<sub>25</sup>				|<img src="https://github.com/SukritJaAIproject/corpus_dataset/blob/main/4_youtube_cut/pic/face7_01.png" width="72">|
|<sub>19</sup>		|<sub>face7_02.mp4</sup>						|<sub>face7_02.csv</sup>							|<sub>(10, 4)</sup>				|<sub>(3765,)</sup>				|<sub>5781</sup>|<sub>25</sup>				|<img src="https://github.com/SukritJaAIproject/corpus_dataset/blob/main/4_youtube_cut/pic/face7_02.png" width="72">|
|<sub>20</sup>		|<sub>face9_1.mp4</sup>							|<sub>face9_1.csv</sup>								|<sub>(29, 4)</sup>				|<sub>(10042,)</sup>			|<sub>11288</sup>|<sub>29</sup>				|<img src="https://github.com/SukritJaAIproject/corpus_dataset/blob/main/4_youtube_cut/pic/face9_1.png" width="72">|
|<sub>21</sup>		|<sub>face9_2.mp4</sup>							|<sub>face9_2.csv</sup>								|<sub>(21, 4)</sup>				|<sub>(8597,)</sup>				|<sub>14162</sup>|<sub>50</sup>				|<img src="https://github.com/SukritJaAIproject/corpus_dataset/blob/main/4_youtube_cut/pic/face9_2.png" width="72">|
|<sub>22</sup>		|<sub>face9_3.mp4</sup>							|<sub>face9_3.csv</sup>								|<sub>(27, 4)</sup>				|<sub>(6170,)</sup>				|<sub>6414</sup>|<sub>25</sup>				|<img src="https://github.com/SukritJaAIproject/corpus_dataset/blob/main/4_youtube_cut/pic/face9_3.png" width="72">|
|<sub>23</sup>		|<sub>face9_4.mp4</sup>							|<sub>face9_4.csv</sup>								|<sub>(81, 4)</sup>				|<sub>(10329,)</sup>			|<sub>16307</sup>|<sub>25</sup>				|<img src="https://github.com/SukritJaAIproject/corpus_dataset/blob/main/4_youtube_cut/pic/face9_4.png" width="72">|
|<sub>24</sup>		|<sub>face9_5.mp4</sup>							|<sub>face9_5.csv</sup>								|<sub>(22, 4)</sup>				|<sub>(2785,)</sup>				|<sub>8864</sup>|<sub>25</sup>				|<img src="https://github.com/SukritJaAIproject/corpus_dataset/blob/main/4_youtube_cut/pic/face9_5.png" width="72">|

	## Table2
|```no.```|```Video```|```lebel```|```x size```|```y size```|
| :---:| :---: | :---: | :---: | :---: |  
|<sub>0</sup>|<sub>ClubFridayShow2</sup>|<sub><sup>['neutral', 'sad']</sup></sub>										|<sub>561.1 MB</sub>|<sub>36 KB</sub>|
|<sub>1</sup>|<sub>Club_Friday_Show</sup>|<sub><sup>['angry', 'happy', 'neutral', 'relax', 'sad']</sup></sub>			|<sub>5.49 GB</sup>|<sub>365 KB</sup>|
|<sub>2</sup>|<sub>Love_in_Depression</sup>|<sub><sup>['angry', 'happy', 'neutral', 'relax', 'sad']</sup></sub>			|<sub>4.3 GB</sup>|<sub>286 KB</sup>|
|<sub>3</sup>|<sub>face10_01</sup>|<sub><sup>['angry', 'happy', 'neutral', 'relax', 'sad']</sup></sub>					|<sub>6.43 GB</sup>|<sub>427 KB</sup>|
|<sub>4</sup>|<sub>face10_02</sup>|<sub><sup>['angry', 'happy', 'neutral', 'relax', 'sad']</sup></sub>					|<sub>8.76 GB</sup>|<sub>582 KB</sup>|
|<sub>5</sup>|<sub>face1_01</sup>|<sub><sup>['angry', 'happy', 'neutral']</sup></sub>									|<sub>312.6 MB</sup>|<sub>20 KB</sup>|
|<sub>6</sup>|<sub>face1_02</sup>|<sub><sup>['angry', 'happy', 'neutral']</sup></sub>									|<sub>2.16 GB</sup>|<sub>144 KB</sup>|
|<sub>7</sup>|<sub>face1_03</sup>|<sub><sup>['angry', 'happy', 'neutral', 'relax', 'sad']</sup></sub>					|<sub>1.79 GB</sup>|<sub>119 KB</sup>|
|<sub>8</sup>|<sub>face1_04</sup>|<sub><sup>['angry', 'happy', 'neutral', 'relax', 'sad']</sup></sub>					|<sub>5.27 GB</sup>|<sub>350 KB</sup>|
|<sub>9</sup>|<sub>face1_05</sup>|<sub><sup>['angry', 'happy', 'neutral', 'relax']</sup></sub>							|<sub>3.84 GB</sup>|<sub>255 KB</sup>|
|<sub>10</sup>|<sub>face2_01</sup>|<sub><sup>['angry', 'happy', 'neutral', 'relax', 'sad']</sup></sub>					|<sub>31.7 GB</sup>|<sub>2.1 MB</sup>|
|<sub>11</sup>|<sub>face2_02</sup>|<sub><sup>['angry', 'happy', 'neutral', 'relax']</sup></sub>							|<sub>12.66 GB</sup>|<sub>841 KB</sup>|
|<sub>12</sup>|<sub>face4</sup>|<sub><sup>['angry', 'happy', 'neutral', 'relax', 'sad']</sup></sub>						|<sub>11.09 GB</sup>|<sub>736 KB</sup>|
|<sub>13</sup>|<sub>face5_01</sup>|<sub><sup>['angry', 'happy', 'neutral', 'relax', 'sad']</sup></sub>					|<sub>24.65 GB</sup>|<sub>1.6 MB</sup>|
|<sub>14</sup>|<sub>face5_02</sup>|<sub><sup>['angry', 'happy', 'neutral', 'relax']</sup></sub>							|<sub>13.22 GB</sup>|<sub>878 KB</sup>|
|<sub>15</sup>|<sub>face5_03</sup>|<sub><sup>['angry', 'sad']</sup></sub>												|<sub>488.5 MB</sup>|<sub>23 KB</sup>|
|<sub>16</sup>|<sub>face6_01</sup>|<sub><sup>['angry', 'happy', 'neutral', 'relax', 'sad']</sup></sub>					|<sub>5.65 GB</sup>|<sub>375 KB</sup>|
|<sub>17</sup>|<sub>face6_02</sup>|<sub><sup>['angry', 'happy', 'neutral', 'relax', 'sad']</sup></sub>					|<sub>16.39 GB</sup>|<sub>1.1 MB</sup>|
|<sub>18</sup>|<sub>face7_01</sup>|<sub><sup>['angry', 'happy', 'neutral', 'relax']</sup></sub>							|<sub>15.87 GB</sup>|<sub>1 MB</sup>|
|<sub>19</sup>|<sub>face7_02</sup>|<sub><sup>['neutral', 'relax']</sup></sub>											|<sub>1.55 GB</sup>|<sub>103 KB</sup>|
|<sub>20</sup>|<sub>face9_1</sup>|<sub><sup>['happy', 'neutral', 'relax']</sup></sub>									|<sub>4.14 GB</sup>|<sub>275 KB</sup>|
|<sub>21</sup>|<sub>face9_2</sup>|<sub><sup>['angry', 'happy', 'neutral', 'relax']</sup></sub>							|<sub>3.54 GB</sup>|<sub>235 KB</sup>|
|<sub>22</sup>|<sub>face9_3</sup>|<sub><sup>['angry', 'happy', 'neutral', 'relax']</sup></sub>							|<sub>2.54 GB</sup>|<sub>169 KB</sup>|
|<sub>23</sup>|<sub>face9_4</sup>|<sub><sup>['angry', 'happy', 'neutral', 'relax', 'sad']</sup></sub>					|<sub>4.26 GB</sup>|<sub>283 KB</sup>|
|<sub>24</sup>|<sub>face9_5</sup>|<sub><sup>['angry', 'happy', 'neutral', 'relax']</sup></sub>							|<sub>1.15 GB</sup>|<sub>76 KB</sup>|

	## Table2 
		- https://drive.google.com/drive/folders/1XoYB0XoHRfXubePhaWj9ZfWi86BfDin-?usp=sharing (healthcam)
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
|<sub>10</sub>|<sub>face2_01</sub>|<sub>https://drive.google.com/file/d/<br>1EchTjT9rWzHSk8YkBmp94-qVtltyaSoj/view?usp=sharing</sub>|<sub>https://drive.google.com/file/d/<br>1I1XcRpQ3LKiHNiWmvip1kcoG9s2miPMm/view?usp=sharing</sub>|
|<sub>11</sub>|<sub>face2_02</sub>|<sub>https://drive.google.com/file/d/<br>11GAEpU52kmiCpZv-B4DrAYe17g1zI6dh/view?usp=sharing</sub>|<sub>https://drive.google.com/file/d/<br>1rUlSbXdQPunmktQaNntFFOmql-6Dboj-/view?usp=sharing</sub>|
|<sub>12</sub>|<sub>face4</sub>|<sub>https://drive.google.com/file/d/<br>1CF_BGlU6WF6rb71hTexjUsqJtJZ3LiBs/view?usp=sharing</sub>|<sub>https://drive.google.com/file/d/<br>1J4GPhgmv4bCgSZlvm22Mx4nEzx9dklBl/view?usp=sharing</sub>|
|<sub>13</sub>|<sub>face5_01</sub>|<sub>https://drive.google.com/file/d/<br>1dMkC3Wxp-_x6YI_mBVNEjrAp3XRDkcMz/view?usp=sharing</sub>|<sub>https://drive.google.com/file/d/<br>19A6d6mHRoGsKhL6am5oCW8QNLkzB2nWR/view?usp=sharing</sub>|
|<sub>14</sub>|<sub>face5_02</sub>|<sub>https://drive.google.com/file/d/<br>108Y-6IB8gYJpwgMVRnH--Jn4R1GSxPaF/view?usp=sharing</sub>|<sub>https://drive.google.com/file/d/<br>1K3y5cDTyC-8YMtXswrkr1XKiu9Br70ot/view?usp=sharing</sub>|
|<sub>15</sub>|<sub>face5_03</sub>|<sub>https://drive.google.com/file/d/<br>1V8ZS2PRaKkoG-Uzhe_-WULXBxUkm-BCY/view?usp=sharing</sub>|<sub>https://drive.google.com/file/d/<br>109SCnJwb60P6BXBtOMkBmwLzRHG5DDGE/view?usp=sharing</sub>|
|<sub>16</sub>|<sub>face6_01</sub>|<sub>https://drive.google.com/file/d/<br>1h6h14_XFeJUcYdDggc2dec-Kn15IFdDi/view?usp=sharing</sub>|<sub>https://drive.google.com/file/d/<br>10vPQms7PraN3uFefwWZVhXdGUsRqK7o4/view?usp=sharing</sub>|
|<sub>17</sub>|<sub>face6_02</sub>|<sub>https://drive.google.com/file/d/<br>1OrOwSbkBZBNkG19Cg7tqdJoQqs1lEqX7/view?usp=sharing</sub>|<sub>https://drive.google.com/file/d/<br>1xMnhhVNOB9SwwR9LYlsP4htHLkz-X6nr/view?usp=sharing</sub>|
|<sub>18</sub>|<sub>face7_01</sub>|<sub>https://drive.google.com/file/d/<br>1TDkl5aEM45eqonZ5qp0Q6-XwS3tcDZbt/view?usp=sharing</sub>|<sub>https://drive.google.com/file/d/<br>1nfMOiCo00MgUSBN-DsV5mJOE2zDE-Vbt/view?usp=sharing</sub>|
|<sub>19</sub>|<sub>face7_02</sub>|<sub>https://drive.google.com/file/d/<br>1lIUr2JPD0KB1o1U-AADkHKG07WBToo-a/view?usp=sharing</sub>|<sub>https://drive.google.com/file/d/<br>1Lo37MFomk305r8fp9r47kQG2PKyEVnfB/view?usp=sharing</sub>|
|<sub>20</sub>|<sub>face9_1</sub>|<sub>https://drive.google.com/file/d/<br>1xUAWJq0hgAZivd8uF_JV7NLl51lXfFgI/view?usp=sharing</sub>|<sub>https://drive.google.com/file/d/<br>18au3wSwHlsqlG4C2a6Tpq1cSmUtjRnWI/view?usp=sharing</sub>|
|<sub>21</sub>|<sub>face9_2</sub>|<sub>https://drive.google.com/file/d/<br>1E6rLCglABL7ILUecVXIkr1-M2oa1URv6/view?usp=sharing</sub>|<sub>https://drive.google.com/file/d/<br>1Hu8ok1ck33XFBBJl-j2jS4GqFA_vmZDZ/view?usp=sharing</sub>|
|<sub>22</sub>|<sub>face9_3</sub>|<sub>https://drive.google.com/file/d/<br>1PSHMT2DSffv38WfgnuCMjmZnMlruP-Fd/view?usp=sharing</sub>|<sub>https://drive.google.com/file/d/<br>1iWroBTCeCFcleiiPQ5iMGlzoFjsg5QKt/view?usp=sharing</sub>|
|<sub>23</sub>|<sub>face9_4</sub>|<sub>https://drive.google.com/file/d/<br>1gGSPmnLdYQfYDVJZrsn1nWc7-3KZhLcG/view?usp=sharing</sub>|<sub>https://drive.google.com/file/d/<br>1bAaK16B40FhWAtFANHE_mhtI_xAG1f4h/view?usp=sharing</sub>|
|<sub>24</sub>|<sub>face9_5</sub>|<sub>https://drive.google.com/file/d/<br>19ocEkiNjohI15Lqg2AwXjFfuBM2Ic4mS/view?usp=sharing</sub>|<sub>https://drive.google.com/file/d/<br>1s5bAFp2LJVmlrnIznVKB47xffD43JaXs/view?usp=sharing</sub>|



	## Styless
	- https://medium.com/analytics-vidhya/writing-github-readme-e593f278a796
	- https://www.pluralsight.com/guides/working-tables-github-markdown
	