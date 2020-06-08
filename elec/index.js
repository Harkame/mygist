const { shell } = require('electron')
const ipc = require('electron').ipcRenderer
let $ = require('jquery');
let fs = require('fs');
let request = require('request');

$('#filter-models').change(function(event)
{
  let status = $('#filter-models').find(":selected").val();
  let search = $('#search-models').val()

  manager.filterModels(search, status);
});

$('#search-models').keyup(function(event)
{
  let status = $('#filter-models').find(":selected").val();
  let search = $('#search-models').val()

  manager.filterModels(search, status);
});



class IndexManager
{
  constructor() {
    this.models = [];
  }

  filterModels(search, status)
  {
    showLoading(true);

    let modelsToDisplay = this.models.filter(model =>
    {
      let find = true;

      if(find)
        if(!model.username.includes(search))
          find = false;

      if(find)
        if(status != '' )
          find = model.status.toLowerCase() == status.toLowerCase();

      return find;
    });

    $('#models').empty();

    console.log(modelsToDisplay);

    modelsToDisplay.forEach(function(model)
    {
      displayModel(model);
    });

    showLoading(false);
  }
}

let manager = new IndexManager();


const colors = require(`colors`);
const path = require(`path`);

const constants = require('./lib/constants.js')

const configHelper = require('./lib/config_helper.js')
const downloadHelper = require('./lib/download_helper.js')
const urlHelper = require('./lib/url_helper.js')

const Model = require('./core/model.js');

$('#btn').on("click", function(event)
{
  getModels();
});
ipc.on('asynchronous-message', (event, arg) =>
{
  console.log(arg);
})

function displayModel(model)
{
  //<img class="col-sm rounded-circle" src="${model.avatarUrl}">

  $('#models').append(`
    <div class="card mb-2 item ml-2">
      <div class="row no-gutters">
        <div class="col-md-4"  style="width : 260px;">
          <img class="col-sm rounded-circle" src="cache/mario.jpg">
        </div>
        <div class="col-md-4">
          <div class="card-body">
            <h5 class="card-title">${model.username}</h5>
          </div>
        </div>
        <div class="col-md-3">
          <div class="card-body">
            <div class="p-3 mb-2 text-white status status-${model.status}">${model.status}</div>
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

    shell.openExternal(`google.com`);
  });
}
var index = 0;

const MAXIMUM_LENGTH = 4;

var onRecordModels = new Map();
let destinationPath;

config = configHelper.readConfig(constants.DEFAULT_CONFIG_PATH);
destinationPath = config[`destinationPath`];


if(!fs.existsSync(destinationPath))
{
  fs.mkdirSync(destinationPath, 0766, function(error){
      if(error)
          console.error(error);
  });
}

main();

//let refreshIntervalId = setInterval(main, 30000);

function main()
{
  console.log(`---------------`);

  config = configHelper.readConfig(constants.DEFAULT_CONFIG_PATH);

  $('#models').empty();

  let models = [];
  let model = new Model();
  model.username = "Tata";
  model.status = 'off';
  models.push(model);
  model = new Model();
  model.username = "Tata";
  model.status = 'public';
  models.push(model);
  model = new Model();
  model.username = "Lala";
  model.status = 'idle';
  models.push(model);
  model = new Model();
  model.username = "Toto";
  model.status = 'private';
  models.push(model);
  model = new Model();
  model.username = "Titi";
  model.status = 'off';
  models.push(model);

  manager.models = models;

  models.forEach(function(model)
  {
    displayModel(model);
  });
  /*
  let spottedModels = config[`models`];

  if(!spottedModels)
    return;

  spottedModels = spottedModels.map(item => item ? item.toLowerCase() : "");

  let splitedModels = [];

  const clone = [...new Set(spottedModels)];

  while(clone.length > 0)
    splitedModels.push(clone.splice(0, MAXIMUM_LENGTH))

  splitedModels.forEach(function(array)
  {
    let searchUrl = urlHelper.createSearchUrl(array);

    request({url : searchUrl, json: true}, function(error, result, json)
    {
      if(error)
      {
        console.error(error);
        return;
      }

      if(!json)
        return;

      let jsonModels = json[`models`];

      if(!jsonModels)
        return;


      jsonModels.forEach(function(jsonModel)
      {
        let model = Object.assign(new Model, jsonModel);

        if(spottedModels.indexOf(model['username'].toLowerCase()) == -1)
          return;

        displayModel(model);

        if(model[`status`] == 'off')
          return;

        if(model['status'] != `public`)
        {
          console.log(`[${model['status']}] : ${model['username']}`.cyan);
          return;
        }
      });
    });
  });
  */
};

function showLoading(show)
{
  if(show)
    $('#loading').show();
  else
  $('#loading').hide();
}
