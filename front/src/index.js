import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import CssBaseline from "@material-ui/core/CssBaseline";
import {createMuiTheme, MuiThemeProvider} from "@material-ui/core/styles";

const theme = createMuiTheme({
    palette: {
        primary: {
            main: "#DB4D55"
        },
        secondary: {
            main: "#32dd0d"
        },
        multilineColor:{
            color:'red'
        },
        background: {
            default: "#191A4B"
        }
    }
});

ReactDOM.render(
  <React.StrictMode>
      <MuiThemeProvider theme={theme}>
          <CssBaseline />
          <App />
      </MuiThemeProvider>
  </React.StrictMode>,
  document.getElementById('root')
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
