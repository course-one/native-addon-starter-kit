// import native addon
const addonGreet = require('bindings')('greet');

// expose module API
exports.hello = addonGreet.greetHello;