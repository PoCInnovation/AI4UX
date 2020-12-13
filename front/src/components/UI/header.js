import React from "react";
import CheckIcon from "@material-ui/icons/Check";
import CloseIcon from "@material-ui/icons/Close";


export default function CheckHeader({ results: header }) {
    console.log('header: ' + header);
    if (header) {
        return (
            <div style={{ minWidth: "250px", display: "flex" }}>
                <CheckIcon style={{ float: "left", marginRight: "10px" }} color={"secondary"}/>
                Page content is constant
            </div>
        )
    } else if (!header) {
        return (
            <div style={{ minWidth: "250px", }}>
                <CloseIcon style={{ float: "left" }} color={"primary"}/>
                Page content isn't constant
            </div>
        )
    }
    return <div/>
}