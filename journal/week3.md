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

```
cd /frontend-react-js
npm i aws-amplify --save
# --save adds it to package.json, --save-dev or -D to save to dev dependencies
```
 
## Configure Amplify

Add the necessary env vars to docker_compose.yml to enable Amplify in the frontend, `AWS_DEFAULT_REGION` already defined, so added gitpod variables for the Cognito User Pool ID and Cognito App Client ID  
```
...
  frontend-react-js:
    environment:
      ...
      REACT_APP_AWS_PROJECT_REGION: "${AWS_DEFAULT_REGION}"
      REACT_APP_AWS_COGNITO_IDENTITY_POOL_ID:
      REACT_APP_AWS_COGNITO_REGION: "${AWS_DEFAULT_REGION}"
      REACT_APP_AWS_USER_POOLS_ID: "${AWS_USER_POOL_ID}" 
      REACT_APP_CLIENT_ID: "${AWS_COGNITO_CLIENT_ID}"
...
```

Add the following to app.js to hook Cognito pool to the app  
```
import { Amplify } from 'aws-amplify';

Amplify.configure({
  "AWS_PROJECT_REGION": process.env.REACT_APP_AWS_PROJECT_REGION,
  "aws_cognito_identity_pool_id": process.env.REACT_APP_AWS_COGNITO_IDENTITY_POOL_ID,
  "aws_cognito_region": process.env.REACT_APP_AWS_COGNITO_REGION,
  "aws_user_pools_id": process.env.REACT_APP_AWS_USER_POOLS_ID,
  "aws_user_pools_web_client_id": process.env.REACT_APP_CLIENT_ID,
  "oauth": {},
  Auth: {
    // We are not using an Identity Pool
    // identityPoolId: process.env.REACT_APP_IDENTITY_POOL_ID, // REQUIRED - Amazon Cognito Identity Pool ID
    region: process.env.REACT_AWS_PROJECT_REGION,           // REQUIRED - Amazon Cognito Region
    userPoolId: process.env.REACT_APP_AWS_USER_POOLS_ID,         // OPTIONAL - Amazon Cognito User Pool ID
    userPoolWebClientId: process.env.REACT_APP_AWS_USER_POOLS_WEB_CLIENT_ID,   // OPTIONAL - Amazon Cognito Web Client ID (26-char alphanumeric string)
  }
});
```

## Conditionally show components based on logged-in or logged-out

`./frontend-reacjt-js/src/pages/HomeFeedPage.js  `

Add to import section:  
`import { Auth } from 'aws-amplify';`

Add to const section: 
`// set a state
const [user, setUser] = React.useState(null);`

Add function:
```
// check if we are authenicated
const checkAuth = async () => {
  Auth.currentAuthenticatedUser({
    // Optional, By default is false. 
    // If set to true, this call will send a 
    // request to Cognito to get the latest user data
    bypassCache: false 
  })
  .then((user) => {
    console.log('user',user);
    return Auth.currentAuthenticatedUser()
  }).then((cognito_user) => {
      setUser({
        display_name: cognito_user.attributes.name,
        handle: cognito_user.attributes.preferred_username
      })
  })
  .catch((err) => console.log(err));
};
```

Add call to function: (replace existing checkAuth function with same name)
```
// check when the page loads if we are authenicated
React.useEffect(()=>{
  loadData();
  checkAuth();
}, [])
```

We'll want to pass user to the following components: (in the return section)  
```
<DesktopNavigation user={user} active={'home'} setPopped={setPopped} />
<DesktopSidebar user={user} />
```

Edit `profileinfo.js` to replace Cookies with Cognito auth
```
const signOut = async () => {
  try {
      await Auth.signOut({ global: true });
      window.location.href = "/"
  } catch (error) {
      console.log('error signing out: ', error);
  }
}
```

Ran a test 'Docker Compose Up' but only saw blank homepage, following the video, needed a fix to a parameter in app.js: `userPoolWebClientId: process.env.REACT_APP_CLIENT_ID`, as it was referencing a non-existent env var.

Reran test and front page was working 😂

## Custom Sign-In Page

1. Updated SigninPage.js to handle error of incorrect login:
![Screenshot 2023-05-02 161300](https://user-images.githubusercontent.com/22940535/235710939-e7a9d6b8-3010-481d-b57b-67dd8978364c.png)

2. Created a new user in the AWS Console:
![image](https://user-images.githubusercontent.com/22940535/235709485-c101696d-cd1b-4d62-989d-6260818d695a.png)

3. Ran AWS CLI command to prevent forced password change:  
`aws cognito-idp admin-set-user-password --user-pool-id us-east-1_iujSlyvwd --username ammarhasan76 --password XXXXXXXX --permanent`  
![image](https://user-images.githubusercontent.com/22940535/235709889-7eba7150-5581-44d7-a47f-a99e251fb74c.png)  
![Screenshot 2023-05-02 153721](https://user-images.githubusercontent.com/22940535/235710573-c88bf0e6-480c-4dad-b84e-114cb98d789c.png)

4. Tested login successfully:
![Screenshot 2023-05-02 154138](https://user-images.githubusercontent.com/22940535/235710717-f5547b70-7d25-4aca-9412-3269fc4b58c1.png)  
![image](https://user-images.githubusercontent.com/22940535/235986265-33e41dc2-e5c9-43b3-8cae-17cdc9230a3c.png)

5. Tested sign-out successfully:  
![image](https://user-images.githubusercontent.com/22940535/235985768-a72c22b5-55a0-4cf0-ac11-6c7c43ce5529.png)  
![image](https://user-images.githubusercontent.com/22940535/235985816-3766bac9-37ca-4fa8-af85-964b53a39258.png)

6. Added preferred username in AWS Console, so it appears in the frontend:  
![image](https://user-images.githubusercontent.com/22940535/235986425-fe0d4fef-1780-4e7e-9996-036def07e360.png)
![image](https://user-images.githubusercontent.com/22940535/235986464-26d30475-aebb-491b-97a5-d985bd9646c5.png)

## Custom Sign-up Page & Confirmation Page

1. Update `SignupPage.js` by replacing cookies with amplify:  
```
...
import { Auth } from 'aws-amplify';
...
```

2. Replace `onsubmit` function:  
```
...
 const onsubmit = async (event) => {
    event.preventDefault();
    setCognitoErrors('')
    try {
        const { user } = await Auth.signUp({
          username: email,
          password: password,
          attributes: {
              name: name,
              email: email,
              preferred_username: username,
          },
          autoSignIn: { // optional - enables auto sign in after user is confirmed
              enabled: true,
          }
        });
        console.log(user);
        window.location.href = `/confirm?email=${email}`
    } catch (error) {
        console.log(error);
        setCognitoErrors(error.message)
    }
    return false
  }
...
```

3. Update `ConfirmationPage.js` by replacing cookies with amplify:  
```
...
import { Auth } from 'aws-amplify';
...
```

4. Replace `resend_code` function:  
```
...
const resend_code = async (event) => {
  setCognitoErrors('')
  try {
    await Auth.resendSignUp(email);
    console.log('code resent successfully');
    setCodeSent(true)
  } catch (err) {
    // does not return a code
    // does cognito always return english
    // for this to be an okay match?
    console.log(err)
    if (err.message == 'Username cannot be empty'){
      setCognitoErrors("You need to provide an email in order to send Resend Activiation Code")   
    } else if (err.message == "Username/client id combination not found."){
      setCognitoErrors("Email is invalid or cannot be found.")   
    }
  }
}
...
```

5. Replace `onsubmit` function:
```
...
const onsubmit = async (event) => {
  event.preventDefault();
  setCognitoErrors('')
  try {
    await Auth.confirmSignUp(email, code);
    window.location.href = "/"
  } catch (error) {
    setCognitoErrors(error.message)
  }
  return false
}
...
```

6. Attempted sign-up but failed due to problem with the Cognito Pool, so had to recreate the pool but with just Email sign-in option, updated the Cognito Pool ID and ClientID and restarted and retested sign-ip & confirmation:  

<screenshots>

Success! :joy:


## Custom Recovery Page

1. Added amplify auth to `RecoverPage.js`
```
...
import { Auth } from 'aws-amplify';
...
```

2. Replaced `onsubmit_send_code` function

```
...
const onsubmit_send_code = async (event) => {
  event.preventDefault();
  setCognitoErrors('')
  Auth.forgotPassword(username)
  .then((data) => setFormState('confirm_code') )
  .catch((err) => setCognitoErrors(err.message) );
  return false
}
...
```

3. Replaced `onsubmit_confirm_code` function

```
...
const onsubmit_confirm_code = async (event) => {
  event.preventDefault();
  setCognitoErrors('')
  if (password == passwordAgain){
    Auth.forgotPasswordSubmit(username, code, password)
    .then((data) => setFormState('success'))
    .catch((err) => setCognitoErrors(err.message) );
  } else {
    setCognitoErrors('Passwords do not match')
  }
  return false
}
...
```

4. Attempted recovery process

<screenshots>

Success :joy:












