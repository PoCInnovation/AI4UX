import './App.css';
import {useState} from "react";
import {Button} from "@material-ui/core";

function App() {
    const [pageName, setPageName] = useState("UX Analyser")
    const [url, setURL] = useState("")

    async function handleAnalyse() {
        if (url.length === 0) {

        }
        setPageName(url)
    }

    return (
        <div>
            <div className="App">
                <p className="Title">{pageName}</p>
                {}
                <div>
                    <input type="text" placeholder="Enter an url" onChange={event => {setURL(event.target.value)}}
                           style={{
                               padding: "10px",
                               borderRadius: "5px",
                               width: "300px",
                               height: "35px",
                               outline: "none",
                               border: 0,
                               display: 'inline-block',
                               marginRight: "20px",
                               marginTop: "-10px"
                           }}
                    />
                    <Button variant="contained" color="primary" onClick={handleAnalyse}>
                        Analyse
                    </Button>
                </div>

            </div>
            <div className="Footer">
                <p style={{display: "inline-block",}}>Made with love by</p>
                <a style={{paddingLeft: "5px", color: "#DB4D55",}} href="http://poc-innovation.com/">PoC</a>
            </div>
        </div>
    );
}

export default App;
