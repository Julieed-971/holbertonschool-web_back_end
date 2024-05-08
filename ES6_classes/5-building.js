export default class Building {
  constructor(sqft) {
    if (this.constructor === Building) {
      this._sqft = sqft;
    } else if (!this.evacuationWarningMessage) {
      throw new Error('Class extending Building must override evacuationWarningMessage');
    }
  }

  get sqft() {
    return this._sqft;
  }
}
