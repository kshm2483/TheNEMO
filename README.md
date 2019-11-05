<p align="center">이미지</p><h1 align="center">NEMO</h1><p align="center">
    Movie Recommendation Project
</p>



<h1>Table of Contents</h1>

[TOC]

# Getting Started

## Prerequisites

- `front` 폴더에서 npm을 install 합니다.

  ```bash
  $ npm install
  ```

- `backend` 폴더에서 pip를 setup합니다.

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



# Deployment

- `backend`서버를 구동시킵니다. `backend`폴더 수준에서 명령어를 입력합니다.

  ```bash
  $ python manage.py runserver
  ```

- `frontend` 서버를 구동시킵니다. `frontend` 폴더 수준에서 명령어를 입력합니다.

  ```bash
  $ npm run serve
  ```

  



# Project Description

## Model structure

![image](/uploads/0be39f97fe1031dd2502d469a8501aa0/image.png)

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

| Field Name | Data Type | Example | Description | Result |
| ---------- | --------- | ------- | ----------- | ------ |
| id         | Int | 1 | movie의 pk값 | 1,2,3,.. |
|title|Char|"toy story(1995)"|제목||
|genres|Char|["Comedy", "Drama"]|장르||
|group|Int|1|cluster시 속해있는 그룹|1,2,3...|
|poster_url|Text|"http:/ ..."|poster url||
|backdroup_url|Text|"dji4Fm0g..."|backdrop url||
|overview|Text||영화 설명||
|adult|Bool|True|성인등급영화확인|True, False|
|recommend_movie|Char|1,3,4|recommendation algorithm 활용시 비슷한 영화|1,2,3...|



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

