const fs = require(`fs`);
const YAML = require(`yaml`);

module.exports = {
  readConfig : function readConfig(configPath)
  {
    return YAML.parse(fs.readFileSync(configPath, `utf8`));
  }
};
