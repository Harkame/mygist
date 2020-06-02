const electron = require('electron');
const app = electron.app;
const BrowserWindow = electron.BrowserWindow;
const ipc = electron.ipcMain
let $ = require('jquery');
let mainWindow;

function createWindow ()
{
  mainWindow = new BrowserWindow({
    width: 800,
    height: 500,
    title: 'ZdS, ça pulpe !',
    maximized: false,
    center: true,
});
  //mainWindow.maximize();

  mainWindow.loadURL(`file://${__dirname}/index.html`);

  mainWindow.on('closed', () =>
  {
    mainWindow = null;
  })
}

app.on('ready', createWindow);

app.on('window-all-closed', () =>
{
  app.quit();
});

app.on('activate', () =>
{
  if (BrowserWindow.getAllWindows().length === 0)
    createWindow()
});

ipc.on('message-synchrone', function (event, arg) {
  console.log(arg)
  event.returnValue = 'Oui voilà je réponds !'
})
