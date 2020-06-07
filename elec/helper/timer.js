const exec = require(`child_process`).exec;

var refreshIntervalId = setInterval(callBack, 2000);

let objects =
[
  {'username' : 'toto', 'onDownload' : false},
  {'username' : 'Tata', 'onDownload' : false}
]

function callBack()
{
  //...

  objects.forEach(function(object)
  {
    if(!object.onDownload)
    {
      let url = buildUrl();

      download(url, object);
    }
    else
      console.log(`On download : ${object.username}`);
  });


  //...
};

function buildUrl(param)
{
  let url = "";

  return url;
}

function download(url, object)
{
  console.log(`Start download : ${object.username}`);

  object.onDownload = true;

  let downloadHandler = exec(`ls`);

  downloadHandler.on(`exit`, function(returnCode)
  {
    object.onDownload = false;
  });
}
