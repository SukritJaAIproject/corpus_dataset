## balance set
	### Train Test video
		- path = '/content/drive/MyDrive/data/balance/'
		- train : a_h_r_sa (anger, happy, relax, sad) | test : stress
		- train : a_h_r_st (anger, happy, relax, stress) | test : sad
		- train : a_h_sa_st(anger, happy, sad, stress) | test : relax
		- train : a_r_sa_st(anger, relax, sad, stress) | test : happy
		- train : h_r_sa_st (happy, relax, sad, stress) | test : anger
	### x_train filename 
		- a_h_r_sa_x_train_balance.npy
		- a_h_r_st_x_train_balance_v1.npy
		- a_h_sa_st_x_train_balance_v1.npy
		- a_r_sa_st_x_train_balance.npy
		- h_r_sa_st_x_train_balance.npy	
	### y_train filename 
		- a_h_r_sa_y_train_balance.npy
		- a_h_r_st_y_train_balance_v1.npy
		- a_h_sa_st_y_train_balance_v1.npy
		- a_r_sa_st_y_train_balance.npy
		- h_r_sa_st_y_train_balance.npy
	### x_test filename 
		- a_h_r_sa_x_test_balance.npy
		- a_h_r_st_x_test_balance_v1.npy
		- a_h_sa_st_x_test_balance_v1.npy
		- a_r_sa_st_x_test_balance.npy
		- h_r_sa_st_x_test_balance.npy
	### y_test filename 
		- a_h_r_sa_y_test_balance.npy
		- a_h_r_st_y_test_balance_v1.npy
		- a_h_sa_st_y_test_balance_v1.npy
		- a_r_sa_st_y_test_balance.npy
		- h_r_sa_st_y_test_balance.npy
	
## skip5frame
	- path_r = '/content/drive/MyDrive/data/'
	- x_path, y_path = path_r+ 'anger_session_talk_x_skip5frame.npy', path_r+ 'anger_session_talk_y_skip5frame.npy'
	- x_path, y_path = path_r+ 'happy_session_talk_x_skip5frame.npy', path_r+ 'happy_session_talk_y_skip5frame.npy'
	- x_path, y_path = path_r+ 'relax_session_talk_x_skip5frame.npy', path_r+ 'relax_session_talk_y_skip5frame.npy'
	- x_path, y_path = path_r+ 'sad_session_talk_x_skip5frame.npy', path_r+ 'sad_session_talk_y_skip5frame.npy'
	- x_path, y_path = path_r+ 'stress_session_talk_x_skip5frame.npy', path_r+ 'stress_session_talk_y_skip5frame.npy'
	
	### skip5frame x_train
		- path = 'drive/MyDrive/data/skip5frame/x/'
		- anger_session_talk_x_skip5frame.npy  : (5812, 384, 384, 3)
		- happy_session_talk_x_skip5frame.npy  : (2973, 384, 384, 3)
		- relax_session_talk_x_skip5frame.npy  : (6733, 384, 384, 3)
		- sad_session_talk_x_skip5frame.npy  : (513, 384, 384, 3)
		- stress_session_talk_x_skip5frame.npy  : (2759, 384, 384, 3)
		
	### skip5frame y_train_numeric
		- path = 'drive/MyDrive/data/skip5frame/y/numeric/'
		- anger_session_talk_y_skip5frame_yn.npy:  (513, 1) [0 1 2 3] ***mistake
		- happy_session_talk_y_skip5frame_yn.npy:  (2973, 1) [0 1 2]
		- relax_session_talk_y_skip5frame_yn.npy:  (6733, 1) [0 1 2 3]
		- sad_session_talk_y_skip5frame_yn.npy:  (513, 1) [0 1 2 3]
		- stress_session_talk_y_skip5frame_yn.npy:  (2759, 1) [0 1 2 3 4]
	
	### skip5frame y_train_string
		- path = 'drive/MyDrive/data/skip5frame/y/string/'
		- anger_session_talk_y_skip5frame.npy :  (5812,) ['angry' 'happy' 'neutral' 'relax' 'sad']
		- happy_session_talk_y_skip5frame.npy :  (2973,) ['happy' 'neutral' 'relax']
		- relax_session_talk_y_skip5frame.npy :  (6733,) ['angry' 'happy' 'neutral' 'relax']
		- sad_session_talk_y_skip5frame.npy :  (513,) ['happy' 'neutral' 'relax' 'sad']
		- stress_session_talk_y_skip5frame.npy :  (2759,) ['angry' 'happy' 'neutral' 'relax' 'sad']	
		
	### all emotion x_train 
	- path = 'https://drive.google.com/drive/folders/1D_8ard8MODZoBapHbFuFtuU5vwUozN9N?usp=sharing
	- ahrss_x_v1.npy, ahrss_y_v1.npy : (18790, 384, 384, 3) (18790,) , [0 1 2 3 4]
	- ahrss_balance_x_train.npy, ahrss_balance_y_train.npy : (29313, 384, 384, 3) (29313,), [0 1 2 3 4]
	- ahrss_balance_x_test.npy, ahrss_balance_y_test.npy : (9772, 384, 384, 3) (9772,) [0 1 2 3 4]
	- ahrss_balance_x.npy, ahrss_balance_y.npy : (39085, 384, 384, 3) (39085,) [0 1 2 3 4]
	
## prepare balance dataset
	### balance x_train
	-	a_h_r_sa_x_train_balance.npy : (26437, 384, 384, 3)
	-	a_h_sa_st_x_train_balance.npy, a_h_sa_st_x_train_balance_v1.npy : (1809641704), (15048, 384, 384, 3)
	-	a_r_sa_st_x_train_balance.npy : (25488, 384, 384, 3)
	-	a_h_r_st_x
	-	h_r_sa_st_x_train_balance.npy : (22158, 384, 384, 3)
	### balance x_test
	-	a_h_r_sa_x_test_balance.npy : (8813, 384, 384, 3)
	-	a_h_sa_st_x_test_balance.npy, a_h_sa_st_x_test_balance_v1.npy : (969099832) , (5017, 384, 384, 3)
	-	a_r_sa_st_x_test_balance.npy : (8497, 384, 384, 3)
	-	a_h_r_st_x_test_balance_v1.npy : (9374, 384, 384, 3)
	-	h_r_sa_st_x_test_balance : (7387, 384, 384, 3)
	### balance y_train
	-	a_h_r_sa_y_train_balance.npy : (26437,), [0 1 2 3 4]
	-	a_h_sa_st_y_train_balance.npy, a_h_sa_st_y_train_balance_v1.npy : (15048,), [0 1 2 3 4] ,  (15048,), [0 1 2 3 4]
	-	a_r_sa_st_y_train_balance.npy : (25488,), [0 1 2 3 4]
	-	a_h_r_st_y_train_balance_v1.npy : (28121,),  [0 1 2 3 4]
	-	h_r_sa_st_y_train_balance.npy : (22158,), [0 1 2 3 4]
	### balance y_test
	-	a_h_r_sa_y_test_balance.npy : (8813,), [0 1 2 3 4]
	-	a_h_sa_st_y_test_balance.npy, a_h_sa_st_y_test_balance_v1.npy : (5017,), [0 1 2 3 4], (5017,) [0 1 2 3 4]
	-	a_r_sa_st_y_test_balance.npy : (8497,) [0 1 2 3 4]
	-	a_h_r_st_y_test_balance_v1.npy : (9374,) [0 1 2 3 4]
	-	h_r_sa_st_y_test_balance.npy :  (7387,) [0 1 2 3 4]
 
## prepare session_talk dataset
	### session_talk x_train
	-	path = 'drive/MyDrive/data/session_talk/x/'
	-	path = 'D:/mu_dataset/' # local path
	-	anger_session_talk_x.npy : (29083, 384, 384, 3)
	-	happy_session_talk_x.npy : (14877, 384, 384, 3)
	-	relax_session_talk_x.npy : (33665, 384, 384, 3)
	-	sad_session_talk_x.npy  : (2562, 384, 384, 3)
	-	stress_session_talk_x.npy : (13803, 384, 384, 3)
	
	### session_talk y_numeric
	-	path = 'drive/MyDrive/data/session_talk/y_numeric/'
	-	anger_session_talk_yn.npy : (29083, 1) [0 1 2 3 4]
	-	happy_session_talk_yn.npy : (14877, 1) [0 1 2]
	-	relax_session_talk_yn.npy : (33665, 1) [0 1 2 3]
	-	sad_session_talk_yn.npy : 	(2562, 1) [0 1 2 3]
	-	stress_session_talk_yn.npy : (13803, 1) [0 1 2 3 4]
	
	### session_talk y_string
	-	path = 'drive/MyDrive/data/session_talk/y_string/'	
	-	anger_session_talk_y.npy : (29083,) ['angry' 'happy' 'neutral' 'relax' 'sad']
	-	happy_session_talk_y.npy : (14877,) ['happy' 'neutral' 'relax']
	-	relax_session_talk_y.npy : (33665,) ['angry' 'happy' 'neutral' 'relax']
	-	sad_session_talk_y.npy :  (2562,) ['happy' 'neutral' 'relax' 'sad']
	-	stress_session_talk_y.npy : (13803,) ['angry' 'happy' 'neutral' 'relax' 'sad']
	
## prepare small_size dataset
	### x_train
		-	path = 'drive/MyDrive/data/small_size/x/'
		-	a_h_r_sa_x.npy:  (16031, 384, 384, 3)
		-	a_h_r_st_x.npy:  (18277, 384, 384, 3)
		-	a_h_sa_st_x.npy:  (12057, 384, 384, 3)
		-	a_r_sa_st_x.npy:  (15817, 384, 384, 3)
		-	h_r_sa_st_x.npy:  (12978, 384, 384, 3)
	### y_train_numeric
		-	a_h_r_sa_yn.npy :  (16031, 1) [0 1 2 3 4]
		-	a_h_r_st_yn.npy :  (18277, 1) [0 1 2 3 4]
		-	a_h_sa_st_yn.npy :  (12057, 1) [0 1 2 3 4]
		-	a_r_sa_st_yn.npy :  (15817, 1) [0 1 2 3 4]
		-	h_r_sa_st_yn.npy :  (12978, 1) [0 1 2 3 4]
	### y_train_string
		-	a_h_r_sa_y.npy :  (16031,) ['angry' 'happy' 'neutral' 'relax' 'sad']
		-	a_h_r_st_y.npy :  (18277,) ['angry' 'happy' 'neutral' 'relax' 'sad']
		-	a_h_sa_st_y.npy :  (12057,) ['angry' 'happy' 'neutral' 'relax' 'sad']
		-	a_r_sa_st_y.npy :  (15817,) ['angry' 'happy' 'neutral' 'relax' 'sad']
		-	h_r_sa_st_y.npy :  (12978,) ['angry' 'happy' 'neutral' 'relax' 'sad']
