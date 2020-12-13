import './App.css';
import {Button} from "@material-ui/core";

function App() {
  return (
      <div>
        <div className="App">
            <p className="Title"> UX Analyzer</p>
            <div>
                <input type="text" placeholder="Enter an url"
                    style={{ padding: "10px", borderRadius: "5px", width: "300px", height: "35px", outline: "none", border: 0, display: 'inline-block', marginRight: "20px", marginTop: "-10px"}}
                />
                <Button variant="contained" color="primary">
                    Analyze
                </Button>
            </div>
        </div>
          <div style={{color: "#FFF", textAlign: "center", position: "absolute", bottom: "0", left: "47%"}} >
            <p style={{ display: "inline-block",}}>Made with love by</p>
            <a style={{paddingLeft: "5px", color: "#DB4D55",}} href="http://poc-innovation.com/">PoC</a>
          </div>
      </div>
  );
}

export default App;
