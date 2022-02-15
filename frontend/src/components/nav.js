import React, { Component } from 'react';
import Button from 'react-bootstrap/Button'
import './nav.scss';
import { Link } from 'react-router-dom';


function Nav(props){
    return <nav>
       <ul className="nav-links">
       <li><Link to="/devices">Devices</Link></li>
        <li><Link to="/login">Login</Link></li>
        <li><Link to="/register">Register</Link></li>


    </ul>
    </nav>
}

export default Nav;