# Akiba API

Django app that allows you to create a wallet and deposit via MPESA Express 

## Project Description

Users can create accounts linked to their mobile numbers and deposit money via M-Pesa

## To run this project you need:
  - Django 4.1.3 (Recommended)
  
## API Endpoints
  - /auth/api/token/
    - desc: get jwt
    - method: post 
    - body: username, password
  - /auth/api/token/refresh/ 
    - desc: refresh expired token
    - method: post 
    - body: refresh_token
  - /auth/register/
    - desc: create new user
    - method: post 
    - body: username, password
  - /wallet/
    - desc: trigger mpesa stk push
    - method: post
    - body: amount
    - auth: Bearer <token>
  - /wallet/account
    - desc: get account details
    - method: get
    - auth: Bearer <token>
  - /wallet/account/
    - desc: create new e-wallet account
    - method: post
    - body: account_no
    - auth: Bearer <token>
    
   
    
  
