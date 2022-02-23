import React from 'react';
import './devices.scss';
import DeviceCard from './deviceCard';
import { useNavigate } from 'react-router-dom';
import { useState } from 'react';

const API_ENDPOINT = process.env.REACT_APP_API_ENDPOINT



function Devices(props) {


    const [devices, setDevices] = useState([]);
    const [error, setError] = useState("");



    const loadDevices = () => {
        fetch(`${API_ENDPOINT}/api/devices/`,
        {
            method: 'GET',
            'headers':{
                'Content-Type':'application/json',
                Authorization:`Token  ${props.token}`
            }
        }).then(data=>{
            if(!data.ok){console.log( data); throw data};
            return data.json();
        })
        .then(
        data => 
            setDevices(data) 
        ).catch(errors => errors.json())
        .then(errors => setError(JSON.stringify(errors)))
        
    }

    return(
        <div>
            <h1>Devices</h1>
            <div className="container">
            {devices?.map( device => {
                return <DeviceCard key={device.id} uuid={device.id} token={props.token} />
            })}
            </div>
            <button onClick={loadDevices}>Get Devices</button>
        </div>
    );
}

export default Devices;