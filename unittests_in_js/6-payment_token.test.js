const assert = require('assert');
const getPaymentTokenFromAPI = require('./6-payment_token');

describe('getPaymentTokenFromAPI', () => {
    it('should resolve with correct data when success is true', (done) => {
        getPaymentTokenFromAPI(true)
            .then((result) => {
                assert.deepStrictEqual(result, {data: 'Successful response from the API' });
                done();
            })
            .catch((err) => done(err));
    });
});