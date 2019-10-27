import React, { createContext, Component } from 'react';

export const UserContext = createContext();

class UserContextProvider extends Component {

    constructor(props){
        super(props);

        this.state = {
            id_token: '',
            logged_in: false,
            light_mode: false,
            clock_mode: false,
            online: true,
            ticket: []
        };
        this.checkConnection = this.checkConnection.bind(this);
        this.addTaskToTicket = this.addTaskToTicket.bind(this);
        this.getSettings = this.getSettings.bind(this);
        this.goOffline = this.goOffline.bind(this);
    };

    checkConnection(){
        var checker = setInterval(() => {
            if(navigator.onLine){
                this.setState({
                    online: true,
                });
                this.sendTicket();
                this.sendSettings();
                clearInterval(checker);
                return;

            };
        }, 2000);
    };

    sendTicket(){

        fetch('http://34.67.56.249:5000/recieve-ticket', {
            method: 'POST',
            headers: {
                'Authorization': this.state.id_token,
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(this.state.ticket)
        }).then(response => {
            this.setState({
                ticket: []
            })
            console.log('ticket sending successful')
            console.log('returning true')
            this.sendSettings();
            return true;
        }).catch((error) => {
            console.log('ticket sending failed')
            console.log("returning false")
            return false;
        });
    };

    addTaskToTicket(data, mode){

        if(mode === "add"){
            this.state.ticket.push({data, mode})
        }else if(mode === "edit"){
            this.state.ticket.push({data, mode})
        }else{
            this.state.ticket.push({data, mode})
        }
    };
    
    sendSettings = () => {

        var settings = {
            clock_mode: this.state.clock_mode,
        };

        if(this.state.logged_in){
            fetch('http://34.67.56.249:5000/post-settings', {
                method: 'POST',
                headers: {
                    'Authorization': this.state.id_token,
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(settings)
            }).catch((error) => {
                console.log('sending settings failed')
                this.goOffline();
            });
        };
    };

    getSettings(){
        if(this.state.logged_in){
            fetch('http://34.67.56.249:5000/get-settings', {
                method: 'GET',
                headers: {
                    'Authorization': this.state.id_token,
                    'Content-Type': 'application/json'
                },
            }).then(response => {
                return response.json();
            }).then(data => {

                var obj = JSON.parse(data)
                this.setState({
                    clock_mode: obj.clock_mode
                });

            }).catch((error) => {
                console.log('get settings failed')
                this.goOffline();
            });
        };
    };

    goOffline(){
        if(this.state.online){
            this.checkConnection();
            this.setState({online: false});
        }else{
            console.log('go offline called: already offline')
        };
    };

    toggleDarkMode = () => {
        if(this.state.light_mode === false){
            this.setState({ light_mode: true });
            document.documentElement.setAttribute("theme", "light")
        }else{
            this.setState({ light_mode: false });
            document.documentElement.setAttribute("theme", "dark")
        }; 
    };

    toggleClockMode = () => {
        if(this.state.clock_mode === false){
            this.setState({ clock_mode: true }, this.sendSettings);
        }else{
            this.setState({ clock_mode: false }, this.sendSettings);
        }; 
    };

    toggleLogin = () => {
        if(this.state.logged_in === false){
            this.setState({ logged_in: true });
        }else{
            this.setState({ 
                logged_in: false,
            });
        }; 
    };

    setId = (id_token) => {
        this.setState({
            id_token: id_token
        });
    }

    destroyId = () => {
        this.setState({
            id_token: ""
        })
    }

    render() {
        return ( 
            <UserContext.Provider value={{...this.state, toggleDarkMode: this.toggleDarkMode, toggleClockMode: this.toggleClockMode, addTaskToTicket: this.addTaskToTicket, sendSettings: this.sendSettings, getSettings: this.getSettings, goOffline: this.goOffline, toggleLogin: this.toggleLogin, setId: this.setId, destroyId: this.destroyId}}>
                {this.props.children}
            </UserContext.Provider>
        );
    };
};

export default UserContextProvider;