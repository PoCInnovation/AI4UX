import React from "react";

import Accessibility from './Accessibility/accessiblity'
import UI from './UI/ui'

import Resume from './Resume/resume'

export default function Analyze({ results }) {
    return (
        <div className="Content">
            <div className="Left-side">
                <Accessibility results={results}/>
                <UI results={results}/>
            </div>
            <div className="Right-side">
                <Resume results={results}/>
            </div>
        </div>
    )
}