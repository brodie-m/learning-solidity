import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import { DAppProvider, ChainId, Kovan, Rinkeby } from '@usedapp/core';

ReactDOM.render(
  <DAppProvider config={{
    networks: [Kovan, Rinkeby]
  }}>

    <App />
  </DAppProvider>,

  document.getElementById('root')
);
