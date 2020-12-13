import React from "react";

import Accessibility from './Accessibility/accessiblity'
import UI from './UI/ui'

import Resume from './Resume/resume'

export default function Analyze({ url }) {
    return (
        <div className="Content">
            <div className="Left-side">
                <Accessibility url={url}/>
                <UI url={url}/>
            </div>
            <div className="Right-side">
                <Resume url={url}/>
            </div>
        </div>
    )
}