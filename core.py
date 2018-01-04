import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import NearestNeighbors


def recommend(rain, temp, irri):
    df = pd.read_csv('./data.csv')

    k_df = df[['Total Rainfall', 'Temperature', 'Need Irrigation']].as_matrix()

    scaler = StandardScaler().fit(k_df)
    k_df = scaler.transform(k_df)

    # rain = input("Enter rainfall in mm:")
    # temp = input("Enter temperature in degree Celsius:")
    # irri = input("Do you have irrigation?")

    if irri == 'y':
        ir = 1
    else:
        ir = 0

    new_mat = np.array([[rain, temp, ir]])
    new_mat = scaler.transform(new_mat)

    neigh = NearestNeighbors(n_neighbors=3)
    neigh.fit(k_df)

    pred = neigh.kneighbors(new_mat, return_distance=False)
    return df.loc[pred[0]]

if __name__ == "__main__":
    print(recommend(2000, 13, 1))
