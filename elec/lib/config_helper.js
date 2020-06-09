const fs = require(`fs`);
const YAML = require(`yaml`);

module.exports = {
  readConfig : function readConfig(configPath)
  {
    return YAML.parse(fs.readFileSync(configPath, `utf8`));
  },
  writeConfig : function readConfig(config, configPath)
  {
    return fs.writeFileSync(configPath, config, 'utf8');
  }
};
