import './App.css';
import {useState} from "react";
import {Button} from "@material-ui/core";
import Alert from '@material-ui/lab/Alert';
import Analyze from "./components/analyse";

const sdk = require('./services/apiSDK');

const ApiSDK = new sdk.ApiSDK()

function App() {
    const [pageName, setPageName] = useState("UX Analyse")
    const [url, setURL] = useState("")
    const [analyse, setAnalyse] = useState(false)
    const [alert, setAlert] = useState(false)
    const [click, setClick] = useState(false);
    const [results, setResults] = useState();

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
        if (url.length === 0 || (await ApiSDK.checkURL(url, false)) === false) {
            setAlert(true)
            setTimeout(function () {
                setAlert(false);
            }, 3000);
            return
        }
        setPageName(url)
        setClick(true)
        await setResults((await ApiSDK.getAll(url)));
        setClick(false);
        setAnalyse(true);
    }

    return (
        <div>
            <div style={analyse === true ? {} : defaultApp}>
                <p style={analyse === true ? titleAlign : defaultTitle}>{pageName}</p>
                {
                    analyse === true ? <Analyze url={url}/> : <div />
                }
                <div style={analyse === true ? inputAlign : {}}>
                    <input type="text" placeholder="Enter an url" onChange={event => {
                        setURL(event.target.value)
                    }} style={defaultInput}/>
                    <Button variant="contained" color="primary" onClick={handleAnalyse}>
                        Analyse
                    </Button>
                </div>
                {alert === true && (
                    <Alert style={{marginTop: "20px",}} severity="error">The url you provided is not valid</Alert>)}
                {click === true ? <Alert style={{marginTop: "20px",}} severity="info">We are currently running the analysis on the website you provided</Alert> : <div /> }
            </div>
            <div className="Footer">
                <p style={{display: "inline-block",}}>Made with love by</p>
                <a style={{paddingLeft: "5px", color: "#DB4D55",}} href="http://poc-innovation.com/" target="_blank"
                   rel="noreferrer">PoC</a>
            </div>
        </div>
    );
}

export default App;
