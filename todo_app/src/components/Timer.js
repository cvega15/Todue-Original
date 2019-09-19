import React from 'react';

class Home extends React.Component {

    constructor(props){

        super(props);
        this.state={
            time: new Date()
        };
    };

    changeTime(){
        this.setState({
            time: new Date()
        })
    }

    componentDidMount(){
        setInterval(()=>this.changeTime(), 1000) 
    }

    render(){
       
        return (
            <div>
                <h2>{this.state.time.toLocaleString()}</h2>            
            </div>
        );
    };
};

export default Home;
