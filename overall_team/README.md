# corpus_dataset

- path = '/content/drive/MyDrive/data/'
	- train : a_h_r_sa (anger, happy, relax, sad) | test : stress
	- train : a_h_r_st (anger, happy, relax, stress) | test : sad
	- train : a_h_sa_st(anger, happy, sad, stress) | test : relax
	- train : a_r_sa_st(anger, relax, sad, stress) | test : happy
	- train : h_r_sa_st (happy, relax, sad, stress) | test : anger
	
- x_train filename 
	- a_h_r_sa_x_train_balance.npy
	- a_h_r_st_x_train_balance_v1.npy
	- a_h_sa_st_x_train_balance_v1.npy
	- a_r_sa_st_x_train_balance.npy
	- h_r_sa_st_x_train_balance.npy
	
- y_train filename 
	- a_h_r_sa_y_train_balance.npy
	- a_h_r_st_y_train_balance_v1.npy
	- a_h_sa_st_y_train_balance_v1.npy
	- a_r_sa_st_y_train_balance.npy
	- h_r_sa_st_y_train_balance.npy
	
- x_test filename 
	'''- a_h_r_sa_x_test_balance.npy
	- a_h_r_st_x_test_balance_v1.npy
	- a_h_sa_st_x_test_balance_v1.npy
	- a_r_sa_st_x_test_balance.npy
	- h_r_sa_st_x_test_balance.npy'''
	
- y_test filename 
	- a_h_r_sa_y_test_balance.npy
	- a_h_r_st_y_test_balance_v1.npy
	- a_h_sa_st_y_test_balance_v1.npy
	- a_r_sa_st_y_test_balance.npy
	- h_r_sa_st_y_test_balance.npy