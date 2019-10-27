import React from 'react';
import { ModalContext } from '../contexts/ModalContext';

class Header extends React.Component {

    static contextType = ModalContext;

    render(){
        const { toggleModal } = this.context;
        var title = this.props.title;
        if(title === 'users tasks'){
            return(
                <div className='header'>

                    { title }
                    <button onClick={ () => toggleModal(null) }>add task</button> 
                
                </div>
            );
        }else{
            return(
                <div className='header'>
                    
                    { title }
                </div>
            );
        }
    };
};

export default Header;
