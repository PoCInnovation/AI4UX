import React, {useEffect, useState} from "react";
import '../content.css'

import { CircularProgressbar } from 'react-circular-progressbar';
import 'react-circular-progressbar/dist/styles.css';

import CircularProgress from '@material-ui/core/CircularProgress';

const sdk = require('../../services/apiSDK');

const ApiSDK = new sdk.ApiSDK()


function Perfomance({ url }) {
    const [perf, setPerf] = useState(-1)

    useEffect(() => {
        console.log(url);
        async function checkPerf() {
            const res =  await ApiSDK.getPerformance(url).catch(() => setPerf(() => 0));
            setPerf(() => res);
        }
        checkPerf()
    }, [])

    if (perf < 0) {
        return (
            <div>
                <CircularProgress style={{marginLeft: "-240px", display: "flex"}}/>
            </div>
        )
    } else if (!perf || perf === 0) {
        return (
            <div>error</div>
        )
    } else {
        return (
            <div style={{width: "100px", height: "100px", display: "flex"}}>
                <CircularProgressbar value={perf.browser * 100} text={`${perf.browser * 100}%`}/>
            </div>
        )
    }
}

export default function Resume({ url }) {
    return (
        <div className="Resume">
            <div className="Resume-cent">
                <Perfomance url={url}/>
                <Perfomance url={url}/>
                <Perfomance url={url}/>
            </div>
        </div>
    )
}