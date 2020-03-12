import React from 'react';
import GoogleLogin from 'react-google-login';
import { GoogleLogout } from 'react-google-login';
import { UserContext } from '../contexts/UserContext';
import { TasksContext } from '../contexts/TasksContext';

class SignIn extends React.Component {

    static contextType = UserContext;

    constructor(props){
        super(props)
        //this.onSignIn = this.onSignIn.bind(this)
        //this.onSignOut = this.onSignOut.bind(this)
    }

    onSignIn(googleUser){
        console.log('login successful')
        this.context.toggleLogin()
        
    }

    onSignOut(){
        console.log('signing out') 
        this.context.toggleLogin()
    }

    componentDidUpdate(){
        /*
        window.gapi.signin2.render(
            "loginButton",
            {
                width: 200,
                height: 50,
                onsuccess: (res) => this.onSignIn(res),
            }
        ) 
        */
    }

    componentDidMount(){
        /*
        window.gapi.signin2.render(
            "loginButton",
            {
                width: 200,
                height: 50,
                onsuccess: (res) => this.onSignIn(res),
            }
        ) 
        */
        /*
        window.gapi.load('auth2', () => {
            this.GoogleAuth = window.gapi.auth2.init({client_id: '195081855240-jjsqpn2t0oucb8ets7li98p8vodja8jd.apps.googleusercontent.com',})

            this.GoogleAuth.then(() => {
                console.log('on init')
                window.gapi.signin2.render(
                    "loginButton",
                    {
                        width: 200,
                        height: 50,
                        onsuccess: (res) => this.onSignIn(res),
                    }
                ) 
                

            })
        
        })
        */
        

        /*
        window.gapi.load('auth2', () => {

            this.GoogleAuth = window.gapi.auth2.init({client_id: '195081855240-jjsqpn2t0oucb8ets7li98p8vodja8jd.apps.googleusercontent.com',})
            this.GoogleAuth.then(() => {
                console.log('on init')
            })
        })
        */
    }

    render(){
        if(this.context.logged_in){
            console.log('rendering as not logged in')
            /*
            return(
                <div id="loginButton"></div>
            )
            */
            return (
                <TasksContext.Consumer>{(TasksContext) => {
                    return(
                        <div>
                            <GoogleLogout
                                clientId = "195081855240-jjsqpn2t0oucb8ets7li98p8vodja8jd.apps.googleusercontent.com"
                                buttonText = "logout"
                                onLogoutSuccess = {(response) => {
                                    this.context.toggleLogin();
                                    localStorage.clear();
                                    TasksContext.clearEverything();
                                }}
                            ></GoogleLogout>
                        </div>
                    )
                }}</TasksContext.Consumer>
            );
            

        }else{
            /*
            console.log('returning as logged in')
            return(
                <button onClick={this.onSignOut}>logout</button>
            )
            */
            
            return(
                <TasksContext.Consumer>{(TasksContext) => {
                    
                    return(
                        <div>
                            <div id="googleButton"></div>
                            {
                                <GoogleLogin
                                    clientId="195081855240-jjsqpn2t0oucb8ets7li98p8vodja8jd.apps.googleusercontent.com"
                                    buttonText="Login with google"
                                    theme="dark"
                                    //responseType="id_token"
                                    //isSignedIn="true" 
                                    //redirectUri="http://localhost:3000/settings"
                                    onSuccess={(response) => {
                                        console.log(response)
                                        var id_token = response.getAuthResponse().id_token;
                                        
                                        fetch("http://34.67.56.249/sign-up-in", {
                                            method: 'POST',
                                            body: id_token
                                        }).then(response => {
                                            return response.json()
                                        }).then(data => {
                                            this.context.toggleLogin();
                                            localStorage.setItem('id_token', id_token)
                                            //localStorage.setItem('access_token', data.access_token)
                                            //localStorage.setItem('refresh_token', data.refresh_token);
                                            //localStorage.setItem('id_token', data.id_token);
                                            TasksContext.getTasks();
                                            this.context.getSettings();

                                        }).catch(error => {
                                            console.log('couldnt sign in')
                                        })
                                    }}
                                    onFailure={() => {console.log('couldnt sign in')}}
                                    cookiePolicy={'single_host_origin'}
                                />
                            }
                        </div>
                    )
                }}</TasksContext.Consumer>
            );
        };
    };
};

export default SignIn;
