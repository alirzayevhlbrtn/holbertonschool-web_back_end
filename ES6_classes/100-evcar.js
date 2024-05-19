import Car from './10-car';

export default class EVCar {
  constructor(brand, motor, color, range) {
    super(brand, motor, color);
    this._range = range;
  }

  get range() {
    return this._range;
  }

  cloneCar() {
    const clonedCar = new Car(this._brand, this._motor, this._color);
    return clonedCar;
  }
}
