const request = require('request');
const assert = require('assert');
const { response } = require('express');
const { error } = require('console');

describe('Index page', () => {
    it('should return status 200 and correct message', (done) => {
        request.get('http://localhost:7865/', (error, response, body) => {
            if (error) {
                return done(error);
            }
            assert.strictEqual(response.statusCode, 200);
            assert.strictEqual(body, 'Welcome to the payment system');
            done();
        });
    });
});

describe('Cart page', () => {
    it('should return status 200 and "Payment methods for cart <id>" when id is a number', (done) => {
        request.get('http://localhost:7865/cart/66', (error, response, body) => {
            if (error) {
                return done(error);
            }
            assert.strictEqual(response.statusCode, 200);
            assert.strictEqual(body, 'Payment methods for cart 66');
            done();
        })
    });

    it('should return 404 when id is NOT a number', (done) => {
        request.get('http://localhost:7865/cart/sixty-six', (error, response, body) => {
            if (error) {
                return done(error);
            }
            assert.strictEqual(response.statusCode, 404);
            done();
        })
    })
});
