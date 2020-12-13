import '../content.css'
import React from "react";

import SSL from './ssl';
import Horizontal from './horizontal'
import Header from './header'

export default function Accessibility({results}) {
    return (
        <div className="Accessibility">
            <h2>Accessibility</h2>
            <div className={"Column"}>
                <SSL {results}/>
            </div>
            <div className={"Column"}>
                <Horizontal url={url}/>
            </div>
            <div className={"Column"}>
                <Header url={url}/>
            </div>
        </div>
    )
}