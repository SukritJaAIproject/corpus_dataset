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
	
## prepare dataset
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