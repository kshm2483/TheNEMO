# Clustering(군집화)

특성이 비슷한 데이터끼리 묶어주는 머신러닝 기법 .



- *minimal sum of squared distance*

$$
\sum\limits_{m=1}^k\sum\limits_{t_{mi}}(C_m - t_{mi})^2
$$



## 1. KMeans

n개의 중심점을 찍은 후에

이 중심점에서 각 점간의 거리의 합이 최소화가 되는 중심점 n의 위치를 찾는다.



### EXAMPLE

```
(1, 1) (1, 2) (2, 1) (5, 5) (5, 6) (6, 5) (7, 7)
```



#### (1) 임의로 데이터를 클러스터링하고 중심점 구하기

`Class A` : (1, 1) (1, 2) (5, 5) => center : (7/3, 8/3)

`Class B` : (2, 1) (7, 7) (5, 6) (6, 5) => center:(20/4, 19/4)



#### (2) 구한 중심점으로 데이터를 다시 클러스터링한 후 중심점 구하기

`Class A` :  (1, 1) (2, 1) (1, 2) => center : (4/3, 4/3) 

`Class B` :  (5, 5) (6, 5) (5, 6) (7, 7) => center : (23/4, 23/4)



#### (3) 구한 중심점으로 데이터를 다시 클러스터링

`Class A` :  (1, 1) (2, 1) (1, 2)

`Class B` :  (5, 5) (6, 5) (5, 6) (7, 7)



#### (4) No change => STOP.





## 2. Hierarchical



## 3. EM(Gaussian Mixture)



## 4. KNN

5. kmenas again