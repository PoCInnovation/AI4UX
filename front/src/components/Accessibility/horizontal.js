import React, {useEffect, useState} from "react";
import CheckIcon from "@material-ui/icons/Check";
import CloseIcon from "@material-ui/icons/Close";

const sdk = require('../../services/apiSDK');

const ApiSDK = new sdk.ApiSDK()


export default function CheckHorizontal({ url }) {
    const [horizontal, setHorizontal] = useState(-1);


    useEffect(() => {
        async function checkHorizontal() {
            const res = await ApiSDK.getHorizontalScroll(url).catch(() => setHorizontal(() => true));
            setHorizontal(() => res);
        }
        checkHorizontal()
    }, [])

    if (horizontal) {
        return (
            <div style={{ minWidth: "250px", display: "flex" }}>
                <CheckIcon style={{ float: "left", marginRight: "10px" }} color={"secondary"}/>
                webpage's width is perfect
            </div>
        )
    } else if (!horizontal) {
        return (
            <div style={{ minWidth: "250px", }}>
                <CloseIcon style={{ float: "left" }} color={"primary"}/>
                webpage is too large
            </div>
        )
    }
    return <div/>
}