# Akiba API

Django app that allows you to create a wallet and deposit via MPESA Express 

## Project Description

Users can create accounts linked to their mobile numbers and deposit money via M-Pesa

## To run this project you need:
  - Django 4.1.3 (Recommended)
  
## API Endpoints
  - /auth/api/token/ ==get jwt==
    - method: post 
    - body: username, password
  - /auth/api/token/refresh/ 
    - method: post 
    - body: refresh_token
  - /auth/register/
    - method: post 
    - body: username, password
  - /wallet/
    - method: post
    - body: amount
    - auth: Bearer <token>
  - /wallet/
    - method: get
    - auth: Bearer <token>
  - /wallet/account/
    - method: post
    - body: account_no
    - auth: Bearer <token>
    
   
    
  
