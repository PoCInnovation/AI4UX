const axios = require('axios');

/**
 * Communicate with our backend
 */
class ApiSDK {
    requester = axios.create({
        baseURL: 'http://localhost:5000',
        timeout: 100000,
    });

    async getSecurity(url) {
        const res = await this.requester.get(`/analyze/security?url=${url}`);
        return Number(res.data);
    }

    async checkAPI() {
        return await this.requester.get('/').then(() => true).catch(() => false);
    }

    async checkURL(url, test) {
        try {
            new URL(url);
        } catch (e) {
            return false;
        }

        let request;
        request = new XMLHttpRequest();
        await request.open('GET', url, true);
        await request.send();
        return request.status !== 404;
    }

    /**
     * Get page keypoint
     *
     * @param url - Website URL
     * @returns return a JSON
     * @returns
     * {
     *      "browser": [words],
     *      "mobile": [words]
     * }
     * ```
     */
    async getKeypoint(url) {
        // /analyze/keypoint?url=https://tresorio.com
        const res = await this.requester.get(`/analyze/keypoint?url=${url}`);
        return res.data;
    }

    /**
     * Get horizontal scroll
     *
     * @param url - Website URL
     * @returns boolean
     */
    async getHorizontalScroll(url) {
        const res = await this.requester.get(`/analyze/horizontal_scroll?url=${url}`);
        return res.data;
    }

    /**
     * Get header consistency
     *
     * @param url - Website URL
     * @returns boolean
     */
    async getHeaderConsistency(url) {
        const res = await this.requester.get(`/analyze/headers_consistency?url=${url}`);
        return res.data;
    }

    /**
     * Get website performance
     *
     * @param url
     * @returns return a JSON
     * @returns
     * {
     *      "browser": score,
     *      "mobile": score
     * }
     * ```
     */
    async getPerformance(url) {
        const res = await this.requester.get(`/analyze/speedtest?url=${url}`);
        return res.data;
    }
}

module.exports = {
    ApiSDK
}