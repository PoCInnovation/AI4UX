import React from "react";
import CheckIcon from "@material-ui/icons/Check";
import CloseIcon from "@material-ui/icons/Close";


export default function Colors({ results: color }) {
    console.log('color: ' + color);
    if (color >= 0.7) {
        return (
            <div style={{ minWidth: "250px", display: "flex" }}>
                <CheckIcon style={{ float: "left", marginRight: "10px" }} color={"secondary"}/>
                Your colors are harmonious
            </div>
        )
    } else if (color < 0.7) {
        return (
            <div style={{ minWidth: "250px", }}>
                <CloseIcon style={{ float: "left" }} color={"primary"}/>
                Page isn't constant
            </div>
        )
    }
    return <div/>
}