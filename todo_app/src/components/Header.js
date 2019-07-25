import React from 'react';

class App extends React.Component{
    
    constructor(){
        super();
        this.state = {
            user_name: "Dudelo"
        };
    };

    handleClick(){
        console.log("i was clicked lolololz");
    };

    render(){
        return(
            <div className='header'>
                <h1>TODO APP</h1>
                <h2>{this.state.user_name}'s tasks</h2>
                <button onClick={this.handleClick}>log out</button>
            </div>
        );
    };
};

export default App;



