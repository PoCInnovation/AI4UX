import React, {useEffect, useState} from "react";
import '../content.css'

import { CircularProgressbar } from 'react-circular-progressbar';
import 'react-circular-progressbar/dist/styles.css';

import CircularProgress from '@material-ui/core/CircularProgress';


function Perfomance({ perf }) {
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

export default function Resume({ perf }) {
    return (
        <div className="Resume">
            <div className="Resume-cent">
                <Perfomance perf={perf}/>
                <Perfomance perf={perf}/>
                <Perfomance perf={perf}/>
            </div>
        </div>
    )
}