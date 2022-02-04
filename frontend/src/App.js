import './App.css';
import {useState} from 'react';
import Login from './components/login';
import Register from './components/register';

function App() {
  const [isLoginActive, setLoginActive]= useState(true);
  return (
    <div className="App">
      <div className="loginContainer">
        {isLoginActive && <Login containerRef={(ref) => this.current = ref}/>}
        {!isLoginActive && <Register containerRef={(ref) => this.current = ref}/>}

      </div>
      <a href="#" className="register-toggle" onClick={() => setLoginActive(!isLoginActive)}>{!isLoginActive ? 'login' : 'register'}</a>
    </div>
  );
}



export default App;
