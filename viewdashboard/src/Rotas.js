import React from 'react'
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom'

import Main from './pages/Main'
import Negociacoes from './pages/Negociacoes'
import Header2 from './Header2'


function Rotas() {
  return (
    <Router>
        <Header2/>
        <Routes>
          <Route exact path="/" element={<Main/>}/>
          <Route exact path="/negociacoes" element={<Negociacoes/>}/>
        </Routes>
    </Router>
  );
}

export default Rotas;