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

module.exports = IndexManager;
