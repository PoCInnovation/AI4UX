import './App.css';
import {useState} from "react";
import {Button} from "@material-ui/core";

function App() {
    const [pageName, setPageName] = useState("UX Analyser")
    const [url, setURL] = useState("")
    const [analyse, setAnalyse] = useState(false)

    const titleAlign = {
        verticalAlign: "text-bottom",
        fontSize: "xx-large",
        color: "#DB4D55",
        textAlign: "center",
    }
    const defaultTitle = {
        verticalAlign: "text-bottom",
        fontSize: "xx-large",
        color: "#DB4D55",
    }

    const inputAlign = {
        minWidth: "520px",
        position: "fixed",
        left: "50%",
        bottom: "70px",
        transform: "translate(-50%, -50%)",
        marginLeft: "48px",
        margin: "0 auto",
    }
    const defaultInput = {
        padding: "10px",
        borderRadius: "5px",
        width: "300px",
        height: "35px",
        outline: "none",
        border: 0,
        display: 'inline-block',
        marginRight: "20px",
        marginTop: "-10px"
    }

    const defaultApp = {
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        justifyContent: "center",
        marginTop: "30vh",
    }
    async function handleAnalyse() {
        if (url.length === 0) {
            return
        }
        if (analyse === false) {
            setAnalyse(!analyse)
        }
        setPageName(url)
    }

    return (
        <div>
            <div style={analyse === true ? {} : defaultApp}>
                <p style={analyse === true ? titleAlign : defaultTitle}>{pageName}</p>
                {

                }
                <div style={analyse === true ? inputAlign : {}}>
                    <input type="text" placeholder="Enter an url" onChange={event => {setURL(event.target.value)}} style={defaultInput}/>
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
