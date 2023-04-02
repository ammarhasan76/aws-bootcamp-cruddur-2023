# Week 3 — Decentralized Authentication

This unit is about integrating Cognito user authentication (ie decentralised, and not natively built in the application)

## Create Cognito User Pool

AWS Console -> Cognito -> Create

Configuration:  
- Sign-in experience:
  - Cognito User Pool (not federated)
  - Cognito user pool sign-in options: username & email sign-in enabled
  - User name requirements: nothing selected

- Secueity Requirements
  - Password Policy: select Cognito defaults
  - MFA: no MFA
  - User account recovery: enable self-service recovery, email only

- Sign-up Experience:
  - Self-service sign-up: enable
  - Attribute Verification and User Account Confirmation: eanble allow Cognito to send verifcations messages, email verification method, keep original attribute when update pending, choose email as the stay-active attribute
  - Required Attributes: name (and no custom attributes)
  - Message Delivery: enable Cognito (SES will need a custom domain), choose your local region, default from

- Integrate App:
  - User pool name: crudder-user-pool
  - Hosted authentication pages: no 
  - Initial app client: Public client, app client name = crudder, no client secret (server-side), 
  - Advanced: no changes
  - Attribute read and write perms: no changes
  
- Review & Create: create!

Evidence:  
![image](https://user-images.githubusercontent.com/22940535/229351382-973378a2-c2f1-45ca-b3dc-1011a9ee9560.png)



  
## Install AWS Amplify

