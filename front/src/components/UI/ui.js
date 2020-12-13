import '../content.css'

import Header from './header'
import Colors from './colors'
import ColorsNumber from "./colorsNumber";

export default function UI({results}) {
    return (
        <div className="UI">
            <h2 style={{font: "Roboto", padding: "8px",}}>UI</h2>
            <div className="Column">
                <Header results={results['4']}/>
            </div>
            <div className="Column">
                <Colors results={(results['10'] + results['11']) / 2}/>
            </div>
            <div className="Column">
                <ColorsNumber results={results['8']}/>
            </div>
        </div>
    )
}