import React, { createContext, Component } from 'react';

export const UserContext = createContext();

class UserContextProvider extends Component {

    constructor(props){
        super(props);

        this.state = {
            id_token: '',
            logged_in: false,
            light_mode: false,
            clock_mode: true
        };
    };

    /* implement this later for all toggling
    toggleTheme() {
    const theme = this.state.theme === 'dark' ? 'light' : 'dark';
    this.setState({ theme });
    document.documentElement.setAttribute("data-theme", theme);
    }
    */

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
            this.setState({ clock_mode: true });
        }else{
            this.setState({ clock_mode: false });
        }; 
    };

    toggleLogin = () => { 
        if(this.state.logged_in === false){
            this.setState({ logged_in: true });
        }else{
            this.setState({ logged_in: false });
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
            <UserContext.Provider value={{...this.state, toggleLogin: this.toggleLogin, setId: this.setId, destroyId: this.destroyId, toggleClockMode: this.toggleClockMode, toggleDarkMode: this.toggleDarkMode}}>
                {this.props.children}
            </UserContext.Provider>
        );
    };
};

export default UserContextProvider;