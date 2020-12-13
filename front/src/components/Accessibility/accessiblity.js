import '../content.css'
import React from "react";
import SSL from './ssl';

export default function Accessibility({ url }) {
    return (
        <div className="Accessibility">
            <h2>Accessibility</h2>
            <SSL url={url}/>
        </div>
    )
}