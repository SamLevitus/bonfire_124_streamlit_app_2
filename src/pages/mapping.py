def locator (col,val):
    a_list=[]
    for i in range(len(df[col])):
        if len(df[col].iloc[i].split(','))>1:
            if val in df[col].iloc[i].split(','):
                a_list.append(i)
        else:
            if val == df[col].iloc[i]:
                a_list.append(i)
    return a_list

df.iloc[locator('states','TX')]