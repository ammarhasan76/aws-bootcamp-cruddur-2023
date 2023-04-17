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

Add the necessary env vars to docker_compose.yml to enable Amplify in the frontend
```
...
  frontend-react-js:
    environment:
      ...
      REACT_APP_AWS_PROJECT_REGION: "${AWS_DEFAUT_REGION}"
      REACT_APP_AWS_COGNITO_IDENTITY_POOL_ID:
      REACT_APP_AWS_COGNITO_REGION: "${AWS_DEFAUT_REGION}"
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








