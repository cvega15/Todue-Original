import React from 'react';
import Timer from './Timer';

class Header extends React.Component {

    constructor(props){

        super(props);
        this.state={
            show_modal: false
        };
    };

    handleClick(){
        
    };

    render(){
        return(
            <div className='header'>
                <Timer />
                <button onClick={this.handleClick}>add task</button> 
            </div>
        );
    };
};

export default Header;
