const { shell } = require('electron')
const ipc = require('electron').ipcRenderer
const fs = require('fs');
const request = require('request');
const notifier = require('node-notifier');
const moment = require('moment');
const $ = require('jquery');
const colors = require(`colors`);
const path = require(`path`);

const constants = require('./lib/constants.js')
const configHelper = require('./lib/config_helper.js')
const downloadHelper = require('./lib/download_helper.js')
const urlHelper = require('./lib/url_helper.js')

const Model = require('./core/model.js');
const IndexManager = require('./core/index_manager.js')

var index = 0;

const MAXIMUM_LENGTH = 4;

var onRecordModels = new Map();
let destinationPath;

const manager = new IndexManager();

config = configHelper.readConfig(constants.DEFAULT_CONFIG_PATH);
destinationPath = config[`destinationPath`];

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

ipc.on('asynchronous-message', (event, arg) =>
{
  console.log(arg);
})

function updateDisplayModel(model)
{
  let card = $(`#card-${model.id}`);

  if(card.length === 0)
  {
    return false;
  }

  let ymlModel = config['models'].find(function(modelRow)
  {
    return modelRow.username == model.username;
  });

  if(!ymlModel)
    ymlModel = {};

  if(ymlModel.notify === 0)
    card.find(`#notify-${model.id}`).addClass('btn-notify-disabled').removeClass('btn-notify-enabled');
  else
    card.find(`#notify-${model.id}`).addClass('btn-notify-enabled').removeClass('btn-notify-disabled');

  return true;
}

function displayModel(model)
{
  //<img class="col-sm rounded-circle" src="${model.avatarUrl}">

  if(updateDisplayModel(model))
    return;

  let ymlModel = config['models'].find(function(modelRow)
  {
    return modelRow.username == model.username;
  });

  if(!ymlModel)
    ymlModel = {};

  $('#models').append(`
    <div id="card-${model.id}" class="card mb-1 item ml-1 mr-1 mt-1">
      <div class="row no-gutters">
        <div class="col-md-4"  style="width : 260px;">
          <img id="img-${model.id}" class="col-sm rounded-circle" src="cache/mario.jpg">
        </div>
        <div class="col-md-3">
          <div class="card-body">
            <h4>${model.username}</h4>
          </div>
        </div>
        <div class="col-md-3">
          <div class="card-body">
            <div class="p-3 mb-2 text-white status status-${model.status}" style="text-align: center;"><h6 class="mb-0">${model.status.toUpperCase()}</h6></div>
            <button type="button" class="btn btn-primary m-1" style="width : 100px"><i class="fa fa-video-camera"></i> Action</button>
            <button id="see-${model.id}" type="button" class="btn btn-primary m-1" style="width : 100px"><i class="fa fa-eye"></i> See</button>
          </div>
        </div>
        <div class="col-md-1">
          <div class="card-body">
            <button id="notify-${model.id}" type="button" class="btn btn-primary m-1 btn-notify-${ymlModel.notify == 1 ? "enabled" : "disabled"}"><i class="fa fa-bell"></i> Notify</button>
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

  $(`#notify-${model.id}`).on('click', function(event)
  {
    let index = -1;

    config['models'].forEach(function(modelRow, indexRow)
    {
      if(modelRow.username.toLowerCase() === model.username.toLowerCase())
        index = indexRow;
    });

    if(index === -1)
    {
      ymlModel = {};
      ymlModel.username = model.username
      ymlModel.notify = 1;
      config['models'].push(ymlModel);
    }
    else
      if(config['models'][index].notify === 0)
        config['models'][index].notify = 1;
      else
        config['models'][index].notify = 0;

    configHelper.writeConfig(constants.DEFAULT_CONFIG_PATH, config);

    displayModel(model);
  });

  $(`#img-${model.id}`).on('mouseover', function(event)
  {
    $(`#img-${model.id}`).attr('src', 'cache/luigi.jpg');
  });

  $(`#img-${model.id}`).on('mouseout', function(event)
  {
    $(`#img-${model.id}`).attr('src', 'cache/mario.jpg');
  });
}


main();

let refreshIntervalId = setInterval(checkNotifications, 30000);



if(!fs.existsSync(destinationPath))
{
  fs.mkdirSync(destinationPath, 0766, function(error){
      if(error)
          console.error(error);
  });
}

function checkNotifications()
{
    let models = [];
    let model = new Model();
    model.username = "Tata";
    model.status = 'off';
    model.id = index++;
    models.push(model);
    model = new Model();
    model.username = "Toto";
    model.status = 'public';
    model.id = index++;
    models.push(model);
    model = new Model();
    model.username = "Lala";
    model.status = 'public';
    model.id = index++;
    models.push(model);

    models.forEach(function(model)
    {
      checkNotification(model);
    });
}

function checkNotification(model)
{
  if(model.status !== 'public')
    return;
  let index = -1;

  config['models'].forEach(function(modelRow, indexRow)
  {
    if(modelRow.username.toLowerCase() === model.username.toLowerCase())
      index = indexRow;
  });

  let ymlModel = {};

  if(index !== -1)
    ymlModel = config['models'][index];

  let notificationDate = moment('1970-01-01');
  let now = moment();

  if(ymlModel.notificationDate)
    notificationDate = moment(ymlModel.notificationDate);

  if(now.diff(notificationDate, 'hours') > 6)
  {
    notifier.notify(
    {
      title: `Is online`,
      message: `${model.username}`,
      icon: 'cache/mario.jpg',
      contentImage: 'cache/mario.jpg',
      actions: ['Cancel', 'Check'],
    },
    function(error, response, metadata)
    {
      switch(response)
      {
        case 'check':
          shell.openExternal('https://github.com');
          break;
        case 'cancel':
        break;
      }
    });

    if(index !== -1)
      config['models'][index].notificationDate = now.toJSON();
    else
    {

    }

    configHelper.writeConfig(constants.DEFAULT_CONFIG_PATH, config);
  }
}

function main()
{
  config = configHelper.readConfig(constants.DEFAULT_CONFIG_PATH);

  $('#models').empty();

  let models = [];
  let model = new Model();
  model.username = "Tata";
  model.status = 'off';
  model.id = index++;
  models.push(model);
  model = new Model();
  model.username = "Toto";
  model.status = 'public';
  model.id = index++;
  models.push(model);
  model = new Model();
  model.username = "Lala";
  model.status = 'public';
  model.id = index++;
  models.push(model);

  /*
  model = new Model();
  model.username = "Toto";
  model.status = 'private';
  models.push(model);
  model = new Model();
  model.username = "Titi";
  model.status = 'off';
  models.push(model);
  */

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
