import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import { DAppProvider, ChainId } from '@usedapp/core';

ReactDOM.render(
  <DAppProvider config ={{
    supportedChains:[ChainId.Kovan,ChainId.Rinkeby, 1337]
  }}>

    <App />
  </DAppProvider>,
  
  document.getElementById('root')
);
