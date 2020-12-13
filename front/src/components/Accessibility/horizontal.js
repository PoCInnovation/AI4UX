import React from "react";
import CheckIcon from "@material-ui/icons/Check";
import CloseIcon from "@material-ui/icons/Close";


export default function CheckHorizontal({ results: horizontal }) {
    console.log('horizon: ' + horizontal);
    if (horizontal) {
        return (
            <div style={{ maxWidth: "200px", display: "flex" }}>
                <CheckIcon style={{ float: "left", marginRight: "10px" }} color={"secondary"}/>
                webpage's width is perfect
            </div>
        )
    } else if (!horizontal) {
        return (
            <div style={{ maxWidth: "200px", }}>
                <CloseIcon style={{ float: "left" }} color={"primary"}/>
                webpage is too large
            </div>
        )
    }
    return <div/>
}