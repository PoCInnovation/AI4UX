import '../content.css'
import {useEffect, useState} from "react";
import CloseIcon from '@material-ui/icons/Close';
import CheckIcon from '@material-ui/icons/Check';

const sdk = require('../../services/apiSDK');

const ApiSDK = new sdk.ApiSDK()


function SSL(url) {
    const [ssl, setSsl] = useState(-1);


    useEffect(() => {
        async function test() {
            const res = await ApiSDK.getSecurity(url).catch((e) => setSsl(() => 0));
            setSsl(() => res);
            console.log(ssl);
        }
        test()
    }, [])

    if (ssl === 10) {
        return (
            <div>
                ssl is supported
            </div>
        )
    } else if (ssl === 5) {
        return (
            <div>
                ssl is not good supported
            </div>
        )
    } else if (ssl === 0) {
        return (
            <div>
                ssl is not supported
            </div>
        )
    }
    return <div/>
}

export default function Accessibility(url) {
    return (
        <div className="Accessibility">
            <h2>Accessibility</h2>
            <SSL url={url}/>
        </div>
    )
}