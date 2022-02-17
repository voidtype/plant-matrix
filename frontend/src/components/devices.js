import React, { Component } from 'react';
import {Card} from 'react-bootstrap'
import './devices.scss';

const API_ENDPOINT = process.env.REACT_APP_API_ENDPOINT



class Devices extends Component {

    state = {
        devices: []
    }

    loadDevices = () => {
        fetch(`${API_ENDPOINT}/api/devices/`,
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
            this.setState({devices:data}) 
        ).catch(errors => errors.json())
        .then(errors => this.setState({errors: JSON.stringify(errors)}))
        
    }

    render() {
        return(
            <div>
                <h1>Devices</h1>
                <div className="container">
                {this.state.devices?.map( device => {
                    return <Card border="light" bg="dark" className="device" key={device.id}>{device.id}</Card>
                })}
                </div>
                <button onClick={this.loadDevices}>Get Devices</button>
          </div>
        );
    }
}

export default Devices;