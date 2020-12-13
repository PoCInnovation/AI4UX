import React from "react";
import CheckIcon from "@material-ui/icons/Check";
import CloseIcon from "@material-ui/icons/Close";


export default function ColorsNumber({ results: num }) {
    console.log('color number: ' + num);
    if (num >= 0.7) {
        return (
            <div style={{ minWidth: "250px", display: "flex" }}>
                <CheckIcon style={{ float: "left", marginRight: "10px" }} color={"secondary"}/>
                Your have enough colors
            </div>
        )
    } else if (num < 0.7) {
        return (
            <div style={{ minWidth: "250px", }}>
                <CloseIcon style={{ float: "left" }} color={"primary"}/>
                You have to much colors
            </div>
        )
    }
    return <div/>
}