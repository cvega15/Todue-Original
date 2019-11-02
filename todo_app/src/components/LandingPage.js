import React from 'react';
import { NavLink, Redirect } from 'react-router-dom';
import { UserContext } from '../contexts/UserContext';
import SignIn from './SignIn';

class LandingPage extends React.Component {

    static contextType = UserContext;

    render(){

        if(this.context.logged_in){
            return(
                <Redirect to='/home' />
            )
        }else{
            return(
                <div className='landing-page' style={{color: "lightgray"}}>
                    <h1>todo app thing</h1>
                    <h3>sign in with google to save your data across multiple devices</h3>
                    <SignIn />
                    <h3>or try it without an account then sign up later to save your data</h3>
                    <NavLink to='/home' className='login-as-guest'>login as guest</NavLink>
                </div>
            );
        }
    };
};

export default LandingPage