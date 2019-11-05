<p align="center"><img src="https://user-images.githubusercontent.com/45934087/67922620-9c06f280-fbee-11e9-90cb-58494b87a912.png"></img></p><h1 align="center">The-NextMovie</h1><p align="center">
    Movie Recommendation Project
</p>


<h1>Table of Contents</h1>

[TOC]

# Project Description

GitHub: [NEMO](<https://github.com/kyeah01/NEMO_movieRecommendation>)

 **The-NextMovie**(이하, NEMO)는 영화 평점 및 유저 데이터 기반 **`영화 맞춤 추천 사이트`** 입니다. 사용자의 취향 및 직업군, 성별, 나이 등을 `Clustering Algorithm` 과 `Recommand Algotirhm` 기반으로 **유사한 유저**를 선별하고 **선호하는 영화**를 추천해주며, 아직 감상하지 않은 영화에 대한 **예상 점수**를 계산해 주어 사용자에게 수준 높은 문화 활동의 경험을 장려하고자 제작되었습니다.



# Getting Started

## Prerequisites

- `front` 폴더에서 npm 모듈을 install 합니다.

  ```bash
  $ npm install
  ```

- `backend` 폴더에서 pip 모듈을 setup합니다.

  ```bash
  $ pip install -r requirements.txt
  ```



## Backend setup

- model 작업을 위한 migrate가 필요합니다.
  `backend` > `manage.py` 파일을 실행시킵니다.

  ```bash
  $ python manage.py migrate
  ```



## Data setup

- `backend` > `db.json` 파일을 load시킵니다.

  ```bash
  $ ./manage.py loaddata db.json
  ```

  (5분여정도 걸립니다.)

  데이터 분석을 위해 사용하는 fuzzywuzzy 라이브러리와 관련하여 `warnings.warn('Using slow pure-python SequenceMatcher. Install python-Levenshtein to remove this warning')`이 뜰 수 있습니다. 당황하지 않고 기다리면 완료됩니다.



# Deployment

- `backend`서버를 구동시킵니다. `backend`폴더 수준에서 명령어를 입력합니다.

  ```bash
  $ python manage.py runserver
  ```

- `frontend` 서버를 구동시킵니다. `frontend` 폴더 수준에서 명령어를 입력합니다.

  ```bash
  $ npm run serve
  ```



# 서비스 소개

## 핵심기술

### 사용자 평점 기반 영화 추천 서비스

------

![image](https://user-images.githubusercontent.com/45934087/67922695-da9cad00-fbee-11e9-8efb-6fcdfe867bb2.png)

 신규 가입 사용자는 **NEMO**에서 제공하는 영화 목록에서 자신이 이미 시청한 영화에 대한 평점을 기입합니다. 해당 과정을 통해 사용자가 선호하는 영화에 대한 정보를 수집하고 이를 기반으로 **추천 알고리즘**을 시행합니다.



![image](https://user-images.githubusercontent.com/45934087/67922765-19326780-fbef-11e9-8328-ddcdc24144aa.png)

  **NEMO**의 메인 페이지에서는 자신이 기입한 영화 정보를 기반으로 다양한 형태의 영화 추천 서비스를 제공합니다. **Matrix Factorization**기술을 통해 사용자의 취향 (장르 등)에 부합하는 영화 들 중 예상 점수가 높은 영화들을 추천 받을 수 있도록 구현하였습니다. 또한, 이외에도 최신 영화, 선호 장르별 추천등의 기능을 함께 제공합니다.



### 빠른 검색

------

![image](https://user-images.githubusercontent.com/45934087/67923208-81357d80-fbf0-11e9-8814-6f0b7b03bd8e.png)

 영화 정보를 Client의 State에 분할, 저장하여 영화 검색 시 서버와의 통신을 최소, 최적화하였습니다. 이를 통해 빠른 검색이 가능 하도록 하였으며,  분할 저장된 정보를 이용, **무한 스크롤**을 구현함으로써 한층 더 높은 수준의 UX를 구현하고자 하였습니다.



### 평점 관리 기능

------

![image](https://user-images.githubusercontent.com/45934087/67923287-bcd04780-fbf0-11e9-9294-196ed897c431.png)

![image](https://user-images.githubusercontent.com/45934087/67923258-a32f0000-fbf0-11e9-966c-1a93c6672ad8.png)

 사용자의 프로필 페이지에서 기존에 평가한 영화에 대한 평점을 수정, 관리 할 수 있으며 해당 영화에 대한 자세한 정보를 제공 받을 수 있도록 구현하였습니다. 이렇게 수정된 평점 역시 이후의 **추천 영화**에 영향을 미침으로써, 사용자의 취향의 변화등에도 빠르게 대응 할 수 있도록 구현하였습니다.



### 유사 유저 정보 제공

------

![image](https://user-images.githubusercontent.com/45934087/67924863-0b7fe080-fbf5-11e9-80de-64aa1acf6818.png)

 자신과 취향이 유사한 사용자들을 제공해 줌으로써 색다른 형식으로 영화를 추천 받을 수 있는 시스템입니다. 해당 사용자의 프로필을 방문하여, 자신이 아직 감상하지 못한 영화 목록을 확인 할 수 있을 뿐만 아니라, 유사한 유저들 간의 커뮤니티를 구성할 수 있도록 구현하였습니다. 또한, 이후 구현될 **추천 영화 패키징 서비스**의 초석으로써 구현되었습니다.

 	※ **추천 영화 패키징**이란, 자신이 감명깊게 보았던 영화 들을 하나의 리스트로 묶어 구독자들에게 제공해주는 부가 상품으로, 사용자들의 사이트 사용 욕구 증진 및 부가적 수익 창출을 위한 시스템을 목표로 하고 있습니다.



### 5가지 유형의 추천 알고리즘

------

![image](https://user-images.githubusercontent.com/45934087/67923389-0c167800-fbf1-11e9-81d8-839e8fc93034.png)

 **NEMO**의 관리자는 **Admin Page**를 통해 사이트에 사용될 알고리즘 5종류 각각 **K-means**, **Hierarchical**, **Gaussian Mixture Model**,**KNN Algotirhm**,**Matrix Factorization**을 손쉽게 변경할 수 있도록 구현하였습니다.



## Model structure

![image](https://user-images.githubusercontent.com/45934061/68007100-f0c56e80-fcbd-11e9-8b6c-1d9c2b8f0265.png)

### Profile

| Field Name        | Data Type | Example   | Description                                 | Result              |
| ----------------- | --------- | --------- | ------------------------------------------- | ------------------- |
| user              | Int       | 1         | user의 pk값                                 | 1,2,3,...           |
| gender            | Char      | "F"       | 성별                                        | "F", "M"            |
| age               | Int       | 23        | 나이                                        | 1,2,3,...           |
| occupation        | Char      | student   | 직업                                        | student...          |
| group             | Int       | 1         | cluster시 속해있는 그룹                     | 1,2,3...            |
| description       | Char      | "hello"   | profile의 한 줄 자기소개                    | ""                  |
| image             | Image     |           | thumnail                                    |                     |
| recommend_user    | Char      | "user1"   | recommendation algorithm 활용시 비슷한 유저 | user1,user2...      |
| subscription      | Bool      | True      | 구독되있는지 여부 확인                      | True, False         |
| subscription_date | Char      | "1502394" | 구독시점의 타임스탬프                       | 12343512, 12341233, |



### Movie

| Field Name      | Data Type | Example             | Description                                 | Result      |
| --------------- | --------- | ------------------- | ------------------------------------------- | ----------- |
| id              | Int       | 1                   | movie의 pk값                                | 1,2,3,..    |
| title           | Char      | "toy story(1995)"   | 제목                                        |             |
| genres          | Char      | ["Comedy", "Drama"] | 장르                                        |             |
| group           | Int       | 1                   | cluster시 속해있는 그룹                     | 1,2,3...    |
| poster_url      | Text      | "http:/ ..."        | poster url                                  |             |
| backdroup_url   | Text      | "dji4Fm0g..."       | backdrop url                                |             |
| overview        | Text      |                     | 영화 설명                                   |             |
| adult           | Bool      | True                | 성인등급영화확인                            | True, False |
| recommend_movie | Char      | 1,3,4               | recommendation algorithm 활용시 비슷한 영화 | 1,2,3...    |



### Rating

| Field Name  | Data Type | Example   | Description                 | Result              |
| ----------- | --------- | --------- | --------------------------- | ------------------- |
| movie       | FK        |           | 영화 FK                     |                     |
| user        | FK        |           | 유저 FK                     |                     |
| rating      | Int       | 3         | 평점                        | 1,2,3,4,5           |
| rating_date | Char      | "1502394" | 평점 남긴 시점의 타임스탬프 | 12343512, 12341233, |



### ClusterModel

| Field Name     | Data Type | Example | Description                                                  | Result          |
| -------------- | --------- | ------- | ------------------------------------------------------------ | --------------- |
| cluster_choice | Bool      | True    | cluster모델이 선택되어있는지 확인하는 column, <br />True : cluster 모델 선택되어 있음<br />False : KNN, matrix factorization등 다른 recommend model 선택되어있음 | True, False     |
| based          | Char      | "user"  | user / movie                                                 | "user", "movie" |
| method         | Int       | 1       | 1 : k-means algorithm이 선택되어있음<br />2 : gaussian mixture algorithm이 선택되어있음<br />3 :  hierarchical algorithm이 선택되어 있음 | 1,2,3           |
| params         | Int       | 3       | cluster의 갯수                                               | 2,3,4...        |





----

##### 사용 기술 및 도구

- Vuex (3.1.1)
- Vue.js (2.6.10)
- SCSS (sass-loder : 8.0.0, node-sass: 4.12.0)
- vue CLI (3.12.0)
- Django (2.2.4)
- Django REST Framework (3.10.2)
- Django REST Framework-jwt (1.11.0)
- python (3.6.8)
- numpy (1.17.0)
- pandas (0.25.1)
- virtualenv (16.7.7)
- K-means, Hierarchical, Gaussian Mixture Model, KNN Algotirhm, Matrix Factorization



##### NEMO Project`s Developer

------

![image](https://user-images.githubusercontent.com/45934087/67922599-8bef1300-fbee-11e9-8fd9-c1712f3f2069.png) 