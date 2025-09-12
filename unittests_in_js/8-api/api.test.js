const request = require('request');
const assert = require('assert');
const { response } = require('express');

describe('Index page', () => {
    it('should return status 200 and correct message', (done) => {
        request.get('http://localhost:7865/', (error, response, body) => {
            if (error) {
                return done(error);
            }
            assert.strictEqual(response.statusCode, 200);

            assert.strictEqual(body, 'Welcome to the payment system');

            done();
        })
    })
});