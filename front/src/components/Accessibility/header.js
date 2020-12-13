import React, {useEffect, useState} from "react";
import CheckIcon from "@material-ui/icons/Check";
import CloseIcon from "@material-ui/icons/Close";

const sdk = require('../../services/apiSDK');

const ApiSDK = new sdk.ApiSDK()


export default function CheckHeader({ url }) {
    const [header, setHeader] = useState(-1);


    useEffect(() => {
        async function checkHorizontal() {
            const res = await ApiSDK.getHeaderConsistency(url).catch(() => setHeader(() => true));
            console.log('header:' + res)
            setHeader(() => res);
        }
        checkHorizontal()
        console.log('-------------------------');
    }, [])

    if (header) {
        return (
            <div style={{ minWidth: "250px", display: "flex" }}>
                <CheckIcon style={{ float: "left", marginRight: "10px" }} color={"secondary"}/>
                Headers are perfect
            </div>
        )
    } else if (!header) {
        return (
            <div style={{ minWidth: "250px", }}>
                <CloseIcon style={{ float: "left" }} color={"primary"}/>
                Header are misplaced
            </div>
        )
    }
    return <div/>
}