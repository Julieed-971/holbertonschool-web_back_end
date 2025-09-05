const { expect } = require('chai');
const calculateNumber = require('./2-calcul_chai');

describe('calculateNumber (chai)', () => {
    it('should return 4 when adding 1 and 3', () => {
        expect(calculateNumber('SUM', 1, 3)).to.equal(4);
    });

    it('should return 6 when adding 1.4 and 4.5', () => {
        expect(calculateNumber('SUM', 1.4, 4.5)).to.equal(6);
    });

    it('should return -4 when SUBTRACTing 1.4 and 4.5', () => {
        expect(calculateNumber('SUBTRACT', 1.4, 4.5)).to.equal(-4);
    });

    it('should return 0.2 when dividing 1.4 and 4.5', () => {
        expect(calculateNumber('DIVIDE', 1.4, 4.5)).to.equal(0.2);
    });

    it('should return \'Error\' when dividing 1.4 and 0', () => {
        expect(calculateNumber('DIVIDE', 1.4, 0)).to.equal('Error');
    })

    it('should round 0.4 down to 0', () => {
        expect(calculateNumber('SUM', 0.4, 0)).to.equal(0);
    });

    it('should round 0.5 up to 1', () => {
        expect(calculateNumber('SUM', 0.5, 0)).to.equal(1);
    });

    it('should handle negative numbers', () => {
        expect(calculateNumber('SUBTRACT', -1.4, -1.6)).to.equal(1);
    });
});
