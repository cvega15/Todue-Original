import React from 'react';


class App extends React.Component{
   
    render(){
        return(
            <div className='header'>
                <button>menu</button>
                <button onClick={this.props.show_modal}>add task</button>
            </div>
        );
    };
};

export default App;
