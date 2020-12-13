const sdk = require('./services/apiSDK');

const ApiSDK = new sdk.ApiSDK()

async function main() {
    const check = await ApiSDK.checkURL('https://tresorio.com');

    console.log('Check');
    console.log(check)

    console.log(await ApiSDK.checkAPI());

    try {
        const keypoint = await ApiSDK.getKeypoint('https://tresorio.com');

        console.log('Keypoint');
        console.log(keypoint);

        const perf = await ApiSDK.getPerformance('https://tresorio.com');

        console.log('Perf');
        console.log(perf);

        const header_consistency = await ApiSDK.getHeaderConsistency('https://tresorio.com');

        console.log('header');
        console.log(header_consistency);

        const horizontal_scroll = await ApiSDK.getHorizontalScroll('https://tresorio.com');

        console.log('scroll');
        console.log(horizontal_scroll);
    } catch (e) {
        console.log(e);
    }

}

main();
