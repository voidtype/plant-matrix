import React, { Component } from 'react';
import Button from 'react-bootstrap/Button'
import './login.scss';


class Login extends Component {
    state = {
        credentials: {username: '', password: ''},
        errors: ""
    }


    login = event => {
        console.log(this.state.credentials);
        fetch('http://localhost:81/api-token-auth/',
        {
            method: 'POST',
            'headers':{'Content-Type':'application/json'},
            body: JSON.stringify(this.state.credentials)
        }
        ).then(data=>{
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
            <Button onClick={this.login}>Login</Button>
            <div className="errors">{this.state.errors}</div>
            </div>
          </div>
        );
    }
}

export default Login;