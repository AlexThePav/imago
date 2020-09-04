import React from 'react';
import './App.css';

import {Home, About, Contact, Plays, Members} from './pages';

import { NavBar } from './navbar';
import { BrowserRouter, Route, Switch } from 'react-router-dom';

function App() {
  return (
    <BrowserRouter>
      <div className="App">
        <header className="App-header">
          <NavBar/>
        </header>
        <main className="App-main">
          <Switch>
            <Route path="/" exact component={Home}/>
            <Route path="/about" component={About}/>
            <Route path="/contact" component={Contact}/>
            <Route path="/plays" component={Plays}/>
            <Route path="/members" component={Members}/>
          </Switch>
        </main>
      </div>
    </BrowserRouter>
  );
}

export default App;
