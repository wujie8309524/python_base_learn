var webPage = require('webpage');
var page = webPage.create();

page.open('http://localhost/python_cookie/index.php',function(s){
            console.log(s);
            var title = page.evaluate(function(){
                return document.title;
            });
            console.log('page title is '+ title);
            phantom.exit();
});

page.open('https://www.google.com/',function(){
        page.zoomFactor = 0.25;
        console.log(page.renderBase64());
        phantom.exit();
})
