'use strict';

function validate()
{
    var url = document.getElementById("url-field");

    var exp = /(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,})/gi;
    var regexp = new RegExp(exp);
    if(regexp.test(url.value)) {
        url.setCustomValidity("");
    }
    else {
        url.setCustomValidity("This is not a valid URL.");
    }
    return false;
}

