import React, {useEffect, useState} from "react";
import CheckIcon from "@material-ui/icons/Check";
import CloseIcon from "@material-ui/icons/Close";

const sdk = require('../../services/apiSDK');

const ApiSDK = new sdk.ApiSDK()


export default function SSL({ url }) {
    const [ssl, setSsl] = useState(-1);


    useEffect(() => {
        async function checkSec() {
            const res = await ApiSDK.getSecurity(url).catch((e) => setSsl(() => 0));
            setSsl(() => res);
        }
        checkSec()
    }, [])

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