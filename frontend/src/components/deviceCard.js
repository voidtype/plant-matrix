import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import {Card} from 'react-bootstrap'
import './devices.scss';

const API_ENDPOINT = process.env.REACT_APP_API_ENDPOINT



 function DeviceCard (props) {
    const deviceNavigate = useNavigate();

    const [sample, setSample] = useState("");
    const [error, setError] = useState("");


    useEffect(()=>{
        loadDevice();
    });

    const loadDevice = () => {
        fetch(`${API_ENDPOINT}/api/samples/${props.uuid}`,
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
            setSample(data.attachment) 
        ).catch(errors => errors.json())
        .then(errors => setError(JSON.stringify(errors)))
        
    }

        return <Card onClick={()=>deviceNavigate(`/device/${props.uuid}`)} border="light" bg="dark" className="device" ><Card.Img variant="top" src={process.env.REACT_APP_API_ENDPOINT+ sample}/>{props.uuid}</Card>;
};

export default DeviceCard;