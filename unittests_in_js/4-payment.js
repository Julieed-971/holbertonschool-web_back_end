const Utils = require('./utils')
const sendPaymentRequestToApi = (totalAmount, totalShipping) => {
    a = totalAmount;
    b = totalShipping;
    const result = Utils.calculateNumber('SUM', a, b)
    console.log('The total is: ' + result);
}
module.exports = sendPaymentRequestToApi;