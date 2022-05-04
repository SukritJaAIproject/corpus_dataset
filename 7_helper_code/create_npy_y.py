# ### Backup code : create numpy y

# !ls 'drive/MyDrive/tech_own/voting_dataset/'
# !ls 'drive/MyDrive/tech_vdo/csv_psy/v1/'
# !ls 'drive/MyDrive/tech_vdo/csv_psy/v2/'
# !ls 'drive/MyDrive/tech_vdo/csv_psy/v2/numpy/'

# ### psy_team
# # psy_team_pathy = 'drive/MyDrive/tech_vdo/csv_psy/v1/' 
# # filenames = ['01.csv', '02.csv', '03.csv', '04.csv', '05.csv', '06.csv', '07.csv', '08.csv', 'pilot01.csv', 'pilot02.csv', 'pilot03.csv', 'pilot04.csv', 'pilot05.csv']
# #
# # psy_team_pathy = 'drive/MyDrive/tech_vdo/csv_psy/v2/' 
# # filenames = ['01_df.csv', '02_df.csv', '03_df.csv', '04_df.csv', '05_df.csv', '06_df.csv', '07_df.csv', '08_df.csv', 'pilot01_df.csv', 'pilot02_df.csv', 'pilot03_df.csv', 'pilot04_df.csv', 'pilot05_df.csv']

# ### data_team
# # data_team_pathy = 'drive/MyDrive/tech_own/data_dict/med/v3/'
# # filenames = ['01_256.csv', '02_256.csv', '03_256.csv', '04_224.csv', '05_94_126.csv', '06_224.csv', '07_224.csv', '08_98_134.csv', 'pilot01_224.csv', 'pilot02_150.csv', 'pilot03_150.csv', 'pilot04_150.csv', 'pilot05_150.csv']
# #
# # data_team_pathy = 'drive/MyDrive/tech_vdo/csv/' 
# # filenames = ['face001.csv', 'face002.csv', 'face003.csv', 'face004.csv', 'face005.csv', 'face006.csv', 'face007.csv', 'face008.csv', 'pilot01.csv', 'pilot02.csv', 'pilot03.csv', 'pilot04.csv', 'pilot05.csv']

# # create numpy y
# for item in filenames:
#   lable = []
#   # df  = pd.read_csv(psy_team_pathy+item)
#   df  = pd.read_csv(data_team_pathy+item)
#   for i in range(df.shape[0]):
#     y = df['label'][i]
#     lable.append(y)
#   lable_ar = np.array(lable)

#   # np.save(psy_team_pathy+item[:-4]+'.npy', lable_ar)
#   # print(item[:-4]+':', lable_ar.shape)

#   # np.save(psy_team_pathy+item+'.npy', lable_ar)
#   # print(item+':', lable_ar.shape)

#   # np.save(data_team_pathy+item[:-8]+'.npy', lable_ar)
#   # print(item+':', lable_ar.shape)

#   np.save(data_team_pathy+item[:-4]+'.npy', lable_ar)
#   print(item[:-4]+':', lable_ar.shape)