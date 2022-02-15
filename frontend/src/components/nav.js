import React, { Component } from 'react';
import Button from 'react-bootstrap/Button'
import './nav.scss';


function Nav(props){
    return <nav>
       <ul className="nav-links">
        <li><a href="/login">Login</a></li>
        <li><a href="/register">Register</a></li>

    </ul>
    </nav>
}

export default Nav;