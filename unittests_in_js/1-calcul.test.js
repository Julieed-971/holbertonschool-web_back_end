const assert = require("assert")
const calculateNumber = require('./1-calcul');

describe('calculateNumber', () => {
    it('should return 4 when adding 1 and 3', () => {
        assert.strictEqual(calculateNumber('SUM', 1, 3), 4);
    });

    it('should return 6 when adding 1.4 and 4.5', () => {
        assert.strictEqual(calculateNumber('SUM', 1.4, 4.5), 6);
    });

    it('should return -4 when substracting 1.4 and 4.5', () => {
        assert.strictEqual(calculateNumber('SUBSTRACT', 1.4, 4.5), -4);
    });

    it('should return 0.2 when dividing 1.4 and 4.5', () => {
        assert.strictEqual(calculateNumber('DIVIDE', 1.4, 4.5), 0.2);
    });

    it('should return \'Error\' when dividing 1.4 and 0', () => {
        assert.strictEqual(calculateNumber('DIVIDE', 1.4, 0), 'Error');
    })

    it('should round 0.4 down to 0', () => {
        assert.strictEqual(calculateNumber('SUM', 0.4, 0), 0);
    });

    it('should round 0.5 up to 1', () => {
        assert.strictEqual(calculateNumber('SUM', 0.5, 0), 1);
    });

    it('should handle negative numbers', () => {
        assert.strictEqual(calculateNumber('SUBSTRACT', -1.4, -1.6), 1);
    });
});
