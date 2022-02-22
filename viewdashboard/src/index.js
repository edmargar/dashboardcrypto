import React from 'react';
import ReactDOM from 'react-dom';
import './assets/css/index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';

import { ThemeProvider, createTheme  } from '@mui/material/styles';
import ParticlesBg from 'particles-bg';


    const theme = createTheme({
      palette: {
        primary: {
          main: 'rgba(255, 0, 0, 0)'
        }
      }
    });


ReactDOM.render(
  <React.StrictMode>
      <div>
        <ParticlesBg color="#064663" num={200} speed={100} type="cobweb" bg={true} />
        <App />
      </div>
  </React.StrictMode>,
  document.getElementById('root')
);

reportWebVitals();
