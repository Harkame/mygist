var MAXIMUM_LENGTH = 5;

var all = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15];
var arrays = [];

while(all.length > 0)
  arrays.push(all.splice(0, MAXIMUM_LENGTH))

arrays.forEach(function(array)
{
  console.log(array);
});
