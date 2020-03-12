import React from 'react';
import { Link, Redirect } from 'react-router-dom';
import { UserContext } from '../contexts/UserContext';
import logo from '../images/ToDue512.png';
import example_image from '../images/app2.png';
import SignIn from './SignIn';

class LandingPage extends React.Component {

    static contextType = UserContext;

    render(){

        if(this.context.logged_in ){
            return(
                <Redirect to='/home' />
            )
        }else{
            return(
                <div className='landing-page' style={{color: "lightgray", backgroundColor: "#040a0e"}}>
                    <div style={{display: "flex", backgroundColor: "#051f2c", position: "sticky", top: "0"}}>
                        <img src={logo} alt="screenshot of the app" style={{width: "10vh", height: "10vh", marginTop: "0vh"}}></img>
                        <h1 style={{fontSize: "5vh", margin: "0vh", marginTop: "1.2vh"}}>To Due</h1>
                    </div>

                    <div style={{margin: "2vh", display: "flex", flexDirection: "column", alignItems: "center"}}>
                        <img src={example_image} className="front-page-image"></img>
                        <p className="front-page-text">To Due is a simple todo app that shows you how long you have to complete a task by showing you a timer along with a countdown bar</p>
                        <div className="sign-in">
                            <p style={{fontSizeS: "1.7vh", paddingLeft: "10px", paddingRight: "10px"}}>you can sign in with google to save your data across multiple devices</p>
                            <p style={{fontSize: "1.7vh", paddingLeft: "10px", paddingRight: "10px"}}>or try it without an account then sign up later to save your data</p>
                            <div style={{display: "flex", justifyContent: "center"}}>
                                <SignIn />
                                <h3 style={{margin: "0.7vh 2vh 2.5vh 2vh",}}>or</h3>
                                <Link to='/home' className='login-as-guest' style={{fontSize: "1.5vh", padding: "6px 6px 0px 6px", height: "32px", color: "white", border: "solid"}}>try as guest</Link>
                            </div>
                        </div>
                    </div>
                </div>
            );
        }
    };
};

export default LandingPage