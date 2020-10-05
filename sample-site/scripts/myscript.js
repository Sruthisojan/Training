/*global document*/

var MyHeading = document.querySelector('h1');
MyHeading.textContent = 'Welcome to Hogwarts!!';
//events
/*document.querySelector("html").onclick = function ()
{
    alert("Ouch! stop poking me!");
}*/
//switching images
var turtleImage = document.querySelector('img');
turtleImage.onclick = function ()
{
    var myimages = turtleImage.getAttribute('src');
    if(myimages === 'images/kitten.jpg')
        {
            turtleImage.setAttribute('src','images/turtle.jpg');
        }
    else
        {
            turtleImage.setAttribute('src','images/kitten.jpg'); 
        }
}
//personalised welcome message
var nameButton = document.querySelector('button');
var myHeading = document.querySelector('h1');
function setUserName()
{
    'use strict';
    var myName = window.prompt('Name please');
    localStorage.setItem('name',myName);
    myHeading.textContent = 'Welcome to Hogwarts, '+myName;
}
if(!localStorage.getItem('name'))
    {
        setUserName();
    }
else
    {
        var storedName = localStorage.getItem('name')
        myHeading.textContent = 'Welcome to Hogwarts, ' + storedName;
    }
nameButton.onclick = function()
{
    'use strict';
    setUserName();
};

