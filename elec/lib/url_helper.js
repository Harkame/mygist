const path = require(`path`);

const constants = require('./constants.js')

module.exports =
{
  createSearchUrl : function createSearchUrl(models)
  {
    let searchUrl = '';

    if(models.length == 0)
      return searchUrl;

    searchUrl += models[0];

    for(let modelIndex = 1; modelIndex < models.length; modelIndex++)
    {
      searchUrl += '  ';
      searchUrl += models[modelIndex];
    }

    return searchUrl;
  }
};
