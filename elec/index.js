const { shell } = require('electron')
const ipc = require('electron').ipcRenderer
let $ = require('jquery');
let fs = require('fs');
let request = require('request');

const configHelper = require('./lib/config_helper.js')
const constants = require('./lib/constants.js')

config = configHelper.readConfig(constants.DEFAULT_CONFIG_PATH);
destinationPath = config[`destinationPath`];

$('#btn').on("click", function(event)
{
  getModels();
});
ipc.on('asynchronous-message', (event, arg) =>
{
  console.log(arg);
})

function getModels()
{
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
  models.push(new Model())
  models.push(new Model())
  models.push(new Model())
  models.push(new Model())
  models.push(new Model())
  models.push(new Model())

  $('#models').empty();

  models.forEach(function(model)
  {
    $('#models').append(`
      <div class="card mb-2 item ml-2">
        <div class="row no-gutters">
          <div class="col-md-4">
            <img class="col-sm rounded" src="./cache/mario.jpg">
          </div>
          <div class="col-md-4">
            <div class="card-body">
              <h5 class="card-title">${model.name}</h5>
            </div>
          </div>
          <div class="col-md-3">
            <div class="card-body">
              <div class="p-3 mb-2 text-white state state-${model.state}">.bg-primary</div>
              <button type="button" class="btn btn-primary m-1"><i class="fa fa-video-camera"></i> Action</button>
              <button id="see-${model.id}" type="button" class="btn btn-primary m-1"><i class="fa fa-eye"></i> See</button>
            </div>
          </div>
        </div>
      </div>
    `);

    $(`#action-${model.id}`).on('click', function(event)
    {
      console.log("onclick");

      shell.openExternal('https://github.com');
    });

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


if(!fs.existsSync(destinationPath))
{
  fs.mkdirSync(destinationPath, 0766, function(error){
      if(error)
          console.error(error);
  });
}

let refreshIntervalId = setInterval(main, 30000);

function main()
{
  console.log(`---------------`);

  config = configHelper.readConfig(constants.DEFAULT_CONFIG_PATH);

  /*
  request({url : searchUrl, json: true}, function(error, result, json)
  {
    if(error)
    {
      console.error(error);
      return;
    }

    jsonModels.forEach(function(jsonModel)
    {

    });
  });
  */
};
