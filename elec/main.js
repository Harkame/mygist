const electron = require('electron');
const app = electron.app;
const BrowserWindow = electron.BrowserWindow;
const ipc = electron.ipcMain
const {Menu} = require('electron')
let mainWindow;
const url = require('url')
const path = require('path')
const electronLocalshortcut = require('electron-localshortcut');

let devToolsOpen = false;

function createWindow ()
{
  mainWindow = new BrowserWindow({
    width: 800,
    height: 500,
    title: 'ModelRecorder',
    maximized: false,
    center: true,
    webPreferences:
    {
      nodeIntegration: true,
      //devTools: false
    },
});
  //mainWindow.maximize();

  //mainWindow.loadURL(`file://${__dirname}/index.html`);
  mainWindow.loadURL(url.format({
    pathname: path.join(__dirname, "index.html"),
    protocol: 'file',
    slashes: true
  }))
  electronLocalshortcut.register(mainWindow, 'F12', () => {
    if(devToolsOpen)
    {
      mainWindow.closeDevTools();
      devToolsOpen = false;
    }
    else
    {
      mainWindow.openDevTools();
      devToolsOpen = true;
    }

  });

  mainWindow.webContents.on('did-finish-load', function()
  {
    mainWindow.openDevTools();
    devToolsOpen = true;
  });

  mainWindow.on('closed', () =>
  {
    mainWindow = null;
  })


  //mainWindow.webContents.on("devtools-opened", () => { mainWindow.webContents.closeDevTools(); });
}

const template =
[
]

const menu = Menu.buildFromTemplate(template)
Menu.setApplicationMenu(menu)


app.on('ready', createWindow);

app.on('window-all-closed', () => {
  if(process.platform !== 'Darwin') {
    app.quit()
  }
})

app.on('activate', () =>
{
  if (BrowserWindow.getAllWindows().length === 0)
    createWindow()
});

app.on('active', () => {
  if(mainWindow == null) {
    createWindow()
  }
})

ipc.on('synchronous-message', function (event, arg) {
  if(arg.type === "ping") {
    console.log("Received pong successfully!")
    event.returnValue = "receivpong";
  }
  else
    event.returnValue = "reeived";
})

ipc.on('asynchronous-message', function (event, arg) {
  console.log(arg)
  event.returnValue = 'Oui voilà je réponds !'
})
