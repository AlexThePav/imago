import React from 'react';
import logo from './logo.svg';
import './App.css';

import {PlayList} from './plays'
import { NavBar } from './navbar';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <NavBar/>
        <div>
          <PlayList/>
        </div>
      </header>
    </div>
  );
}

export default App;
