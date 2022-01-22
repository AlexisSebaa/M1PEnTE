import pandas as pd


df = pd.read_csv('athlete_events.csv') #Fichier data original

df.drop(df[df['Year'] < 2000].index, inplace=True) #Supprime les JO avant 2000
df.drop(df[df['Season'] == 'Winter'].index, inplace=True)#Supprime les JO d'Hiver
df = df.drop_duplicates(subset = ["ID"])
df.drop(['ID','Name', 'Age', 'Team', 'NOC', 'Games', 'Year', 'Season', 'City', 'Event', 'Medal' ], axis=1, inplace=True)
#Supprime les catégories qui ne nous intéressent pas

df.dropna(subset = ['Height'], inplace=True) #enleve les athletes de taille inconnue
df.dropna(subset = ['Weight'], inplace=True) #enleve les athletes de poids inconnu
df.reset_index(drop=True, inplace=True)

sexe = df['Sex'] == 'M' #Critere de differenciation sur le genre
dfM = df[sexe] # Fichier dataframe Homme
dfF = df[~sexe] # Fichier dataframe Femme
dfM.drop(['Sex'], axis=1, inplace=True)
dfF.drop(['Sex'], axis=1, inplace=True)

# Basketball 

dfbM = dfM.iloc[::]
dfbM.drop(dfbM[dfbM['Sport'] != 'Basketball'].index, inplace=True)
dfbM.drop(['Sport'], axis=1, inplace=True)
dfbM.reset_index(drop=True, inplace=True)
dfbM.to_excel('databasketH.xlsx', index=False)


dfbF = dfF.iloc[::]
dfbF.drop(dfbF[dfbF['Sport'] != 'Basketball'].index, inplace=True)
dfbF.drop(['Sport'], axis=1, inplace=True)
dfbF.reset_index(drop=True, inplace=True)
dfbF.to_excel('databasketF.xlsx', index=False)


# Volleyball 

dfvM = dfM.iloc[::]
dfvM.drop(dfvM[dfvM['Sport'] != 'Volleyball'].index, inplace=True)
dfvM.drop(['Sport'], axis=1, inplace=True)
dfvM.reset_index(drop=True, inplace=True)
dfvM.to_excel('datavolleyH.xlsx', index=False)

dfvF = dfF.iloc[::]
dfvF.drop(dfvF[dfvF['Sport'] != 'Volleyball'].index, inplace=True)
dfvF.drop(['Sport'], axis=1, inplace=True)
dfvF.reset_index(drop=True, inplace=True)
dfvF.to_excel('datavolleyF.xlsx', index=False)


# Fencing

dffM = dfM.iloc[::]
dffM.drop(dffM[dffM['Sport'] != 'Fencing'].index, inplace=True)
dffM.drop(['Sport'], axis=1, inplace=True)
dffM.reset_index(drop=True, inplace=True)
dffM.to_excel('datafencingH.xlsx', index=False)

dffF = dfF.iloc[::]
dffF.drop(dffF[dffF['Sport'] != 'Fencing'].index, inplace=True)
dffF.drop(['Sport'], axis=1, inplace=True)
dffF.reset_index(drop=True, inplace=True)
dffF.to_excel('datafencingF.xlsx', index=False)

# Swimming

dfsM = dfM.iloc[::]
dfsM.drop(dfsM[dfsM['Sport'] != 'Swimming'].index, inplace=True)
dfsM.drop(['Sport'], axis=1, inplace=True)
dfsM.reset_index(drop=True, inplace=True)
dfsM.to_excel('dataswimH.xlsx', index=False)

dfsF = dfF.iloc[::]
dfsF.drop(dfsF[dfsF['Sport'] != 'Swimming'].index, inplace=True)
dfsF.drop(['Sport'], axis=1, inplace=True)
dfsF.reset_index(drop=True, inplace=True)
dfsF.to_excel('dataswimF.xlsx',index=False)

# Triathlon

dftM = dfM.iloc[::]
dftM.drop(dftM[dftM['Sport'] != 'Triathlon'].index, inplace=True)
dftM.drop(['Sport'], axis=1, inplace=True)
dftM.reset_index(drop=True, inplace=True)
dftM.to_excel('datatriH.xlsx', index=False)

dftF = dfF.iloc[::]
dftF.drop(dftF[dftF['Sport'] != 'Triathlon'].index, inplace=True)
dftF.drop(['Sport'], axis=1, inplace=True)
dftF.reset_index(drop=True, inplace=True)
dftF.to_excel('datatriF.xlsx',index=False)

##end 

