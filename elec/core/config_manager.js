const ConfigHelper = require('../lib/config_helper.js')

class ConfigManager
{
  constructor() {
    this.models = [];
  }

  getConfig(configPath)
  {
    this.config = ConfigHelper.readConfig('config/config.yml');
  }

  addModel(model)
  {
    this.getConfig();

    let index = this.getModelIndex(model);

    if(index !== -1)
      this.updateModel(model);
    else
    {
      this.config['models'].push(model);
      ConfigHelper.writeConfig('config/config.yml', this.config)
    }
  }

  updateModel(model)
  {
    this.getConfig();

    let index = this.getModelIndex(model)

    if(index === -1)
      this.addModel(model);
    else
    {
      this.config['models'][index] = model;
      ConfigHelper.writeConfig('config/config.yml', this.config)
    }
  }

  deleteModel(model)
  {
    this.getConfig();

    let index = this.getModelIndex();

    if(index === -1)
      return;

    this.config['model'].splice(index, 1);
    ConfigHelper.writeConfig('config/config.yml', this.config)
  }

  getModelIndex(model)
  {
    let index = -1;

    this.config['models'].forEach(function(modelRow, indexRow)
    {
      if(modelRow.username.toLowerCase() === model.username.toLowerCase())
        index = indexRow;
    });

    return index;
  }
}

module.exports = ConfigManager;
