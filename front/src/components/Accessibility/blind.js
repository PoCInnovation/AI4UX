import React, {useEffect, useState} from "react";
import CheckIcon from "@material-ui/icons/Check";
import CloseIcon from "@material-ui/icons/Close";


export default function CheckHeader({ results: blind }) {
    console.log('blind: ' + blind);
    if (blind < 0.25) {
        return (
            <div style={{ maxWidth: "200px", display: "flex" }}>
                <CheckIcon style={{ float: "left", marginRight: "10px" }} color={"secondary"}/>
                color blind can use your site
            </div>
        )
    } else if (blind >= 0.25) {
        return (
            <div style={{ maxWidth: "200px", }}>
                <CloseIcon style={{ float: "left" }} color={"primary"}/>
                color blind persons can't use your site
            </div>
        )
    }
    return <div/>
}