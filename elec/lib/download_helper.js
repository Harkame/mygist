const fs = require(`fs`);
const path = require(`path`);

const constants = require('./constants.js')


const exec = require(`child_process`).exec;


module.exports =
{
  download : function download(model, onRecordModels, destinationPath)
  {
    console.log(`start download ${model['username']}`.green);

    onRecordModels.set(model['username'], true);

    let index = 0;
    let filename = path.join(destinationPath, `${model['username']}_${index}.flv`);

    while(fs.existsSync(filename))
      filename = path.join(destinationPath, `${model['username']}_${index++}.flv`);

    console.log(model.getStreamUrl());

    let command = `${constants.RTMPDUMP_PATH} -r "${model.getStreamUrl()}" -o ${filename} --resume`;

    if(model['username'].toLowerCase() == "jenmason")
      command = `${constants.FFMPEG_PATH} -i ${model.getStreamUrl()} -y -f flv ${filename}`;

    exec(command).on('exit', (code) =>
    {
      onRecordModels.set(model['username'], false);
      console.log(`Stop download ${model['username']}`.red)
    });
  }
};
