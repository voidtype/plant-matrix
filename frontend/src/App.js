import './App.css';
import {useState} from 'react';
import Login from './components/login';
import Nav from './components/nav';
import Devices from './components/devices';

import Register from './components/register';
import {BrowserRouter as Router, Routes, Route} from 'react-router-dom';

function App() {
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
            <Nav />
            <Routes>

              <Route path ="/login" element={<Login userLogin={userLogin}/>} />
              <Route path ="/devices" element={<Devices token={token}/>} />
              <Route path ="/register" element={<Register />} />
            </Routes>

          </div>
      </div>
    </Router>
  );
}



export default App;
