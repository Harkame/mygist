const ipc = require('electron').ipcRenderer
let $ = require('jquery');
//require('./models/model.js')
/*
let notifyBtn = document.getElementById("btn");

notifyBtn.addEventListener('click', function(event)
{
  ipcRenderer.send('asynchronous-message', 'ping')
})
*/

$('#btn').on("click", function(event)
{
  //ipcRenderer.send('asynchronous-message', 'ping');
  //const reponse = ipc.sendSync("synchronous-message", { type: "ping"});
  //console.log(reponse);
  let models = [];
  models.push(new Model())
  models.push(new Model())
  models.push(new Model())
  models.push(new Model())
  models.push(new Model())

  $('#models').empty();

  models.forEach(function(model)
  {
    $('#models').append(`
      <li class="list-group-item">
        <p>${model.name}</p>
      </li>
    `);
  });
});
ipc.on('asynchronous-message', (event, arg) =>
{
  console.log(arg);
})

var index = 0;
class Model {
  constructor() {
    this.id = 'id_' + index++;
    this.name = "ModelName-" + index;
  }
  set name(name) {
    this._name = name.charAt(0).toUpperCase() + name.slice(1);
  }
  get name() {
    return this._name;
  }
  sayHello() {
    console.log('Hello, my name is ' + this.name + ', I have ID: ' + this.id);
  }
}
