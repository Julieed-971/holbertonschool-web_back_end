const sinon = require('sinon');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./4-payment');

describe('sendPaymentRequestToApi', () => {
    it('should stub Utils.calculateNumber, check arguments, and verify log output', () => {
        const stub = sinon.stub(Utils, 'calculateNumber').returns(10);
        
        const consoleSpy = sinon.spy(console, 'log');
        
        sendPaymentRequestToApi(100,20)

        sinon.assert.calledWith(stub, 'SUM', 100,20);

        sinon.assert.calledWith(consoleSpy, 'The total is: 10');

        Utils.calculateNumber.restore();
        console.log.restore();
    })
})
