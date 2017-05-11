import pandas as pd

c="../../data/phi_c.csv"
theta="../../data/phi_theta.csv"
q="../../data/phi_q.csv"
w="../../data/phi_w.csv"

phi_c=pd.read_csv(c, index_col=0, usecols=[1,2]).dropna().sort_index()
phi_t=pd.read_csv(theta, index_col=0, usecols=[1,2]).dropna().sort_index()
phi_q=pd.read_csv(q, index_col=0, usecols=[1,2]).dropna().sort_index()
phi_w=pd.read_csv(w, index_col=0, usecols=[1,2]).dropna().sort_index()

phi_c.to_csv("../../data/phi_c2.csv", index=True)
phi_t.to_csv("../../data/phi_t2.csv", index=True)
phi_q.to_csv("../../data/phi_q2.csv", index=True)
phi_w.to_csv("../../data/phi_w2.csv", index=True)

