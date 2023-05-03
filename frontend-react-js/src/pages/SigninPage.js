import './SigninPage.css';
import React from "react";
import {ReactComponent as Logo} from '../components/svg/logo.svg';
import { Link } from "react-router-dom";

// [DONE] Authenication
// import Cookies from 'js-cookie'
import { Auth } from 'aws-amplify';

export default function SigninPage() {

  const [email, setEmail] = React.useState('');
  const [password, setPassword] = React.useState('');
  const [errors, setErrors] = React.useState('');

  const onsubmit = async (event) => {
    setErrors('') // set errors to blank so we don't see errors
    event.preventDefault(); // don't submit the form so the below code can run
      Auth.signIn(email, password) // pass-in authentication details and a user object is returned
        .then(user => {
          // console.log('user',user) // this doesn't seem to add anything to the console output? the user object appears in the console even with this console.log commented out
          localStorage.setItem("access_token", user.signInUserSession.accessToken.jwtToken) // store JWT in secure local storage
          window.location.href = "/"
        })
        .catch(error => {
          console.log('Error!', error)
          if (error.code == 'UserNotConfirmedException') {
            window.location.href = "/confirm" // send to user confirmation page if the user is not confirmed yet
          }
      setErrors(error.message)
    });
    return false
  }
  
  const email_onchange = (event) => {
    setEmail(event.target.value);
  }
  const password_onchange = (event) => {
    setPassword(event.target.value);
  }

  let el_errors;
  if (errors){
    el_errors = <div className='errors'>{errors}</div>;
  }

  return (
    <article className="signin-article">
      <div className='signin-info'>
        <Logo className='logo' />
      </div>
      <div className='signin-wrapper'>
        <form 
          className='signin_form'
          onSubmit={onsubmit}
        >
          <h2>Sign into your Cruddur account</h2>
          <div className='fields'>
            <div className='field text_field username'>
              <label>Email</label>
              <input
                type="text"
                value={email}
                onChange={email_onchange} 
              />
            </div>
            <div className='field text_field password'>
              <label>Password</label>
              <input
                type="password"
                value={password}
                onChange={password_onchange} 
              />
            </div>
          </div>
          {el_errors}
          <div className='submit'>
            <Link to="/forgot" className="forgot-link">Forgot Password?</Link>
            <button type='submit'>Sign In</button>
          </div>

        </form>
        <div className="dont-have-an-account">
          <span>
            Don't have an account?
          </span>
          <Link to="/signup">Sign up!</Link>
        </div>
      </div>

    </article>
  );
}