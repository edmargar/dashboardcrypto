import React, { Component } from 'react'
import Rotas from "../../Rotas";
import {api} from '../../api';

class Main extends Component{
    state = {
        negotiations: [],
    }

    async componentDidMount(){
        const response = await api.get('');
        this.setState({negotiations: response.data});
    }

    render(){

        const {negotiations} = this.state;

        return(
            <div>
                <h1>Negotiations</h1>
                {console.log(negotiations)}
                {negotiations.map(negotiation => (
                    <li key={negotiation.id}>
                        <h5>{negotiation.tipo}</h5>
                    </li>
                ))}
            </div>
        );
    }

}

export default Main;