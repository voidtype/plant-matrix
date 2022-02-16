import React, { Component } from 'react';
import Button from 'react-bootstrap/Button'
import './nav.scss';
import { Link } from 'react-router-dom';
import Account from './account';


function Nav(props){
    //these components are only rendered if the UI has not yet got a token. Consider moving to its own component
    const loginRegister = <div><li><Link to="/login">Login</Link></li><li><Link to="/register">Register</Link></li></div>;
    return <nav>

       <ul className="nav-links">
       {props.token &&<li><Link to="/devices">Devices</Link></li>}
       {props.token && <Account token={props.token} userLogin={props.userLogin}/>}
       {!props.token && loginRegister}


    </ul>
    </nav>
}

export default Nav;