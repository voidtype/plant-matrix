import './App.css';
import {useState} from 'react';
import Login from './components/login';
import Nav from './components/nav';

import Register from './components/register';
import {BrowserRouter as Router, Routes, Route} from 'react-router-dom';

function App() {
  const [isLoginActive, setLoginActive]= useState(true);
  return (
    <Router>
      <div className="App">
          <div className="loginContainer">
            <Nav />
            <Routes>

              <Route path ="/login" element={<Login />} />
              <Route path ="/register" element={<Register />} />
            </Routes>

          </div>
      </div>
    </Router>
  );
}



export default App;
