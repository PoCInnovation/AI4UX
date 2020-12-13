import '../content.css'
import React from "react";

import SSL from './ssl';
import Horizontal from './horizontal'
import Header from './header'
import Blind from './blind'

export default function Accessibility({results}) {
    return (
        <div className="Accessibility">
            <h2>Accessibility</h2>
            <div className={"Column"}>
                <SSL results={results['14']}/>
            </div>
            <div className={"Column"}>
                <Horizontal results={results['2']}/>
            </div>
            <div className={"Column"}>
                <Header results={results['3']}/>
            </div>
            <div className={"Column"}>
                <Blind results={results['9']}/>
            </div>
        </div>
    )
}