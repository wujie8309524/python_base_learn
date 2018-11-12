/*
    phantomjs jpeg.js
    用来生成截图
*/

var webPage = require('webpage');
var page = webPage.create();

page.viewportSize = { width: 1920, height: 1080 };
page.open("https://www.google.com", function start(status) {
	  page.render('google_home.jpeg', {format: 'jpeg', quality: '100'});
	    phantom.exit();
});
