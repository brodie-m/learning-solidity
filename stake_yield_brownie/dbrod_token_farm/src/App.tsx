import { Container } from '@material-ui/core';
import React from 'react';
import Header from './Components/Header';
import Main from './Components/Main';


function App() {
  return (
    <div className="App">
      <Header/>
      <Container maxWidth="md">
        <Main/>
      </Container>
    </div>
  );
}

export default App;
