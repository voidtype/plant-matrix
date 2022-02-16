import React, { Component, useEffect } from 'react';
import { Dropdown } from 'react-bootstrap'
import './account.scss';
import { Link } from 'react-router-dom';
import {useState} from 'react';
import { BsFillPersonFill, BsFillCaretDownFill } from "react-icons/bs";

const API_ENDPOINT = process.env.REACT_APP_API_ENDPOINT

function Account(props){
    //save the user state
    const [user, setUser] = useState("");

    //these components are only rendered if the UI has not yet got a token. Consider moving to its own component
    const loginRegister = <div><li><Link to="/login">Login</Link></li><li><Link to="/register">Register</Link></li></div>;
    
    useEffect(() => {
        //if we already know who's logged in, don't bother the back end
        if (user){return};
        console.log("current user: " + user);
        fetch(`${API_ENDPOINT}/api/users/current`,
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
            setUser(data.username) 
        ).catch(errors => errors.json())
        .then(errors => this.setState({errors: JSON.stringify(errors)}))
    })

    function logout(){
        props.userLogin ("");

    }
    
    return <Dropdown><Dropdown.Toggle><BsFillPersonFill className="icon" /> <div className="text">{user}</div> </Dropdown.Toggle>
    <Dropdown.Item onClick={logout}>Logout</Dropdown.Item>
    </Dropdown>
}

export default Account;