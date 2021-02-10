import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import InfoWindowModal from './components/ConfirmNewGameModal';

it('renders without crashing', () => {
  const div = document.createElement('div');
  ReactDOM.render(<App />, div);
});

it('should restart the game', () => {
  const button_restart = document.getElementsByClassName('btn btn-danger btn-ok');
  (<InfoWindowModal />, button_restart);
});
