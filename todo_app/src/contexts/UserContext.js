import React, { createContext, Component } from 'react';

export const UserContext = createContext();

class UserContextProvider extends Component {

    constructor(props){
        super(props);

        var logged_in = false; 
        var light_mode = false;
        var clock_mode = false;
        var ticket = [];

        if(localStorage.getItem('id_token') !== null){
            logged_in = true;
        }
        
        if(localStorage.getItem('light_mode') === 'true'){
            document.documentElement.setAttribute("theme", "light")
            light_mode = true;
        }else if(localStorage.getItem('light_mode') === 'false'){
            light_mode = false;
        }else{
            localStorage.setItem('light_mode', 'false');
        };

        if(localStorage.getItem('clock_mode') === 'true'){
            clock_mode = true;
        }else if(localStorage.getItem('clock_mode') === 'false'){
            clock_mode = false;
        }else{
            localStorage.setItem('clock_mode', 'false');
        };

        if(localStorage.getItem('ticket') !== null){
            ticket = JSON.parse(localStorage.getItem('ticket'));
        }else{
            localStorage.setItem('ticket', '[]')
        };

        this.state = {
            logged_in: logged_in,
            is_synced: false,
            light_mode: light_mode,
            clock_mode: clock_mode,
            online: true,
            ticket: ticket
        };
        this.checkConnection = this.checkConnection.bind(this);
        this.addTaskToTicket = this.addTaskToTicket.bind(this);
        this.getSettings = this.getSettings.bind(this);
        this.goOffline = this.goOffline.bind(this);
    };

    componentDidMount(){
        if(this.state.logged_in){
            this.checkConnection();
        }
    }

    checkConnection(){
        var checker = setInterval(() => {
            console.log('checking connection')
            if(navigator.onLine){
                console.log('going online')
                this.setState({
                    online: false,
                });
                this.sendTicket();
                this.sendSettings();
            }
        }, 3000);
    };

    goOffline(error){
        console.log("goin offline")
        console.log(error.body)
        if(this.state.online){
            this.checkConnection();
            this.setState({
                online: false,
                is_synced: false
            });
        };
    };

    sendSettings = () => {
        var settings = {
            clock_mode: this.state.clock_mode,
        };

        if(this.state.logged_in){
            fetch('http://34.67.56.249/post-settings', {
                method: 'POST',
                headers: {
                    'Authorization': localStorage.getItem('id_token'),
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(settings)
            }).catch((error) => {
                console.log('sending settings failed')
                this.goOffline(error);
            });
        };
    };

    sendTicket(){

        fetch('http://34.67.56.249/recieve-ticket', {
            method: 'POST',
            headers: {
                'Authorization': localStorage.getItem('id_token'),
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(this.state.ticket)
        }).then(response => {
            if(response.ok === false){
                throw response
            }
            this.setState({
                ticket: [],
                is_synced: true
            })
            localStorage.setItem('ticket', '[]')

            this.sendSettings();
            return true;
        }).catch((error) => {
            this.goOffline(error);
            return false;
        });
    };

    addTaskToTicket(data, mode){
        console.log('adding to ticket')
        if(mode === "add"){
            this.state.ticket.push({data, mode})
        }else if(mode === "edit"){
            this.state.ticket.push({data, mode})
        }else{
            this.state.ticket.push({data, mode})
        }
        localStorage.setItem('ticket', JSON.stringify(this.state.ticket))
    };

    getSettings(){
        if(this.state.logged_in){
            fetch('http://34.67.56.249/get-settings', {
                method: 'GET',
                headers: {
                    'Authorization': localStorage.getItem('id_token'),
                    'Content-Type': 'application/json'
                },
            }).then(response => {
                if(response.ok === false){
                    throw response
                }
                return response.json();
            }).then(data => {

                var obj = JSON.parse(data)
                this.setState({
                    clock_mode: obj.clock_mode,
                });
            }).catch((error) => {
                console.log('get settings failed')
                this.goOffline(error);
            });
        };
    };

    toggleDarkMode = () => {
        if(localStorage.getItem('light_mode') === 'false'){
            this.setState({ light_mode: true });
            document.documentElement.setAttribute("theme", "light")
            localStorage.setItem('light_mode', 'true');
        }else{
            this.setState({ light_mode: false });
            document.documentElement.setAttribute("theme", "dark")
            localStorage.setItem('light_mode', 'false');
        }; 
    };

    toggleClockMode = () => {
        if(localStorage.getItem('clock_mode') === 'false'){
            this.setState({ clock_mode: true }, this.sendSettings);
            localStorage.setItem('clock_mode', 'true');
        }else{
            this.setState({ clock_mode: false }, this.sendSettings);
            localStorage.setItem('clock_mode', 'false');
        }; 
    };

    toggleLogin = () => {
        if(this.state.logged_in === false){
            this.setState({ logged_in: true });
            //this.eventSource = new EventSource("events");
        }else{
            this.setState({ 
                logged_in: false,
            });
        }; 
    };

    syncTrue = () => {
        this.setState({
            is_synced: true
        })
    }

    refreshToken = () => {
        fetch('https://oauth2.googleapis.com/token', {
            method: 'POST',
            headers: {
                'code': localStorage.getItem('auth_code'),
                'client_id': '195081855240-jjsqpn2t0oucb8ets7li98p8vodja8jd.apps.googleusercontent.com',
                'client_secret': ''
           }
        }).then(response => {
            console.log(response)
        }).catch((error) => {

            console.log(error)
            this.goOffline(error);
        });
        
        //localStorage.setItem('id_token', new_id_token);
    }

    render() {


        return ( 
            <UserContext.Provider value={{...this.state, syncTrue: this.syncTrue, toggleDarkMode: this.toggleDarkMode, toggleClockMode: this.toggleClockMode, addTaskToTicket: this.addTaskToTicket, sendSettings: this.sendSettings, getSettings: this.getSettings, goOffline: this.goOffline, toggleLogin: this.toggleLogin, setId: this.setId, destroyId: this.destroyId}}>
                {this.props.children}
            </UserContext.Provider>
        );
    };
};

export default UserContextProvider;