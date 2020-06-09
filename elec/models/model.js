
class Model
{
  var index = 0;

  constructor() {
    this.id = index++;
  }
  set name(name) {
    this.id = index++;
    this._name = name.charAt(0).toUpperCase() + name.slice(1);
  }
  get name() {
    return this._name;
  }
  sayHello() {
    console.log('Hello, my name is ' + this.name + ', I have ID: ' + this.id);
  }
}
