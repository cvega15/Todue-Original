import React from 'react';
import { NavLink } from 'react-router-dom';

class Navbar extends React.Component {

    render(){
        return(
            <div className='navbar'>
                <NavLink to='/home' className='navlink'>home</NavLink>
                <NavLink to='/settings' className='navlink'>settings</NavLink>
            </div>
        );
    };
};

export default Navbar