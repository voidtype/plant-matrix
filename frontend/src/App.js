import './App.css';
import './App.scss';

import {useState} from 'react';
import Login from './components/login';
import Nav from './components/nav';
import Devices from './components/devices';
import Device from './components/device'

import Register from './components/register';
import {BrowserRouter as Router, Routes, Route} from 'react-router-dom';



function App() {
  document.title = "Teraharvest";

//  const [isLoginActive, setLoginActive]= useState(true);
  const [token, setToken] = useState('');
  const userLogin = (tok) => {
    setToken(tok);
    console.log(token);
  }
  return (
    <Router>
      <div className="App">
          <div className="loginContainer">
            <Nav token={token}  userLogin={userLogin}/>
            <Routes>

              <Route path ="/login" element={<Login userLogin={userLogin} token={token}/>} />
              <Route path ="/devices" element={<Devices token={token}/>} />
              <Route path ="/device/:uuid" element={<Device />} />
              <Route path ="/register" element={<Register />} />
            </Routes>

          </div>
      </div>
    </Router>
  );
}



export default App;
