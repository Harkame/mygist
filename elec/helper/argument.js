const ArgumentParser = require('argparse').ArgumentParser;

function get_argments()
{
  var parser = new ArgumentParser({
    addHelp:true,
    description: 'Argparse example'
  });

  parser.addArgument(
    [ '-c', '--config_file' ],
    {
      help: 'config file'
    }
  );

  parser.addArgument(
    [ '-d', '--destination_path' ],
    {
      help: 'destination path'
    }
  );

  parser.addArgument(
    [ '-r', '--rtmp' ],
    {
      help: 'rtmp path'
    }
  );

  parser.addArgument(
    '-v',
    {
      help: 'verbosity level',
      action : 'count',
    }
  );

  return parser.parseArgs();
}
