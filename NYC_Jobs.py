#-------------------------------------------------
# Developer:   Artur MArkowski    Date: 2020-03-03
# Last update: Artur MArkowski    Date: 2021-11-20
# ================================================

# NYC Jobs
# https://www1.nyc.gov/jobs/explore-careers.page
# https://data.cityofnewyork.us/api/views/kpav-sd4t/rows.csv

# '''Best codes'''

	# x= list(df) ;print(x,'\n')                    # Get all columns as list
	# x= df['Agency'].to_list() ;print(x,'\n')      # Get list of all values in the column
	# x= df.columns ;print(x,'\n')                  # Get all columns as index
	# x= df.count() ;print(x,'\n')          		# Count values for each column
	# x= df[var].count() ;print(x,'\n')			    # Get count
	# x= df[var].nunique() ;print(x,'\n')			# Get unique
	# x= df[var].idxmax() ;print(x,'\n')            # Get index of max count value
	# x= df[var].index.values						# Get array of index values :df[df.a==4].index.values
	# x= df.to_dict('dict') ;print(x,'\n')		    # Convert df to dictionary
	# x= df.to_dict('list') ;print(x,'\n')		    # Convert df to list
	# x= pd.DataFrame(dict) ;print(x,'\n')		    # Convert dictionary to df

    # Cheat Sheets:
    # https://www.python-graph-gallery.com/cheat-sheets/

print('NYC Jobs\n')

'''Code settings
================================================='''
# Declare initial variables:
on=True; off=(); debug_mode=(); n_rows=None; output=(); drive=(); url_data=(); code_pause=(); p=(); pp=(); fix_data_encoding=(); etl=(); charts=(); plt_show=(); save=()

# debug_mode = True ######## ######## ######## ######## ######## ######## ######## ######## ######## ########

if debug_mode: 
    # save=True
    # p = True    # print results
    pp = True    # print results - temporarly
    output=True
    # code_pause  = True
    "Load Data"
    # url_data = True
    # small number of rows can include na's only and print error...
    # n_rows = 100
    "Tidy Data"
    # fix_data_encoding = True
    "Charts"
    etl=True
    charts=True
    plt_show = True
else:
    # save=True
    output=True
    "Load Data"
    url_data = True
    "Tidy Data"
    # fix_data_encoding = True
    "Charts"
    etl=True
    charts=True
    plt_show = True

'''Import libraries
================================================='''
if on:
    print('Importing libraries...')

    # import clipboard
    # import pyperclip
    # from collections import Counter

    from datetime import date

    import time
    # from time import perf_counter
    ts_code = time.perf_counter()   # timestart_code:
    # time.sleep(0.5)
    def tt(): # Total time:
        return round(time.perf_counter() - ts_code, 3)
    def mt(): # Module time:
        return round(time.perf_counter() - ts, 3)
    def ts(): # Total time:
        return time.perf_counter()        # timestart
    # ts = time.perf_counter()
    ts = ts()
    
    # ts = time.perf_counter()      #time start
    # print(tt())                   #total time
    # if debug_mode: print('\n>>>',sys._getframe().f_lineno,'   t:',tt()); os.system("pause"); sys.exit() # >>>>> >>>>> 
    # if debug_mode: print('>>>>:',sys._getframe().f_lineno); #sys.exit() # >>>>>>>>>>>>>>>>>>>>>>>>>>>>

    import sys, os
    # print("Python version: " + sys.version)
    # pause()                           # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> [Press <ENTER> to exit...]
    # os.system("pause")                # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> [Press any key to continue . . .]
    # print(sys._getframe().f_lineno)   # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # sys.exit()                        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # print('\n>>>',sys._getframe().f_lineno,'   t:',tt()); os.system("pause"); sys.exit()
    
    def pause(): # Press <ENTER> to exit...
        programPause = input("Press <ENTER> to exit...\n")
    def dg(msg = None): # Get code line number
        # https://stackoverflow.com/questions/3056048/filename-and-line-number-of-python-script
        # print(f">>> {sys._getframe().f_back.f_lineno}: {msg if msg is not None else ''}")
        print(f"\n>>> {sys._getframe().f_back.f_lineno}: {msg if msg is not None else ''}")
        # print(f">>> {sys._getframe().f_back.f_lineno}: {msg if msg is not None else ''}\n")
    def sp(msg = None): # System Pause
        print(f">>> {sys._getframe().f_back.f_lineno}: {msg if msg is not None else ''}");os.system("pause") 
    def ex(msg = None): # System Pause
        print(f">>> {sys._getframe().f_back.f_lineno}: exit: {msg if msg is not None else ''}");sys.exit()
    # dg('debug')
    # sp('pause')
    # ex('exit')

    import numpy as np
    import pandas as pd
    # from pandas import Timestamp
    # https://towardsdatascience.com/pretty-displaying-tricks-for-columnar-data-in-python-2fe3b3ed9b83
    # https://thispointer.com/python-pandas-how-to-display-full-dataframe-i-e-print-all-rows-columns-without-truncation/
    # pd.options.display.max_columns = None           # Remove the max column limit for displaying on the screen
    # pd.options.display.width=None                   # Get all the data in a single line fashion
    # pd.options.display.width=20                     # Get all the data in a single line fashion
    # pd.options.display.width=20                     # Get all the data in a single line fashion
    # https://pandas.pydata.org/docs/reference/api/pandas.set_option.html
    # pd.set_option('display.max_rows', None)         # Default value of max_rows is 10
    # pd.set_option('display.width', None)
    # pd.set_option('display.max_row', 20)            # Set ipython's max row display
    # pd.set_option('display.max_columns', 5)         # Set iPython's max column width to 50

    # https://stackoverflow.com/questions/27722658/set-max-string-length-in-pandas/47798996
    # pd.set_option('display.max_colwidth', 50)       # Defaulst is 50
    # pd.set_option('display.max_colwidth', 30)       # Defaulst is 50 /max col name is 29...
    
    
    # pd.set_option('display.max_row', 1000)          # Set ipython's max row display
    # pd.set_option('display.max_columns', 50)        # Set iPython's max column width to 50

    if fix_data_encoding:
        # pip install ftfy
        import ftfy

    if charts:
        pass
        # import matplotlib.pyplot as plt
        # import seaborn as sns
        # import plotly.express as px

    # print('Importing libraries completed!  ', tt(),'sec')
    print('>>>', tt(),'sec')
    # print("Python version: " + sys.version)                 # Python version
    # dg(tt())
    # print(mt()) #module time
    # dg('exit');sys.exit() # >>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # dg(mt());sys.exit() # >>>>>>>>>>>>>>>>>>>>>>>>>>>>
# dg('exit'); os.system("pause"); sys.exit() # >>>>>>>>>>>>>>>>>>>>>>>>>>>>

'''Functions
================================================='''
if on:
    test=()
    # test=True
    def longest_string(string_list): # Get longest string in the list
        # return max(len(s) for s in string_list)
        return max(len(str(s)) for s in string_list)
    if test:
        x= ['abc', 'de', 'longest string', '1234']
        x= list(df['Job Description'])  #string
        x= longest_string(x) ;print(x,'\n')

    def MergeDict(dict1, dict2): # Merge two dictionaries
        return dict1.update(dict2)
    if test:
        x= MergeDict(dict1, dict2)
        x= pd.DataFrame(dict1, index=['Total:']) ;print(x)

'''Loading Data (df)
================================================='''
if etl:
    ts = time.perf_counter()

    '''Select data source
    -------------------------------------------------'''
    dir_path = 'D:\D\DATA\CSV' # to save chart
    if url_data:
        source_adr = 'https://data.cityofnewyork.us/api/views/kpav-sd4t/rows.csv'
        # source_adr = 'https://media.geeksforgeeks.org/wp-content/uploads/employees.csv'
        # source_adr = 'https://data.cityofnewyork.us/api/views/kpav-sd4t/rows.csv'

        # source_adr = 'https://data.ok.gov/sites/default/files/res_vacation_and_sick_day_comparison_ycet-mnvb.csv' #obj,int
    else: # Drive
        # dir_path = 'D:\D\DATA\CSV'

        file_name = 'NYC_Jobs_2020-02-25.csv'
        file_name = 'NYC_Jobs_2020-03-31.csv'
        file_name = 'NYC_Jobs_2020-04-07.csv'
        file_name = 'NYC_Jobs_2020-04-14.csv'
        file_name = 'NYC_Jobs_2020-04-21.csv'
        file_name = 'NYC_Jobs_2020-04-28.csv'
        file_name = 'NYC_Jobs_2020-05-05.csv'
        file_name = 'NYC_Jobs_2020-05-12.csv'
        # file_name = 'NYC_Jobs_nonan.csv'
        # file_name = 'NYC_Jobs_nan.csv'
        file_name = 'NYC_Jobs.csv'
        # file_name = '______.csv'

        source_adr = str(dir_path + '\\' + file_name)

    '''Load Data
    -------------------------------------------------'''
    if on: 
        print('\nLoading data...')
        source_adr = source_adr.strip() # Trim whitespaces
        print(source_adr)

        df = pd.read_csv(source_adr, nrows=n_rows)    #speed: 4949.1 MB/s (nrows=10)

        # df = pd.read_csv(source_adr)    #speed: 139.1 MB/s
        # df = pd.read_csv(source_adr, delimiter=',') #speed: 139.1 MB/s
        # df = pd.read_csv(source_adr, encoding='utf-8')  #speed: 106.1 MB/s
        # df = pd.read_csv(source_adr, engine='python')   #speed: 90.6 MB/s
        # df = pd.read_csv(source_adr, delimiter=',', engine='python') #speed: 90.6 MB/s
    # ts_code = time.perf_counter()   # timestart_code:

    t_downloading = round(mt(), 3)   # timer - max 5
    if p:print('>>>', t_downloading, 'sec  |  shape:',df.shape,'\n')

    # dg(mt());sys.exit() # >>>>>>>>>>>>>>>>>>>>>>>>>>>>

    '''Loading Data summary
    -------------------------------------------------'''
    def memory_calculate(df):
        # 1 Bit       = Binary Digit (0 or 1)
        # 8 Bits      = 1 Byte
        # 1024 Bytes  = 1 KB (Kilo Byte)  = 1024              Bytes   **1
        # 1024 KB     = 1 MB (Mega Byte)  = 1048576           Bytes   **2
        # 1024 MB     = 1 GB (Giga Byte)  = 1073741824        Bytes   **3
        # 1024 GB     = 1 TB (Tera Byte)  = 1099511627776     Bytes   **4
        # 1024 TB     = 1 PB (Peta Byte)  = 1125899906842624  Bytes   **5

        # obj_size = sys.getsizeof([])
        obj_size = sys.getsizeof(df)
        if p:print(obj_size, 'Bytes')
        r= 0; x = 1024
        x2=round(obj_size,r+1)

        # # 'One way:
        # if obj_size < (x-(0.05)): obj_size= str(x2)+' Bytes'
        # elif obj_size < (x**2-(x*0.05)): obj_size= str(round(x2/x,r+1))+' KB'
        # elif obj_size < (x**3-(x**2*0.05)): obj_size= str(round(x2/x**2,r+1))+' MB'
        # elif obj_size < (x**4-(x**3*0.05)): obj_size= str(round(x2/x**3,r+1))+' GB'
        # elif obj_size < (x**5-(x**4*0.05)): obj_size= str(round(x2/x**4,r+1))+' TB'
        # if p:print(obj_size)
        # print('Loading data completed!    - Time:', t_downloading, 'sec  |  Size:', obj_size)

        # 'Second way:
        if obj_size < (x-(0.05)): 
            obj_size= x2
            unit= 'Bytes'
            x=1
        elif obj_size < (x**2-(x*0.05)): 
            obj_size= round(x2/x,r+1)
            unit= 'KB'
            x=1024
        elif obj_size < (x**3-(x**2*0.05)): 
            obj_size= round(x2/x**2,r+1)
            unit= 'MB'
            x=1048576
        elif obj_size < (x**4-(x**3*0.05)): 
            obj_size= round(x2/x**3,r+1)
            unit= 'GB'
            x=1073741824
        elif obj_size < (x**5-(x**4*0.05)): 
            obj_size= round(x2/x**4,r+1)
            unit= 'TB'
            x=1099511627776
        if p:print(obj_size,unit)
        # speed = round((sys.getsizeof(df)/1048576)/t_downloading,1)
        speed = ((x2/x)/t_downloading)
        speed = round(speed,1)
        speed = str(speed)+' MB/s' #str(unit)
        obj_size = str(obj_size)+' '+unit
        print('>>>',t_downloading,'sec  |  size:', obj_size,'  |  speed:',speed)
    if on: memory_calculate(df)
    # dg('memory_calculate');sys.exit() # >>>>>>>>>>>>>>>>>>>>>>>>>>>>

    '''Save to CSV - Raw data
    -------------------------------------------------'''
    def save_to_CSV(df):
        # if debug_mode: sys.exit() # >>>>>>>>>>>>>>>>>>>>>>>>>>>>
        # df.to_csv(r"D:\D\DATA\CSV\NYC_Jobs.csv", index=False, encoding='utf8')

        file_name = 'NYC_Jobs.csv'
        source_adr = str(dir_path + '\\' + file_name)
        df.to_csv(source_adr, index=False, encoding='utf8')

        # df = df.iloc[0:10, :] # extract first 10 rows
        # df.to_csv("NYC_Jobs_10.csv", index=False)
        # df.to_csv("NYC_Jobs_10.csv", index=False, encoding='utf8')
        # df.to_csv("NYC_Jobs_.csv", index=False)
        # df.to_csv("NYC_Jobs_5.csv", index=False, encoding='utf8')
        print('Saved as:',source_adr)
    if url_data: 
        if save: save_to_CSV(df)
    # dg('save_to_CSV');sys.exit() # >>>>>>>>>>>>>>>>>>>>>>>>>>>>

    '''Data summary (add total no. of duplicates*)
    -------------------------------------------------'''
    if on:
        x= date.today()                 # date today
        df_row= df.shape[0]
        df_col= df.shape[1]
        df_na= df.isna().sum().sum()
        if df_na == 0: 
            pass # Display just 0:
            df_na_str= '-'
        else:
            df_na_pr= df_na/(df_row*df_col)
            df_na_pr= '{:.0%}'.format(df_na_pr)
            # df_na_str= str(df_na)+'-('+str(df_na_pr)+')'  # 9934-(11%)
            # df_na_str= str(df_na)+'/'+str(df_na_pr)+''    # 9934/11%
            # df_na_str= str(df_na)+':'+str(df_na_pr)+''    # 9934:11%
            # df_na_str= str(df_na_pr)+'('+str(df_na)+')'   # 11%(9934)
            # df_na_str= '('+str(df_na_pr)+')/'+str(df_na)  # (11%)/9934
            # df_na_str= str(df_na_pr)+'/'+str(df_na)+''    # 11%/9934
            # df_na_str= str(''+df_ na_pr)+':'+str(df_na)+''    # 11%:9934
            df_na_str= str(''+df_na_pr+'') # 11%
        if p:print(df_na_str)
        # col_max= df['Process Date'].max()

        dict1 = {
            'Rows':df_row, 
            'Columns':df_col, 
            'NA':[df_na_pr]
            # 'NA':df_na_str
            }
        df_stat= pd.DataFrame(dict1, index=['Total:'])
        if p:print(df_stat)

        # DATA TYPES:
        #------------------------------------------------------------
        # Create dictionary of available data types:
        x= df.dtypes.value_counts()
        x= list(x.index)
        dict2= {}
        for i in x:
            dict2[str(i)] = df.dtypes.value_counts()[i]
            if p:print(i,'->',dict2[str(i)],'\n')

        # Merge two dictionaries:
        if p:print(dict1,'\n')
        if p:print(dict2,'\n')

        def Merge(dict1, dict2): 
            return(dict1.update(dict2))

        Merge(dict1, dict2)
        if p:print(dict1,'\n')
        if p:print(list(dict1),'\n')
        df_stat_merged= pd.DataFrame(dict1, index=['  Total:'])
        df_stat = df_stat_merged
        if p:print('\n')
        if p:print(df_stat,'\n')

        # Insert column separator:
        if on:
            # Syntax: 'DataFrame.insert(loc, column, value, allow_duplicates = False)'
            df_stat.insert(3,'|','|')
            if p:print(df_stat,'\n')
        
        # if output:
    print();print(df_stat,'\n\n','-'*100)
    print('>>>',sys._getframe().f_lineno,'   t:',mt(),'- File processing') #; os.system("pause"); sys.exit() # >>>>> >>>>> 
    # dg(tt());sys.exit() # >>>>>>>>>>>>>>>>>>>>>>>>>>>>

'''Tidy Data
================================================='''
if etl:
    ts = time.perf_counter()       # timestart:
    
    x = df.copy(deep=True)  # Copy df (deep): https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.copy.html

    '''Get count of all distinct values in the column:
    -------------------------------------------------'''
    if p:
        print(df)           # Get list of columns
        print(list(df))     # Get list of columns
        # var= 'Job ID'
        var= 'Agency'
        # var= 'Job Category'
        dg('Get count of all distinct values in the column: '+var)
        x = df.pivot_table(index=[var], aggfunc='size') # Get count of all distinct values
        if p:
            # print()
            print(x,'\n')                                   # values count df
            print(list(x),'\n')                             # list values count
            print(list(x.index),'\n')                       # list of values
            print(max(x)),'\n'                              # max count value
            y= np.array(x) ;print(np.unique(y),'\n')        # list unique values
            x= np.array(x) ;y= np.unique(x) ;print(y)       # index of max value
            # x= np.array(x) ;y= np.unique(x) ;print(y)       # list unique values
            
            for i in list(x)[:10]: print(i)                 # iterate values count
            for i in df[var][:10]: print(i)                 # iterate values

            # dg(mt());sys.exit() # >>>>>>>>>>>>>>>>>>>>>>>>>>>>

        # Loop in column and get element [from:to]:
        for i in range(len(df[var][:10])):
            # pass
            print()
            print(df[var][i])
            print(df[var].index[i])

            if df['Agency'][i] == '<no category>': 
            # if df[var][i].isnull(): 
            # if df[var][i] == : 
            # if df[df[var][i].isnull()]:
                pass
                print(i)
            # ValueError: The truth value of a Series is ambiguous. Use a.empty, a.bool(), a.item(), a.any() or a.all().
            
            # dg(mt());sys.exit() # >>>>>>>>>>>>>>>>>>>>>>>>>>>>

        print(df[df[var].isna()])   #df is empty
        print(df[var].isna())

        # dg(mt());sys.exit() # >>>>>>>>>>>>>>>>>>>>>>>>>>>>

        for i in df[var].isna():
            # if i == True:
            if i == False:pass
            else:
                print(i)
    # dg(mt());sys.exit() # >>>>>>>>>>>>>>>>>>>>>>>>>>>>

    '''REMOVE df dupliacates (Alter df):
    -------------------------------------------------'''
    if on:
        # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.drop_duplicates.html
        # https://www.geeksforgeeks.org/python-pandas-dataframe-drop_duplicates/
        x = df.copy(deep=True)  # Copy df (deep): https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.copy.html

        # dropping ALL duplicte values:
        # -------------------------------------------------
        if p:print(df.shape[0])
        # x.drop_duplicates(subset = None, keep = 'last', inplace = True, ignore_index=True) 
        x.drop_duplicates(keep = 'first', inplace = True, ignore_index=True)   
        if p:print(x.shape[0])
        if p:print('>>> Number of removed row duplicates:', (df.shape[0]-x.shape[0]))
    df= x.copy(deep=True)    # Alter df
    # del x
    # ex()

    '''CHANGE df data types:
    -------------------------------------------------'''
    if on:
        if p: dg('CHANGE data types:')
        if p:print(df.shape)
        if p:print(df.dtypes)
        # https://www.geeksforgeeks.org/change-data-type-for-one-or-more-columns-in-pandas-dataframe/
        # https://stackoverflow.com/questions/39092067/pandas-dataframe-convert-column-type-to-string-or-categorical?rq=1

        col_obj = ['Job Category idx']
        col_int = ['Job ID','# Of Positions']
        # col_dat = ['Posting Date','Post Until','Posting Updated','Process Date']
        col_dat = ['Posting Date','Posting Updated','Process Date']
        col_dat_dmy = ['Post Until'] # 05-MAR-2020
        col_dec = ['Salary Range From', 'Salary Range To']
        col_str = ['Recruitment Contact']
        # col_str = ['Title Code No']     # '1002A'

        if p:print(list(df['Post Until']))
        # dg(mt());sys.exit() # >>>>>>>>>>>>>>>>>>>>>>>>>>>>

        if p:
            pass
            print()
            dg('>>>Get column list and values:')
            x= df['Agency'].to_list(); print(x,'\n')   # Get list of all values in the column
            x= df.columns; print(x,'\n')                # Get all columns as index
            x= list(df); print(x,'\n')                  # Get all columns as list

            # dg(mt());sys.exit() # >>>>>>>>>>>>>>>>>>>>>>>>>>>>

        """ Change columns type to integer: """
        if off:
            print(df[col_int].dtypes)
            for col in col_int: 
                df[col] = df[col].astype('int')


        """ Change columns type to dates: """
        if on:
            for col in col_dat: 
                df[col] = pd.to_datetime(df[col], format='%m/%d/%Y')  # "02/23/2018"

            for col in col_dat_dmy: 
                df[col] = pd.to_datetime(df[col], format='%d-%b-%Y')  # "23-MAR-2018"

            # dg(mt());sys.exit() # >>>>>>>>>>>>>>>>>>>>>>>>>>>>

        """ Change columns type to String: """
        if on:
            # df[col_str] = df[col_str].astype(int)
            # df[col_str] = df[col_str].astype(str)
            # df[col_str] = df[col_str].astype('str')
            # df[col_str] = df[col_str].astype('string')
            # df[col_str] = df[col_str].astype('category')
            # df[col_str] = pd.Categorical(df[col_str])           # filling all column with col name...?

            for col in list(df):
                if col not in col_int + col_dat + col_dat_dmy + col_dec:
                    pass
                    # df[col] = df[col].astype('category')
                    # df[col] = df[col].astype('str')
                    df[col] = df[col].astype('string')

        """ Check data types: """
        if p:
            print()
            x= df.dtypes.value_counts() ;print(x,'\n')
            # col_one_arr = df['one'].to_numpy()
            print(list(df['Post Until']))
        
        # dg(mt());sys.exit() # >>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # ex()

    '''TRANSFORM Column [Posting Type]:
    -------------------------------------------------'''
    if on:
        # Find job id, where posting type is internal, external or both and create list with new categories.
        # Then replace column with new category values.
        # https://datatofish.com/count-duplicates-pandas/

        ext_int = 'Ext-Int'     # Value to replace with
        # var= 'Posting Type'     #['External', 'Internal']
        # var= 'Agency'
        var= 'Job ID'

        if p: # Statistics
            dg('TRANSFORM Column [Posting Type]:')
            print(df.shape)
            # dg(mt());sys.exit() # >>>>>>>>>>>>>>>>>>>>>>>>>>>>
            x= df[var] ;print(x,'\n')
            x= df[var].count() ;print(x,'\n')
            x= df[var].nunique() ;print(x,'\n')
            # dg(mt());sys.exit() # >>>>>>>>>>>>>>>>>>>>>>>>>>>>

            # Get list of unque values count (duplicates >= 2):
            x = df.pivot_table(index=[var], aggfunc='size')

            # Get list statistics:
            print(x,'\n')                                   # values count df
            print(list(x),'\n')                             # list values count (dublicates > 1)
            print(list(x.index),'\n')                       # list of values
            print(max(x),'\n')                              # max count value
            print(x.idxmax(),'\n')                          # Get index of max count value
            # dg(mt());sys.exit() # >>>>>>>>>>>>>>>>>>>>>>>>>>>>

            # number_list = [1, 2, 3]
            # max_value = max(x)
            # Return the max value of the list
            # x = x.index(max(x))

            y= np.array(x) ;print(np.unique(y),'\n')        # list unique values count
            # x= np.array(x) ;y= np.unique(x) ;print(y)     # list unique values

            for i in list(x)[:10]: print(i)                      # iterate values count
            for i in df[var][:10]: print(i)                      # iterate values

            # sp() # system pause
            # dg(mt());sys.exit() # >>>>>>>>>>>>>>>>>>>>>>>>>>>>

        if on: # Iterate through column values: #['External', 'Internal']
            # print()
            listExt=[]
            listInt=[]
            # sp()
            if p:print(range(len(df[var])))
            # for i in range(len(df[var][:10])):
            for i in range(len(df[var])): 
                # print(i)
                x= df[var][i]
                if df['Posting Type'][i] == 'External': 
                    pass
                    # print(i,x,'Extern')
                    listExt.append(x)
                elif df['Posting Type'][i] == 'Internal': 
                    pass
                    # print(i,x,'Internal')
                    listInt.append(x)
                else:
                    pass
                    # print('None')
            # print()
            if p:print('\n',listExt[:10])
            if p:print('\n',len(listExt))
            if p:print('\n',listInt[:10])
            if p:print('\n',len(listInt))
            # dg(mt());sys.exit() # >>>>>>>>>>>>>>>>>>>>>>>>>>>>

            # Build new column:
            posting_type_2=[]
            # for i in range(len(df[var][:100])): 
            for i in range(len(df[var])):
                job_id= df[var][i]   #Job ID number
                # print(job_id)
                if job_id in listExt: 
                    if job_id in listInt:
                        # print(i,job_id,x)
                        x= ext_int
                    else:
                        # print(i,job_id,x)
                        x= 'External'
                else: 
                    # print(i,job_id,x)
                    x= 'Internal'
                # print(job_id)
                posting_type_2.append(x)

        if p: # Results:
            print()
            print('Posting Type 2:',len(posting_type_2))
            y= np.array(posting_type_2) ;print('Posting Type 2:',np.unique(y))         # print list unique values

            # print(posting_type_2,'\n')
            print(len(posting_type_2),'\n')
            print(df.iloc[ :10,[0,2]])
            # print(df.iloc[333:338])

            # 333 424683 2
            # 334 348229 2
            # 335 151131 external
            # 336 389713 int
            # 337 438105 2
            # 338 424597 2

            # dg(mt());sys.exit() # >>>>>>>>>>>>>>>>>>>>>>>>>>>>

        if on: # Insert/replace column
            # Insert new column: ------------------------------------------------
            # df.insert(3, "Posting Type 2", posting_type_2)

            # Replace column: ---------------------------------------------------
            # where 1 is the axis number (0 for rows and 1 for columns.)
            df= df.drop(['Posting Type'], axis=1)
            # df= df.drop(['Posting Type','# Of Positions'], axis=1)
            df.insert(2, 'Posting Type', posting_type_2)

            if p:
                df.info()
                print(df.shape)
                print(df.iloc[ :10,[0,2,3]])

            # dg(tt());sys.exit() # >>>>>>>>>>>>>>>>>>>>>>>>>>>>

    '''Remove row duplicates:
    -------------------------------------------------'''
    if on:
        # dg(tt());sys.exit() # >>>>>>>>>>>>>>>>>>>>>>>>>>>>
        x= df.shape[0]  # record old row count

        # if p:print(df.shape)
        dg('Remove row duplicates:'); print(df.shape)

        # df.drop_duplicates(subset = None, keep = 'last', inplace = True, ignore_index=True)
        # if p:print(df.shape)

        # 'Dropping - ALL row duplictes: ------------------------------------
        df.drop_duplicates(keep = 'first', inplace = True, ignore_index=True)
        # if p:print(df.shape)
        dg('Remove duplicates - all cols:'); print(df.shape)

        # 'Dropping - row with duplictes in SELECTED columns: -------------------
        df.drop_duplicates(subset = 'Job ID', keep = 'first', inplace = True, ignore_index=True)
        # if p:print(df.shape)
        dg('Remove duplicates - in Job ID:'); print(df.shape)

        # 'Check result:
        if p:
            # dg(tt());sys.exit() # >>>>>>>>>>>>>>>>>>>>>>>>>>>>
            print()
            print('Number of duplicated rows removed:',x-df.shape[0])
            print(df.shape)
            # print(df)
            # df.info()
            # print()

            # Find duplicated Job IDs:------------------------------
            x= df['Job ID'].value_counts() #;print(x)
            #   x= df.groupby('Job ID').count() ;print(x)
            print(list(x))
            print(x[:15])
            print(df.iloc[:15])

            # Test if duplicated value exists: 422000 389713
            # print(df['Job ID'])
            x= 422000
            if x in list(df['Job ID']): print(x,'- True')
            else: print('False')
            # dg(tt());sys.exit() # >>>>>>>>>>>>>>>>>>>>>>>>>>>>
        # dg(tt());sys.exit() # >>>>>>>>>>>>>>>>>>>>>>>>>>>>

    '''Fix data encoding (overheat processor: 26 sec):
    -------------------------------------------------'''
    if fix_data_encoding:
        dg('Fix data encoding (overheat processor: 26 sec)?')
        if on:
            print(df.dtypes)
            print()
            print(df['Preferred Skills'].dtype.name)
            print(list(df))
            # print(df['Job Description'])
            print(df['Preferred Skills'][4])
            # print(list(df['Job Description']))
            dg();sp()

        # import ftfy  # pip install ftfy
        for i in list(df):
            # if df[i].dtypes == 'object':
            if df[i].dtype.name == 'string':
                # print(i)
                # dg();sp()
                # x = df[i]
                # x = str(x)
                # df[i] = ftfy.fix_text(x)
                # print(range(len(df[i])))

                for j in range(len(df[i])):
                    x = df.at[j,i]
                    x = str(x)
                    df.at[j,i] = ftfy.fix_text(x)
        
        if p:print(df['Preferred Skills'][4])
        
        # 'Check values: col_GroupBy = 'Preferred Skills'                #[1140]

        # print(df['Posting Type'].shape[0])
        # print(df['Job Category'].shape[0])

        # dg(tt());sys.exit() # >>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # ex()

    '''Column [Job Category] (16) / Export to Dict:
    -------------------------------------------------'''
    if on:
        if p:print(df.shape[0])
        # dg(tt());sys.exit() # >>>>>>>>>>>>>>>>>>>>>>>>>>>>

        # https://onedrive.live.com/view.aspx?resid=50272B73B7FDE70A!484&ithint=file%2cxlsx&authkey=!ACzvZNajZee0-vI
        # https://www1.nyc.gov/jobs/explore-careers.page            # Jobs | City of New York
        # https://a127-jobs.nyc.gov/index_new.html?agency=008       # Applicant Searches
        # https://opendata.cityofnewyork.us/data/                   # NYC Open Data

        df_old = df.copy()  # Copy dataframe as old before changes

        # Define value for missing categories (must be string type):
        no_category= '_Not Available'
        # d = {'a': 1, 'b': 2}
        job_categories= [
            no_category,
            '_Clerical & Administrative Support',
            '_Community & Business Services',
            '_Information Technology & Telecommunications',
            '_Maintenance & Operations',
            'Administration & Human Resources',
            'Building Operations & Maintenance',
            'Communications & Intergovernmental Affairs',
            'Constituent Services & Community Programs',
            'Engineering, Architecture & Planning',
            'Finance, Accounting & Procurement',
            'Health',
            'Legal Affairs',
            'Policy, Research & Analysis',
            'Public Safety, Inspections & Enforcement',
            'Social Services',
            'Technology, Data & Innovation'
            ]
        job_cat_clean = list(job_categories) # Copy list to be able to restore original

        
        if p: # Get index number of the list item
            print('\n',job_categories.index(no_category))
            for i in job_categories: print(i)

        if off: # Replace job_categories with clean one:
            print()
            # print(job_categories,'\n')
            for i in range(len(job_categories)):
                # print(job_categories[i])
                job_categories[i]= job_categories[i].replace(",", " ")
                job_categories[i]= job_categories[i].replace("&", " ")
                #get rid of all the duplicate whitespaces and newline characters:
                job_categories[i]= " ".join(job_categories[i].split())  
            # print(job_categories,'\n')
            for i in job_categories:
                print(i)

            # s = '  Hello  World    From Pankaj \t\n\r\tHi There  '
            # print('\n',s)
            # s= " ".join(s.split())
            # print(s)

        if on: # Replace job_cat_clean with clean one:
            # print(job_cat_clean,'\n')
            for i in range(len(job_cat_clean)):
                # print(job_cat_clean[i])
                # list_no_mach.append(s)
                job_cat_clean[i]= job_cat_clean[i].replace(",", " ")
                job_cat_clean[i]= job_cat_clean[i].replace("&", " ")
                job_cat_clean[i]= job_cat_clean[i].replace("_", "")
                #get rid of all the duplicate whitespaces and newline characters:
                job_cat_clean[i]= " ".join(job_cat_clean[i].split())
            
            if p: # Print all categories:
                print()
                print(job_cat_clean,'\n')
                for i in job_cat_clean: 
                    print(job_cat_clean.index(i), i)
                print()

        if off: # Get rid of all the duplicate whitespaces and newline characters (no column replacement):
            # print()
            col_name= 'Job Category'
            # col_name= 'Agency'

            # Fill na with any text value:
            # https://stackoverflow.com/questions/26837998/pandas-replace-nan-with-blank-empty-string
            df[col_name].fillna(no_category, inplace=True)
            list_no_mach=[]
            list_result=[]

            # x= df.loc[:,['Job Category']]
            # x= df.loc[:,['Agency']]
            # x= df['Agency'].unique()

            # x= df
            x= df.sort_values(by=[col_name], ascending=True)
            x= x[col_name].unique()
            print(len(x))
            for i in x:
                # clean text:
                i= i.replace(',', ' ')
                i= i.replace('&', ' ')

                i= ' '.join(i.split()) # 'Get rid of all the duplicate whitespaces and newline characters
                print(i) # Print clean text

                # 'Test module:
                # if 'Legal Affairs' in i:
                # if 'Finance Accounting Procurement' in i:
                #     print(i)

                # 'Replace categories with *
                for ii in job_cat_clean:
                    i= i.replace(ii, "*")
                
                # 'Get list of unmaches: s= 'string'
                s= i.replace("*",'')
                s= s.lstrip()
                if s != '': 
                    # print(s)
                    s= ' '.join(s.split())  # 'Get rid of all the duplicates whitespaces
                    list_no_mach.append(s)
                    # list_no_mach = list(set(list_no_mach))
                
                # 'Print values where categories didn't match:
                if off:
                    # print(i.replace(' ',''))
                    # print(''.join(set(i)))
                    str_= ''.join(set(i.replace(' ','')))
                    if str_ != '*':
                        pass
                        print(i)
                        # list_no_mach.append(i)


                # 'Fix unrecognised categories:
                i= i.replace('Legal', "Legal Affairs")
                i= i.replace('Policy Analysis', "Policy Research Analysis")

                # 'Run replace categories with * again:
                for ii in job_cat_clean:
                    i= i.replace(ii, "*")
                
                # 'Print final result
                # print(i)
                # print(i.replace(' ',''))

                # 'Get list of final result with undetected categories:
                i= i.replace(' ','')    # 'Remove all spaces
                i= i.replace("*",'')    # 'Remove * to get empty string
                if i != '': 
                    # print(i)
                    # s= ' '.join(s.split())  # 'Get rid of all the duplicates whitespaces
                    list_result.append(i)




            
            if on: # Print report:
                list_no_mach = list(set(list_no_mach))  # Remove duplicates form the list
                total_undetected= len(list_no_mach)     # Get total number of unmached categories
                list_result = list(set(list_result))    # Remove duplicates form the list

                print(
                    '\nUndetected categories ('
                    +str(total_undetected)
                    +'):', 
                    list_no_mach)
                # print('  Total:',len(list_no_mach))     # Get total number of unmached categories
                # list_no_mach = list(set(list_no_mach))  # Remove duplicates form the list
                # print('  List: ',list_no_mach)          # List of undetected categories

                print('                    After:',list_result)
                # print('                After ['+str(len(list_result))+']:',list_result)

        # dg(tt());sys.exit() # >>>>>>>>>>>>>>>>>>>>>>>>>>>> 

        '''Replace column values'''
        if on: # Replace column values without duplicates, whitespaces and newline characters:

            # Set variables:
            col_name= 'Job Category'

            Job_category_names=[]   # series with fixed categories for new column
            Job_category_idx=[]     # series with fixed categories for new column
            list_no_mach=[]         # list with originally undetected cetegories
            list_result=[]          # list after manipulations, empty if all categories were matched.
            list_names=[]           # list created for each row with final value to replace with.
            list_cat_idx=[]         # list created for each row with final value to replace with.
            cat_count=[]            # list for all distinct job categories
            cat_to_string=()        # initialise boolean value
            dict_categories={}      # categories with all job IDs

            # About converting categories: list of categories for each row need to be as single string value to be able to use separator between each of them and count distinct values in further analysis. 
            # list object with integers -  will cause problems with 'distinct' function and 'join' with separator...
            
            cat_to_string=True          # if disabled, categories will remain as list
            sep = ' | '                 # when joining multiple categories for one row (if string values only)

            def col_val():
                # 'Replace cetegory names with... (select one only):
                # 'Used: list.append(index) or list.append(list[index])

                # return list_names.append(str(job_cat_clean.index(ii)))             # index as string
                return list_names.append(job_categories[job_cat_clean.index(ii)])  # name (str)

                # 'Doesn't work with functions: distinct or join:
                # return list_names.append(job_cat_clean.index(ii))    # index as integer

            def f_cat_idx():
                return list_cat_idx.append(job_cat_clean.index(ii))    # index as integer
            
            def iterobj(object): # Iterate object to print values
                print()
                for i in object:print(i)
                # for i in list(object):print(i)
            # iterobj(df)                   # Call function - list column names
            # iterobj(df[col_name])         # Call function - list column values
            # iterobj(df['Posting Type'])   # Call function - list column values

            def itercol(dfi,col): # Iterate dataframe column to print values
                print()
                for i in list(dfi[col]):print(i)    # - doesn't work
            # itercol(df,col_name) # Iterate and print values

            # dict_categories['key'] = 'val'
            # https://bytes.com/topic/python/answers/632526-append-data-list-within-dict
            # ListDict = {
            #     'one' : ['oneone' , 'onetwo' , 'onethree'],
            #     'two' : ['twoone' , 'twotwo', 'twothree'],
            #     'three' : ['threeone' , 'threetwo', 'threethree']}
            # ListDict['two'].append('twofour')
            #
            # https://stackoverflow.com/questions/26367812/appending-to-list-in-python-dictionary
            # ListDict.setdefault('four', []).append('fourone')
            # ListDict['four'].append('fourtwo')
            # ListDict.setdefault('four', []).append('fourtwo')
            # ListDict.setdefault('four', []).append('fourthree')
            # print(ListDict)
            
            # for i in job_cat_clean:
            #     dict_categories.setdefault(i,[])

            df[col_name].fillna(no_category, inplace=True) # Fill na with any text value
            
            if p: # Column statistics
                dg()
                x= df[col_name] # Set Dataframe column to process
                print(len(x))
                print(df[col_name].shape[0])
                print(df[col_name])
                print(list(df[col_name]))
                for i in list(df[col_name]):print(i) # Print list of all job categories

                # Set column name for processing:
                x= df.sort_values(by=[col_name], ascending=True)[col_name].unique()     # df.sort[column].unique

                print(len(x)) # Get list all unique values:
                print(df[col_name].index.values) # Get array of index values => df[df.a==4].index.values
                iterobj(x) # Iterate and print values
                itercol(df,col_name) # Iterate and print values

                # dg(tt());sys.exit() # >>>>>>>>>>>>>>>>>>>>>>>>>>>>

            # Start replacement:
            # https://stackoverflow.com/questions/41070549/get-index-when-looping-through-one-column-of-pandas
            x= df[col_name] # Set Dataframe column to process
            for idx, i in x.iteritems():
                # dg(tt());sys.exit() # >>>>>>>>>>>>>>>>>>>>>>>>>>>>

                if p: # Iterate column
                    pass
                    # print()
                    # print(i)
                    # print(idx, df['Job Category'][idx])
                    # print(idx, df['Job ID'][idx])
                    # dg();sp() # >>>>>>>>>>>>>>>>>>>>>>>>>>>>

                # clean text:
                i= i.replace(',', ' ')
                i= i.replace('&', ' ')
                i= i.replace('_', '')
                i= ' '.join(i.split())  #'Get rid of all the duplicate whitespaces and newline characters
                # if p:print(i)     #'Print clean text
                i2=i    #'Duplicate clean 'i' for use in list - cat_count, "i" will be replaced with empty string later if all cat will match...
                for ii in job_cat_clean: #'Replace categories with * [1st]
                    # print(ii)
                    if ii in i:
                        # print(ii)
                        col_val()       # create list with cat name
                        f_cat_idx()     # create list with cat index

                        i= i.replace(ii,'')
                        # i= i.replace(ii, "*")
                        # i= i.replace(ii, str(job_cat_clean.index(ii))+',')

                # print(list_names)
                # list_names=[]
                # print(i)
                # print(list_cat_idx)
                
                # 'Get list of unmaches: s= 'string'
                s= i.replace("_",'')
                s= s.lstrip()
                if s != '': 
                    # print(s)
                    s= ' '.join(s.split())  # 'Get rid of all the duplicates whitespaces
                    list_no_mach.append(s)
                
                # 'Print values where categories didn't match:
                if off:
                    # print(i.replace(' ',''))
                    # print(''.join(set(i)))
                    str_= ''.join(set(i.replace(' ','')))
                    if str_ != '*':
                        pass
                        print(i)
                        # list_no_mach.append(i)

                # 'Fix unrecognised categories:
                i= i.replace('Legal', "Legal Affairs")
                i= i.replace('Policy Analysis', "Policy Research Analysis")

                # 'Run replace categories with * again [2nd]:
                for ii in job_cat_clean:
                    if ii in i:
                        # print(ii,'-',i)     # print category list-column value
                        col_val()           # create list with cat name
                        f_cat_idx()         # create list with cat index
                        i= i.replace(ii,'') # remove name - replace with empty string


                # Append  Job_category_names: -------------------------------------------------
                # 'Apend list with distinct categories:
                # print(i2)
                for ii in job_cat_clean:
                    if ii in i2:
                        # print(ii,'-',i2)                            # print category list-column value
                        cat_count.append(ii)
                # list_names = list(set(list_names))                  # remove duplicates from the list
                if cat_to_string: list_names=sep.join(list_names)   # concatenate list item to one string
                Job_category_names.append(list_names)               # Append new column
                Job_category_idx.append(list_cat_idx)               # Append new column
                if p: # Print list of cat indexes and names!
                    print(list_cat_idx)                             # print list of categories (index)
                    print(list_names,'\n')                          # print list of categories (names)

                for ii in list_cat_idx: # Append dictionary with categories
                    pass
                    # print(ii)
                    # print(job_cat_clean[ii])
                    # ListDict['two'].append('twofour')
                        # dict_categories[job_cat_clean[ii]].append(ii)
                        # dict_categories[str(ii)].append(ii)

                        # dict_categories.setdefault(ii, []).append(df['Job ID'][idx])
                    dict_categories.setdefault(job_categories[ii], []).append(df['Job ID'][idx])
                        # dict_categories[ii] = list(set(dict_categories[ii]))

                list_names=[]                                       # Clear temp list for use in next df row
                list_cat_idx=[]                                     # Clear temp list for use in next df row
                if p: #'Print final result:
                    print(i)
                    print(i2)
                    print(i.replace(' ',''))
                # 'Get list of final result with undetected categories:
                # i= i.replace(' ','')              # 'Remove all spaces
                i= ' '.join(i.split())              # 'Get rid of all the duplicates whitespaces
                if i != '': 
                    # print(i)
                    s= ' '.join(s.split())          # 'Get rid of all the duplicates whitespaces
                    list_result.append(i)
            
            cat_count = list(set(cat_count))        # remove duplicates from the list
            if no_category in cat_count:
                cat_count.remove(no_category)       # remove 'no value' category
            if p: # Statistics - Job cattegry
                print()
                print(len(cat_count))               # number of different categories
                for ii in cat_count: print(ii)      # iterate all categories
                print('\n',dict_categories)              # print dictionary of job ids by category
            
            list_no_mach = list(set(list_no_mach))  # Remove duplicates form the list
            total_undetected= len(list_no_mach)     # Get total number of unmached categories
            list_result = list(set(list_result))    # Remove duplicates form the list

            '''Print report'''
            d_CatSum={}     # Dictionary of Job Category (summary)
            if on:
                sumcat=0
                for ii in sorted(dict_categories):
                    # print(ii)
                    # print(job_categories.index(ii))
                    d_CatSum.setdefault(ii, []).append(len(dict_categories[ii]))
                    # d_CatSum.setdefault('Idx', []).append(job_categories.index(ii))
                    pass
                    # dict_categories[ii] = list(set(dict_categories[ii]))
                    # print(ii, dict_categories[ii])
                    # print(ii,len(dict_categories[ii]))
                    sumcat=sumcat+len(dict_categories[ii])
                if p:
                    print('\n')
                    print(sumcat)                                 # sum of all values in categories
                    print(len(dict_categories))                   # sum of all cateogires in dictionary

                # #'Print undetected Job categories if recognised:
                # list_result=('1')
                # if len(list_result) == 0: 
                #     pass
                #     # dg('Number of unrecognised job categories = 0')
                # else: 
                #     print('!Number of undetected job categories ='+str(list_result)+'')


            '''Create dataframe [Job Category]'''
            if on:
                # https://stackoverflow.com/questions/20461165/how-to-convert-index-of-a-pandas-dataframe-into-a-column
                x= pd.DataFrame(d_CatSum, index=['Total'])
                x= x.transpose()
                # 'Copy index to column:
                # x['index1'] = x.index     # One way
                # x.reset_index(level=0, inplace=True)
                # x.rename(columns={'index': 'Job Category'}, inplace=True)
                # x.reset_index(level=0, inplace=True)
                #
                df_JobCategory = x
                # print(list(df_JobCategory))         #['index', 'Job Category', 'Total']
                # x= df_JobCategory.dtypes.value_counts() ;print(x,'\n')c
                # x= df_JobCategory.dtypes ;print(x,'\n')
                print(f">>> {sys._getframe().f_lineno}: Dataframe 'Job ID by Category' - created")

            '''Print undetected Job categories if recognised'''
            # list_result=('1') # Test condition if false
            if len(list_result) == 0: 
                pass
                # dg('Number of unrecognised job categories = 0')
            else: 
                print('>>>',sys._getframe().f_lineno,'!!! Number of undetected job categories = '+str(list_result)+'')
            # ex()


            '''Export dataframe dictionary'''
            dict_JobCategory = ()
            if on:
                dict_JobCategory = df_JobCategory.to_dict('dict')
                if pp: #'Dictionary - Job ID by Category:'
                    pass
                    # print()
                    # dg('Dictionary - Job ID by Category:')
                    # print(dict_JobCategory,'\n')
                x= pd.DataFrame(dict_JobCategory) #;print(x)
                if off:
                    dg('Job ID by Category:')
                    pd.set_option('display.max_colwidth', None)   # Defaulst is 50 /max col name is 29...
                    print(x,'\n')                                 # Print df
                    pd.set_option('display.max_colwidth', 30)     # Defaulst is 50 /max col name is 29...

            if off:
                x= x[:20]
                for i in x.index:
                    print(x[i])
                    print(Job_category_names[i])

            if p: # Get total number of unmached categories
                # 'Compare 'Job category' with 'Job_category_names'
                # print(len(Job_category_names))
                # print(len(df[col_name]))
                # print(df[col_name].shape[0])

                print(
                    '\nUndetected categories ('
                    +str(total_undetected)
                    +'):', 
                    list_no_mach)
                # print('  Total:',len(list_no_mach))     # Get total number of unmached categories
                # list_no_mach = list(set(list_no_mach))  # Remove duplicates form the list
                # print('  List: ',list_no_mach)          # List of undetected categories

                print('                    After:',list_result)
                # print('                After ['+str(len(list_result))+']:',list_result)

        # dg(tt());sys.exit() # >>>>>>>>>>>>>>>>>>>>>>>>>>>> 

        # str = "Messi is the best soccer player"
        # print("soccer" in str)

        # sentence = ['this','is','a','sentence']
        # print('-'.join(sentence))

        if p: # Find duplicated Job IDs
            x= df['Job Category'].value_counts() ;print(x)
            x= df.groupby('Job ID').count() ;print(x)
            x= df[col_name].value_counts() ;print(x)
        
        if p: # iterate distinct categories and count
            print()
            for i in x.index: print(x[i], i)

        if p: # List all distinct categories:
            print()
            print(list(x.index))

            for i in range(len(df[var])):
                # print(i)
                # print(df['Agency'][i])
                if df['Agency'][i] == '<no category>':
                    print(df['Agency'][i])

        '''Replace column [Job Category] [idx:9]:
        -------------------------------------------------'''
        if on:
            
            if off: # Insert new column:
                
                df.insert(10, "Job Category idx", Job_category_idx)
            if on: # Replace column
                # where 1 is the axis number (0 for rows and 1 for columns.)
                df= df.drop(['Job Category'], axis=1)
                # df= df.drop(['Posting Type','# Of Positions'], axis=1)
                df.insert(9, 'Job Category', Job_category_names)

            # print(list(df))
            # print(list(df['Job Category']))
            # print(list(df['Job Category idx']))

        '''Restore NA values in [Job Category]:
        -------------------------------------------------'''
        if on:
            # https://stackoverflow.com/questions/13445241/replacing-blank-values-white-space-with-nan-in-pandas
            # df[col_name].fillna(no_category, inplace=True)
            # df = df.replace(r'^\s*$', np.nan, regex=True)
            df[col_name] = df[col_name].replace(no_category, np.nan, regex=True) # Leave empty cells?
    # dg(tt());sys.exit() # >>>>>>>>>>>>>>>>>>>>>>>>>>>>

    '''Change columns object type to string:
    -------------------------------------------------'''
    if on:
        for col in list(df):
            if col not in (col_int + col_dat + col_dat_dmy + col_dec + col_obj):
                pass
                # df[col] = df[col].astype('category')
                # df[col] = df[col].astype('str')
                df[col] = df[col].astype('string')



        # Print all rows for specific job category:
        if off:
            for val in range(len(job_categories)): print(val, job_categories[val])
            for val in range(len(df[col_name])):
                # print(val)
                # Health
                if 'Maintenance & Operations' in df[col_name][val]:
                # if 'Community & Business Services' in df[col_name][val]:
                    print(df[col_name][val])



        # print('\n>>>',sys._getframe().f_lineno,'   t:',mt()); os.system("pause"); sys.exit() # >>>>> >>>>> >>>>> >>>>> >>>>> >>>>> >>>>> >>>>>

    '''Save to CSV after data data cleansing:
    -------------------------------------------------'''
    if save:
        # df = df.iloc[0:10, :]     # extract first 5 rows
        # df.to_csv(r'D:\D\DATA\CSV\NYC_Jobs_clean.csv', index = False, header=True)

        file_name = 'NYC_Jobs_clean.csv'
        source_adr = str(dir_path + '\\' + file_name)
        print('Clean data saved:',source_adr)
        df.to_csv(source_adr, index=False, encoding='utf8')

        # df.to_csv("NYC_Jobs_5.csv")
        # df.to_csv("NYC_Jobs_nostr.csv", index=False, encoding='utf8')

    '''Tidy Data Summary
    -------------------------------------------------'''
    if on:
        print('-'*100)
        print('>>>',sys._getframe().f_lineno,':',mt(),'sec - Tidy data')
        # print('*** Recent jobs update', col_max, '(Today) ***')


    df_old = df.copy()  # Update old dataframe

'''Data processing
================================================='''
# df_old = df.copy()  # Update old dataframe
if etl:
    ts = time.perf_counter()

    '''
    - List all columns with index number:
    - Get longest string in the column:
    - Get sum of distinct values for each column:
    - Get lists of values grouped by parameter for each column:
    - Get Column names by Data Type:
    '''


    '''List all columns with index number:
    -------------------------------------------------'''
    if off:
        print()
        #List all columns with index number:
        x= list(df.columns) ;print(x,'\n')
        for i in range(len(x)):
            print(i, x[i])
        
        # ---------------------------------------------
        print('\n>>>',sys._getframe().f_lineno,'\n')
        x= df ;print(x,'\n')
        x= df.shape ;print(x,'\n')
        x= df.shape[0] ;print(x,'\n')
        x= df.shape[1] ;print(x,'\n')
        x= df.count() ;print(x,'\n') #Count values for each column
        x= df.isna().sum() ;print(x,'\n')   #Sum all NA per col
        x= df.isnull().sum() ;print(x,'\n') #Sum all NA per col
        x= df.isna().sum().sum() ;print(x,'\n') #Sum all NA in df
        x= df.dtypes  ;print(x,'\n') #Get data types per col
        x= df.describe() ;print(x,'\n') #Desc. stats (NumCol)
        # x= df.value_count() ;print(x,'\n') #AttributeError: 'DataFrame' object has no attribute 'value_counts'
        x= df.info() # autorun #|Column|Non-Null|Count|Dtype

        x = pd.DataFrame(data=None, index=None, columns=None, dtype=None, copy=False) ;print(x,'\n')


        x= list(df.describe()) ;print(x,'\n')
        x= list(df.columns) ;print(x,'\n')
        x= list(df.columns)[0] ;print(x,'\n')
        x= list(df.columns)[3] ;print(x,'\n')

        x= df.columns ;print(x,'\n')
        x= pd.DataFrame(x) ;print(x,'\n')

        #List all columns:
        x= df.columns ;print(x,'\n')
        x= list(df.columns) ;print(x,'\n')
        for i in x: print(i)

        #List all columns with index number:
        print()
        for i in range(len(x)):
            #
            print(i, end = " ")
            print(':', end = " ")
            print(x[i])
            #
            print(i, x[i],'\n')

    '''Get longest string in the column:
    -------------------------------------------------'''
    if off:
        # Get longest string in the column:
        def longest_string(string_list):
            return max(len(str(s)) for s in string_list)

        x= list(df['Job Description'])  #string
        x= longest_string(x)
        print(x,'\n')

        # ---------------------------------------------
        # 1) 
        # Get longest string in the column (Function):
        def longest_string(string_list):
            # return max(len(s) for s in string_list)
            return max(len(str(s)) for s in string_list)

        l = ['abc', 'de', 'longest string', '1234']
        x= longest_string(l)
        print(x,'\n')

        x= list(df['Job ID'])   #integer
        x= longest_string(x)
        print(x,'\n')

        x= list(df['Salary Range To'])  #float
        x= longest_string(x)
        print(x,'\n')

        x= list(df['Job Description'])  #string
        x= longest_string(x)
        print(x,'\n')

        x= list(df['Recruitment Contact'])  #nan
        x= longest_string(x)
        print(x,'\n')

        # 2)
        # Must be object type
        x= df['Job Description'].str.len()
        print(x,'\n')
        x= max(df['Job Description'].str.len())
        print(x,'\n')

    '''Get sum of distinct values for each column:
    -------------------------------------------------'''
    if off:
        print()
        # Get sum of distinct values for each column:
        x= len(df['Level'].unique()) ;print(x,'\n')

        # ---------------------------------------------
        x= df['Level'].unique() ;print(x,'\n')
        x= df['Level'].unique().sum() ;print(x,'\n')
        x= len(df['Level'].unique()) ;print(x,'\n')

    '''Get lists of values grouped by parameter for each column:
    -------------------------------------------------'''

    x= list(df)
    col_name = []
    col_name_len=[]
    col_val = []
    col_val_full = []
    col_count = []
    col_na = []
    data_types = []
    val_len = []
    max_len = []
    col_dist = []

    #For each column name:
    for i in list(df):
        # if p:print(i,df[i].dtypes,'\n')
        # if p:print(df[i].dtypes,'\n')
        # if p:print(str(df.at[0,i])[0:5])

        #Column names:
        # col_name.append(i[0:20])
        col_name.append(i)

        #Find max char lenght from the column names: (29) ..to set pd.max.col.lenght
        for i in col_name: col_name_len.append(len(i))
        
        # NA values:
        na_c= df[i].isnull().sum()/df.shape[0]
        # col_na.append(df[i].isnull().sum())
        if na_c == 0: col_na.append('-')
        else: 
            na_c= '{:.0%}'.format(na_c)
            col_na.append(na_c)

        #Data types:
        data_types.append(df[i].dtypes)

        #Distinct values:
        col_dist.append(len(df[i].unique()))
        # col_dist.append(len(df[i].unique(dropna=True)))

        #Max string lenght:
        max_len.append(max(len(str(x)) for x in list(df[i])))

        #First row value:
        col_val_full.append(df.at[0,i])


        # if df[i].dtypes == 'object':
        #     # col_name.append(i[0:20])
        #     # col_val.append(str(df.at[0,i])[0:30])
        #     # max_len.append(max(df[i].str.len())) # max str len
        #     # if p:print(len(str(df.at[0,i])))
        #     # val_len.append(len(df.at[0,i]))
        # else:
        #     pass
        #     # col_name.append(i[0:20])
        #     # col_val.append(df.at[0,i])
        #     # max_len.append(str(max(df[i]))) # max val
        #     # max_len.append('-')
        #     # max_len.append(max(str(df.at[0,i])))
        #     # if p:print(len(str(df.at[0,i])))
        #     # if p:print(df[i].dtypes)
        #     # if p:print(df.at[0,i])
        #     # val_len.append(df.at[0,i])

        # val_len.append(len(str(df.at[0,i])))
        # col_count.append(df[i].count())
        # col_val.append(str(df.at[0,i])[0:11])

    dict_ = {
        '[Column name]': col_name,
        '[Distinct]': col_dist,
        '[Max char]': max_len,
        '[NA]': col_na,
        '[Data type]': data_types,
        '[First row value]':col_val_full,
        # 'Column first row value -------': col_val
        # 'Count': col_count,
        # '<Val len>': val_len,
        }

    df_columns= pd.DataFrame(dict_)

    # Print results:
    if off:
        print(data_types)
        for i in data_types: print(i)

        print(col_val_full[17],'\n')
        print(val_len,'\n')
        print(col_dist,'\n')
        print(max_len,'\n')
        print(col_na,'\n')
        print(col_count,'\n')
        print(col_val,'\n')
        for i in col_val: print(i)

        print(col_name,'\n')
        print(max(col_name_len),'\n')

        #Compare two list values one by one:
        print(list(df),'\n')
        print(range(len(col_name)),'\n')
        for i in range(len(col_name)): 
            print(col_name[i])  #col names 1
            print(list(df)[i])  #col names 2

        # Dictionary:
        print(dict_,'\n')
        for key in dict_:print(key, '->', dict_[key])

        # Columns:
        print(df_columns,'\n')

    '''Get Column names by Data Type:
    -------------------------------------------------'''
    # https://thispointer.com/pandas-4-ways-to-check-if-a-dataframe-is-empty-in-python/
    if off:

        x= df.dtypes.value_counts()     # built in function
        for x in list(x.index):
            df_column= df.select_dtypes(x)
            print(x,'type:\n', len(list(df_column)),'\n')

        # dtypes= []
        # dtypes= list(x.index)
        # dtypes= ['object','integer','float','datetime','bool','category']
        # for x in dtypes:pass


        x= df.dtypes.value_counts()     # built in function
        print(x,'\n')
        print(x[0],'\n')
        print(x.index,'\n')
        print(x.index[0],'\n')
        print(list(x.index),'\n')
        for i in list(x.index):print(i)
        print()

        # Iterate output to access index names and values:
        for i in range(len(x)):print(x.index[i],':', x[i])

        # df.select_dtypes('object')
        # df.empty


        # Get Column names by Data Type:
        dtypes= []
        # dtypes= ['object','integer','float','datetime','bool','category']
        dtypes= list(x.index)
        for x in dtypes:
            df_column= df.select_dtypes(x)
            print(x,'type:\n', len(list(df_column)),'\n')

        if off: 
            # Get Column names by Data Type - old
            dtypes= []
            dtypes= ['object','integer','float','datetime','bool','category']
            for x in dtypes:
                isempty= df.select_dtypes(x).empty # bool val
                if isempty: 
                    print('no',x)
                else: 
                    df_column= df.select_dtypes(x)
                    print(x,'type:\n', len(list(df_column)),'\n') # Count column names
                    print(x,'type:\n', list(df_column),'\n') # List column names
                    # print(x,'type:\n', df_column,'\n') # List column valies
        
        if p:print()

        # Get specific column values:
        #------------------------------------------------
        print(list(df),'\n') # Get list of all columns
        print(df['Post Until'],'\n') # Select column
        print(list(df['Post Until']),'\n') # convert to list

        # https://pbpython.com/pandas_dtypes.html
        # https://www.w3schools.com/python/python_datatypes.asp
        # Text Type: 	    str
        # Numeric Types: 	int, float, complex
        # Sequence Types: 	list, tuple, range
        # Mapping Type: 	dict
        # Set Types: 	    set, frozenset
        # Boolean Type: 	bool
        # Binary Types: 	bytes, bytearray, memoryview

        x= df.select_dtypes(include=['datetime64'])
        # print(x,'\n')

        # Is column date type?
        for col in df.columns:
            # print(col)
            # if df[col].dtype == 'int':
            if df[col].dtype == 'datetime64[ns]':
                pass
                print(col)

    # x= df.dtypes.value_counts() ;print(x,'\n')
# dg(tt());sys.exit() # >>>>>>>>>>>>>>>>>>>>>>>>>>>>

'''Data summary
================================================='''
if etl:
    # print('\n>>>',sys._getframe().f_lineno,'   t:',tt()); os.system("pause"); sys.exit() # >>>>> >>>>> >>>>> >>>>> >>>>> >>>>> >>>>> >>>>>

    x= date.today()
    df_row= df.shape[0]
    df_col= df.shape[1]
    df_na= df.isna().sum().sum()
    df_na_pr= df_na/(df_row*df_col)
    df_na_pr= '{:.0%}'.format(df_na_pr)
    # df_na= str(df_na)+'-('+str(df_na_pr)+')'  # 9934-(11%)
    # df_na= str(df_na)+'/'+str(df_na_pr)+''    # 9934/11%
    # df_na= str(df_na_pr)+'('+str(df_na)+')'   # 11%(9934)
    # df_na= '('+str(df_na_pr)+')/'+str(df_na)  # (11%)/9934
    df_na= str(df_na_pr)+'/'+str(df_na)+''    # 11%/9934
    # print(df_na)
    col_max= df['Process Date'].max()

    dict = {
        'Rows':[df_row], 
        'Columns':[df_col], 
        'NA':[df_na_pr]}
        # 'NA':[df_na]}
    df_stat1= pd.DataFrame(dict, index=[''])
    # print(df_stat1)

    dict1= dict
    if p:print(dict1)

    #=====================================================

    # Create dictionary of available data types:
    #------------------------------------------------------------
    x= df.dtypes.value_counts()
    x= list(x.index)
    dict2= {}
    for i in x:
        dict2[str(i)] = df.dtypes.value_counts()[i]
        # print(i,'->',dict2[str(i)])
    # print(dict2)


    if p:print(dict1,'\n')
    if p:print(dict2,'\n')

    def Merge(dict1, dict2): 
        return(dict1.update(dict2))

    Merge(dict1, dict2)
    if p:print(dict1,'\n')
    if p:print(list(dict1),'\n')
    df_stat_merged= pd.DataFrame(dict1, index=['  Total:'])
    # print('\n')
    # print(df_stat_merged,'\n')

    # Insert column separator:
    # Syntax:
    # 'DataFrameName.insert(loc, column, value, allow_duplicates = False)'
    df_stat_merged.insert(3, '|', 
                            '|')

    # df_stat_merged.insert(3, ' |  Data types:', 
    #                          ' |       Total:')
# dg(tt());sys.exit() # >>>>>>>>>>>>>>>>>>>>>>>>>>>>

'''Summary statistics - Categories
================================================='''
if etl:
    # col_list = ['Job ID','# Of Positions','Salary Frequency','Full-Time/Part-Time indicator','Job Category','Agency','Work Location','Civil Service Title','Division/Work Unit','Business Title']

    dict= {} # clear dictionary in case was used before
    col_list = ['Recent jobs update', 'Job ID', '# Of Positions']
    for i in col_list:
        if i == '# Of Positions': dict[i]= df[i].sum()
        elif i == 'Recent jobs update': dict[i]= col_max
        else: dict[i] = df[i].nunique()
    # for i in dict: print(i,':',dict[i])
    df_stat2= pd.DataFrame(dict, index=['  Total:'])
    df_stat2.insert(1, ' |'
                     , ' |')

    # print()
    # print(df_stat2)
    # dg(tt());sys.exit() # >>>>>>>>>>>>>>>>>>>>>>>>>>>>

    '''Jobs by groups category'''
    # print('\n>>>',sys._getframe().f_lineno,'   t:',tt()); os.system("pause"); sys.exit() # >>>>> >>>>> >>>>> >>>>> >>>>> >>>>> >>>>> >>>>>

    dg('Count of distinct for each category:')
    dict= {} # clear dictionary in case was used before
    col_list = ['Job Category','Agency','Work Location','Civil Service Title','Division/Work Unit','Business Title']
    # col_list = ['Job Category','Agency','Work Location','Civil Service Title','Division/Work Unit','Business Title','Career Level']
    for i in col_list: dict[i] = df[i].nunique()
    dict['Job Category'] = len(cat_count) # Replace value in dictionary:
    dict_category= dict

    # print(dict)
    # for i in dict: print(i,':',dict[i])
    # sp()
    df_stat3= pd.DataFrame(dict, index=['  Total:'])
    # print(df_stat3);print()
    # sp()

    # dg(tt());sys.exit() # >>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # replace: cat_count
    '''
    Print statistics
    ================================================='''
    # print('\n>>>',sys._getframe().f_lineno,'   t:',tt()); os.system("pause"); sys.exit() # >>>>> >>>>> >>>>> >>>>> >>>>> >>>>> >>>>> >>>>>

    if output:
        print('\n')
        # print('Imported data summary:')
        # print('-----------------------')
        # print('_______________________')
        # print(df_stat,'\n')
        # print(df_stat1)
        print(df_stat_merged)                   #Rows  Columns   NA  |  object  integer  float  datetime...
        print('\n')
        # print('Summary statistics:')          
        # print('--------------------')
        # print('____________________')
        print(df_stat2)                         #Recent jobs update  |  Job ID  # Of Positions...
        print('\n')
        # print('Jobs by groups category:')
        # print('------------------------')
        # print('________________________')
        print(df_stat3)                         #Job Category  Agency  Work Location...
        # print(df.info())
        print()
        print('-'*100)

    '''
    Data processing timer
    ================================================='''
    # print('\n>>>',sys._getframe().f_lineno,'   t:',tt()); os.system("pause"); sys.exit() # >>>>> >>>>> >>>>> >>>>> >>>>> >>>>> >>>>> >>>>>


    # print('Data processing completed! - time:', mt(), 'sec')
    # print('>>>',sys._getframe().f_lineno,'   t:',mt(),'- Data processing') #;os.system("pause") ;sys.exit() # >>>>> >>>>> >>>>> >>>>> >>>>> >>>>> >>>>> >>>>>
    # print()
    # print('*** Recent jobs update', col_max, '(Today) ***')
# dg(tt());sys.exit() # >>>>>>>>>>>>>>>>>>>>>>>>>>>>

'''Data analysis
================================================='''
if etl:
    dg('Data Analysis')
    # print('\n>>>',sys._getframe().f_lineno,'   t:',tt()); os.system("pause"); sys.exit() # >>>>> >>>>> >>>>> >>>>> >>>>> >>>>> >>>>> >>>>>

    ts = time.perf_counter()        # timestart:


    '''
    - General statistics:
    - Describe df
    - Get Column names by Data Type:
    - Get specific column values:
    - Aggregate function: Get the number of unique values for each column:
    - Print dataframe for specific value:
    - Create chart:
    '''

    '''General statistics:
    ------------------------------------------------'''
    if off:
        pass
        # df.info()             # autorun #|Column|Non-Null|Count|Dtype

        x= df ;print(x,'\n')
        x= df.shape ;print(x,'\n')
        x= df.count() ;print(x,'\n')
        x= df.isna().sum().sum() ;print(x,'\n')  # Sum NA in all dataframe 
        x= df.isnull().sum() ;print(x,'\n')      # Sum NA for each column (list) 
        x= df.dtypes ;print(x,'\n')
        x= df.describe() ;print(x,'\n')          # only for int and float...

    '''df describe()
    ------------------------------------------------'''
    if off:
        #Index(['count', 'mean', 'std', 'min', '25%', '50%', '75%', 'max'], dtype='object')

        print('\n')
        x= df.describe()        # Desc. stats (NumCol only)
        print(x.index,'\n') 
        # print(x,'\n') 

        x= x.loc[['mean','50%','min','max'], : ]
        print(x,'\n') 
        dg(tt());sys.exit() # >>>>>>>>>>>>>>>>>>>>>>>>>>>>

    '''Get Column names by Data Type:
    ------------------------------------------------'''
    if off:
        x= df.dtypes.value_counts()
        print(x,'\n')
        df.select_dtypes('object')
        df.empty
        dtypes= []
        dtypes= ['object','integer','float','datetime','bool','category']
        for x in dtypes: 
            isempty= df.select_dtypes(x).empty # bool val
            if isempty: 
                print('no',x)
            else: 
                df_column= df.select_dtypes(x)
                # print(x,'type:\n', list(df_column),'\n') # List column names
                print(x,'type:\n', df_column,'\n') # List column valies
        print()
        dg(tt());sys.exit() # >>>>>>>>>>>>>>>>>>>>>>>>>>>>

    '''Get specific column index by its name:
    ------------------------------------------------'''
    # https://stackoverflow.com/questions/13021654/get-column-index-from-column-name-in-python-pandas
    # df.columns.get_loc("pear")

    '''Get specific column values:
    ------------------------------------------------'''
    if off: # Max Date:
        # x= list(df) ;print(x,'\n')        # Get list of all columns
        # x= df['Title Code No'] ;print(x,'\n') # Select column
        # x= df.loc[:10, 'Post Until'] ;print(x,'\n')
        # x= list(x) ;print(x,'\n')          # convert to list
        # x= df.isna().sum().sum() ;print(x,'\n') # Sum na in all dataframe
        # x= date.today() ;print(x,'\n')

        # Get values for selected column:
        x= df['Title Code No'] ;print(x,'\n')
        x=list(x) ;print(x,'\n')    # List values
        # for i in x: print(i)        # Iterate values

        # '1002A'

        if on: # Max Date:
            col_list = ['Posting Date','Post Until','Posting Updated','Process Date']
            for i in col_list:
                # x= df[i].min()
                x= df[i].max()
                print(x,'-',i)
            print()


            # x= df['Posting Date'].max() ;print(x,'\n') # Select column
            # x= df['Post Until'].max() ;print(x,'\n') # Select column
            # x= df['Posting Updated'].max() ;print(x,'\n') # Select column
            # x= df['Process Date'].min() ;print(x,'\n') # Select column
            # # x= df.iloc[0:3, [30]]
            # # x=list(x)
            # # x=x.to_list
            # # x= df.at[10,'Post Until']
            # # x= df.ix[0:9,1]

        dg(tt());sys.exit() # >>>>>>>>>>>>>>>>>>>>>>>>>>>>

    '''Print dataframe for specific columns values:
    ------------------------------------------------'''
    if off:  #['Posting Type']
        # https://cmdlinetips.com/2018/02/how-to-subset-pandas-dataframe-based-on-values-of-a-column/
        
        filter_val= df['Posting Type']=='Ext/Int'
        # filter_val= df['Posting Type']=='Internal'
        # filter_val= df['Posting Type']=='External'


        # print(x)
        # print(x.shape)

        # x= df[filter_val]
        # x= df['Posting Type'][filter_val]
        # x= df.loc[:,['Job ID','Posting Type','Business Title']][filter_val]
        # x= df.iloc[:,[0,2,4]][filter_val]
        x= df.iloc[:,[0,2,5,4]][filter_val]
        print()
        print(x,'\n')
        dg(tt());sys.exit() # >>>>>>>>>>>>>>>>>>>>>>>>>>>>

    if off:  #['Job Category']
        print()
        # print(list(df))

        # filter_val= df['Title Code No']=='1002A'
        # x= df.iloc[:,[0,7]][filter_val]

        # filter_val= df['Job Category']=='*Not Available'
        val_ToFilter=''
        col_ToSort=''

        col_names = [
            'Posting Date',
            'Job ID',
            # 'Post Until',
            'Job Category',
            # 'Business Title'
            ]
        #--------------------------------------------
        col_ToFilter = 'Job Category'
        #--------------------------------------------
        col_ToSort = 'Posting Date'
        # col_ToSort = 'Job Category'
        #--------------------------------------------
        val_ToFilter = no_category
        # val_ToFilter = '_Clerical & Administrative Support'
        # val_ToFilter = '_Community & Business Services'
        # val_ToFilter = '_Information Technology & Telecommunications'
        # val_ToFilter = '_Maintenance & Operations'
        # val_ToFilter = 'Administration & Human Resources'
        # val_ToFilter = 'Building Operations & Maintenance'
        # val_ToFilter = 'Communications & Intergovernmental Affairs'
        # val_ToFilter = 'Constituent Services & Community Programs'
        # val_ToFilter = 'Engineering, Architecture & Planning'
        # val_ToFilter = 'Finance, Accounting & Procurement'
        # val_ToFilter = 'Health'
        # val_ToFilter = 'Legal Affairs'
        # val_ToFilter = 'Policy, Research & Analysis'
        # val_ToFilter = 'Public Safety, Inspections & Enforcement'
        # val_ToFilter = 'Social Services'
        # val_ToFilter = 'Technology, Data & Innovation'

        print(val_ToFilter,'\n')

        
        # filter_val= df[col_ToFilter]==val_ToFilter                  # values to filter
        filter_val= df[col_ToFilter].str.contains(val_ToFilter)     # values to filter (wildcard)
        x= df.loc[:,col_names]                                      # select columns

        "Error with NA"
        # x= x.fillna('na')
        x= x[filter_val]                                            # vilter values

        x= x.sort_values(by=[col_ToSort], ascending=True)           # sort df
        # print(x)

        # pd.set_option('display.max_colwidth', None)   #Defaulst is 50 /max col name is 29...
        # pd.set_option('display.max_colwidth', 130)   #Defaulst is 50 /max col name is 29...
        pd.set_option('display.max_colwidth', 90)   #Defaulst is 50 /max col name is 29...
        print(x,'\n')
        pd.set_option('display.max_colwidth', 30)   #Defaulst is 50 /max col name is 29...
        print()
        dg(tt());sys.exit() # >>>>>>>>>>>>>>>>>>>>>>>>>>>>

    if off:  #['Job Category'] by [Posting Date]
        print()
        # print(list(df),'\n')

        # filter_val= df['Title Code No']=='1002A'
        # x= df.iloc[:,[0,7]][filter_val]

        # filter_val= df['Posting Type']=='*Not Available'
        val_ToFilter=''
        col_ToSort=''

        col_names = [
            'Posting Date',
            # 'Job ID',
            'Posting Type',
            # 'Post Until',
            # 'Job Category',
            # 'Business Title'
            ]
        #--------------------------------------------
        col_ToFilter = 'Job Category'
        #--------------------------------------------
        col_ToSort = 'Posting Date'
        # col_ToSort = 'Job Category'
        #--------------------------------------------
        # val_ToFilter = no_category
        # val_ToFilter = '_Clerical & Administrative Support'
        # val_ToFilter = '_Community & Business Services'
        # val_ToFilter = '_Information Technology & Telecommunications'
        # val_ToFilter = '_Maintenance & Operations'
        # val_ToFilter = 'Administration & Human Resources'
        # val_ToFilter = 'Building Operations & Maintenance'
        # val_ToFilter = 'Communications & Intergovernmental Affairs'
        # val_ToFilter = 'Constituent Services & Community Programs'
        # val_ToFilter = 'Engineering, Architecture & Planning'
        # val_ToFilter = 'Finance, Accounting & Procurement'
        # val_ToFilter = 'Health'
        # val_ToFilter = 'Legal Affairs'
        # val_ToFilter = 'Policy, Research & Analysis'
        # val_ToFilter = 'Public Safety, Inspections & Enforcement'
        # val_ToFilter = 'Social Services'
        # val_ToFilter = 'Technology, Data & Innovation'

        # filter_val= df[col_ToFilter]==val_ToFilter                  # values to filter
        filter_val= df[col_ToFilter].str.contains(val_ToFilter)     # values to filter (wildcard)
        x= df.loc[:,col_names]                                      # select columns
        # x= x[filter_val]                                            # vilter values
        x= x.sort_values(by=[col_ToSort], ascending=True)           # sort df

        # # Print dataframe:
        # # pd.set_option('display.max_colwidth', None)   #Defaulst is 50 /max col name is 29...
        # # pd.set_option('display.max_colwidth', 130)   #Defaulst is 50 /max col name is 29...
        # pd.set_option('display.max_colwidth', 90)   #Defaulst is 50 /max col name is 29...
        # print(x,'\n')
        # pd.set_option('display.max_colwidth', 30)   #Defaulst is 50 /max col name is 29...
        # print()



        ''' Export df to dict and dict to df: '''
        # x= x.to_dict('dict') ;print(x,'\n')
        x= x.to_dict('list') ;print(x,'\n')
        # from pandas import Timestamp
        x= pd.DataFrame(x) ;print(x,'\n')

        # Save df as new df:
        df_JobCategory_PostingDate = x
        print(df_JobCategory_PostingDate,'\n')

        dg(tt());sys.exit() # >>>>>>>>>>>>>>>>>>>>>>>>>>>>
        # print('\n>>>',sys._getframe().f_lineno,'   t:',mt()) #;os.system("pause") ;sys.exit() # >>>>> >>>>> >>>>> >>>>>


    '''Aggregate function: Get the number of unique values for each column:
    ------------------------------------------------'''
    # Print df stats sorted by column:
    # print(df_columns.sort_values(by=['Distinct'], ascending=False, na_position='last'))

    # Test aggregate:
    if off:
        # x= df.nunique() ;print(x,'\n')
        # x= df.agg(['count', 'size', 'nunique']) ;print(x,'\n')
        # x= df.groupby('Posting Type').agg(['count', 'size', 'nunique']).stack() ;print(x,'\n')

        # x= df.groupby('Posting Type').agg(['count', 'nunique']).stack() ;print(x,'\n')
        # x= df.groupby('Full-Time/Part-Time indicator').agg(['count', 'nunique']).stack() ;print(x,'\n')
        # x= df.groupby('Salary Frequency').agg(['count', 'nunique']).stack() ;print(x,'\n')


        # # Aggregate manual:
        # x= df.loc[:,['Job ID','Salary Frequency']]  #;print(x,'\n')
        # x= x.groupby('Salary Frequency').agg(['count', 'nunique']).stack() ;print(x,'\n')
        # print(x,'\n')
        # print(list(x))
        # print(list(x.index),'\n')

        # dg(tt());sys.exit() # >>>>>>>>>>>>>>>>>>>>>>>>>>>>


        # Aggregate with variables function:
        #--------------------------------------------
        # x= df.count() ;print(x,'\n')          #Count values for each column

        col_ToGroup = 'Job ID'
        # col_ToGroup = 'Work Location'
        # col_ToGroup = 'Posting Date'
        # col_ToGroup = 'Job Category'
        # col_ToGroup = 'Posting Type'
        # col_ToGroup = '# Of Positions'

        # col_GroupBy = 'Full-Time/Part-Time indicator'   #[2]
        # col_GroupBy = 'Posting Type'                    #[3]    [Ext/Int, Internal, External]
        # col_GroupBy = 'Salary Frequency'                #[3]
        # col_GroupBy = 'Title Classification'            #[5]
        # col_GroupBy = 'Career Level'                    #[6]
        # col_GroupBy = 'Level'                           #[15]
        # col_GroupBy = 'Agency'                          #[53]
        col_GroupBy = 'Job Category'                    #[122]
        # col_GroupBy = 'Work Location'                   #[225]
        # col_GroupBy = 'Civil Service Title'             #[285]
        # col_GroupBy = 'Division/Work Unit'              #[636]
        # col_GroupBy = 'Business Title'                  #[1112]

        # 'Other columns:
        # col_GroupBy = 'Process Date'                    #[1]
        # col_GroupBy = 'Recruitment Contact'             #[1]
        # col_GroupBy = '# Of Positions'                  #[33]
        # col_GroupBy = 'Residency Requirement'           #[64]
        # col_GroupBy = 'Salary Range From'               #[494]
        # col_GroupBy = 'Preferred Skills'                #[1140]
        # col_GroupBy = 'Recruitment Contact'             #[1]
        # col_GroupBy = 'Posting Date'                    #[1]

        aggrBy = [
            'count', 
            # 'size', 
            # 'nunique'
            ]

        x= df.loc[:,[col_ToGroup,col_GroupBy]]  #;print(x,'\n')         # Select df columns
        x[col_GroupBy]= x[col_GroupBy].fillna('[NA]')                   # Fill <NA> if any

        x= x.groupby(col_GroupBy).agg(aggrBy).stack() #;print(x,'\n')   # Group and aggregate by
        # x= x.sort_values(by=[col_ToGroup], ascending=False)             # Sort table

        # Print outputs:
        print()
        print(col_ToGroup,'-      count:', df[col_ToGroup].count())
        print(col_ToGroup,'-   distinct:', df[col_ToGroup].nunique())
        print(col_ToGroup,'- duplicates:', df[col_ToGroup].count()-df[col_ToGroup].nunique(),'\n')
        print(x)
        print('NA:',df[col_GroupBy].isna().sum(),'\n')     #Sum all NA per col
        # print(col_GroupBy,'- Values count:',df[col_GroupBy].count())     #Count values for each column

        
        # print(x.shape)
        # print(list(x))
        # print(list(x.index),'\n')
        # for i in list(x.index): print(i[0])    
        # for i, row in x.iterrows(): print(i[0], row[col_ToGroup])
        dg(tt());sys.exit() # >>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # Group [Posting Date] by [Job Category]:
    if on:
        pd.set_option('display.max_colwidth', None)
        col_ToGroup = 'Job Category'
        col_GroupBy = 'Posting Date'
        aggrBy = ['count']

        x= df.loc[:,[col_ToGroup,col_GroupBy]] # Select df columns
        # print(x,'\n')
        x= x.sort_values(by=[col_GroupBy], ascending=True) # Sort table
        dg('Posting Date by Job Category:')
        pd.set_option('display.max_colwidth', 50)   # Defaulst is 50 /max col name is 29...
        print(x,'\n')
        pd.set_option('display.max_colwidth', None)   # Defaulst is 50 /max col name is 29...

        x[col_GroupBy]= x[col_GroupBy].fillna('[NA]')                   # Fill <NA> if any

        x= x.groupby(col_GroupBy).agg(aggrBy).stack() #;print(x,'\n')   # Group and aggregate by
        x= x.sort_values(by=[col_ToGroup], ascending=False)             # Sort table
        # print('\nGroup ['+col_ToGroup+'] by ['+col_GroupBy+']:')
        # print(x)
        # print('NA:',df[col_GroupBy].isna().sum(),'\n')     #Sum all NA per col
        pd.set_option('display.max_colwidth', 30)
        # dg(tt());sys.exit() # >>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # dg(tt());sys.exit() # >>>>>>>>>>>>>>>>>>>>>>>>>>>>


    '''Data analysis timer
    ================================================='''
    # print('\n>>>',sys._getframe().f_lineno,'   t:',tt()); os.system("pause"); sys.exit() # >>>>> >>>>> >>>>> >>>>> >>>>> >>>>> >>>>> >>>>>


    # print('Data processing completed! - time:', mt(), 'sec')
    # print('>>>',sys._getframe().f_lineno,'   t:',mt(),'- Data analysis') 
    # print()
    # print('*** Recent jobs update', col_max, '(Today) ***')

    # Specified statistics:
    #------------------------------------------------
    if off:
        # 'Count distict values, use nunique:
        x= df['Agency'].nunique()
        print(x,'\n')
        # 'Count only non-null values, use count:
        x= df['Agency'].count()
        print(x,'\n')
        # 'Count total values including null values, use size attribute:
        x= df['Agency'].size
        print(x,'\n')


        x= (df)
        print(x,'\n')
        # 'frequency count for column_ :
        x= df.Agency.value_counts()
        print(x,'\n')
        x= df['Agency'].value_counts()
        print(x,'\n')
        x= df['Posting Type'].value_counts()
        print(x,'\n')

        for x in df['Posting Type'].value_counts():
            print(x)
        print()


        # 'Multi-column frequency count :
        x = df.groupby(['Posting Type']).count()
        print(x,'\n')
        x= df.groupby(['Agency', 'Posting Type']).size()
        print(x,'\n')


        ''' Distinct values '''
        x= df
        # print(x,'\n')
        # 'Count distinct Posting Type for each Agency:
        x= df.groupby('Agency')['Posting Type'].nunique()
        print(x,'\n')

        # Count distinct 'Agency' for each 'Posting Type':
        x= df.groupby('Posting Type')['Agency'].nunique()
        print(x,'\n')



        # -----------------------------------------------
        print()
        # df.info()
        x= df.isnull().sum()
        print(x,'\n')
        x= df.dtypes
        print(x,'\n')
        x= df.describe()
        print(x,'\n')
        x= list(df)
        print(x,'\n')
        x= df.iloc[2] # 2, 155
        print(x,'\n')
        x= list(df.iloc[2, 2]) # ['I', 'n', 't', 'e', 'r', 'n', 'a', 'l'] 
        print(x,'\n')
        x= df.loc[:10, 'Agency']
        x= list(x)
        print(x,'\n')


    # print('Data processing completed! - time:', mt(), 'sec')
    # print('>>>',sys._getframe().f_lineno,'   t:',tt(),'- Code execution') #;os.system("pause") ;sys.exit() # >>>>> >>>>> >>>>> >>>>> >>>>> >>>>> >>>>> >>>>>

    '''Pause Code
    ================================================='''
    if output:

        # print('\n>>>',sys._getframe().f_lineno,'   t:',tt()); os.system("pause"); sys.exit() # >>>>> >>>>> >>>>> >>>>> >>>>> >>>>> >>>>> >>>>>

        # https://stackoverflow.com/questions/7180914/pause-resume-a-python-script-in-middle

        print('')
        def pause():
            programPause = input("Press <ENTER> to exit...\n")

        if code_pause:
            # pause()             # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> [Press ENTER]
            os.system("pause")  # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> [Press ANY key]

    '''Continue to other outputs
    ================================================='''
    ts = time.perf_counter()        # timestart:

    # if debug_mode: sys.exit() # >>>>>>>>>>>>>>>>>>>>>>>>>>>>
    if off:
        print('\n')
        print('Column list:')
        print('------------')
        # print('____________')
        print(list(df))
        # print()
        print()
        print(df)           # Print data frame
        print()

        if code_pause:
            # pause()             # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> [Press ENTER]
            os.system("pause")  # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> [Press ANY key]

    if output:
        
        # print()
        # dg('Dictionary - Job ID by Category:')
        # print(dict_JobCategory,'\n')
        # print('\n')
        print('>>>',sys._getframe().f_lineno,':',tt(),'sec - Column Statistics:')
        print()
        dg('Dataset overview:')
        df_columns= df_columns.sort_values(by=['[Distinct]'], ascending=False, na_position='last') # Sort
        print(df_columns)           # Print data frame

    '''Function describe() - get part of the output only
    ================================================='''
    if on:
        #Index(['count', 'mean', 'std', 'min', '25%', '50%', '75%', 'max'], dtype='object')

        print('\n')
        df_desc= df.describe()        # Desc. stats (NumCol only)
        # print(df_desc.index,'\n')     # Desc. stats df index
        # print(df_desc,'\n') 
        # x= df_desc.loc[['mean','50%','min','max'], : ] ;print(x,'\n') 
        # x= df_desc.loc[['min','max'],['Salary Range From', 'Salary Range To']] ;print(x,'\n') 

        x= df_desc.loc[['min','50%','max'], : ] ;print(x,'\n') 
        x= df_desc.loc[['mean'], : ] ;print(x,'\n') 

        # print('-'*100)
        # print('>>>',sys._getframe().f_lineno,':',mt(),'sec - Column statistics') #;os.system("pause") #;sys.exit() # >>>>> >>>>> >>>>> >>>>> >>>>> >>>>> >>>>> >>>>>

'''Code total time'''
print('-'*100)
print('>>>',sys._getframe().f_lineno,':',tt(),'sec - Code total time\n') 
if code_pause: sp()

'''Charts
================================================='''
if charts:
    import matplotlib.pyplot as plt
    import seaborn as sns
    # import plotly.express as px
    
    # print('\n>>>',sys._getframe().f_lineno,'   t:',mt(),'- Exit code') ;os.system("pause") ;sys.exit() # >>>>> >>>>>
    ts = time.perf_counter()        # timestart:
    # print('-'*100)
    dg('Charts:')
    # ex()
    file_name=()
    # print()
    # pause()             # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> [Press ENTER]
    # os.system("pause")  # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> [Press ANY key]


    def dfGroupBy(GroupCol,GroupByCol): #'Group dataframe by column
        aggrBy = ['count']
        x= df.loc[:,[GroupCol,GroupByCol]]                      # Select df columns
        x[GroupByCol]= x[GroupByCol].fillna('[NA]')             # Fill <NA> if any
        x= x.groupby(GroupByCol).agg(aggrBy).stack()            # Group and aggregate by
        # x= x.sort_values(by=[GroupCol], ascending=False)        # Sort table
        # print(x,'\n')

        # Rename/append index value:
        # https://stackoverflow.com/questions/19851005/rename-pandas-dataframe-index
        idx_list=[]
        for idx, row in x.iterrows(): 
            # print(idx, row[GroupCol])     # Print index and row
            idx_list.append(idx[0])
        x.index = idx_list
        abc = x

        # print('Group '+GroupCol+' by '+GroupByCol+':')    # Print title
        dfGroupBy= x
        return dfGroupBy
    def DfToDict(df): #'Convert Dataframe to Dictionary
        dict_type = 'dict'
        DfToDict = df.to_dict(dict_type)
        return DfToDict
    def DfToList(df):       #'Convert Dataframe to List
        dict_type = 'list'
        DfToDict = df.to_dict(dict_type)
        return DfToDict
    def DictToDf(dict): #'Convert Dictionary to Dataframe
        return pd.DataFrame(dict)
    if off: #'Test functions
        GroupCol = 'Job ID'
        # GroupCol = 'Posting Date'
        # ------------------------
        # GroupByCol = 'Full-Time/Part-Time indicator'
        GroupByCol = 'Posting Type'
        # GroupByCol = 'Salary Frequency'
        # GroupByCol = 'Career Level'
        # GroupByCol = 'Agency'
        # GroupByCol = 'Civil Service Title'
        # GroupByCol = 'Job Category'
        dg()
        x= dfGroupBy(GroupCol,GroupByCol) ;print('\n',x)
        x= DfToDict(x) ;print('\n',x)
        x= DictToDf(x) ;print('\n',x)
        ex(tt())


    if etl:pass
    else: # Load Tidy Data
        pass
        print('Loading data...')
        dir_path = 'D:\D\DATA\CSV'
        n_rows=None
        # n_rows=100
        # n_rows=550  #includes: Daily 1
        file_name = 'NYC_Jobs_clean.csv'
        source_adr = str(dir_path + '\\' + file_name)
        print(source_adr)
        df = pd.read_csv(source_adr, nrows=n_rows)
        # df= df.fillna('na') #Fill NA
    df_old = df.copy()  # Update old dataframe (Archive)
    # df = df_old.copy()  # Update new dataframe (Restore)

    '''Check data'''
    if off:
        x = df.iloc[:,[0,1,2,3,10,14]]; print(list(x))
        x = df.iloc[:,[2,3,14,29]]; print(list(x))
        print(x)
        print(x.shape)
        print(df_old.shape)
    print(df.shape)
    print()
    print('[Job ID]:            count:',df['Job ID'].count())
    print('[# Of Positions] :     sum:',df['# Of Positions'].sum())
 
    "GroupBy"
    if off:
        x= list(df)
        x= df.groupby(['Salary Frequency']).size()
        x= df.groupby(['Salary Frequency','Posting Type']).size()
        x= df.groupby(['Posting Type','Salary Frequency']).size()

        "List all columns with index number:"
        print() ;print(x,'\n')
        for i in range(len(list(x))): print(list(x)[i])     # List all columns (df)
        for i in range(len(list(x))): print(i, list(x)[i])  # List all columns with index number (df)
        ex(tt())

    "Chart: ['Posting Type', 'Full-Time/Part-Time indicator', 'Salary Frequency'] ~ 3 x plot: "
    if on:
        # dg('Dashboard:')
        file_name = 'Dashboard.png'

        if off: #'Get data into Dictionaries - manyally
            dict_1 = {'Job ID': {'F': 1287, 'P': 49, '[NA]': 89}}
            dict_2 = {'Job ID': {'Annual': 1280, 'Daily': 13, 'Hourly': 132}}
            dict_3 = {'Job ID': {'Ext/Int': 1098, 'External': 8, 'Internal': 319}}
            dict_list = [
                dict_3,
                dict_1,
                dict_2,
                ]
        if on: #'Get data into Dictionaries
            # dg('Dictionaries:')
            if on: #'Dict 1:
                GroupCol = 'Job ID'
                GroupByCol = 'Posting Type'
                # GroupByCol = 'Career Level'
                # GroupByCol = 'Agency'
                # GroupByCol = 'Civil Service Title'
                x= dfGroupBy(GroupCol,GroupByCol)
                # print('\n',x)
                dict_1= DfToDict(x)
                # print(dict_1)     #'Print dictionary
                # print('\n',DictToDf(dict_1))
            if on: #'Dict 2:
                GroupCol = 'Job ID'
                GroupByCol = 'Salary Frequency'
                x= dfGroupBy(GroupCol,GroupByCol)
                # print('\n',x)
                dict_2= DfToDict(x)
                # print(dict_2)     #'Print dictionary
                # print('\n',DictToDf(dict_2))
            if on: #'Dict 3:
                GroupCol = 'Job ID'
                GroupByCol = 'Full-Time/Part-Time indicator'
                x= dfGroupBy(GroupCol,GroupByCol)
                # print('\n',x)
                dict_3= DfToDict(x)
                # print(dict_3)     #'Print dictionary
                # print('\n',DictToDf(dict_3))
            dict_list = [dict_1, dict_2, dict_3]
            # print(dict_list)

            # dg('Exit code'); sys.exit() #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        if off: #'Some plot
            for i in range(len(dict_list)):
                print('\n',i)
                # print(dict_list[i])
                dfg= pd.DataFrame(dict_list[i]) ;print(dfg)
                print(list(dfg))
                # plt.subplot(3 ,1, 1+i)
                # dfg.plot.bar(figsize=(3.5,2), fontsize=9, rot=0)
                dfg.plot.bar(y='Job ID',figsize=(3.5,2), fontsize=9, rot=0, legend=False)
            plt.show()
        
        '''Plot Styles:'''
            # plt.style.use('seaborn')
            # plt.style.use('seaborn-dark')
            # plt.style.use('seaborn-darkgrid')
            # plt.style.use('seaborn-dark-palette')
            # plt.style.use('seaborn-colorblind')
            # plt.style.use('seaborn-muted')
        '''Chart'''
        if on:
            "Figure parameters:"
            plt.figure(figsize=(9,2))
            plt.suptitle('New York City - current job postings',fontweight='bold', fontsize=12)
            # plt.title('Number of job postings by category')
            plt.subplots_adjust(
                left=0.1,
                right=0.95,
                top=0.70,
                bottom=0.2,
                wspace=0.3,
                hspace=0.5)
            
            chart_titles=[
                'PostingType',
                'Full-Time/Part-Time indicator',
                'Salary Frequency']
            
            chart_styles=[
                'seaborn',
                'seaborn-pastel',
                'ggplot',
                # 'darkgrid',
                # 'seaborn-colorblind'
                ]

            # fig = plt.figure()
            # axes = fig.subplots(nrows=2, ncols=2)

            # plt.subplots(sharex=False, sharey=True)

            # dg('Exit code'); sys.exit() #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            
            for i in range(len(dict_list)):

                "Dataframe:"
                # print('\n',i)
                # print(dict_list[i])
                dfg= pd.DataFrame(dict_list[i]) #;print(dfg)
                # print(list(dfg))
                
                "Dataframe series axes:"
                # x=df.index.values   ;print(x,'\n')
                x=dfg.index.tolist()  #;print(x,'\n')   # Labels
                # y=df['Job ID']      ;print(y,'\n')
                y=list(dfg['Job ID']) #;print(y,'\n')    # height/width


                "Plot style:"
                plt.style.use(chart_styles[i])

                "Subplots orientation:"
                # fig, axs = plt.subplots(3, sharex=False, sharey=True, gridspec_kw={'hspace': 0.5, 'wspace': 0})
                # plt.subplots(sharex=False, sharey=True, gridspec_kw={'hspace': 0.5, 'wspace': 0})
                # plt.subplot(311+i)
                #
                # plt.subplot(3 ,1, 1+i)      # stack verticaly  
                plt.subplot(1 ,3, 1+i)      # stack horizontaly 
                # plt.subplot(2 ,2, 1+i)      # test
                
                "Plot data:"
                plt.bar(x,height=y)     # plot verticaly
                # plt.barh(x,width=y)     # plot horizontaly

                "Add figure details:"
                # dfg.plot.bar(figsize=(3.5,2), fontsize=9, rot=0)
                # dfg.plot.bar(y='Job ID',figsize=(3.5,2), fontsize=9, rot=0, legend=False)
                plt.title(chart_titles[i], fontsize=9)

                "Bars value labels:"
                x= list(dfg['Job ID'])
                for i, value in enumerate(x):
                    # print(i)
                    # print(value)
                    plt.text(
                        i + 0, 
                        value + 75,         # at the top
                        # value/dfg[i]+0,   # at the bottom
                        str(value),       # value
                        # dfg[i],           # value
                        color='darkslategrey',  # darkslategrey navy black
                        fontsize=9, 
                        # fontweight='bold',
                        horizontalalignment='center',
                        verticalalignment='center',
                        )

                "Axes limit"
                colMax=dfg['Job ID'].max() #;print(colMax)
                plt.ylim(0,colMax*1.3)

            "Save figure:"
            if save:
                source_adr = str(dir_path + '\\' + file_name)
                print('\nChart saved:',source_adr)
                plt.savefig(source_adr)

            # plt.savefig(r'D:\D\DATA\Outputs\NYC Jobs\Dashboard.png')
            # plt.tight_layout()    # co to robi?
            # dg('Exit code'); sys.exit() #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

            "Show figure:"
            dg('3 x plot:')
            if plt_show:plt.show()
        
        if off:
            # https://matplotlib.org/3.1.0/gallery/subplots_axes_and_figures/subplots_demo.html
            fig, axs = plt.subplots(3, sharex=False, sharey=True, gridspec_kw={'hspace': 0.5, 'wspace': 0})
            # fig, axs = plt.subplots(1,3)
            fig.suptitle('Vertically stacked subplots')
            
            for i in range(len(dict_list)):
                print(i)
                dfg= pd.DataFrame(dict_list[i]) ;print(dfg)


                # axs[0].plot(x, y)
                # axs[i].plot(dfg)
                axs[i].plot(dfg)

                # plt.subplot(3 ,1, 1+i)
                # dfg.plot.bar(figsize=(3.5,2), fontsize=9, rot=0)
                # dfg.plot(kind='bar', alpha=0.75, rot=0, label="Presence / Absence of cultural centre")

            if plt_show:plt.show()

        # #This will create the bar graph for poulation
        # plt.subplot(2,1,1)
        # plt.plot(figsize=(3.5,2), fontsize=9, rot=0)
        # plt.ylabel('Population in Millions')

        # #The below code will create the second plot.
        # plt.subplot(2,1,2)
        # plt.plot(figsize=(3.5,2), fontsize=9, rot=0)
        # plt.ylabel('GDP in Billions')

        # plt.show()

        if off:
            df=pd.DataFrame({
                'x': range(1,101), 
                'y': np.random.randn(100)*15+range(1,101), 
                'z': (np.random.randn(100)*15+range(1,101))*2 })
            # Cut your window in 1 row and 2 columns, and start a plot in the first part
            plt.subplot(121)
            plt.plot( 'x', 'y', kind='bar', data=df, marker='o', alpha=0.4)
            plt.title("A subplot with 2 lines")
            # And now add something in the second part:
            plt.subplot(122)
            plt.plot( 'x','z', data=df, linestyle='none', marker='o', color="orange", alpha=0.3)
            # plt.savefig('PNG/#194_matplotlib_subplot1.png', dpi=96)
            # Show the graph
            if plt_show:plt.show()

        # dfg.plot.bar(figsize=(3.5,2), fontsize=9, rot=0)

        # Job ID
        if off:
            # First part:
            df= pd.DataFrame(dict_1) ;print(df,'\n')
            # x=df.index.values   ;print(x,'\n')
            x=df.index.tolist()   ;print(x,'\n')
            # y=df['Job ID']      ;print(y,'\n')
            y=list(df['Job ID']) ;print(y,'\n')
            #
            plt.subplot(131)
            plt.bar(x,height=y)     # plot verticaly
            # plt.barh(x,width=y)     # plot horizontaly
            # plt.plot(x, y, kind='bar', data=df, marker='o', alpha=0.4)
            # df.plot.bar(rot=0)
            plt.title("title 1")

            # Second part:
            df= pd.DataFrame(dict_2) ;print(df,'\n')
            x=df.index.values   ;print(x,'\n')
            y=df['Job ID']      ;print(y,'\n')
            #
            plt.subplot(132)
            plt.bar(x,height=y)     # plot verticaly
            plt.title("title 2")

            # Third part:
            df= pd.DataFrame(dict_3) ;print(df,'\n')
            x=df.index.values   ;print(x,'\n')
            y=df['Job ID']      ;print(y,'\n')
            #
            plt.subplot(133)
            plt.bar(x,height=y)     # plot verticaly
            plt.title("title 3")

            # plt.savefig('PNG/#194_matplotlib_subplot1.png', dpi=96)
            # Show the graph
            if plt_show:plt.show()

        # dfg[:10].plot(kind = 'bar',subplots=True, layout = (4,3))
        # plt.show()

        # plt.figure(1)
        # # plt.subplot(2 ,1, 1)
        # dfg.plot.bar(figsize=(3.5,2), fontsize=9, rot=0)

        # plt.figure(2)
        # # plt.subplot(2 ,1, 2)
        # dfg.plot.bar(figsize=(3.5,2), fontsize=9, rot=0)
        # plt.show()

        # fig = plt.figure()
        # axes = fig.subplots(nrows=2, ncols=2)
        # plt.show()

    "Chart: ['Job ID','Job Category']"
    if on:
        # https://www.python-graph-gallery.com/barplot/

        # Job ID by Job Category
        # From module: Tidy Data - Column [Job Category] (16) / Export to Dict: Export to dict "dict_JobCategory" (line: 1111)
        # dg('Job Postings by Category:')
        file_name = 'Job Postings by Category.png'

        "Set Dataframe from dictionary"
        if etl:pass
        else:
            dict_JobCategory= {'Total': {'Administration & Human Resources': 132, 'Building Operations & Maintenance': 106, 'Communications & Intergovernmental Affairs': 55, 'Constituent Services & Community Programs': 119, 'Engineering, Architecture & Planning': 347, 'Finance, Accounting & Procurement': 141, 'Health': 109, 'Legal Affairs': 141, 'Policy, Research & Analysis': 210, 'Public Safety, Inspections & Enforcement': 196, 'Social Services': 75, 'Technology, Data & Innovation': 186, '_Clerical & Administrative Support': 11, '_Community & Business Services': 6, '_Information Technology & Telecommunications': 14, '_Maintenance & Operations': 5, '_Not Available': 2}}
        # print(dict_JobCategory)
        dfg= pd.DataFrame(dict_JobCategory)
        dg('Job ID by Category:')
        pd.set_option('display.max_colwidth', None)
        print(dfg)
        # pd.set_option('display.max_colwidth', 50)
        # sp()

        # dg('Exit code'); sys.exit() #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

        # 'Copy index to new column:
        # df.reset_index(level=0, inplace=True)
        # df.rename(columns={'index': 'Job Category'}, inplace=True)
        # df.reset_index(level=0, inplace=True)

        
        column= 'Total'
        dfg= dfg.sort_values(by=[column], ascending=True) # Sort df
        # dfg= dfg.sort_values(by=[column], ascending=True, na_position='last')
        # print('\n',dfg)

        # print('\n>>>',sys._getframe().f_lineno,'   t:',tt()); os.system("pause"); sys.exit() # >>>>> >>>>> >>>>> >>>>> >>>>> >>>>> >>>>> >>>>>

        # Chart: Bar plot - horizontal
        #----------------------------------------------------------------

        # import matplotlib.pyplot as plt
        # Colours:
        # https://python-graph-gallery.com/196-select-one-color-with-matplotlib/

        "seaborn"
        # import seaborn as sns
        #104 Seaborn Themes:
        # https://python-graph-gallery.com/104-seaborn-themes/
        # sns.set_style(style=None)
        # sns.set_style("dark")
        sns.set_style("darkgrid")
        # sns.set_style("white")
        # sns.set_style("whitegrid")

        # import plotly.express as px

        # Bars - horizontal:
        dfg.plot.barh(
            width=0.7,
            # figsize=(7,5),                                      #.Figure size
            # fontsize=9,                                         #.Font size
            # rot=0,                                              #.Rotate labels
            # color=['black', 'red', 'green', 'blue', 'cyan'],    #.Different color for each bar
            # color=(0.2, 0.4, 0.6, 0.6),                         #.Color RGB
            edgecolor='lightsteelblue',                         #.Color of border
            color='lightsteelblue',

            # Error:
            # color_continuous_scale='Inferno',     # error
            # cmap="BuPu",                          # error
            # alpha=0.4                     
            )

        # Axis:
        # ax_names = '_Not Available' # er
        plt.xticks(
            color='dimgrey',
            # fontweight='bold',
            )
        plt.yticks(
            color='darkslategrey',
            fontweight='bold',
            )

        # Bars labels:
        x= list(dfg[column])
        for index, value in enumerate(x):
            plt.text(
                value + 9, 
                index - .25, 
                str(value), 
                color='darkslategrey',  # darkslategrey navy black
                fontsize=9, 
                # fontweight='bold'
                )

        # Title:
        plt.title(
            'Number of job postings by category', 
            # 'Number of jobs \nby categories', 
            loc='left',     # 'center', 'right', 'left'
            horizontalalignment='center', 
            verticalalignment='bottom',   #('top', 'bottom', 'center', 'baseline')
            fontsize='14', 
            fontweight='bold', 
            color = 'steelblue', 
            )

        # Labels:
        plt.xlabel(
            'Job postings', 
            fontweight='bold', 
            color = 'steelblue', 
            # fontsize='15', 
            horizontalalignment='center'
            )
        plt.ylabel(
            'Job Category', 
            fontweight='bold', 
            color = 'steelblue', 
            # fontsize='15', 
            horizontalalignment='center'
            )

        # Legend:
        # https://matplotlib.org/3.2.1/tutorials/intermediate/legend_guide.html
        # https://stackoverflow.com/questions/44413020/how-to-specify-legend-position-in-matplotlib-in-graph-coordinates
        vloc= "lower right"     # "upper left", "lower left", "upper right", "center right", "lower right"
        plt.legend(loc=vloc)
        # ax.legend(bbox_to_anchor=(1,0), loc="lower right",  bbox_transform=fig.transFigure)

        # Margins:
        plt.subplots_adjust(
            left= 0.60, 
            right = 0.95,
            bottom= 0.15,
            top = 0.91
            )

        # Remove labels:
        # plt.tick_params(labelbottom='off')

        # Limit:
        colMax=dfg[column].max() #;print(colMax)
        # plt.ylim(0,5)
        plt.xlim(0,colMax*1.2)

        # Borders:
        # plt.spines['bottom'].set_color('red')
        # plt.spines["bottom"].set_color("red")
        # plt.spines["left"].set_color("orange")

        # Background:
        # ax = plt.gca()
        # ax.set_facecolor('silver')   # aliceblue


        "Save figure:"
        if save:
            source_adr = str(dir_path + '\\' + file_name)
            print('\nChart saved:',source_adr)
            plt.savefig(source_adr)

        # Code time:
        # print('>>>',sys._getframe().f_lineno,':',tt(),'sec - [Job Categories]') #;os.system("pause") ;sys.exit() # >>>>> >>>>> >>>>> >>>>>

        # Show graphic:
        if plt_show:plt.show()
        # dg('Job Categories')

        # Exit code:
        # print('\n>>>',sys._getframe().f_lineno,) ;sys.exit() # >>>>>>>>>>>>>>>>>>>>>>>>>>>>

    "Chart: NA values"
    if on:
        # https://www.geeksforgeeks.org/python-visualize-missing-values-nan-values-using-missingno-library/

        # https://github.com/ResidentMario/missingno
        
        file_name = 'NA Values.png'
        # import pandas as pd

        # #--------------------------------------------------------
        # import missingno as msno 
        # msno.matrix(df) # Visualize missing values as a matrix 
        # # msno.bar(df)    # Visualize values as a bar chart 
        # # msno.heatmap(df) # Visualize the correlation between the number of 

        #--------------------------------------------------------
        # https://dev.to/tomoyukiaota/visualizing-the-patterns-of-missing-value-occurrence-with-python-46dj
        # import seaborn as sns
        x= df
        # x= x.T # Transpose
        sns.heatmap(x.isnull(), cbar=False)
        if plt_show:plt.show()

        "Save figure:"
        if save:
            source_adr = str(dir_path + '\\' + file_name)
            print('\nChart saved:',source_adr)
            plt.savefig(source_adr)
        # ex()

    "seaborn: statistical data visualization"
        # https://seaborn.pydata.org/index.html
        # https://seaborn.pydata.org/examples/index.html

    "Funnel Chart in Python"
    if on:
        # https://plotly.com/python/
        # https://plotly.com/python/funnel-charts/

        if etl: # Build from scratch:
            # df= df_stat3 ;print('\n',df)
            # x= x.transpose()    # transpose
            # df= df.T              # transpose

            # x= dict_category  # Saved dict from etl

            dict= {} # clear dictionary in case was used before
            col_list = ['Job Category','Agency','Work Location','Civil Service Title','Division/Work Unit','Business Title']
            # col_list = ['Job Category','Agency','Work Location','Civil Service Title','Division/Work Unit','Business Title','Career Level']
            for i in col_list: dict[i] = df[i].nunique()
            dict['Job Category'] = len(cat_count) # Replace value in dictionary:
            x= dict

            # print('\n',x)
            # ex()

            # Transform dict:
            number=[]; category=[]
            for i in x: 
                # print(i,':',data[i])
                category.append(i)
                number.append(x[i])
            # print(number)
            # print(stage)
            x = {}
            x["value"] = number
            x["category"] = category
            # print('\n',x)

            # Sort dictionary:
            x= DictToDf(x) #;print('\n',x)
            # x= x.sort_values(by=['number'], ascending=False) #;print('\n',x)
            x= x.sort_values(by=['value'], ascending=True)
            dg('Funnel Chart:')
            print(x)
            x= DfToList(x) #;print('\n',x)
            data= x
            # print('\n',data)
        else: # Dictionary
            # Descending:
            # data= {'number': [1238, 695, 301, 244, 53, 15, 5], 'stage': ['Business Title', 'Division/Work Unit', 'Civil Service Title', 'Work Location', 'Agency', 'Job Category', 'Career Level']}

            # Ascending:
            data= {'number': [5, 15, 53, 244, 301, 695, 1238], 'stage': ['Career Level', 'Job Category', 'Agency', 'Work Location', 'Civil Service Title', 'Division/Work Unit', 'Business Title']}
        # print('\n',data)

        if off: #Show chart:
            import plotly.express as px
            fig = px.funnel(data, x='value', y='category')
            fig.show()



    "Caveats!!!"
    # https://www.data-to-viz.com/caveats.html

    "Sankey Diagram with Python and Plotly"
    # https://www.python-graph-gallery.com/sankey-diagram/
    # https://www.python-graph-gallery.com/sankey-diagram-with-python-and-plotly

    "Network chart"
    # https://www.python-graph-gallery.com/network-chart/


'''Exit procedure:
================================================='''
if on:
    dg(tt()) # >>>>>>>>>>>>>>>>>>>>>>>>>>>>
    sp('END') # >>>>>>>>>>>>>>>>>>>>>>>>>>>>
    del df, pd, sys#, gc
