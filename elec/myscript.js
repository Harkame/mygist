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
const { shell } = require('electron')
$('#btn').on("click", function(event)
{
  getModels();
});
ipc.on('asynchronous-message', (event, arg) =>
{
  console.log(arg);
})

function getModels() {
  //ipcRenderer.send('asynchronous-message', 'ping');
  //const reponse = ipc.sendSync("synchronous-message", { type: "ping"});
  //console.log(reponse);
  let models = [];
  models.push(new Model())
  models.push(new Model())
  models.push(new Model())
  models.push(new Model())
  models.push(new Model())
  models.push(new Model())
  models.push(new Model())
  models.push(new Model())
  models.push(new Model())
  models.push(new Model())

  $('#models').empty();

  models.forEach(function(model)
  {
    /*
    $('#models').append(`
      <li class="list-group-item">
        <img id='img-${model.id}' class="col-sm rounded model-img" src="mario.jpg">
        <p class='col-md' id='name-${model.id}'>${model.name}</p>
        <button class='col-sm' id='action-${model.id}' type="button" class="btn btn-primary"><i class="fa fa-video-camera"></i> Action</button>
        <div class='col-sm state-${model.state}' state-${model.state}' class='state state-${model.state}' id='state-${model.id}'>
          <p>Available<p>
        </div>
      </li>
    `);
    */

    //<svg class="bd-placeholder-img" width="100%" height="250" xmlns="http://www.w3.org/2000/svg" aria-label="Placeholder: Image" preserveAspectRatio="xMidYMid slice" role="img"><title>Placeholder</title><rect width="100%" height="100%" fill="#868e96"/><text x="50%" y="50%" fill="#dee2e6" dy=".3em">Image</text></svg>
    $('#models').append(`
      <div class="card mb-3" style="max-width: 540px;">
        <div class="row no-gutters">
          <div class="col-md-4">
            <img class="col-sm rounded" src="mario.jpg">
          </div>
          <div class="col-md-4">
            <div class="card-body">
              <h5 class="card-title">Card title</h5>
            </div>
          </div>
          <div class="col-md-4">
            <div class="card-body">
              <div class="col-sm state state-${model.state}">
                <p>Available<p>
              </div>
              <button type="button" class="btn btn-primary"><i class="fa fa-video-camera"></i> Action</button>
              <button id="see-${model.id} "type="button" class="btn btn-primary"><i class="fa fa-eye"></i> See</button>
            </div>
          </div>
        </div>
      </div>
    `);

    $(`#see-${model.id}`).on('click', function(event)
    {
      console.log("onclick");

      shell.openExternal('https://github.com');
    });
  });
}
var index = 0;
class Model {
  constructor() {
    this.id = index;
    this.name = "ModelName-" + index;
    this.state = index;
    index++;
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


getModels();
