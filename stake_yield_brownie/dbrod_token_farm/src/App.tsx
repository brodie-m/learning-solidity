import { Container } from '@material-ui/core';
import React from 'react';
import Header from './Components/Header';


function App() {
  return (
    <div className="App">
      <Header/>
      <Container maxWidth="md">
        <div>
          hi
        </div>
      </Container>
    </div>
  );
}

export default App;
