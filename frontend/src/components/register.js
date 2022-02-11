import React, { Component } from 'react';
import './login.scss';

//TODO: move this to a more broad reaching context 
const API_ENDPOINT = process.env.REACT_APP_API_ENDPOINT

class Register extends Component {
    state = {
        credentials: {username: '', password: '',email:''},
        errors:""
    }


    register = event => {
        console.log(this.state.credentials);
        fetch(`${API_ENDPOINT}/api/users/`,
        {
            method: 'POST',
            'headers':{'Content-Type':'application/json'},
            body: JSON.stringify(this.state.credentials)
        }).then(data=>{
            if(!data.ok){throw data}
            data.json()
        })
        .then(
        data => {
            console.log(data.token); 
        }).catch(errors => errors.json())
        .then(errors => this.setState({errors: JSON.stringify(errors)}))
        
    }

    inputChanged = event => {
        const cred = this.state.credentials;
        cred[event.target.name] = event.target.value;
        this.setState({credentials: cred})
    }

    render() {
        return(
            <div className="base-container">
                <div className="content">
                <div className="logocontainer">
                <img src="./img/logo.png" width="360" className="logo"></img></div>
            <h1>login user</h1>
            <label>Username 
            <input type="text" name="username" value={this.state.credentials.username} onChange={this.inputChanged}></input></label>
            <br />
            <label>Password 
            <input type="password" name="password" value={this.state.credentials.password} onChange={this.inputChanged}></input></label>
            <br />
            <label>email 
            <input type="email" name="email" value={this.state.credentials.email} onChange={this.inputChanged}></input></label>
            <br />
            <button onClick={this.register}>Register</button>
          <div className="errors">{this.state.errors}</div>
          </div>
          </div>
        );
    }
}

export default Register;