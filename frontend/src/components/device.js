import React, { Component } from 'react';
import {Card} from 'react-bootstrap'
import './devices.scss';

const API_ENDPOINT = process.env.REACT_APP_API_ENDPOINT



class Device extends Component {

    state = {
        sample: ""
    }

    componentDidMount(){
        this.loadDevice();
    }

    loadDevice = () => {
        fetch(`${API_ENDPOINT}/api/samples/${this.props.uuid}`,
        {
            method: 'GET',
            'headers':{
                'Content-Type':'application/json',
                Authorization:`Token  ${this.props.token}`
            }
        }).then(data=>{
            if(!data.ok){console.log( data); throw data};
            return data.json();
        })
        .then(
        data => 
            this.setState({sample:data.attachment}) 
        ).catch(errors => errors.json())
        .then(errors => this.setState({errors: JSON.stringify(errors)}))
        
    }

    render() {
        return(

             <Card border="light" bg="dark" className="device" ><Card.Img variant="top" src={process.env.REACT_APP_API_ENDPOINT+ this.state.sample}/>{this.props.uuid}</Card>
                
        );
    }
}

export default Device;