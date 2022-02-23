import React from 'react';
import { useParams } from 'react-router-dom';

const API_ENDPOINT = process.env.REACT_APP_API_ENDPOINT



function Device (props)  {

    let {uuid} = useParams();



    const loadImage = () => {
        fetch(`${API_ENDPOINT}/api/samples/${uuid}`,
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
            this.setState({sample:data.attachment}) 
        ).catch(errors => errors.json())
        .then(errors => this.setState({errors: JSON.stringify(errors)}))
        
    }

    return(

            <div>{uuid}</div>
            
    );
    
}

export default Device;