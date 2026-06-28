### Installations

1. [Anaconda](https://www.anaconda.com/products/distribution#download-section)
2. [MySQL Workbench](https://dev.mysql.com/downloads/workbench/)
3. [MySQL Server](https://dev.mysql.com/downloads/mysql/)

Execute in conda env python 3.7.16 : 
```
conda create --name Steg python=3.7.16
conda activate Steg
cd api/python
pip install -r ai-server-requirements.txt
```
Edit path in ai-server-make-activate.cmd and ai-server-validate-activate.cmd (Sohan -> your username)


Execute in conda env python 3.11 :
```
conda create --name LOGIN python=3.11
conda activate LOGIN
cd api/python
pip install -r login-server-requirements.txt
```
Edit path in login-server-activate.cmd (Sohan -> your username)


Extract utils.rar into api/python folder (replace any files if prompted): 
```
https://drive.google.com/file/d/1XeH8IrYYcyD4Ks-jbC4H2Mg7ZggoPav5/view?usp=sharing
```

In MYSQL Workbench (replace <mysql username> in ALTER command)
```
ALTER USER '<mysql username>'@'localhost' IDENTIFIED WITH mysql_native_password BY 'root';

create database mini_project;

use mini_project;

CREATE TABLE client_credentials (
    id INT AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    company_name VARCHAR(255) NOT NULL,
    uid VARCHAR(255) NOT NULL,
    PRIMARY KEY (id),
    UNIQUE (email),
    UNIQUE (uid)
);
```
In frontend folder : 
```
npm i --force
```
To run all : 
Go to api/python and run all cmd files. Go to frontend and run all cmd files. All servers will start automatically.


Papers to read
```
https://arxiv.org/pdf/1904.05343
```
