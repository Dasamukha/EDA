def repair(dfname):
    no = ['no','NO','No','N','n']
    repair_col = []
    final_col = []
    for col in dfname.columns:
        repair_col.append(col)


    for x in repair_col:
        x = x.strip()
        x = x.capitalize()
        x = x.replace(' ', '_')
        print(x)
        var = input('Change '+ x +" name to : (if You don't want to change type no)")
        print('var',var)
        if var in no:
            # final_col.append(x)
            print(x)
        else:
            print(var)
            # final_col.append(x)


    # print(final_col)






    # dfname.columns = final_col
#%%
