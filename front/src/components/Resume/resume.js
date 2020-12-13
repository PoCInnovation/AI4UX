import React, {useEffect, useState} from "react";
import '../content.css'

import {CircularProgressbar} from 'react-circular-progressbar';
import 'react-circular-progressbar/dist/styles.css';

import CircularProgress from '@material-ui/core/CircularProgress';


function Perfomance({perf, desc}) {
    console.log('perf:' + perf)
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
            <div>
                <div style={{width: "100px", height: "100px", display: "flex"}}>
                    <CircularProgressbar value={perf * 100} text={`${desc}`}/>
                </div>
            </div>
        )
    }
}

export default function Resume({results}) {
    return (
        <div className="Resume">
            <div className="Resume-cent">
                <Perfomance perf={results['0']} desc={"Perf"}/>
                <Perfomance perf={results['1']} desc={"Design"}/>
                <Perfomance perf={results['7']} desc={"Clutter"}/>
            </div>
        </div>
    )
}