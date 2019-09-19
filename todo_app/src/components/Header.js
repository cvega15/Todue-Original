import React from 'react';
import Timer from './Timer';
import { ModalContext } from '../contexts/ModalContext';

class Header extends React.Component {

    static contextType = ModalContext;
    render(){
        const { toggleModal } = this.context;
        return(
            <div className='header'>
                <Timer />
                <button onClick={ () => toggleModal(null) }>add task</button> 
            </div>
        );
    };
};

export default Header;
