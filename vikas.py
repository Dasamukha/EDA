def repair(dfname):
    no = ['no', 'NO', 'No', 'N', 'n']
    repair_col = []
    final_col = []
    for col in dfname.columns:
        repair_col.append(col)
    print(repair_col)

    for x in repair_col:
        x = x.strip()
        x = x.capitalize()
        x = x.replace(' ', '_')
        print(x)
        var = input('Change ' + x + " name to : (if You don't want to change type no)")
        print('var', var)
        if var in no:
            final_col.append(x)
            # print(x)
        else:
            # print(var)
            final_col.append(var)
    print(final_col)
    dfname.columns = final_col


def describe_all(dfname):
    print('Size of dataframe :', dfname.shape)
    print('----------------------------')
    print('Null Values in each Column ka Total\n', dfname.isnull().sum())
    print('----------------------------')
    print('Duplicate Values Count :', dfname.duplicated().sum())


def obj_type(dfname):
    obj = []
    for x in dfname.columns:
        if dfname[x].dtypes == 'object':
            obj.append(x)

    print('Object Columns Are :', obj)
