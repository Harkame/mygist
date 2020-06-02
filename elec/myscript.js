const ipc = require('electron').ipcRenderer

const btn = document.getElementById('btn')
btn.addEventListener('click', function () {
  console.log("sendsync");
    const reponse = ipc.sendSync('message-synchrone', 'Allez hop !')
    document.getElementById('syncReponse').innerHTML = reponse
})
