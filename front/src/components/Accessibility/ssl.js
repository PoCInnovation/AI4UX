import React from "react";
import CheckIcon from "@material-ui/icons/Check";
import CloseIcon from "@material-ui/icons/Close";


export default function SSL({ results: ssl }) {
    if (ssl === 10) {
        return (
            <div style={{ minWidth: "250px", }}>
                <CheckIcon style={{ float: "left", marginRight: "10px" }} color={"secondary"}/>
                ssl is supported
            </div>
        )
    } else if (ssl === 5) {
        return (
            <div style={{ minWidth: "250px", }}>
                <CloseIcon style={{ float: "left" }} color={"primary"}/>
                ssl is not good supported
            </div>
        )
    } else if (ssl === 0) {
        return (
            <div style={{ minWidth: "250px", }}>
                <CloseIcon style={{ float: "left" }} color={"primary"}/>
                ssl is not supported
            </div>
        )
    }
    return <div/>
}