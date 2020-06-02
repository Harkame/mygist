const axios = require('axios')

axios.post('https://www.travian.com/fr/gameworld/login', {
	"gameWorld":
	{
		"url": "https://ts3.travian.fr/"
	},
	"usernameOrEmail": "AzertyQwerty",
	"password": "azerty42"
})
.then((res) => {
  console.log(`statusCode: ${res.statusCode}`)
  console.log(res)
})
.catch((error) => {
  console.error(error)
})
