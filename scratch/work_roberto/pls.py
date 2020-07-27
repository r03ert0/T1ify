
from skimage import io
from sklearn.cross_decomposition import PLSRegression
from skimage.util.shape import view_as_windows
import numpy as np
from matplotlib import pyplot as plt

t1 = io.imread("jpgs/t1w_OAS30001_MR_d0757_3.jpg")
t2 = io.imread("jpgs/t2w_OAS30001_MR_d0757_3.jpg")

R=5
R1=3

window_shape = (R, R)
window_shape1 = (R1, R1)

n1 = view_as_windows(t1, window_shape)
n2 = view_as_windows(t2, window_shape1)

# print(t1.shape,n1.shape)

X=[]
for i in range(n1.shape[0]):
    for j in range(n1.shape[1]):
        X.append(np.ravel(n1[i,j]))
X=np.array(X)

Y=[]
for i in range(n2.shape[0]):
    for j in range(n2.shape[1]):
        Y.append(np.ravel(n2[i,j]))
Y=np.array(Y)
pls2 = PLSRegression(n_components=2)

pls2.fit(X,Y)

Y_pred = pls2.predict(X)

o = int(R**2/2+0.5)
o1 = int(R1**2/2+0.5)

print("R^2:", pls2.score(X, Y))

# plt.scatter(Y_pred[:,o],Y[:,4],alpha=0.01)

t2_pred = np.zeros((n2.shape[0],n2.shape[1]))
n=0
for i in range(n2.shape[0]):
    for j in range(n2.shape[1]):
        t2_pred[i,j] = Y_pred[n,o1]
        n=n+1
plt.gray()
plt.imshow(t2_pred)
plt.show()
